import sympy
import copy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree

import SCRBenchmark.SRSDFeynman as srsdf
import SCRBenchmark.Constants.StringKeys as sk
from SCRBenchmark import create_dataset_from_sampling_objectives
from SCRBenchmark import Benchmark

import SCRBenchmark.SRSDFeynman as srsdf
import SCRBenchmark.Constants.StringKeys as sk
from SCRBenchmark import create_dataset_from_sampling_objectives, get_constraint_descriptor
from SCRBenchmark import Benchmark

# CONSTRAINT_SAMPLING_SIZE = 10_000_000
CONSTRAINT_SAMPLING_SIZE = 100_000

# This code determines the constraints for each equation. To this end, a large
# set of uniform input data is sampled for the defined input space of the
# equation. This data is then:
# 1) plugged into the equation to calculate the image of the function. If all
#    values are e.g. positive, they all have a sign of '+' thus the function.
# 2) plugged into the symbolic first-order derivatives of the function (derived
#    over all available inputs). This time we get the gradients of the original
#    function. If all values of df/dx_1 are zero or positive we know that the
#    function is monotonic non-decreasing over x_1.
# 3) the same is repeated for second-order derivatives to determine convexity
#    and concavity.
#   
# The above simple approach would only recognize constraints that are valid for
# the whole input space. However, for e.g. Feynman2 (I.6.20a), the probabilistic density
# function of the normal distribution with $\mu=0$ and $\sigma=1$, the function
# is monotonic non-decreasing for values of $theta \leq 0$ and monotonic
# non-increasing for values of $theta \geq 0$. See
# examples/data/checking_constraints.ipynb for a visual explanation.
#
# To advance this simple approach, instead, all gradients are calculated for the
# whole input data and a decision tree classifier is employed to find suitable
# cutting points for the input space. We restrict the tree size to prevent large
# numbers of found constraints (especially with cyclic changes of
# gradients in trigonometric functions and multiples of pi).

def tree_to_constraints(clf, node, bounds):
    # Recursively traverse the decision tree to extract constraints
    
    if clf.tree_.children_left[node] == -1:
        # leaf node is reached, stop traverse
        if clf.tree_.value[node][0][0] == 1: 
            # internal array representation of trees. If class [0] is certain ==1, it is negative
            return [(bounds, sk.EQUATION_CONSTRAINTS_DESCRIPTOR_NEGATIVE)]
        if clf.tree_.value[node][0][1] == 1:
            # internal array representation of trees. If class [1] is certain ==1, it is positive
            return [(bounds, sk.EQUATION_CONSTRAINTS_DESCRIPTOR_POSITIVE)]
        raise 'ERROR Class not considered' 
        # return None
    
    # not a leaf node: split bounds on current threshold 
    # to recursively traverse to leafs
    bleft = bounds.copy() #copy existing bounds for left
    bright = bounds.copy() # and right tree

    #extract selected feature and threshold of the feature
    f = clf.tree_.feature[node]
    s = clf.tree_.threshold[node]

    # split bounds on the feature used for distinction
    # replace the resulting bounds for the feature with the threshold
    bleft[f] = (bounds[f][0], s)
    bright[f] = (s, bounds[f][1])

    # traverse left and right subtree and combine results
    return [x for x in tree_to_constraints(clf, clf.tree_.children_left[node], bleft)] + \
           [x for x in tree_to_constraints(clf, clf.tree_.children_right[node], bright)]

def evaluate_equation(eq, local_dict, xs):
    # Evaluate the equation for each row in the dataset
    f = sympy.lambdify(local_dict, eq, "numpy")
    #calculate gradient per data point
    # old: 
    #   gradients = np.array([ f(*row) for row in xs ])
    # speedup of 5:
    def l(x):
        return f(*x)
    return xs.apply(l, axis=1, raw=True)

def range_to_space(range, names):
    # Convert range to a sampling space dictionary
    return [{'name': str(names[i]),
             'low': float(range[i][0]),
             'high': float(range[i][1])} 
            for i in range]

constraints_textual = []
for equation_dictionary_entry in srsdf.AllEquations:
    bench = Benchmark(srsdf.AllEquations[equation_dictionary_entry], initialize_constraint_checking_datasets=False)
    
    print(bench.equation.get_eq_name())

    # generate large set of data for the full input space
    variable_display_names = bench.equation.get_var_names()
    variable_names = [str(var) for var in bench.equation.x]
    data = pd.DataFrame(create_dataset_from_sampling_objectives(
                            # replace the actual standard sampling targets with their respective uniform variant
                            [samp.to_uniform_sampling() for samp in bench.equation.sampling_objs], 
                            bench.equation.sympy_eq, 
                            bench.equation.eq_func, 
                            bench.equation.check_if_valid, 
                            CONSTRAINT_SAMPLING_SIZE,
                            patience=CONSTRAINT_SAMPLING_SIZE), 
                        columns=variable_display_names + ["target"])

    # function itself to calculate image
    f = [(bench.equation.sympy_eq, "", "", 0)] 

    # first-order derivatives    
    f_primes = [(sympy.Derivative(bench.equation.sympy_eq, var, 1).doit(), var.name, var_display_name, 1) 
                for (var, var_display_name) 
                in list(zip(bench.equation.x, bench.equation.get_var_names()))]
    
    # second-order derivatives
    f_seconds = [(sympy.Derivative(bench.equation.sympy_eq, var, 2).doit(), var.name, var_display_name, 2) 
                 for (var, var_display_name) 
                 in list(zip(bench.equation.x, bench.equation.get_var_names()))]
    
    # combine all for subsequent checks
    f_all = f + f_primes + f_seconds 

    constraints = []

    vars = [(x, y.get_value_range()) for (x, y) in zip(variable_names, bench.equation.sampling_objs)]
    ranges = {i: (x[1][0], x[1][1]) for i, x in enumerate(vars)}

    for derivative, variable, variable_name, degree in f_all:
        derivative_name_id = f'{variable_name}_{degree}'
        gradient_sign_id = f'{variable_name} {degree} sign'

        data[derivative_name_id] = evaluate_equation(derivative, bench.equation.x, data[variable_display_names])
        data[gradient_sign_id] = np.sign(data[derivative_name_id])

        d1 = data[data[gradient_sign_id] != 0] # remove all gradients of 0 as we do not care for strong monotonicity
        classes = np.unique(d1[gradient_sign_id])

        if len(classes) <= 1:
            # Gradients are either all zero, all negative valued, or all positive valued.
            if len(classes) == 0: # no gradients remain -> all were zero
                constraint_descriptor = sk.EQUATION_CONSTRAINTS_DESCRIPTOR_ZERO
            elif len(classes) == 1:  # only one type of gradient in the data
                if classes[0] == 1: # 1 is sign positive
                    constraint_descriptor = sk.EQUATION_CONSTRAINTS_DESCRIPTOR_POSITIVE    
                else:  # -1 is sign negative
                    constraint_descriptor = sk.EQUATION_CONSTRAINTS_DESCRIPTOR_NEGATIVE  
               
            constraints.append({
                sk.EQUATION_CONSTRAINTS_VAR_NAME_KEY: variable,
                sk.EQUATION_CONSTRAINTS_VAR_DISPLAY_NAME_KEY: variable_name,
                sk.EQUATION_CONSTRAINTS_ORDER_DERIVATIVE_KEY: degree,
                sk.EQUATION_CONSTRAINTS_DESCRIPTOR_KEY: constraint_descriptor,
                sk.EQUATION_CONSTRAINTS_DERIVATIVE_KEY: str(derivative),
                # use original space of the full input domain as specified by the
                # benchmark as constraint is valid for the full domain 
                sk.EQUATION_CONSTRAINTS_SAMPLE_SPACE_KEY: [{'name': str(var),
                                                            'low': float(range[0]),
                                                            'high': float(range[1])} 
                                                           for (var, range) in vars],
                sk.EQUATION_CONSTRAINTS_ID_KEY: len(constraints)  
            })
        else: 
            # Gradient switches at unknown domain subspaces. We use a decision
            # tree to find suitable cutting points for subspaces but restrict
            # the decision tree to depth of 2 as we desire only meaningful cuts.
            # e.g. most often, the sign changes at 0 or at multiples of pi for
            # equations with trigonometric functions.
            
            clf = tree.DecisionTreeClassifier(max_depth=2)
            clf = clf.fit(d1[variable_display_names], d1[gradient_sign_id]) 

            if clf.score(d1[variable_display_names], d1[gradient_sign_id]) >= (1 - (1 / CONSTRAINT_SAMPLING_SIZE)):
                # continue only if gradients could be easily separated along the
                # input domain
                for (range, constraint_descriptor) in tree_to_constraints(clf, 0, ranges):
                    # traversing tree and returning constraints
                    s = range_to_space(range, bench.equation.x)
                    constraints.append({
                        sk.EQUATION_CONSTRAINTS_VAR_NAME_KEY: variable,
                        sk.EQUATION_CONSTRAINTS_VAR_DISPLAY_NAME_KEY: variable_name,
                        sk.EQUATION_CONSTRAINTS_ORDER_DERIVATIVE_KEY: degree,
                        sk.EQUATION_CONSTRAINTS_DESCRIPTOR_KEY: constraint_descriptor,
                        sk.EQUATION_CONSTRAINTS_DERIVATIVE_KEY: str(derivative),
                        # use the divided subspace for the constraint as
                        # gradients changed for certain cutting points
                        sk.EQUATION_CONSTRAINTS_SAMPLE_SPACE_KEY: s,
                        sk.EQUATION_CONSTRAINTS_ID_KEY: len(constraints)  
                    })

    constraints_textual.append(str({sk.EQUATION_EQUATION_NAME_KEY: bench.equation.get_eq_name(),
                                    sk.EQUATION_CONSTRAINTS_CONSTRAINTS_KEY: constraints}).replace('\'', '\"'))

with open("generate/feynman_srsdf_constraint_info.json", "w") as text_file:
    text_file.write('[')
    text_file.write(',\n'.join(constraints_textual))
    text_file.write(']')