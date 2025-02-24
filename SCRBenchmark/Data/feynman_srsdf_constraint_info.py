SRSD_EQUATION_CONSTRAINTS = [
  {
    "EquationName": "FeynmanICh6Eq20",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "sqrt(2)*exp(-x0**2/(2*x1**2))/(2*sqrt(pi)*x1)",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": -0.1
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "sqrt(2)*exp(-x0**2/(2*x1**2))/(2*sqrt(pi)*x1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "theta",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-sqrt(2)*x0*exp(-x0**2/(2*x1**2))/(2*sqrt(pi)*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "theta",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-sqrt(2)*x0*exp(-x0**2/(2*x1**2))/(2*sqrt(pi)*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 3
      }
    ]
  },
  {
    "EquationName": "FeynmanICh6Eq20a",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "sqrt(2)*exp(-x0**2/2)/(2*sqrt(pi))",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "theta",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-sqrt(2)*x0*exp(-x0**2/2)/(2*sqrt(pi))",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 0.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "theta",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-sqrt(2)*x0*exp(-x0**2/2)/(2*sqrt(pi))",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 10.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "theta",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "sqrt(2)*(x0**2 - 1)*exp(-x0**2/2)/(2*sqrt(pi))",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": -1.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "theta",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "sqrt(2)*(x0**2 - 1)*exp(-x0**2/2)/(2*sqrt(pi))",
        "sample_space": [
          {
            "name": "x0",
            "low": -1.0,
            "high": 1.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x0",
        "var_display_name": "theta",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "sqrt(2)*(x0**2 - 1)*exp(-x0**2/2)/(2*sqrt(pi))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 10.0
          }
        ],
        "id": 5
      }
    ]
  },
  {
    "EquationName": "FeynmanICh6Eq20b",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "sqrt(2)*exp(-(x0 - x1)**2/(2*x2**2))/(2*sqrt(pi))",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x2",
        "var_display_name": "sigma",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "sqrt(2)*(x0 - x1)**2*exp(-(x0 - x1)**2/(2*x2**2))/(2*sqrt(pi)*x2**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 1
      }
    ]
  },
  {
    "EquationName": "FeynmanICh8Eq14",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "sqrt((x0 - x1)**2 + (x2 - x3)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "x2",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "(-(x0 - x1)**2/((x0 - x1)**2 + (x2 - x3)**2) + 1)/sqrt((x0 - x1)**2 + (x2 - x3)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "x1",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "(-(x0 - x1)**2/((x0 - x1)**2 + (x2 - x3)**2) + 1)/sqrt((x0 - x1)**2 + (x2 - x3)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x2",
        "var_display_name": "y2",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "(-(x2 - x3)**2/((x0 - x1)**2 + (x2 - x3)**2) + 1)/sqrt((x0 - x1)**2 + (x2 - x3)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x3",
        "var_display_name": "y1",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "(-(x2 - x3)**2/((x0 - x1)**2 + (x2 - x3)**2) + 1)/sqrt((x0 - x1)**2 + (x2 - x3)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 4
      }
    ]
  },
  {
    "EquationName": "FeynmanICh9Eq18",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "6.6743e-11*x0*x1/((x2 - x3)**2 + (x4 - x5)**2 + (x6 - x7)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x7",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "m1",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "6.6743e-11*x1/((x2 - x3)**2 + (x4 - x5)**2 + (x6 - x7)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x7",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "m2",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "6.6743e-11*x0/((x2 - x3)**2 + (x4 - x5)**2 + (x6 - x7)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x7",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "m1",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x7",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "m2",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x7",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 4
      }
    ]
  },
  {
    "EquationName": "FeynmanICh10Eq7",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 100000.0,
            "high": 100000000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "m_0",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 100000.0,
            "high": 100000000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.11265005605362e-17*x0*x1/(1 - 1.11265005605362e-17*x1**2)**(3/2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 100000.0,
            "high": 100000000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "m_0",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 100000.0,
            "high": 100000000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "-x0*(3.71397044170836e-34*x1**2/(1.11265005605362e-17*x1**2 - 1) - 1.11265005605362e-17)/(1 - 1.11265005605362e-17*x1**2)**(3/2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 100000.0,
            "high": 100000000.0
          }
        ],
        "id": 4
      }
    ]
  },
  {
    "EquationName": "FeynmanICh11Eq19",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "x1",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x1",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 0.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "x1",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x1",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "y1",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x0",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "y1",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x2",
        "var_display_name": "x2",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x3",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 0.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x2",
        "var_display_name": "x2",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x3",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x3",
        "var_display_name": "y2",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x2",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x3",
        "var_display_name": "y2",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x2",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 7
      },
      {
        "var_name": "x4",
        "var_display_name": "x3",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x5",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 0.0
          }
        ],
        "id": 8
      },
      {
        "var_name": "x4",
        "var_display_name": "x3",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x5",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 0.0,
            "high": 10.0
          }
        ],
        "id": 9
      },
      {
        "var_name": "x5",
        "var_display_name": "y3",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x4",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 0.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 10
      },
      {
        "var_name": "x5",
        "var_display_name": "y3",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x4",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": 0.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 11
      },
      {
        "var_name": "x0",
        "var_display_name": "x1",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 12
      },
      {
        "var_name": "x1",
        "var_display_name": "y1",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 13
      },
      {
        "var_name": "x2",
        "var_display_name": "x2",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 14
      },
      {
        "var_name": "x3",
        "var_display_name": "y2",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 15
      },
      {
        "var_name": "x4",
        "var_display_name": "x3",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 16
      },
      {
        "var_name": "x5",
        "var_display_name": "y3",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 17
      }
    ]
  },
  {
    "EquationName": "FeynmanICh12Eq1",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0*x1",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "mu",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x1",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "Nn",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "mu",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "Nn",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 4
      }
    ]
  },
  {
    "EquationName": "FeynmanICh12Eq2",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "q1",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "28235825615.541*x1/(pi*x2**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 0.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "q1",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "28235825615.541*x1/(pi*x2**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "q2",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "28235825615.541*x0/(pi*x2**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "q2",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "28235825615.541*x0/(pi*x2**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "q1",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "q2",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 5
      }
    ]
  },
  {
    "EquationName": "FeynmanICh12Eq4",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "28235825615.541*x0/(pi*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "28235825615.541*x0/(pi*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "q1",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "28235825615.541/(pi*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-56471651231.082*x0/(pi*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-56471651231.082*x0/(pi*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x0",
        "var_display_name": "q1",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "169414953693.246*x0/(pi*x1**4)",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "169414953693.246*x0/(pi*x1**4)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 7
      }
    ]
  },
  {
    "EquationName": "FeynmanICh12Eq5",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "q2",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x1",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 0.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "q2",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x1",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 10.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "Ef",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x0",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "Ef",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "q2",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "Ef",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 5
      }
    ]
  },
  {
    "EquationName": "FeynmanICh12Eq11",
    "Constraints": [
      {
        "var_name": "x1",
        "var_display_name": "Ef",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x0",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 0
      },
      {
        "var_name": "x1",
        "var_display_name": "Ef",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "Ef",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 3
      },
      {
        "var_name": "x2",
        "var_display_name": "B",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 4
      },
      {
        "var_name": "x3",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 5
      }
    ]
  },
  {
    "EquationName": "FeynmanICh13Eq4",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "0.5*x0*(x1**2 + x2**2 + x3**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "m",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "0.5*x1**2 + 0.5*x2**2 + 0.5*x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "1.0*x0*x1",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 0.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.0*x0*x1",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x2",
        "var_display_name": "u",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "1.0*x0*x2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x2",
        "var_display_name": "u",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.0*x0*x2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x3",
        "var_display_name": "w",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "1.0*x0*x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 0.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x3",
        "var_display_name": "w",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.0*x0*x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 10.0
          }
        ],
        "id": 7
      },
      {
        "var_name": "x0",
        "var_display_name": "m",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 8
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "1.0*x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 9
      },
      {
        "var_name": "x2",
        "var_display_name": "u",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "1.0*x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 10
      },
      {
        "var_name": "x3",
        "var_display_name": "w",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "1.0*x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 11
      }
    ]
  },
  {
    "EquationName": "FeynmanICh13Eq12",
    "Constraints": [
      {
        "var_name": "x2",
        "var_display_name": "r2",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-6.6743e-11*x0*x1/x2**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x3",
        "var_display_name": "r1",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "6.6743e-11*x0*x1/x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "m1",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "m2",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x2",
        "var_display_name": "r2",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "1.33486e-10*x0*x1/x2**3",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x3",
        "var_display_name": "r1",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-1.33486e-10*x0*x1/x3**3",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 5
      }
    ]
  },
  {
    "EquationName": "FeynmanICh14Eq3",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "9.80665*x0*x1",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": -1.0,
            "high": 0.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "9.80665*x0*x1",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 1.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "m",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "9.80665*x1",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": -1.0,
            "high": 0.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "m",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "9.80665*x1",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 1.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "z",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "9.80665*x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": -1.0,
            "high": 1.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x0",
        "var_display_name": "m",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": -1.0,
            "high": 1.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x1",
        "var_display_name": "z",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": -1.0,
            "high": 1.0
          }
        ],
        "id": 6
      }
    ]
  },
  {
    "EquationName": "FeynmanICh14Eq4",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "0.5*x0*x1**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 100.0,
            "high": 10000.0
          },
          {
            "name": "x1",
            "low": -1.0,
            "high": 1.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "k_spring",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "0.5*x1**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 100.0,
            "high": 10000.0
          },
          {
            "name": "x1",
            "low": -1.0,
            "high": 1.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "x",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "1.0*x0*x1",
        "sample_space": [
          {
            "name": "x0",
            "low": 100.0,
            "high": 10000.0
          },
          {
            "name": "x1",
            "low": -1.0,
            "high": 0.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "x",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.0*x0*x1",
        "sample_space": [
          {
            "name": "x0",
            "low": 100.0,
            "high": 10000.0
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 1.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "k_spring",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 100.0,
            "high": 10000.0
          },
          {
            "name": "x1",
            "low": -1.0,
            "high": 1.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "x",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "1.0*x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 100.0,
            "high": 10000.0
          },
          {
            "name": "x1",
            "low": -1.0,
            "high": 1.0
          }
        ],
        "id": 5
      }
    ]
  },
  {
    "EquationName": "FeynmanICh15Eq10",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "x0*x1/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 0.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0*x1/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 10000000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "m_0",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x1/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 0.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "m_0",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x1/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 10000000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.11265005605362e-17*x0*x1**2/(1 - 1.11265005605362e-17*x1**2)**(3/2) + x0/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x0",
        "var_display_name": "m_0",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "x0*x1*(-3.71397044170836e-34*x1**2/(1.11265005605362e-17*x1**2 - 1) + 3.33795016816086e-17)/(1 - 1.11265005605362e-17*x1**2)**(3/2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 0.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "x0*x1*(-3.71397044170836e-34*x1**2/(1.11265005605362e-17*x1**2 - 1) + 3.33795016816086e-17)/(1 - 1.11265005605362e-17*x1**2)**(3/2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 10000000.0
          }
        ],
        "id": 7
      }
    ]
  },
  {
    "EquationName": "FeynmanICh15Eq3t",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "(x0 - 1.11265005605362e-17*x1*x2)/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-06,
            "high": 0.0001
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "t",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-06,
            "high": 0.0001
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x2",
        "var_display_name": "x",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-1.11265005605362e-17*x1/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-06,
            "high": 0.0001
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 0.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x2",
        "var_display_name": "x",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-1.11265005605362e-17*x1/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-06,
            "high": 0.0001
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "t",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-06,
            "high": 0.0001
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "u",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "-(2.47598029447224e-34*x1*x2 + (x0 - 1.11265005605362e-17*x1*x2)*(3.71397044170836e-34*x1**2/(1.11265005605362e-17*x1**2 - 1) - 1.11265005605362e-17))/(1 - 1.11265005605362e-17*x1**2)**(3/2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-06,
            "high": 0.0001
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "x",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-06,
            "high": 0.0001
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          }
        ],
        "id": 6
      }
    ]
  },
  {
    "EquationName": "FeynmanICh15Eq3x",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "x",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100.0,
            "high": 100.0
          },
          {
            "name": "x1",
            "low": -100000000.0,
            "high": 100000000.0
          },
          {
            "name": "x2",
            "low": 1e-06,
            "high": 0.0001
          }
        ],
        "id": 0
      },
      {
        "var_name": "x1",
        "var_display_name": "u",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "1.11265005605362e-17*x1*(x0 - x1*x2)/(1 - 1.11265005605362e-17*x1**2)**(3/2) - x2/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100.0,
            "high": 100.0
          },
          {
            "name": "x1",
            "low": -100000000.0,
            "high": 100000000.0
          },
          {
            "name": "x2",
            "low": 1e-06,
            "high": 0.0001
          }
        ],
        "id": 1
      },
      {
        "var_name": "x2",
        "var_display_name": "t",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-x1/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100.0,
            "high": 100.0
          },
          {
            "name": "x1",
            "low": -100000000.0,
            "high": 0.0
          },
          {
            "name": "x2",
            "low": 1e-06,
            "high": 0.0001
          }
        ],
        "id": 2
      },
      {
        "var_name": "x2",
        "var_display_name": "t",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-x1/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100.0,
            "high": 100.0
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 100000000.0
          },
          {
            "name": "x2",
            "low": 1e-06,
            "high": 0.0001
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "x",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -100.0,
            "high": 100.0
          },
          {
            "name": "x1",
            "low": -100000000.0,
            "high": 100000000.0
          },
          {
            "name": "x2",
            "low": 1e-06,
            "high": 0.0001
          }
        ],
        "id": 4
      },
      {
        "var_name": "x2",
        "var_display_name": "t",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -100.0,
            "high": 100.0
          },
          {
            "name": "x1",
            "low": -100000000.0,
            "high": 100000000.0
          },
          {
            "name": "x2",
            "low": 1e-06,
            "high": 0.0001
          }
        ],
        "id": 5
      }
    ]
  },
  {
    "EquationName": "FeynmanICh16Eq6",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "u",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-1.11265005605362e-17*x1*(x0 + x1)/(1.11265005605362e-17*x0*x1 + 1)**2 + 1/(1.11265005605362e-17*x0*x1 + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100000000.0,
            "high": 100000000.0
          },
          {
            "name": "x1",
            "low": -100000000.0,
            "high": 100000000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-1.11265005605362e-17*x0*(x0 + x1)/(1.11265005605362e-17*x0*x1 + 1)**2 + 1/(1.11265005605362e-17*x0*x1 + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100000000.0,
            "high": 100000000.0
          },
          {
            "name": "x1",
            "low": -100000000.0,
            "high": 100000000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "u",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "x1*(2.47598029447224e-34*x1*(x0 + x1)/(1.11265005605362e-17*x0*x1 + 1) - 2.22530011210724e-17)/(1.11265005605362e-17*x0*x1 + 1)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": -100000000.0,
            "high": 100000000.0
          },
          {
            "name": "x1",
            "low": -100000000.0,
            "high": 0.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "u",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "x1*(2.47598029447224e-34*x1*(x0 + x1)/(1.11265005605362e-17*x0*x1 + 1) - 2.22530011210724e-17)/(1.11265005605362e-17*x0*x1 + 1)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": -100000000.0,
            "high": 100000000.0
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 100000000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "x0*(2.47598029447224e-34*x0*(x0 + x1)/(1.11265005605362e-17*x0*x1 + 1) - 2.22530011210724e-17)/(1.11265005605362e-17*x0*x1 + 1)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": -100000000.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": -100000000.0,
            "high": 100000000.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "x0*(2.47598029447224e-34*x0*(x0 + x1)/(1.11265005605362e-17*x0*x1 + 1) - 2.22530011210724e-17)/(1.11265005605362e-17*x0*x1 + 1)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 100000000.0
          },
          {
            "name": "x1",
            "low": -100000000.0,
            "high": 100000000.0
          }
        ],
        "id": 5
      }
    ]
  },
  {
    "EquationName": "FeynmanICh18Eq4",
    "Constraints": [
      {
        "var_name": "x1",
        "var_display_name": "r1",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0/(x0 + x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x3",
        "var_display_name": "r2",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x2/(x0 + x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "r1",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x3",
        "var_display_name": "r2",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 3
      }
    ]
  },
  {
    "EquationName": "FeynmanICh18Eq12",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0*x1*sin(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.1415926535897932 # PI
            # "high": 3.1415926535897932 # PI
            # "high": 3.1416133642196655 
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "x0*x1*sin(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 3.1415926535897932, # PI
            # "low": 3.1416133642196655,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x1*sin(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.1416133642196655
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x1*sin(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 3.1415926535897932, # PI
            # "low": 3.1416133642196655,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "F",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*sin(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.1416133642196655
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "F",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x0*sin(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 3.1415926535897932, # PI
            # "low": 3.1416133642196655,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "theta",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*x1*cos(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 1.5707963267948966, # 0.5pi 
            # "high": 1.5708144903182983
          }
        ],
        "id": 6
      },
      {
        "var_name": "x2",
        "var_display_name": "theta",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x0*x1*cos(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 1.5707963267948966, # 0.5pi 
            # "low": 1.5708144903182983,
            "high": 4.7123889803846898 # 1.5pi 
            # "high": 4.7124412059783936
          }
        ],
        "id": 7
      },
      {
        "var_name": "x2",
        "var_display_name": "theta",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*x1*cos(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 4.7123889803846898, # 1.5pi 
            # "low": 4.7124412059783936,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 8
      },
      {
        "var_name": "x0",
        "var_display_name": "r",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 9
      },
      {
        "var_name": "x1",
        "var_display_name": "F",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 10
      },
      {
        "var_name": "x2",
        "var_display_name": "theta",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-x0*x1*sin(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.1416133642196655
          }
        ],
        "id": 11
      },
      {
        "var_name": "x2",
        "var_display_name": "theta",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "-x0*x1*sin(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 3.1415926535897932, # PI
            # "low": 3.1416133642196655,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 12
      }
    ]
  },
  {
    "EquationName": "FeynmanICh18Eq16",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0*x1*x2*sin(x3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141595244407654
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "x0*x1*x2*sin(x3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 3.1415926535897932, # PI
            # "low": 3.141595244407654,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "m",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x1*x2*sin(x3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141595244407654
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "m",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x1*x2*sin(x3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 3.1415926535897932, # PI
            # "low": 3.141595244407654,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*x2*sin(x3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141595244407654
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x0*x2*sin(x3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 3.1415926535897932, # PI
            # "low": 3.141595244407654,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*x1*sin(x3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141595244407654
          }
        ],
        "id": 6
      },
      {
        "var_name": "x2",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x0*x1*sin(x3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 3.1415926535897932, # PI
            # "low": 3.141595244407654,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 7
      },
      {
        "var_name": "x3",
        "var_display_name": "theta",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*x1*x2*cos(x3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 1.5707963267948966, # 0.5pi 
            # "high": 1.5707734823226929
          }
        ],
        "id": 8
      },
      {
        "var_name": "x3",
        "var_display_name": "theta",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x0*x1*x2*cos(x3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 1.5707963267948966, # 0.5pi 
            # "low": 1.5707734823226929,
            "high": 4.7123889803846898 # 1.5pi 
            # "high": 4.712395429611206
          }
        ],
        "id": 9
      },
      {
        "var_name": "x3",
        "var_display_name": "theta",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*x1*x2*cos(x3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 4.7123889803846898, # 1.5pi 
            # "low": 4.712395429611206,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 10
      },
      {
        "var_name": "x0",
        "var_display_name": "m",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 11
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 12
      },
      {
        "var_name": "x2",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 13
      },
      {
        "var_name": "x3",
        "var_display_name": "theta",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-x0*x1*x2*sin(x3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141595244407654
          }
        ],
        "id": 14
      },
      {
        "var_name": "x3",
        "var_display_name": "theta",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "-x0*x1*x2*sin(x3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 3.1415926535897932, # PI
            # "low": 3.141595244407654,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 15
      }
    ]
  },
  {
    "EquationName": "FeynmanICh24Eq6",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "0.25*x0*x3**2*(x1**2 + x2**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "m",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "0.25*x3**2*(x1**2 + x2**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "omega",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "0.5*x0*x1*x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 0.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "omega",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "0.5*x0*x1*x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x2",
        "var_display_name": "omega_0",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "0.5*x0*x2*x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x2",
        "var_display_name": "omega_0",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "0.5*x0*x2*x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x3",
        "var_display_name": "x",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "0.5*x0*x3*(x1**2 + x2**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 0.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x3",
        "var_display_name": "x",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "0.5*x0*x3*(x1**2 + x2**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 10.0
          }
        ],
        "id": 7
      },
      {
        "var_name": "x0",
        "var_display_name": "m",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 8
      },
      {
        "var_name": "x1",
        "var_display_name": "omega",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "0.5*x0*x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 9
      },
      {
        "var_name": "x2",
        "var_display_name": "omega_0",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "0.5*x0*x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 10
      },
      {
        "var_name": "x3",
        "var_display_name": "x",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "0.5*x0*(x1**2 + x2**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 11
      }
    ]
  },
  {
    "EquationName": "FeynmanICh25Eq13",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "x0/x1",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.001,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0/x1",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.001
          },
          {
            "name": "x1",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1/x1",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.001,
            "high": 0.001
          },
          {
            "name": "x1",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "C",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-x0/x1**2",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.001,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "C",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-x0/x1**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.001
          },
          {
            "name": "x1",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 4
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.001,
            "high": 0.001
          },
          {
            "name": "x1",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 5
      },
      {
        "var_name": "x1",
        "var_display_name": "C",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "2*x0/x1**3",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.001,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 6
      },
      {
        "var_name": "x1",
        "var_display_name": "C",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "2*x0/x1**3",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.001
          },
          {
            "name": "x1",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 7
      }
    ]
  },
  {
    "EquationName": "FeynmanICh26Eq2",
    "Constraints": []
  },
  {
    "EquationName": "FeynmanICh27Eq6",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "1/(x1/x2 + 1/x0)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 10.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "d1",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1/(x0**2*(x1/x2 + 1/x0)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 10.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "n",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-1/(x2*(x1/x2 + 1/x0)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 10.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x2",
        "var_display_name": "d2",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x1/(x2**2*(x1/x2 + 1/x0)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 10.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "d1",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "2*(-1 + 1/(x0*(x1/x2 + 1/x0)))/(x0**3*(x1/x2 + 1/x0)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 10.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "n",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "2/(x2**2*(x1/x2 + 1/x0)**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 10.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "d2",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "2*x1*(x1/(x2*(x1/x2 + 1/x0)) - 1)/(x2**3*(x1/x2 + 1/x0)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 10.0
          }
        ],
        "id": 6
      }
    ]
  },
  {
    "EquationName": "FeynmanICh29Eq4",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "3.33564095198152e-9*x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "omega",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "3.33564095198152e-9",
        "sample_space": [
          {
            "name": "x0",
            "low": 1000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "omega",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 2
      }
    ]
  },
  {
    "EquationName": "FeynmanICh29Eq16",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "sqrt(x0**2 + 2*x0*x1*cos(x2 - x3) + x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "x1",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "(-(x0 + x1*cos(x2 - x3))**2/(x0**2 + 2*x0*x1*cos(x2 - x3) + x1**2) + 1)/sqrt(x0**2 + 2*x0*x1*cos(x2 - x3) + x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "x2",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "(-(x0*cos(x2 - x3) + x1)**2/(x0**2 + 2*x0*x1*cos(x2 - x3) + x1**2) + 1)/sqrt(x0**2 + 2*x0*x1*cos(x2 - x3) + x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 2
      }
    ]
  },
  {
    "EquationName": "FeynmanICh30Eq3",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0*sin(x1*x2/2)**2/sin(x2/2)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": -6.283185307179586,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "Int_0",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "sin(x1*x2/2)**2/sin(x2/2)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": -6.283185307179586,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "Int_0",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": -6.283185307179586,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 2
      }
    ]
  },
  {
    "EquationName": "FeynmanICh30Eq5",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0/(x1*sin(x2))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-11,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141620635986328
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "x0/(x1*sin(x2))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-11,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 3.1415926535897932, # PI
            # "low": 3.141620635986328,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "lambda",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1/(x1*sin(x2))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-11,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141620635986328
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "lambda",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "1/(x1*sin(x2))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-11,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 3.1415926535897932, # PI
            # "low": 3.141620635986328,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "n",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-x0/(x1**2*sin(x2))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-11,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141620635986328
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "n",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-x0/(x1**2*sin(x2))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-11,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 3.1415926535897932, # PI
            # "low": 3.141620635986328,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "theta",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-x0*cos(x2)/(x1*sin(x2)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-11,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 1.5707963267948966, # 0.5pi 
            # "high": 1.5707963109016418
          }
        ],
        "id": 6
      },
      {
        "var_name": "x2",
        "var_display_name": "theta",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-x0*cos(x2)/(x1*sin(x2)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-11,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1.5707963267948966, # 0.5pi 
            # "low": 1.5707963109016418,
            "high": 4.7123889803846898 # 1.5pi 
            # "high": 4.712378025054932
          }
        ],
        "id": 7
      },
      {
        "var_name": "x2",
        "var_display_name": "theta",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-x0*cos(x2)/(x1*sin(x2)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-11,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 4.7123889803846898, # 1.5pi 
            # "low": 4.712378025054932,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 8
      },
      {
        "var_name": "x0",
        "var_display_name": "lambda",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-11,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 9
      },
      {
        "var_name": "x1",
        "var_display_name": "n",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "2*x0/(x1**3*sin(x2))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-11,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141620635986328
          }
        ],
        "id": 10
      },
      {
        "var_name": "x1",
        "var_display_name": "n",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "2*x0/(x1**3*sin(x2))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-11,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 3.1415926535897932, # PI
            # "low": 3.141620635986328,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 11
      },
      {
        "var_name": "x2",
        "var_display_name": "theta",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "x0*(1 + 2*cos(x2)**2/sin(x2)**2)/(x1*sin(x2))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-11,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141620635986328
          }
        ],
        "id": 12
      },
      {
        "var_name": "x2",
        "var_display_name": "theta",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "x0*(1 + 2*cos(x2)**2/sin(x2)**2)/(x1*sin(x2))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-11,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 3.1415926535897932, # PI
            # "low": 3.141620635986328,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 13
      }
    ]
  },
  {
    "EquationName": "FeynmanICh32Eq5",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "6.9862982685735e-16*x0**2*x1**2/pi",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 100000.0,
            "high": 10000000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "1.3972596537147e-15*x0*x1**2/pi",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 100000.0,
            "high": 10000000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.3972596537147e-15*x0*x1**2/pi",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 100000.0,
            "high": 10000000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "a",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.3972596537147e-15*x0**2*x1/pi",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 100000.0,
            "high": 10000000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "1.3972596537147e-15*x1**2/pi",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 100000.0,
            "high": 10000000.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "a",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "1.3972596537147e-15*x0**2/pi",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 100000.0,
            "high": 10000000.0
          }
        ],
        "id": 5
      }
    ]
  },
  {
    "EquationName": "FeynmanICh32Eq17",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "0.00353914989750933*pi*x0**2*x1**2*x2**4/(x2**2 - x3**2)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": -100000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x3",
            "low": -100000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "Ef",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "0.00707829979501867*pi*x0*x1**2*x2**4/(x2**2 - x3**2)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": -100000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x3",
            "low": -100000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "Ef",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "0.00707829979501867*pi*x0*x1**2*x2**4/(x2**2 - x3**2)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": -100000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x3",
            "low": -100000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "0.00707829979501867*pi*x0**2*x1*x2**4/(x2**2 - x3**2)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": -100000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x3",
            "low": -100000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "Ef",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "0.00707829979501867*pi*x1**2*x2**4/(x2**2 - x3**2)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": -100000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x3",
            "low": -100000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "0.00707829979501867*pi*x0**2*x2**4/(x2**2 - x3**2)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": -100000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x3",
            "low": -100000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "omega",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "pi*x0**2*x1**2*x2**2*(0.0141565995900373*x2**2*(6*x2**2/(x2**2 - x3**2) - 1)/(x2**2 - x3**2) - 0.113252796720299*x2**2/(x2**2 - x3**2) + 0.042469798770112)/(x2**2 - x3**2)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": -100000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x3",
            "low": -100000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x3",
        "var_display_name": "omega_0",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "0.0141565995900373*pi*x0**2*x1**2*x2**4*(6*x3**2/(x2**2 - x3**2) + 1)/(x2**2 - x3**2)**3",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": -100000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x3",
            "low": -100000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 7
      }
    ]
  },
  {
    "EquationName": "FeynmanICh34Eq10",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0/(1 - 3.33564095198152e-9*x1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "omega_0",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1/(1 - 3.33564095198152e-9*x1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "3.33564095198152e-9*x0/(1 - 3.33564095198152e-9*x1)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "omega_0",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "-2.22530011210724e-17*x0/(3.33564095198152e-9*x1 - 1)**3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          }
        ],
        "id": 4
      }
    ]
  },
  {
    "EquationName": "FeynmanICh34Eq8",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": -100000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": -100000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x2",
        "var_display_name": "B",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": -100000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 2
      }
    ]
  },
  {
    "EquationName": "FeynmanICh34Eq14",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x1*(3.33564095198152e-9*x0 + 1)/sqrt(1 - 1.11265005605362e-17*x0**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100000000.0,
            "high": 100000000.0
          },
          {
            "name": "x1",
            "low": 1000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.11265005605362e-17*x0*x1*(3.33564095198152e-9*x0 + 1)/(1 - 1.11265005605362e-17*x0**2)**(3/2) + 3.33564095198152e-9*x1/sqrt(1 - 1.11265005605362e-17*x0**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100000000.0,
            "high": 100000000.0
          },
          {
            "name": "x1",
            "low": 1000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "omega_0",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "(3.33564095198152e-9*x0 + 1)/sqrt(1 - 1.11265005605362e-17*x0**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100000000.0,
            "high": 100000000.0
          },
          {
            "name": "x1",
            "low": 1000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "x1*(7.42280218439397e-26*x0 - (3.33564095198152e-9*x0 + 1)*(3.71397044170836e-34*x0**2/(1.11265005605362e-17*x0**2 - 1) - 1.11265005605362e-17))/(1 - 1.11265005605362e-17*x0**2)**(3/2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100000000.0,
            "high": 100000000.0
          },
          {
            "name": "x1",
            "low": 1000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "omega_0",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -100000000.0,
            "high": 100000000.0
          },
          {
            "name": "x1",
            "low": 1000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 4
      }
    ]
  },
  {
    "EquationName": "FeynmanICh34Eq27",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "3.313e-34*x0/pi",
        "sample_space": [
          {
            "name": "x0",
            "low": 1000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "omega",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "3.313e-34/pi",
        "sample_space": [
          {
            "name": "x0",
            "low": 1000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "omega",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 2
      }
    ]
  },
  {
    "EquationName": "FeynmanICh37Eq4",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0 + x1 + 2*sqrt(x0*x1)*cos(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 0
      },
      {
        "var_name": "x2",
        "var_display_name": "delta",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-2*sqrt(x0*x1)*sin(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.1415518522262573
          }
        ],
        "id": 1
      },
      {
        "var_name": "x2",
        "var_display_name": "delta",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-2*sqrt(x0*x1)*sin(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 3.1415926535897932, # PI
            # "low": 3.1415518522262573,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "I1",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-sqrt(x0*x1)*cos(x2)/(2*x0**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 1.5707963267948966, # 0.5pi 
            # "high": 1.570838749408722
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "I1",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "-sqrt(x0*x1)*cos(x2)/(2*x0**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 1.5707963267948966, # 0.5pi 
            # "low": 1.570838749408722,
            "high": 4.7123889803846898 # 1.5pi 
            # "high": 4.712414503097534
          }
        ],
        "id": 4
      },
      {
        "var_name": "x0",
        "var_display_name": "I1",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-sqrt(x0*x1)*cos(x2)/(2*x0**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 4.7123889803846898, # 1.5pi 
            # "low": 4.712414503097534,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 5
      },
      {
        "var_name": "x1",
        "var_display_name": "I2",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-sqrt(x0*x1)*cos(x2)/(2*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 1.5707963267948966, # 0.5pi 
            # "high": 1.570838749408722
          }
        ],
        "id": 6
      },
      {
        "var_name": "x1",
        "var_display_name": "I2",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "-sqrt(x0*x1)*cos(x2)/(2*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 1.5707963267948966, # 0.5pi 
            # "low": 1.570838749408722,
            "high": 4.7123889803846898 # 1.5pi 
            # "high": 4.712414503097534
          }
        ],
        "id": 7
      },
      {
        "var_name": "x1",
        "var_display_name": "I2",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-sqrt(x0*x1)*cos(x2)/(2*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 4.7123889803846898, # 1.5pi 
            # "low": 4.712414503097534,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 8
      },
      {
        "var_name": "x2",
        "var_display_name": "delta",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-2*sqrt(x0*x1)*cos(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 1.5707963267948966, # 0.5pi 
            # "high": 1.570838749408722
          }
        ],
        "id": 9
      },
      {
        "var_name": "x2",
        "var_display_name": "delta",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "-2*sqrt(x0*x1)*cos(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 1.5707963267948966, # 0.5pi 
            # "low": 1.570838749408722,
            "high": 4.7123889803846898 # 1.5pi 
            # "high": 4.712414503097534
          }
        ],
        "id": 10
      },
      {
        "var_name": "x2",
        "var_display_name": "delta",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-2*sqrt(x0*x1)*cos(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 4.7123889803846898, # 1.5pi 
            # "low": 4.712414503097534,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 11
      }
    ]
  },
  {
    "EquationName": "FeynmanICh38Eq12",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "3.88724918104e-78/(pi*x0*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-28,
            "high": 1e-26
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "m",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-3.88724918104e-78/(pi*x0**2*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-28,
            "high": 1e-26
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-7.77449836208e-78/(pi*x0*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-28,
            "high": 1e-26
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 0.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-7.77449836208e-78/(pi*x0*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-28,
            "high": 1e-26
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 1e-09
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "m",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "7.77449836208e-78/(pi*x0**3*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-28,
            "high": 1e-26
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "2.332349508624e-77/(pi*x0*x1**4)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-28,
            "high": 1e-26
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          }
        ],
        "id": 5
      }
    ]
  },
  {
    "EquationName": "FeynmanICh39Eq10",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "1.5*x0*x1",
        "sample_space": [
          {
            "name": "x0",
            "low": 10000.0,
            "high": 1000000.0
          },
          {
            "name": "x1",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "pr",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.5*x1",
        "sample_space": [
          {
            "name": "x0",
            "low": 10000.0,
            "high": 1000000.0
          },
          {
            "name": "x1",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "V",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.5*x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 10000.0,
            "high": 1000000.0
          },
          {
            "name": "x1",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "pr",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 10000.0,
            "high": 1000000.0
          },
          {
            "name": "x1",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "V",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 10000.0,
            "high": 1000000.0
          },
          {
            "name": "x1",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 4
      }
    ]
  },
  {
    "EquationName": "FeynmanICh39Eq11",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x1*x2/(x0 - 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 10000.0,
            "high": 1000000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "gamma",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-x1*x2/(x0 - 1)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 10000.0,
            "high": 1000000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "pr",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x2/(x0 - 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 10000.0,
            "high": 1000000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 2
      },
      {
        "var_name": "x2",
        "var_display_name": "V",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x1/(x0 - 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 10000.0,
            "high": 1000000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "gamma",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "2*x1*x2/(x0 - 1)**3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 10000.0,
            "high": 1000000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "pr",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 10000.0,
            "high": 1000000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "V",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 10000.0,
            "high": 1000000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 6
      }
    ]
  },
  {
    "EquationName": "FeynmanICh39Eq22",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "1.380649e-23*x0*x1/x2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "n",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.380649e-23*x1/x2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "T",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.380649e-23*x0/x2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 2
      },
      {
        "var_name": "x2",
        "var_display_name": "V",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-1.380649e-23*x0*x1/x2**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "n",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "T",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "V",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "2.761298e-23*x0*x1/x2**3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 6
      }
    ]
  },
  {
    "EquationName": "FeynmanICh40Eq1",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0*exp(-7.10292768111229e+23*x1*x2/x3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+25,
            "high": 1e+27
          },
          {
            "name": "x1",
            "low": 1e-24,
            "high": 1e-22
          },
          {
            "name": "x2",
            "low": -1.0,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "n_0",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "exp(-7.10292768111229e+23*x1*x2/x3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+25,
            "high": 1e+27
          },
          {
            "name": "x1",
            "low": 1e-24,
            "high": 1e-22
          },
          {
            "name": "x2",
            "low": -1.0,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "m",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-7.10292768111229e+23*x0*x2*exp(-7.10292768111229e+23*x1*x2/x3)/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+25,
            "high": 1e+27
          },
          {
            "name": "x1",
            "low": 1e-24,
            "high": 1e-22
          },
          {
            "name": "x2",
            "low": -1.0,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "m",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-7.10292768111229e+23*x0*x2*exp(-7.10292768111229e+23*x1*x2/x3)/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+25,
            "high": 1e+27
          },
          {
            "name": "x1",
            "low": 1e-24,
            "high": 1e-22
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x2",
        "var_display_name": "x",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-7.10292768111229e+23*x0*x1*exp(-7.10292768111229e+23*x1*x2/x3)/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+25,
            "high": 1e+27
          },
          {
            "name": "x1",
            "low": 1e-24,
            "high": 1e-22
          },
          {
            "name": "x2",
            "low": -1.0,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x3",
        "var_display_name": "T",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "7.10292768111229e+23*x0*x1*x2*exp(-7.10292768111229e+23*x1*x2/x3)/x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+25,
            "high": 1e+27
          },
          {
            "name": "x1",
            "low": 1e-24,
            "high": 1e-22
          },
          {
            "name": "x2",
            "low": -1.0,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x3",
        "var_display_name": "T",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "7.10292768111229e+23*x0*x1*x2*exp(-7.10292768111229e+23*x1*x2/x3)/x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+25,
            "high": 1e+27
          },
          {
            "name": "x1",
            "low": 1e-24,
            "high": 1e-22
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x0",
        "var_display_name": "n_0",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+25,
            "high": 1e+27
          },
          {
            "name": "x1",
            "low": 1e-24,
            "high": 1e-22
          },
          {
            "name": "x2",
            "low": -1.0,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 7
      },
      {
        "var_name": "x1",
        "var_display_name": "m",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "5.04515816431112e+47*x0*x2**2*exp(-7.10292768111229e+23*x1*x2/x3)/x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+25,
            "high": 1e+27
          },
          {
            "name": "x1",
            "low": 1e-24,
            "high": 1e-22
          },
          {
            "name": "x2",
            "low": -1.0,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 8
      },
      {
        "var_name": "x2",
        "var_display_name": "x",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "5.04515816431112e+47*x0*x1**2*exp(-7.10292768111229e+23*x1*x2/x3)/x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+25,
            "high": 1e+27
          },
          {
            "name": "x1",
            "low": 1e-24,
            "high": 1e-22
          },
          {
            "name": "x2",
            "low": -1.0,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 9
      }
    ]
  },
  {
    "EquationName": "FeynmanICh41Eq16",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "3.68620963570564e-51*x0**3/(pi**3*(exp(2.39959613196403e-11*x0/(pi*x1)) - 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "omega",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-8.84541438344777e-62*x0**3*exp(2.39959613196403e-11*x0/(pi*x1))/(pi**4*x1*(exp(2.39959613196403e-11*x0/(pi*x1)) - 1)**2) + 1.10586289071169e-50*x0**2/(pi**3*(exp(2.39959613196403e-11*x0/(pi*x1)) - 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "T",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "8.84541438344777e-62*x0**4*exp(2.39959613196403e-11*x0/(pi*x1))/(pi**4*x1**2*(exp(2.39959613196403e-11*x0/(pi*x1)) - 1)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "omega",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "x0*(-3.68620963570564e-51*x0**2*(5.75806159653671e-22*exp(2.39959613196403e-11*x0/(pi*x1)) - 1.15161231930734e-21*exp(4.79919226392805e-11*x0/(pi*x1))/(exp(2.39959613196403e-11*x0/(pi*x1)) - 1))/(pi**2*x1**2*(exp(2.39959613196403e-11*x0/(pi*x1)) - 1)) - 5.30724863006866e-61*x0*exp(2.39959613196403e-11*x0/(pi*x1))/(pi*x1*(exp(2.39959613196403e-11*x0/(pi*x1)) - 1)) + 2.21172578142338e-50)/(pi**3*(exp(2.39959613196403e-11*x0/(pi*x1)) - 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 3
      }
    ]
  },
  {
    "EquationName": "FeynmanICh43Eq16",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "mu_drift",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.0001,
            "high": 0.0001
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.001,
            "high": 0.1
          }
        ],
        "id": 0
      },
      {
        "var_name": "x1",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.0001,
            "high": 0.0001
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.001,
            "high": 0.1
          }
        ],
        "id": 1
      },
      {
        "var_name": "x2",
        "var_display_name": "Volt",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.0001,
            "high": 0.0001
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 0.001,
            "high": 0.1
          }
        ],
        "id": 2
      }
    ]
  },
  {
    "EquationName": "FeynmanICh43Eq31",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "1.380649e-23*x0*x1",
        "sample_space": [
          {
            "name": "x0",
            "low": 10000000000000.0,
            "high": 1000000000000000.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "mob",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.380649e-23*x1",
        "sample_space": [
          {
            "name": "x0",
            "low": 10000000000000.0,
            "high": 1000000000000000.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "T",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.380649e-23*x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 10000000000000.0,
            "high": 1000000000000000.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "mob",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 10000000000000.0,
            "high": 1000000000000000.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "T",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 10000000000000.0,
            "high": 1000000000000000.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 4
      }
    ]
  },
  {
    "EquationName": "FeynmanICh43Eq43",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "1.380649e-23*x1/(x2*(x0 - 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 100.0,
            "high": 10000.0
          },
          {
            "name": "x2",
            "low": 1e-21,
            "high": 1e-19
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "gamma",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-1.380649e-23*x1/(x2*(x0 - 1)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 100.0,
            "high": 10000.0
          },
          {
            "name": "x2",
            "low": 1e-21,
            "high": 1e-19
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.380649e-23/(x2*(x0 - 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 100.0,
            "high": 10000.0
          },
          {
            "name": "x2",
            "low": 1e-21,
            "high": 1e-19
          }
        ],
        "id": 2
      },
      {
        "var_name": "x2",
        "var_display_name": "A",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-1.380649e-23*x1/(x2**2*(x0 - 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 100.0,
            "high": 10000.0
          },
          {
            "name": "x2",
            "low": 1e-21,
            "high": 1e-19
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "gamma",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "2.761298e-23*x1/(x2*(x0 - 1)**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 100.0,
            "high": 10000.0
          },
          {
            "name": "x2",
            "low": 1e-21,
            "high": 1e-19
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 100.0,
            "high": 10000.0
          },
          {
            "name": "x2",
            "low": 1e-21,
            "high": 1e-19
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "A",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "2.761298e-23*x1/(x2**3*(x0 - 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 100.0,
            "high": 10000.0
          },
          {
            "name": "x2",
            "low": 1e-21,
            "high": 1e-19
          }
        ],
        "id": 6
      }
    ]
  },
  {
    "EquationName": "FeynmanICh44Eq4",
    "Constraints": [
      {
        "var_name": "x2",
        "var_display_name": "V2",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.380649e-23*x0*x1/x2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+24,
            "high": 1e+26
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          },
          {
            "name": "x3",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 0
      },
      {
        "var_name": "x3",
        "var_display_name": "V1",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-1.380649e-23*x0*x1/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+24,
            "high": 1e+26
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          },
          {
            "name": "x3",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "n",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+24,
            "high": 1e+26
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          },
          {
            "name": "x3",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "T",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+24,
            "high": 1e+26
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          },
          {
            "name": "x3",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 3
      },
      {
        "var_name": "x2",
        "var_display_name": "V2",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-1.380649e-23*x0*x1/x2**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+24,
            "high": 1e+26
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          },
          {
            "name": "x3",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 4
      },
      {
        "var_name": "x3",
        "var_display_name": "V1",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "1.380649e-23*x0*x1/x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+24,
            "high": 1e+26
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 1e-05,
            "high": 0.001
          },
          {
            "name": "x3",
            "low": 1e-05,
            "high": 0.001
          }
        ],
        "id": 5
      }
    ]
  },
  {
    "EquationName": "FeynmanICh47Eq23",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "sqrt(x0*x1/x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 5e-06,
            "high": 1.5e-05
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 2.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "gamma",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "sqrt(x0*x1/x2)/(2*x0)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 5e-06,
            "high": 1.5e-05
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 2.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "pr",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "sqrt(x0*x1/x2)/(2*x1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 5e-06,
            "high": 1.5e-05
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 2.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x2",
        "var_display_name": "rho",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-sqrt(x0*x1/x2)/(2*x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 5e-06,
            "high": 1.5e-05
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 2.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "gamma",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-sqrt(x0*x1/x2)/(4*x0**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 5e-06,
            "high": 1.5e-05
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 2.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "pr",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-sqrt(x0*x1/x2)/(4*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 5e-06,
            "high": 1.5e-05
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 2.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "rho",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "3*sqrt(x0*x1/x2)/(4*x2**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 2.0
          },
          {
            "name": "x1",
            "low": 5e-06,
            "high": 1.5e-05
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 2.0
          }
        ],
        "id": 6
      }
    ]
  },
  {
    "EquationName": "FeynmanICh48Eq2",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "8.98755178736818e+16*x0/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-29,
            "high": 1e-27
          },
          {
            "name": "x1",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "m",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "8.98755178736818e+16/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-29,
            "high": 1e-27
          },
          {
            "name": "x1",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.0*x0*x1/(1 - 1.11265005605362e-17*x1**2)**(3/2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-29,
            "high": 1e-27
          },
          {
            "name": "x1",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "m",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-29,
            "high": 1e-27
          },
          {
            "name": "x1",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "-8.98755178736818e+16*x0*(3.71397044170836e-34*x1**2/(1.11265005605362e-17*x1**2 - 1) - 1.11265005605362e-17)/(1 - 1.11265005605362e-17*x1**2)**(3/2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-29,
            "high": 1e-27
          },
          {
            "name": "x1",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 4
      }
    ]
  },
  {
    "EquationName": "FeynmanICh50Eq26",
    "Constraints": [
      {
        "var_name": "x3",
        "var_display_name": "alpha",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*cos(x1*x2)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "x1",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 1
      },
      {
        "var_name": "x3",
        "var_display_name": "alpha",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 2
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh2Eq42",
    "Constraints": [
      {
        "var_name": "x1",
        "var_display_name": "T2",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*x3/x4",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x4",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x2",
        "var_display_name": "T1",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-x0*x3/x4",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x4",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "kappa",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x4",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "T2",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x4",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x2",
        "var_display_name": "T1",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x4",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x3",
        "var_display_name": "A",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x4",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 5
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh3Eq24",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "x0/(4*pi*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0/(4*pi*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 100.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "Pwr",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1/(4*pi*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100.0,
            "high": 100.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-x0/(2*pi*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-x0/(2*pi*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 100.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x0",
        "var_display_name": "Pwr",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -100.0,
            "high": 100.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "3*x0/(2*pi*x1**4)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "3*x0/(2*pi*x1**4)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 100.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 7
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh4Eq23",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "28235825615.541*x0/(pi*x1)",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "28235825615.541*x0/(pi*x1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "28235825615.541/(pi*x1)",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-28235825615.541*x0/(pi*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-28235825615.541*x0/(pi*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "56471651231.082*x0/(pi*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "56471651231.082*x0/(pi*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 7
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh6Eq11",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "p_d",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "28235825615.541*cos(x1)/(pi*x2**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 1.5707963267948966, # 0.5pi 
            # "high": 1.570794403553009
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "p_d",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "28235825615.541*cos(x1)/(pi*x2**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x1",
            "low": 1.5707963267948966, # 0.5pi 
            # "low": 1.570794403553009,
            "high": 4.7123889803846898 # 1.5pi 
            # "high": 4.7123565673828125
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "p_d",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "28235825615.541*cos(x1)/(pi*x2**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x1",
            "low": 4.7123889803846898, # 1.5pi 
            # "low": 4.7123565673828125,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "p_d",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 3
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh6Eq15a",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "p_d",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "84707476846.623*x1*sqrt(x3**2 + x4**2)/(pi*x2**5)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x1",
            "low": -1e-08,
            "high": 0.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": -1e-08,
            "high": 1e-08
          },
          {
            "name": "x4",
            "low": -1e-08,
            "high": 1e-08
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "p_d",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "84707476846.623*x1*sqrt(x3**2 + x4**2)/(pi*x2**5)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 1e-08
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": -1e-08,
            "high": 1e-08
          },
          {
            "name": "x4",
            "low": -1e-08,
            "high": 1e-08
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "z",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "84707476846.623*x0*sqrt(x3**2 + x4**2)/(pi*x2**5)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-20,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": -1e-08,
            "high": 1e-08
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": -1e-08,
            "high": 1e-08
          },
          {
            "name": "x4",
            "low": -1e-08,
            "high": 1e-08
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "z",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "84707476846.623*x0*sqrt(x3**2 + x4**2)/(pi*x2**5)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-20
          },
          {
            "name": "x1",
            "low": -1e-08,
            "high": 1e-08
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": -1e-08,
            "high": 1e-08
          },
          {
            "name": "x4",
            "low": -1e-08,
            "high": 1e-08
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "p_d",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x1",
            "low": -1e-08,
            "high": 1e-08
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": -1e-08,
            "high": 1e-08
          },
          {
            "name": "x4",
            "low": -1e-08,
            "high": 1e-08
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "z",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x1",
            "low": -1e-08,
            "high": 1e-08
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": -1e-08,
            "high": 1e-08
          },
          {
            "name": "x4",
            "low": -1e-08,
            "high": 1e-08
          }
        ],
        "id": 5
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh6Eq15b",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "p_d",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "84707476846.623*sin(x1)*cos(x1)/(pi*x2**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 1.5707963267948966, # 0.5pi 
            # "high": 1.5707998871803284
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "p_d",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "84707476846.623*sin(x1)*cos(x1)/(pi*x2**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x1",
            "low": 1.5707963267948966, # 0.5pi 
            # "low": 1.5707998871803284,
            "high": 3.1415926535897932 # PI
            # "high": 3.141592653589793
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "p_d",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141592653589793
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 2
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh8Eq7",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "16941495369.3246*x0**2/(pi*x1)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1e-12,
            "high": 1e-10
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "33882990738.6492*x0/(pi*x1)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1e-12,
            "high": 1e-10
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "33882990738.6492*x0/(pi*x1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1e-12,
            "high": 1e-10
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "d",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-16941495369.3246*x0**2/(pi*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1e-12,
            "high": 1e-10
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "33882990738.6492/(pi*x1)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1e-12,
            "high": 1e-10
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "d",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "33882990738.6492*x0**2/(pi*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1e-12,
            "high": 1e-10
          }
        ],
        "id": 5
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh8Eq31",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "4.427e-12*x0**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "Ef",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "8.854e-12*x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "Ef",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "8.85400000000000e-12",
        "sample_space": [
          {
            "name": "x0",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 2
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh10Eq9",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "112943302462.164*x0/(x1 + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "112943302462.164*x0/(x1 + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "sigma_den",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "112943302462.164/(x1 + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "chi",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-112943302462.164*x0/(x1 + 1)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "chi",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-112943302462.164*x0/(x1 + 1)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x0",
        "var_display_name": "sigma_den",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x1",
        "var_display_name": "chi",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "225886604924.328*x0/(x1 + 1)**3",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x1",
        "var_display_name": "chi",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "225886604924.328*x0/(x1 + 1)**3",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          }
        ],
        "id": 7
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh11Eq3",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1e-09,
            "high": 1e-07
          },
          {
            "name": "x2",
            "low": 1e-28,
            "high": 1e-26
          },
          {
            "name": "x3",
            "low": -100000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x4",
            "low": -100000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x1",
        "var_display_name": "Ef",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1e-09,
            "high": 1e-07
          },
          {
            "name": "x2",
            "low": 1e-28,
            "high": 1e-26
          },
          {
            "name": "x3",
            "low": -100000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x4",
            "low": -100000000000.0,
            "high": 100000000000.0
          }
        ],
        "id": 1
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh11Eq17",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "n_0",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+27,
            "high": 1e+29
          },
          {
            "name": "x1",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          },
          {
            "name": "x4",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x1",
        "var_display_name": "p_d",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+27,
            "high": 1e+29
          },
          {
            "name": "x1",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          },
          {
            "name": "x4",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x2",
        "var_display_name": "Ef",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+27,
            "high": 1e+29
          },
          {
            "name": "x1",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          },
          {
            "name": "x4",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 2
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh11Eq20",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "2.41432350534664e+22*x0*x1**2*x2/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "2.41432350534664e+22*x0*x1**2*x2/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "n_rho",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "2.41432350534664e+22*x1**2*x2/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "n_rho",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "2.41432350534664e+22*x1**2*x2/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x2",
        "var_display_name": "Ef",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "2.41432350534664e+22*x0*x1**2/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x3",
        "var_display_name": "T",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-2.41432350534664e+22*x0*x1**2*x2/x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x3",
        "var_display_name": "T",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-2.41432350534664e+22*x0*x1**2*x2/x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x0",
        "var_display_name": "n_rho",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 7
      },
      {
        "var_name": "x1",
        "var_display_name": "p_d",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "4.82864701069328e+22*x0*x2/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 8
      },
      {
        "var_name": "x1",
        "var_display_name": "p_d",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "4.82864701069328e+22*x0*x2/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 9
      },
      {
        "var_name": "x2",
        "var_display_name": "Ef",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 10
      },
      {
        "var_name": "x3",
        "var_display_name": "T",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "4.82864701069328e+22*x0*x1**2*x2/x3**3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 11
      },
      {
        "var_name": "x3",
        "var_display_name": "T",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "4.82864701069328e+22*x0*x1**2*x2/x3**3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 12
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh11Eq27",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "8.854e-12*x0*x1*x2/(-x0*x1/3 + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-33,
            "high": 1e-31
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "n",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "2.95133333333333e-12*x0*x1**2*x2/(-x0*x1/3 + 1)**2 + 8.854e-12*x1*x2/(-x0*x1/3 + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-33,
            "high": 1e-31
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "alpha",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "2.95133333333333e-12*x0**2*x1*x2/(-x0*x1/3 + 1)**2 + 8.854e-12*x0*x2/(-x0*x1/3 + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-33,
            "high": 1e-31
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x2",
        "var_display_name": "Ef",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "8.854e-12*x0*x1/(-x0*x1/3 + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-33,
            "high": 1e-31
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "n",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "9*x1**2*x2*(-5.90266666666667e-12*x0*x1/(x0*x1 - 3) + 5.90266666666667e-12)/(x0*x1 - 3)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-33,
            "high": 1e-31
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "alpha",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "9*x0**2*x2*(-5.90266666666667e-12*x0*x1/(x0*x1 - 3) + 5.90266666666667e-12)/(x0*x1 - 3)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-33,
            "high": 1e-31
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "Ef",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-33,
            "high": 1e-31
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 6
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh11Eq28",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0*x1/(-x0*x1/3 + 1) + 1",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-33,
            "high": 1e-31
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "n",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*x1**2/(3*(-x0*x1/3 + 1)**2) + x1/(-x0*x1/3 + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-33,
            "high": 1e-31
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "alpha",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0**2*x1/(3*(-x0*x1/3 + 1)**2) + x0/(-x0*x1/3 + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-33,
            "high": 1e-31
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "n",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "6*x1**2*(-x0*x1/(x0*x1 - 3) + 1)/(x0*x1 - 3)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-33,
            "high": 1e-31
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "alpha",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "6*x0**2*(-x0*x1/(x0*x1 - 3) + 1)/(x0*x1 - 3)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-33,
            "high": 1e-31
          }
        ],
        "id": 4
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh13Eq17",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "6.28331859077038e-7*x0/(pi*x1)",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "6.28331859077038e-7*x0/(pi*x1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "I",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "6.28331859077038e-7/(pi*x1)",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-6.28331859077038e-7*x0/(pi*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-6.28331859077038e-7*x0/(pi*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          }
        ],
        "id": 4
      },
      {
        "var_name": "x0",
        "var_display_name": "I",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          }
        ],
        "id": 5
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "1.25666371815408e-6*x0/(pi*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          }
        ],
        "id": 6
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "1.25666371815408e-6*x0/(pi*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.001,
            "high": 0.1
          }
        ],
        "id": 7
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh13Eq23",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+27,
            "high": 1e+29
          },
          {
            "name": "x1",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "rho_c_0",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+27,
            "high": 1e+29
          },
          {
            "name": "x1",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.11265005605362e-17*x0*x1/(1 - 1.11265005605362e-17*x1**2)**(3/2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+27,
            "high": 1e+29
          },
          {
            "name": "x1",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "rho_c_0",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+27,
            "high": 1e+29
          },
          {
            "name": "x1",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "-x0*(3.71397044170836e-34*x1**2/(1.11265005605362e-17*x1**2 - 1) - 1.11265005605362e-17)/(1 - 1.11265005605362e-17*x1**2)**(3/2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+27,
            "high": 1e+29
          },
          {
            "name": "x1",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 4
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh13Eq34",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0*x1/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+27,
            "high": 1e+29
          },
          {
            "name": "x1",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "rho_c_0",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x1/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+27,
            "high": 1e+29
          },
          {
            "name": "x1",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.11265005605362e-17*x0*x1**2/(1 - 1.11265005605362e-17*x1**2)**(3/2) + x0/sqrt(1 - 1.11265005605362e-17*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+27,
            "high": 1e+29
          },
          {
            "name": "x1",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "rho_c_0",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+27,
            "high": 1e+29
          },
          {
            "name": "x1",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "x0*x1*(-3.71397044170836e-34*x1**2/(1.11265005605362e-17*x1**2 - 1) + 3.33795016816086e-17)/(1 - 1.11265005605362e-17*x1**2)**(3/2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+27,
            "high": 1e+29
          },
          {
            "name": "x1",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 4
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh15Eq4",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "mom",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 0
      },
      {
        "var_name": "x1",
        "var_display_name": "B",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 1
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh15Eq5",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "p_d",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x1",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 0
      },
      {
        "var_name": "x1",
        "var_display_name": "Ef",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x1",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 1
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh21Eq32",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "28235825615.541*x0/(pi*x1*(1 - 3.33564095198152e-9*x2))",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "28235825615.541*x0/(pi*x1*(1 - 3.33564095198152e-9*x2))",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "28235825615.541/(pi*x1*(1 - 3.33564095198152e-9*x2))",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-28235825615.541*x0/(pi*x1**2*(1 - 3.33564095198152e-9*x2))",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-28235825615.541*x0/(pi*x1**2*(1 - 3.33564095198152e-9*x2))",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x2",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "94.1845762362074*x0/(pi*x1*(1 - 3.33564095198152e-9*x2)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "94.1845762362074*x0/(pi*x1*(1 - 3.33564095198152e-9*x2)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 7
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-56471651231.082*x0/(pi*x1**3*(3.33564095198152e-9*x2 - 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 8
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "-56471651231.082*x0/(pi*x1**3*(3.33564095198152e-9*x2 - 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 9
      },
      {
        "var_name": "x2",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-6.28331859077038e-7*x0/(pi*x1*(3.33564095198152e-9*x2 - 1)**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 10
      },
      {
        "var_name": "x2",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "-6.28331859077038e-7*x0/(pi*x1*(3.33564095198152e-9*x2 - 1)**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1000000.0,
            "high": 100000000.0
          }
        ],
        "id": 11
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh24Eq17",
    "Constraints": [
      # {
      #   "var_name": "",
      #   "var_display_name": "",
      #   "order_derivative": 0,
      #   "descriptor": "positive",
      #   "derivative": "sqrt(1.11265005605362e-17*x0**2 - pi**2/x1**2)",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": -100000000000.0,
      #       "high": 100000000000.0
      #     },
      #     {
      #       "name": "x1",
      #       "low": 0.001,
      #       "high": 0.1
      #     }
      #   ],
      #   "id": 0
      # },
      # {
      #   "var_name": "x0",
      #   "var_display_name": "omega",
      #   "order_derivative": 1,
      #   "descriptor": "negative",
      #   "derivative": "1.11265005605362e-17*x0/sqrt(1.11265005605362e-17*x0**2 - pi**2/x1**2)",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": -100000000000.0,
      #       "high": -42763264.0
      #     },
      #     {
      #       "name": "x1",
      #       "low": 0.001,
      #       "high": 0.1
      #     }
      #   ],
      #   "id": 1
      # },
      # {
      #   "var_name": "x0",
      #   "var_display_name": "omega",
      #   "order_derivative": 1,
      #   "descriptor": "positive",
      #   "derivative": "1.11265005605362e-17*x0/sqrt(1.11265005605362e-17*x0**2 - pi**2/x1**2)",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": -42763264.0,
      #       "high": 100000000000.0
      #     },
      #     {
      #       "name": "x1",
      #       "low": 0.001,
      #       "high": 0.1
      #     }
      #   ],
      #   "id": 2
      # },
      # {
      #   "var_name": "x1",
      #   "var_display_name": "d",
      #   "order_derivative": 1,
      #   "descriptor": "positive",
      #   "derivative": "pi**2/(x1**3*sqrt(1.11265005605362e-17*x0**2 - pi**2/x1**2))",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": -100000000000.0,
      #       "high": 100000000000.0
      #     },
      #     {
      #       "name": "x1",
      #       "low": 0.001,
      #       "high": 0.1
      #     }
      #   ],
      #   "id": 3
      # },
      # {
      #   "var_name": "x0",
      #   "var_display_name": "omega",
      #   "order_derivative": 2,
      #   "descriptor": "negative",
      #   "derivative": "(-1.23799014723612e-34*x0**2/(1.11265005605362e-17*x0**2 - pi**2/x1**2) + 1.11265005605362e-17)/sqrt(1.11265005605362e-17*x0**2 - pi**2/x1**2)",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": -100000000000.0,
      #       "high": 100000000000.0
      #     },
      #     {
      #       "name": "x1",
      #       "low": 0.001,
      #       "high": 0.1
      #     }
      #   ],
      #   "id": 4
      # },
      # {
      #   "var_name": "x1",
      #   "var_display_name": "d",
      #   "order_derivative": 2,
      #   "descriptor": "negative",
      #   "derivative": "-pi**2*(3 + pi**2/(x1**2*(1.11265005605362e-17*x0**2 - pi**2/x1**2)))/(x1**4*sqrt(1.11265005605362e-17*x0**2 - pi**2/x1**2))",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": -100000000000.0,
      #       "high": 100000000000.0
      #     },
      #     {
      #       "name": "x1",
      #       "low": 0.001,
      #       "high": 0.1
      #     }
      #   ],
      #   "id": 5
      # }
    ]
  },
  {
    "EquationName": "FeynmanIICh27Eq16",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "0.002654362423132*x0**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "Ef",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "0.005308724846264*x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "Ef",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "0.00530872484626400",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 2
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh27Eq18",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "8.854e-12*x0**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "Ef",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.7708e-11*x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "Ef",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "1.77080000000000e-11",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 2
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh34Eq2a",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x1/(2*pi*x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 0.0
          },
          {
            "name": "x2",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x1/(2*pi*x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x0/(2*pi*x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0/(2*pi*x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 5
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh34Eq2",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x1*x2/2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 0.0
          },
          {
            "name": "x2",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x1*x2/2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x0*x2/2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*x2/2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "r",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": -10000000.0,
            "high": 10000000.0
          },
          {
            "name": "x2",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 6
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh34Eq11",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "g_",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1.0,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": -1e-07,
            "high": 1e-07
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 0
      },
      {
        "var_name": "x1",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1.0,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": -1e-07,
            "high": 1e-07
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 1
      },
      {
        "var_name": "x2",
        "var_display_name": "B",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1.0,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": -1e-07,
            "high": 1e-07
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 2
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh34Eq29a",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "1.6565e-34*x0/(pi*x1)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "1.6565e-34*x0/(pi*x1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.6565e-34/(pi*x1)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "m",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-1.6565e-34*x0/(pi*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "m",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-1.6565e-34*x0/(pi*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 4
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 5
      },
      {
        "var_name": "x1",
        "var_display_name": "m",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "3.313e-34*x0/(pi*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 6
      },
      {
        "var_name": "x1",
        "var_display_name": "m",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "3.313e-34*x0/(pi*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 7
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh34Eq29b",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "g_",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1.0,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": -1e-22,
            "high": 1e-22
          }
        ],
        "id": 0
      },
      {
        "var_name": "x1",
        "var_display_name": "B",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1.0,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": -1e-22,
            "high": 1e-22
          }
        ],
        "id": 1
      },
      {
        "var_name": "x2",
        "var_display_name": "Jz",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1.0,
            "high": 1.0
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": -1e-22,
            "high": 1e-22
          }
        ],
        "id": 2
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh35Eq18",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0/(exp(7.24297051603992e+22*x1*x2/x3) + exp(-7.24297051603992e+22*x1*x2/x3))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-25,
            "high": 1e-23
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "n_0",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1/(exp(7.24297051603992e+22*x1*x2/x3) + exp(-7.24297051603992e+22*x1*x2/x3))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-25,
            "high": 1e-23
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "mom",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x0*(-7.24297051603992e+22*x2*exp(7.24297051603992e+22*x1*x2/x3)/x3 + 7.24297051603992e+22*x2*exp(-7.24297051603992e+22*x1*x2/x3)/x3)/(exp(7.24297051603992e+22*x1*x2/x3) + exp(-7.24297051603992e+22*x1*x2/x3))**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-25,
            "high": 1e-23
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x2",
        "var_display_name": "B",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x0*(-7.24297051603992e+22*x1*exp(7.24297051603992e+22*x1*x2/x3)/x3 + 7.24297051603992e+22*x1*exp(-7.24297051603992e+22*x1*x2/x3)/x3)/(exp(7.24297051603992e+22*x1*x2/x3) + exp(-7.24297051603992e+22*x1*x2/x3))**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-25,
            "high": 1e-23
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x3",
        "var_display_name": "T",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*(7.24297051603992e+22*x1*x2*exp(7.24297051603992e+22*x1*x2/x3)/x3**2 - 7.24297051603992e+22*x1*x2*exp(-7.24297051603992e+22*x1*x2/x3)/x3**2)/(exp(7.24297051603992e+22*x1*x2/x3) + exp(-7.24297051603992e+22*x1*x2/x3))**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-25,
            "high": 1e-23
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x0",
        "var_display_name": "n_0",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-25,
            "high": 1e-23
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x1",
        "var_display_name": "mom",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "x0*x2**2*(1.04921243792447e+46*(exp(7.24297051603992e+22*x1*x2/x3) - exp(-7.24297051603992e+22*x1*x2/x3))**2/(exp(7.24297051603992e+22*x1*x2/x3) + exp(-7.24297051603992e+22*x1*x2/x3))**2 - 5.24606218962236e+45)/(x3**2*(exp(7.24297051603992e+22*x1*x2/x3) + exp(-7.24297051603992e+22*x1*x2/x3)))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-25,
            "high": 1e-23
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x2",
        "var_display_name": "B",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "x0*x1**2*(1.04921243792447e+46*(exp(7.24297051603992e+22*x1*x2/x3) - exp(-7.24297051603992e+22*x1*x2/x3))**2/(exp(7.24297051603992e+22*x1*x2/x3) + exp(-7.24297051603992e+22*x1*x2/x3))**2 - 5.24606218962236e+45)/(x3**2*(exp(7.24297051603992e+22*x1*x2/x3) + exp(-7.24297051603992e+22*x1*x2/x3)))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-25,
            "high": 1e-23
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 7
      },
      {
        "var_name": "x3",
        "var_display_name": "T",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-x0*x1*x2*(-1.04921243792447e+46*x1*x2*(exp(7.24297051603992e+22*x1*x2/x3) - exp(-7.24297051603992e+22*x1*x2/x3))**2/(x3*(exp(7.24297051603992e+22*x1*x2/x3) + exp(-7.24297051603992e+22*x1*x2/x3))) + 5.24606218962236e+45*x1*x2*exp(7.24297051603992e+22*x1*x2/x3)/x3 + 5.24606218962236e+45*x1*x2*exp(-7.24297051603992e+22*x1*x2/x3)/x3 + 1.44859410320798e+23*exp(7.24297051603992e+22*x1*x2/x3) - 1.44859410320798e+23*exp(-7.24297051603992e+22*x1*x2/x3))/(x3**3*(exp(7.24297051603992e+22*x1*x2/x3) + exp(-7.24297051603992e+22*x1*x2/x3))**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-25,
            "high": 1e-23
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 8
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh35Eq21",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0*x1*tanh(7.24297051603992e+22*x1*x2/x3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-25,
            "high": 1e-23
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "n_rho",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x1*tanh(7.24297051603992e+22*x1*x2/x3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-25,
            "high": 1e-23
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "mom",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "7.24297051603992e+22*x0*x1*x2*(1 - tanh(7.24297051603992e+22*x1*x2/x3)**2)/x3 + x0*tanh(7.24297051603992e+22*x1*x2/x3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-25,
            "high": 1e-23
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x2",
        "var_display_name": "B",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "7.24297051603992e+22*x0*x1**2*(1 - tanh(7.24297051603992e+22*x1*x2/x3)**2)/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-25,
            "high": 1e-23
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x3",
        "var_display_name": "T",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-7.24297051603992e+22*x0*x1**2*x2*(1 - tanh(7.24297051603992e+22*x1*x2/x3)**2)/x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-25,
            "high": 1e-23
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x0",
        "var_display_name": "n_rho",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-25,
            "high": 1e-23
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x1",
        "var_display_name": "mom",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "x0*x2*(1.04921243792447e+46*x1*x2*tanh(7.24297051603992e+22*x1*x2/x3)/x3 - 1.44859410320798e+23)*(tanh(7.24297051603992e+22*x1*x2/x3)**2 - 1)/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-25,
            "high": 1e-23
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x2",
        "var_display_name": "B",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "1.04921243792447e+46*x0*x1**3*(tanh(7.24297051603992e+22*x1*x2/x3)**2 - 1)*tanh(7.24297051603992e+22*x1*x2/x3)/x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-25,
            "high": 1e-23
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 7
      },
      {
        "var_name": "x3",
        "var_display_name": "T",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "x0*x1**2*x2*(1.04921243792447e+46*x1*x2*tanh(7.24297051603992e+22*x1*x2/x3)/x3 - 1.44859410320798e+23)*(tanh(7.24297051603992e+22*x1*x2/x3)**2 - 1)/x3**3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e-25,
            "high": 1e-23
          },
          {
            "name": "x2",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 8
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh36Eq38",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "7.24297051603992e+22*x0*x1/x2 + 9.10197825916707e+16*x0*x3*x4/x2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x4",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "7.24297051603992e+22*x0*x1/x2 + 9.10197825916707e+16*x0*x3*x4/x2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x4",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "mom",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "7.24297051603992e+22*x1/x2 + 9.10197825916707e+16*x3*x4/x2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x4",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "H",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "7.24297051603992e+22*x0/x2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x4",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "H",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "7.24297051603992e+22*x0/x2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x4",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 4
      },
      {
        "var_name": "x2",
        "var_display_name": "T",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-7.24297051603992e+22*x0*x1/x2**2 - 9.10197825916707e+16*x0*x3*x4/x2**2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x4",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "T",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-7.24297051603992e+22*x0*x1/x2**2 - 9.10197825916707e+16*x0*x3*x4/x2**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x4",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 6
      },
      {
        "var_name": "x3",
        "var_display_name": "alpha",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "9.10197825916707e+16*x0*x4/x2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x4",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 7
      },
      {
        "var_name": "x3",
        "var_display_name": "alpha",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "9.10197825916707e+16*x0*x4/x2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x4",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 8
      },
      {
        "var_name": "x4",
        "var_display_name": "M",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "9.10197825916707e+16*x0*x3/x2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x4",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 9
      },
      {
        "var_name": "x4",
        "var_display_name": "M",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "9.10197825916707e+16*x0*x3/x2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x4",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 10
      },
      {
        "var_name": "x0",
        "var_display_name": "mom",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x4",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 11
      },
      {
        "var_name": "x1",
        "var_display_name": "H",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x4",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 12
      },
      {
        "var_name": "x2",
        "var_display_name": "T",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "x0*(1.44859410320798e+23*x1 + 1.82039565183341e+17*x3*x4)/x2**3",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x4",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 13
      },
      {
        "var_name": "x2",
        "var_display_name": "T",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "x0*(1.44859410320798e+23*x1 + 1.82039565183341e+17*x3*x4)/x2**3",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x4",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 14
      },
      {
        "var_name": "x3",
        "var_display_name": "alpha",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x4",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 15
      },
      {
        "var_name": "x4",
        "var_display_name": "M",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": 10.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x4",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 16
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh37Eq1",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "mom",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -1000000.0,
            "high": 1000000.0
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 0
      },
      {
        "var_name": "x1",
        "var_display_name": "chi",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -1000000.0,
            "high": 1000000.0
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 1
      },
      {
        "var_name": "x2",
        "var_display_name": "B",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -1000000.0,
            "high": 1000000.0
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 2
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh38Eq3",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "x0*x1*x2/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0*x1*x2/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "Y",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x1*x2/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "Y",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x1*x2/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "A",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x0*x2/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "A",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*x2/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "x",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*x1/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x3",
        "var_display_name": "d",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-x0*x1*x2/x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 7
      },
      {
        "var_name": "x3",
        "var_display_name": "d",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-x0*x1*x2/x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 8
      },
      {
        "var_name": "x0",
        "var_display_name": "Y",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 9
      },
      {
        "var_name": "x1",
        "var_display_name": "A",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 10
      },
      {
        "var_name": "x2",
        "var_display_name": "x",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 11
      },
      {
        "var_name": "x3",
        "var_display_name": "d",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "2*x0*x1*x2/x3**3",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 12
      },
      {
        "var_name": "x3",
        "var_display_name": "d",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "2*x0*x1*x2/x3**3",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.0001,
            "high": 0.01
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 13
      }
    ]
  },
  {
    "EquationName": "FeynmanIICh38Eq14",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0/(2*x1 + 2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "Y",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1/(2*x1 + 2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "sigma",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-2*x0/(2*x1 + 2)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "Y",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "sigma",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "x0/(x1 + 1)**3",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 4
      }
    ]
  },
  {
    "EquationName": "FeynmanIIICh4Eq32",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "1/(exp(2.39959613196403e-11*x0/(pi*x1)) - 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "omega",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-2.39959613196403e-11*exp(2.39959613196403e-11*x0/(pi*x1))/(pi*x1*(exp(2.39959613196403e-11*x0/(pi*x1)) - 1)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "T",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "2.39959613196403e-11*x0*exp(2.39959613196403e-11*x0/(pi*x1))/(pi*x1**2*(exp(2.39959613196403e-11*x0/(pi*x1)) - 1)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "omega",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "(-5.75806159653671e-22*exp(2.39959613196403e-11*x0/(pi*x1)) + 1.15161231930734e-21*exp(4.79919226392805e-11*x0/(pi*x1))/(exp(2.39959613196403e-11*x0/(pi*x1)) - 1))/(pi**2*x1**2*(exp(2.39959613196403e-11*x0/(pi*x1)) - 1)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 3
      }
    ]
  },
  {
    "EquationName": "FeynmanIIICh4Eq33",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "3.313e-34*x0/(pi*(exp(2.39959613196403e-11*x0/(pi*x1)) - 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "omega",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-7.94986198519682e-45*x0*exp(2.39959613196403e-11*x0/(pi*x1))/(pi**2*x1*(exp(2.39959613196403e-11*x0/(pi*x1)) - 1)**2) + 3.313e-34/(pi*(exp(2.39959613196403e-11*x0/(pi*x1)) - 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "T",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "7.94986198519682e-45*x0**2*exp(2.39959613196403e-11*x0/(pi*x1))/(pi**2*x1**2*(exp(2.39959613196403e-11*x0/(pi*x1)) - 1)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x1",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 2
      }
    ]
  },
  {
    "EquationName": "FeynmanIIICh7Eq38",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "mom",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "6.03682463024449e+33*pi*x1",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "mom",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "6.03682463024449e+33*pi*x1",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 0.1
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "B",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "6.03682463024449e+33*pi*x0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "B",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "6.03682463024449e+33*pi*x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "mom",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "B",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 5
      }
    ]
  },
  {
    "EquationName": "FeynmanIIICh8Eq54",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "sin(3018412315122245888053292650463232*pi*x0*x1)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-18,
            "high": 1e-16
          }
        ],
        "id": 0
      }
    ]
  },
  {
    "EquationName": "FeynmanIIICh9Eq52",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "p_d",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "1.2073649260489e+34*pi*x1*sin(x2*(x3 - x4)/2)**2/(x2*(x3 - x4)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x1",
            "low": -1000.0,
            "high": 0.0
          },
          {
            "name": "x2",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x3",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x4",
            "low": 100000000.0,
            "high": 10000000000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "p_d",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.2073649260489e+34*pi*x1*sin(x2*(x3 - x4)/2)**2/(x2*(x3 - x4)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x3",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x4",
            "low": 100000000.0,
            "high": 10000000000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "Ef",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "1.2073649260489e+34*pi*x0*sin(x2*(x3 - x4)/2)**2/(x2*(x3 - x4)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-20,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x3",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x4",
            "low": 100000000.0,
            "high": 10000000000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "Ef",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.2073649260489e+34*pi*x0*sin(x2*(x3 - x4)/2)**2/(x2*(x3 - x4)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-20
          },
          {
            "name": "x1",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x3",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x4",
            "low": 100000000.0,
            "high": 10000000000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "p_d",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x1",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x3",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x4",
            "low": 100000000.0,
            "high": 10000000000.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "Ef",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-20,
            "high": 1e-20
          },
          {
            "name": "x1",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x2",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x3",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x4",
            "low": 100000000.0,
            "high": 10000000000.0
          }
        ],
        "id": 5
      }
    ]
  },
  {
    "EquationName": "FeynmanIIICh10Eq19",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "x0*sqrt(x1**2 + x2**2 + x3**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0*sqrt(x1**2 + x2**2 + x3**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "mom",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "sqrt(x1**2 + x2**2 + x3**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "mom",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "Bx",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-x0*(x1**2/(x1**2 + x2**2 + x3**2) - 1)/sqrt(x1**2 + x2**2 + x3**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "Bx",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "-x0*(x1**2/(x1**2 + x2**2 + x3**2) - 1)/sqrt(x1**2 + x2**2 + x3**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "By",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-x0*(x2**2/(x1**2 + x2**2 + x3**2) - 1)/sqrt(x1**2 + x2**2 + x3**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 6
      },
      {
        "var_name": "x2",
        "var_display_name": "By",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "-x0*(x2**2/(x1**2 + x2**2 + x3**2) - 1)/sqrt(x1**2 + x2**2 + x3**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 7
      },
      {
        "var_name": "x3",
        "var_display_name": "Bz",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-x0*(x3**2/(x1**2 + x2**2 + x3**2) - 1)/sqrt(x1**2 + x2**2 + x3**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-23,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 8
      },
      {
        "var_name": "x3",
        "var_display_name": "Bz",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "-x0*(x3**2/(x1**2 + x2**2 + x3**2) - 1)/sqrt(x1**2 + x2**2 + x3**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-23
          },
          {
            "name": "x1",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": -0.1,
            "high": 0.1
          }
        ],
        "id": 9
      }
    ]
  },
  {
    "EquationName": "FeynmanIIICh12Eq43",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "3.313e-34*x0/pi",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 100.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "n",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "3.313e-34/pi",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 100.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "n",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 100.0
          }
        ],
        "id": 2
      }
    ]
  },
  {
    "EquationName": "FeynmanIIICh13Eq18",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "6.03682463024449e+33*pi*x0*x1**2*x2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "6.03682463024449e+33*pi*x0*x1**2*x2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "E_n",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "6.03682463024449e+33*pi*x1**2*x2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "d",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "1.2073649260489e+34*pi*x0*x1*x2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "d",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "1.2073649260489e+34*pi*x0*x1*x2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x2",
        "var_display_name": "k",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "6.03682463024449e+33*pi*x0*x1**2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "k",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "6.03682463024449e+33*pi*x0*x1**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x0",
        "var_display_name": "E_n",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 7
      },
      {
        "var_name": "x1",
        "var_display_name": "d",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "1.2073649260489e+34*pi*x0*x2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 8
      },
      {
        "var_name": "x1",
        "var_display_name": "d",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "1.2073649260489e+34*pi*x0*x2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 9
      },
      {
        "var_name": "x2",
        "var_display_name": "k",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x2",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 10
      }
    ]
  },
  {
    "EquationName": "FeynmanIIICh14Eq14",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "I_0",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "exp(7.24297051603992e+22*x1*x2/x3) - 1",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1e-22,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "I_0",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "exp(7.24297051603992e+22*x1*x2/x3) - 1",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1e-22,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x2",
        "var_display_name": "Volt",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "7.24297051603992e+22*x0*x1*exp(7.24297051603992e+22*x1*x2/x3)/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1e-22,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x2",
        "var_display_name": "Volt",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "7.24297051603992e+22*x0*x1*exp(7.24297051603992e+22*x1*x2/x3)/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1e-22,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "I_0",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1e-22,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "5.24606218962236e+45*x0*x2**2*exp(7.24297051603992e+22*x1*x2/x3)/x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1e-22,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x1",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "5.24606218962236e+45*x0*x2**2*exp(7.24297051603992e+22*x1*x2/x3)/x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1e-22,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x2",
        "var_display_name": "Volt",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "5.24606218962236e+45*x0*x1**2*exp(7.24297051603992e+22*x1*x2/x3)/x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1e-22,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 7
      },
      {
        "var_name": "x2",
        "var_display_name": "Volt",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "5.24606218962236e+45*x0*x1**2*exp(7.24297051603992e+22*x1*x2/x3)/x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1e-22,
            "high": 1e-20
          },
          {
            "name": "x2",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x3",
            "low": 10.0,
            "high": 1000.0
          }
        ],
        "id": 8
      }
    ]
  },
  {
    "EquationName": "FeynmanIIICh15Eq12",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "2*x0*(1 - cos(x1*x2))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "U",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "2 - 2*cos(x1*x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "k",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "2*x0*x2*sin(x1*x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 2
      },
      {
        "var_name": "x2",
        "var_display_name": "d",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "2*x0*x1*sin(x1*x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "U",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "k",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "2*x0*x2**2*cos(x1*x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "d",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "2*x0*x1**2*cos(x1*x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 0.1,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 6
      }
    ]
  },
  {
    "EquationName": "FeynmanIIICh15Eq14",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "5.4879845e-68/(pi**2*x0*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "E_n",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-5.4879845e-68/(pi**2*x0**2*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "d",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-1.0975969e-67/(pi**2*x0*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "E_n",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "1.0975969e-67/(pi**2*x0**3*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "d",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "3.2927907e-67/(pi**2*x0*x1**4)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 4
      }
    ]
  },
  {
    "EquationName": "FeynmanIIICh15Eq27",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "2*pi*x0/(x1*x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "2*pi*x0/(x1*x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 100.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "alpha",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "2*pi/(x1*x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100.0,
            "high": 100.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "n",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-2*pi*x0/(x1**2*x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "n",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-2*pi*x0/(x1**2*x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 100.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 4
      },
      {
        "var_name": "x2",
        "var_display_name": "d",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-2*pi*x0/(x1*x2**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "d",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-2*pi*x0/(x1*x2**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 100.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 6
      },
      {
        "var_name": "x0",
        "var_display_name": "alpha",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -100.0,
            "high": 100.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 7
      },
      {
        "var_name": "x1",
        "var_display_name": "n",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "4*pi*x0/(x1**3*x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 8
      },
      {
        "var_name": "x1",
        "var_display_name": "n",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "4*pi*x0/(x1**3*x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 100.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 9
      },
      {
        "var_name": "x2",
        "var_display_name": "d",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "4*pi*x0/(x1*x2**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": -100.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 10
      },
      {
        "var_name": "x2",
        "var_display_name": "d",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "4*pi*x0/(x1*x2**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 100.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          }
        ],
        "id": 11
      }
    ]
  },
  {
    "EquationName": "FeynmanIIICh17Eq37",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0*(x1*cos(x2) + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "beta",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x1*cos(x2) + 1",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "alpha",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*cos(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 1.5707963267948966, # 0.5pi 
            # "high": 1.570783257484436
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "alpha",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x0*cos(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 1.5707963267948966, # 0.5pi 
            # "low": 1.570783257484436,
            "high": 4.7123889803846898 # 1.5pi 
            # "high": 4.712449312210083
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "alpha",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*cos(x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 4.7123889803846898, # 1.5pi 
            # "low": 4.712449312210083,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 4
      },
      {
        "var_name": "x0",
        "var_display_name": "beta",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 5
      },
      {
        "var_name": "x1",
        "var_display_name": "alpha",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 6
      }
    ]
  },
  {
    "EquationName": "FeynmanIIICh19Eq51",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "-3.63185176721637e+87*x0*x1**4/x2**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 100.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "m",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-3.63185176721637e+87*x1**4/x2**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 100.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-1.45274070688655e+88*x0*x1**3/x2**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 0.0
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 100.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-1.45274070688655e+88*x0*x1**3/x2**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 100.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x2",
        "var_display_name": "n",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "7.26370353443274e+87*x0*x1**4/x2**3",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 100.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x0",
        "var_display_name": "m",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 100.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x1",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-4.35822212065964e+88*x0*x1**2/x2**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 100.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x2",
        "var_display_name": "n",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-2.17911106032982e+88*x0*x1**4/x2**4",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 100.0
          }
        ],
        "id": 7
      }
    ]
  },
  {
    "EquationName": "FeynmanIIICh21Eq20",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "-x0*x1*x2/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e+29,
            "high": -1e+27
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": -1e-11
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "-x0*x1*x2/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e+29,
            "high": -1e+27
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": -1e-11
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "rho_c_0",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-x1*x2/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e+29,
            "high": -1e+27
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": -1e-11
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "rho_c_0",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-x1*x2/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e+29,
            "high": -1e+27
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": -1e-11
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-x0*x2/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e+29,
            "high": -1e+27
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": -1e-11
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-x0*x2/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e+29,
            "high": -1e+27
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": -1e-11
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "A_vec",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-x0*x1/x3",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e+29,
            "high": -1e+27
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": -1e-11
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 6
      },
      {
        "var_name": "x3",
        "var_display_name": "m",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x0*x1*x2/x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e+29,
            "high": -1e+27
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": -1e-11
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 7
      },
      {
        "var_name": "x3",
        "var_display_name": "m",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*x1*x2/x3**2",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e+29,
            "high": -1e+27
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": -1e-11
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 8
      },
      {
        "var_name": "x0",
        "var_display_name": "rho_c_0",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e+29,
            "high": -1e+27
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": -1e-11
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 9
      },
      {
        "var_name": "x1",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e+29,
            "high": -1e+27
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": -1e-11
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 10
      },
      {
        "var_name": "x2",
        "var_display_name": "A_vec",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e+29,
            "high": -1e+27
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": -1e-11
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 11
      },
      {
        "var_name": "x3",
        "var_display_name": "m",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "-2*x0*x1*x2/x3**3",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e+29,
            "high": -1e+27
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": -1e-11
          },
          {
            "name": "x2",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 12
      },
      {
        "var_name": "x3",
        "var_display_name": "m",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-2*x0*x1*x2/x3**3",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e+29,
            "high": -1e+27
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": -1e-11
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          }
        ],
        "id": 13
      }
    ]
  },
  {
    "EquationName": "FeynmanBonus1",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "3.32662926626791e-57*x0**2*x1**2/(x2**2*sin(x3/2)**4)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "Z_1",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "6.65325853253582e-57*x0*x1**2/(x2**2*sin(x3/2)**4)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "Z_2",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "6.65325853253582e-57*x0**2*x1/(x2**2*sin(x3/2)**4)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 2
      },
      {
        "var_name": "x2",
        "var_display_name": "E_n",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-6.65325853253582e-57*x0**2*x1**2/(x2**3*sin(x3/2)**4)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 3
      },
      {
        "var_name": "x3",
        "var_display_name": "theta",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-6.65325853253582e-57*x0**2*x1**2*cos(x3/2)/(x2**2*sin(x3/2)**5)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141590118408203
          }
        ],
        "id": 4
      },
      {
        "var_name": "x3",
        "var_display_name": "theta",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-6.65325853253582e-57*x0**2*x1**2*cos(x3/2)/(x2**2*sin(x3/2)**5)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x3",
            "low": 3.1415926535897932, # PI
            # "low": 3.141590118408203,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 5
      },
      {
        "var_name": "x0",
        "var_display_name": "Z_1",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "6.65325853253582e-57*x1**2/(x2**2*sin(x3/2)**4)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 6
      },
      {
        "var_name": "x1",
        "var_display_name": "Z_2",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "6.65325853253582e-57*x0**2/(x2**2*sin(x3/2)**4)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 7
      },
      {
        "var_name": "x2",
        "var_display_name": "E_n",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "1.99597755976075e-56*x0**2*x1**2/(x2**4*sin(x3/2)**4)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 8
      },
      {
        "var_name": "x3",
        "var_display_name": "theta",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "3.32662926626791e-57*x0**2*x1**2*(1 + 5*cos(x3/2)**2/sin(x3/2)**2)/(x2**2*sin(x3/2)**4)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x1",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x2",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 9
      }
    ]
  },
  {
    "EquationName": "FeynmanBonus2",
    "Constraints": [
      {
        "var_name": "x1",
        "var_display_name": "k_G",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*(sqrt(1 + 2*x2**2*x3/(x0*x1**2))*cos(x4 - x5) + 1)/x2**2 - 2*x3*cos(x4 - x5)/(x1**2*sqrt(1 + 2*x2**2*x3/(x0*x1**2)))",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x2",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x3",
            "low": 1e+25,
            "high": 1e+27
          },
          {
            "name": "x4",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          },
          {
            "name": "x5",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 0
      }
    ]
  },
  {
    "EquationName": "FeynmanBonus3",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0*(1 - x1**2)/(x1*cos(x2 - x3) + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "d",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "(1 - x1**2)/(x1*cos(x2 - x3) + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "d",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "alpha",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "2*x0*(2*x1*cos(x2 - x3)/(x1*cos(x2 - x3) + 1) - (x1**2 - 1)*cos(x2 - x3)**2/(x1*cos(x2 - x3) + 1)**2 - 1)/(x1*cos(x2 - x3) + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 3
      }
    ]
  },
  {
    "EquationName": "FeynmanBonus4",
    "Constraints": [
      # {
      #   "var_name": "",
      #   "var_display_name": "",
      #   "order_derivative": 0,
      #   "descriptor": "positive",
      #   "derivative": "sqrt(2)*sqrt((x1 - x2 - x3**2/(2*x0*x4**2))/x0)",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e+23,
      #       "high": 1e+25
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x2",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x3",
      #       "low": -10000000000.0,
      #       "high": 10000000000.0
      #     },
      #     {
      #       "name": "x4",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     }
      #   ],
      #   "id": 0
      # },
      # {
      #   "var_name": "x0",
      #   "var_display_name": "m",
      #   "order_derivative": 1,
      #   "descriptor": "negative",
      #   "derivative": "sqrt(2)*x0*sqrt((x1 - x2 - x3**2/(2*x0*x4**2))/x0)*(-(x1 - x2 - x3**2/(2*x0*x4**2))/(2*x0**2) + x3**2/(4*x0**3*x4**2))/(x1 - x2 - x3**2/(2*x0*x4**2))",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e+23,
      #       "high": 1e+25
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x2",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x3",
      #       "low": -10000000000.0,
      #       "high": 10000000000.0
      #     },
      #     {
      #       "name": "x4",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     }
      #   ],
      #   "id": 1
      # },
      # {
      #   "var_name": "x1",
      #   "var_display_name": "E_n",
      #   "order_derivative": 1,
      #   "descriptor": "positive",
      #   "derivative": "sqrt(2)*sqrt((x1 - x2 - x3**2/(2*x0*x4**2))/x0)/(2*(x1 - x2 - x3**2/(2*x0*x4**2)))",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e+23,
      #       "high": 1e+25
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x2",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x3",
      #       "low": -10000000000.0,
      #       "high": 10000000000.0
      #     },
      #     {
      #       "name": "x4",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     }
      #   ],
      #   "id": 2
      # },
      # {
      #   "var_name": "x2",
      #   "var_display_name": "U",
      #   "order_derivative": 1,
      #   "descriptor": "negative",
      #   "derivative": "-sqrt(2)*sqrt((x1 - x2 - x3**2/(2*x0*x4**2))/x0)/(2*(x1 - x2 - x3**2/(2*x0*x4**2)))",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e+23,
      #       "high": 1e+25
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x2",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x3",
      #       "low": -10000000000.0,
      #       "high": 10000000000.0
      #     },
      #     {
      #       "name": "x4",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     }
      #   ],
      #   "id": 3
      # },
      # {
      #   "var_name": "x3",
      #   "var_display_name": "L",
      #   "order_derivative": 1,
      #   "descriptor": "positive",
      #   "derivative": "-sqrt(2)*x3*sqrt((x1 - x2 - x3**2/(2*x0*x4**2))/x0)/(2*x0*x4**2*(x1 - x2 - x3**2/(2*x0*x4**2)))",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e+23,
      #       "high": 1e+25
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x2",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x3",
      #       "low": -10000000000.0,
      #       "high": -132292.0
      #     },
      #     {
      #       "name": "x4",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     }
      #   ],
      #   "id": 4
      # },
      # {
      #   "var_name": "x3",
      #   "var_display_name": "L",
      #   "order_derivative": 1,
      #   "descriptor": "negative",
      #   "derivative": "-sqrt(2)*x3*sqrt((x1 - x2 - x3**2/(2*x0*x4**2))/x0)/(2*x0*x4**2*(x1 - x2 - x3**2/(2*x0*x4**2)))",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e+23,
      #       "high": 1e+25
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x2",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x3",
      #       "low": -132292.0,
      #       "high": 10000000000.0
      #     },
      #     {
      #       "name": "x4",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     }
      #   ],
      #   "id": 5
      # },
      # {
      #   "var_name": "x4",
      #   "var_display_name": "r",
      #   "order_derivative": 1,
      #   "descriptor": "positive",
      #   "derivative": "sqrt(2)*x3**2*sqrt((x1 - x2 - x3**2/(2*x0*x4**2))/x0)/(2*x0*x4**3*(x1 - x2 - x3**2/(2*x0*x4**2)))",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e+23,
      #       "high": 1e+25
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x2",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x3",
      #       "low": -10000000000.0,
      #       "high": 10000000000.0
      #     },
      #     {
      #       "name": "x4",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     }
      #   ],
      #   "id": 6
      # },
      # {
      #   "var_name": "x0",
      #   "var_display_name": "m",
      #   "order_derivative": 2,
      #   "descriptor": "positive",
      #   "derivative": "sqrt(2)*sqrt(-(-x1 + x2 + x3**2/(2*x0*x4**2))/x0)*(-x1 + x2 + (-x1 + x2 + x3**2/(x0*x4**2))**2/(-2*x1 + 2*x2 + x3**2/(x0*x4**2)) + 2*x3**2/(x0*x4**2) - x3**2*(-x1 + x2 + x3**2/(x0*x4**2))/(x0*x4**2*(-2*x1 + 2*x2 + x3**2/(x0*x4**2))))/(x0**2*(-2*x1 + 2*x2 + x3**2/(x0*x4**2)))",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e+23,
      #       "high": 1e+25
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x2",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x3",
      #       "low": -10000000000.0,
      #       "high": 10000000000.0
      #     },
      #     {
      #       "name": "x4",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     }
      #   ],
      #   "id": 7
      # },
      # {
      #   "var_name": "x1",
      #   "var_display_name": "E_n",
      #   "order_derivative": 2,
      #   "descriptor": "negative",
      #   "derivative": "-sqrt(2)*sqrt(-(-x1 + x2 + x3**2/(2*x0*x4**2))/x0)/(4*(-x1 + x2 + x3**2/(2*x0*x4**2))**2)",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e+23,
      #       "high": 1e+25
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x2",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x3",
      #       "low": -10000000000.0,
      #       "high": 10000000000.0
      #     },
      #     {
      #       "name": "x4",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     }
      #   ],
      #   "id": 8
      # },
      # {
      #   "var_name": "x2",
      #   "var_display_name": "U",
      #   "order_derivative": 2,
      #   "descriptor": "negative",
      #   "derivative": "-sqrt(2)*sqrt(-(-x1 + x2 + x3**2/(2*x0*x4**2))/x0)/(4*(-x1 + x2 + x3**2/(2*x0*x4**2))**2)",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e+23,
      #       "high": 1e+25
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x2",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x3",
      #       "low": -10000000000.0,
      #       "high": 10000000000.0
      #     },
      #     {
      #       "name": "x4",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     }
      #   ],
      #   "id": 9
      # },
      # {
      #   "var_name": "x3",
      #   "var_display_name": "L",
      #   "order_derivative": 2,
      #   "descriptor": "negative",
      #   "derivative": "sqrt(2)*sqrt(-(-x1 + x2 + x3**2/(2*x0*x4**2))/x0)*(1 - x3**2/(x0*x4**2*(-2*x1 + 2*x2 + x3**2/(x0*x4**2))))/(x0*x4**2*(-2*x1 + 2*x2 + x3**2/(x0*x4**2)))",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e+23,
      #       "high": 1e+25
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x2",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x3",
      #       "low": -10000000000.0,
      #       "high": 10000000000.0
      #     },
      #     {
      #       "name": "x4",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     }
      #   ],
      #   "id": 10
      # },
      # {
      #   "var_name": "x4",
      #   "var_display_name": "r",
      #   "order_derivative": 2,
      #   "descriptor": "negative",
      #   "derivative": "sqrt(2)*x3**2*sqrt(-(-x1 + x2 + x3**2/(2*x0*x4**2))/x0)*(3 - x3**2/(x0*x4**2*(-2*x1 + 2*x2 + x3**2/(x0*x4**2))))/(x0*x4**4*(-2*x1 + 2*x2 + x3**2/(x0*x4**2)))",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e+23,
      #       "high": 1e+25
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x2",
      #       "low": 1e+25,
      #       "high": 1e+27
      #     },
      #     {
      #       "name": "x3",
      #       "low": -10000000000.0,
      #       "high": 10000000000.0
      #     },
      #     {
      #       "name": "x4",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     }
      #   ],
      #   "id": 11
      # }
    ]
  },
  {
    "EquationName": "FeynmanBonus5",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "244808.861301089*pi*x0**1.5/sqrt(x1 + x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x1",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x2",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "d",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "367213.291951633*pi*x0**0.5/sqrt(x1 + x2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x1",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x2",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "m1",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-122404.430650544*pi*x0**1.5/(x1 + x2)**(3/2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x1",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x2",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 2
      },
      {
        "var_name": "x2",
        "var_display_name": "m2",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-122404.430650544*pi*x0**1.5/(x1 + x2)**(3/2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x1",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x2",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "d",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "183606.645975816*pi/(x0**0.5*sqrt(x1 + x2))",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x1",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x2",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "m1",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "183606.645975816*pi*x0**1.5/(x1 + x2)**(5/2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x1",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x2",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "m2",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "183606.645975816*pi*x0**1.5/(x1 + x2)**(5/2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x1",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x2",
            "low": 1e+23,
            "high": 1e+25
          }
        ],
        "id": 6
      }
    ]
  },
  {
    "EquationName": "FeynmanBonus6",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "sqrt(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": -1e-09,
            "high": 1e-09
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "epsilon",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "2*x0*x1*x2**2/(x3*x4**2*x5**2*x6**4*sqrt(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": -1e-09,
            "high": 1e-09
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "epsilon",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "2*x0*x1*x2**2/(x3*x4**2*x5**2*x6**4*sqrt(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": -1e-09,
            "high": 1e-09
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "E_n",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0**2*x2**2/(x3*x4**2*x5**2*x6**4*sqrt(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": -1e-09,
            "high": 1e-09
          }
        ],
        "id": 3
      },
      {
        "var_name": "x2",
        "var_display_name": "L",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "2*x0**2*x1*x2/(x3*x4**2*x5**2*x6**4*sqrt(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": -1e-09,
            "high": 1e-09
          }
        ],
        "id": 4
      },
      {
        "var_name": "x3",
        "var_display_name": "m",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-x0**2*x1*x2**2/(x3**2*x4**2*x5**2*x6**4*sqrt(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": -1e-09,
            "high": 1e-09
          }
        ],
        "id": 5
      },
      {
        "var_name": "x4",
        "var_display_name": "Z_1",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-2*x0**2*x1*x2**2/(x3*x4**3*x5**2*x6**4*sqrt(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": -1e-09,
            "high": 1e-09
          }
        ],
        "id": 6
      },
      {
        "var_name": "x5",
        "var_display_name": "Z_2",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-2*x0**2*x1*x2**2/(x3*x4**2*x5**3*x6**4*sqrt(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": -1e-09,
            "high": 1e-09
          }
        ],
        "id": 7
      },
      {
        "var_name": "x6",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-4*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**5*sqrt(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": -1e-09,
            "high": 0.0
          }
        ],
        "id": 8
      },
      {
        "var_name": "x6",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-4*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**5*sqrt(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": 0.0,
            "high": 1e-09
          }
        ],
        "id": 9
      },
      # {
      #   "var_name": "x0",
      #   "var_display_name": "epsilon",
      #   "order_derivative": 2,
      #   "descriptor": "positive",
      #   "derivative": "2*x1*x2**2*(-2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4*(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1)) + 1)/(x3*x4**2*x5**2*x6**4*sqrt(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1))",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": -1e-16,
      #       "high": 1e-16
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1e-18,
      #       "high": 1e-16
      #     },
      #     {
      #       "name": "x2",
      #       "low": 1e-10,
      #       "high": 1e-08
      #     },
      #     {
      #       "name": "x3",
      #       "low": 1e-30,
      #       "high": 1e-28
      #     },
      #     {
      #       "name": "x4",
      #       "low": 1.0,
      #       "high": 10.0
      #     },
      #     {
      #       "name": "x5",
      #       "low": 1.0,
      #       "high": 10.0
      #     },
      #     {
      #       "name": "x6",
      #       "low": -1e-09,
      #       "high": 1e-09
      #     }
      #   ],
      #   "id": 10
      # },
      {
        "var_name": "x1",
        "var_display_name": "E_n",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-x0**4*x2**4/(x3**2*x4**4*x5**4*x6**8*(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1)**(3/2))",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": -1e-09,
            "high": 1e-09
          }
        ],
        "id": 11
      },
      # {
      #   "var_name": "x2",
      #   "var_display_name": "L",
      #   "order_derivative": 2,
      #   "descriptor": "positive",
      #   "derivative": "2*x0**2*x1*(-2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4*(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1)) + 1)/(x3*x4**2*x5**2*x6**4*sqrt(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1))",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": -1e-16,
      #       "high": 1e-16
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1e-18,
      #       "high": 1e-16
      #     },
      #     {
      #       "name": "x2",
      #       "low": 1e-10,
      #       "high": 1e-08
      #     },
      #     {
      #       "name": "x3",
      #       "low": 1e-30,
      #       "high": 1e-28
      #     },
      #     {
      #       "name": "x4",
      #       "low": 1.0,
      #       "high": 10.0
      #     },
      #     {
      #       "name": "x5",
      #       "low": 1.0,
      #       "high": 10.0
      #     },
      #     {
      #       "name": "x6",
      #       "low": -1e-09,
      #       "high": 1e-09
      #     }
      #   ],
      #   "id": 12
      # },
      {
        "var_name": "x3",
        "var_display_name": "m",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "x0**2*x1*x2**2*(-x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4*(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1)) + 2)/(x3**3*x4**2*x5**2*x6**4*sqrt(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": -1e-09,
            "high": 1e-09
          }
        ],
        "id": 13
      },
      {
        "var_name": "x4",
        "var_display_name": "Z_1",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "2*x0**2*x1*x2**2*(-2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4*(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1)) + 3)/(x3*x4**4*x5**2*x6**4*sqrt(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": -1e-09,
            "high": 1e-09
          }
        ],
        "id": 14
      },
      {
        "var_name": "x5",
        "var_display_name": "Z_2",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "2*x0**2*x1*x2**2*(-2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4*(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1)) + 3)/(x3*x4**2*x5**4*x6**4*sqrt(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": -1e-09,
            "high": 1e-09
          }
        ],
        "id": 15
      },
      {
        "var_name": "x6",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "4*x0**2*x1*x2**2*(-4*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4*(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1)) + 5)/(x3*x4**2*x5**2*x6**6*sqrt(2*x0**2*x1*x2**2/(x3*x4**2*x5**2*x6**4) + 1))",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-16,
            "high": 1e-16
          },
          {
            "name": "x1",
            "low": 1e-18,
            "high": 1e-16
          },
          {
            "name": "x2",
            "low": 1e-10,
            "high": 1e-08
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1.0,
            "high": 10.0
          },
          {
            "name": "x6",
            "low": -1e-09,
            "high": 1e-09
          }
        ],
        "id": 16
      }
    ]
  },
  {
    "EquationName": "FeynmanBonus7",
    "Constraints": [
      # {
      #   "var_name": "",
      #   "var_display_name": "",
      #   "order_derivative": 0,
      #   "descriptor": "positive",
      #   "derivative": "299792458.0*sqrt(1.98030940509831e-27*pi*x0 - x1/x2**2)",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e-27,
      #       "high": 1e-25
      #     },
      #     {
      #       "name": "x1",
      #       "low": -1.0,
      #       "high": 1.0
      #     },
      #     {
      #       "name": "x2",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     }
      #   ],
      #   "id": 0
      # },
      # {
      #   "var_name": "x0",
      #   "var_display_name": "rho",
      #   "order_derivative": 1,
      #   "descriptor": "positive",
      #   "derivative": "2.9684091207747e-19*pi/sqrt(1.98030940509831e-27*pi*x0 - x1/x2**2)",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e-27,
      #       "high": 1e-25
      #     },
      #     {
      #       "name": "x1",
      #       "low": -1.0,
      #       "high": 1.0
      #     },
      #     {
      #       "name": "x2",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     }
      #   ],
      #   "id": 1
      # },
      # {
      #   "var_name": "x1",
      #   "var_display_name": "alpha",
      #   "order_derivative": 1,
      #   "descriptor": "negative",
      #   "derivative": "-149896229.0/(x2**2*sqrt(1.98030940509831e-27*pi*x0 - x1/x2**2))",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e-27,
      #       "high": 1e-25
      #     },
      #     {
      #       "name": "x1",
      #       "low": -1.0,
      #       "high": 1.0
      #     },
      #     {
      #       "name": "x2",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     }
      #   ],
      #   "id": 2
      # },
      # {
      #   "var_name": "x2",
      #   "var_display_name": "d",
      #   "order_derivative": 1,
      #   "descriptor": "negative",
      #   "derivative": "299792458.0*x1/(x2**3*sqrt(1.98030940509831e-27*pi*x0 - x1/x2**2))",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e-27,
      #       "high": 1e-25
      #     },
      #     {
      #       "name": "x1",
      #       "low": -1.0,
      #       "high": 1.0
      #     },
      #     {
      #       "name": "x2",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     }
      #   ],
      #   "id": 3
      # },
      # {
      #   "var_name": "x0",
      #   "var_display_name": "rho",
      #   "order_derivative": 2,
      #   "descriptor": "negative",
      #   "derivative": "-2.93918425002487e-46*pi**2/(1.98030940509831e-27*pi*x0 - x1/x2**2)**(3/2)",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e-27,
      #       "high": 1e-25
      #     },
      #     {
      #       "name": "x1",
      #       "low": -1.0,
      #       "high": 1.0
      #     },
      #     {
      #       "name": "x2",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     }
      #   ],
      #   "id": 4
      # },
      # {
      #   "var_name": "x1",
      #   "var_display_name": "alpha",
      #   "order_derivative": 2,
      #   "descriptor": "negative",
      #   "derivative": "-74948114.5/(x2**4*(1.98030940509831e-27*pi*x0 - x1/x2**2)**(3/2))",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e-27,
      #       "high": 1e-25
      #     },
      #     {
      #       "name": "x1",
      #       "low": -1.0,
      #       "high": 1.0
      #     },
      #     {
      #       "name": "x2",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     }
      #   ],
      #   "id": 5
      # },
      # {
      #   "var_name": "x2",
      #   "var_display_name": "d",
      #   "order_derivative": 2,
      #   "descriptor": "positive",
      #   "derivative": "-299792458.0*x1*(x1/(x2**2*(1.98030940509831e-27*pi*x0 - x1/x2**2)) + 3)/(x2**4*sqrt(1.98030940509831e-27*pi*x0 - x1/x2**2))",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e-27,
      #       "high": 1e-25
      #     },
      #     {
      #       "name": "x1",
      #       "low": -1.0,
      #       "high": 1.0
      #     },
      #     {
      #       "name": "x2",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     }
      #   ],
      #   "id": 6
      # }
    ]
  },
  {
    "EquationName": "FeynmanBonus8",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x0/(12214328760283.5*x0*(1 - cos(x1)) + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-24,
            "high": 1e-22
          },
          {
            "name": "x1",
            "low": -3.1415926535897932, # PI
            # "low": -3.141592653589793,
            "high": 3.1415926535897932 # PI
            # "high": 3.141592653589793
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "E_n",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "6.70286989185314e-27*x0*(12214328760283.5*cos(x1) - 12214328760283.5)/(x0*(1 - cos(x1)) + 8.18710564965003e-14)**2 + 1/(12214328760283.5*x0*(1 - cos(x1)) + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-24,
            "high": 1e-22
          },
          {
            "name": "x1",
            "low": -3.1415926535897932, # PI
            # "low": -3.141592653589793,
            "high": 3.1415926535897932 # PI
            # "high": 3.141592653589793
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "theta",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-8.18710564965003e-14*x0**2*sin(x1)/(x0*(1 - cos(x1)) + 8.18710564965003e-14)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-24,
            "high": 1e-22
          },
          {
            "name": "x1",
            "low": -3.1415926535897932, # PI
            # "low": -3.141592653589793,
            "high": -4.5622482502949424e-05
          }
        ],
        "id": 2
      },
      # {
      #   "var_name": "x1",
      #   "var_display_name": "theta",
      #   "order_derivative": 1,
      #   "descriptor": "negative",
      #   "derivative": "-8.18710564965003e-14*x0**2*sin(x1)/(x0*(1 - cos(x1)) + 8.18710564965003e-14)**2",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e-24,
      #       "high": 1e-22
      #     },
      #     {
      #       "name": "x1",
      #       "low": -4.5622482502949424e-05,
      #       "high": 3.1415926535897932 # PI
      #       # "high": 3.141592653589793
      #     }
      #   ],
      #   "id": 3
      # },
      {
        "var_name": "x0",
        "var_display_name": "E_n",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "(-x0*(cos(x1) - 1)/(x0*(cos(x1) - 1) - 8.18710564965003e-14) + 1)*(1.63742112993001e-13*cos(x1) - 1.63742112993001e-13)/(x0*(cos(x1) - 1) - 8.18710564965003e-14)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-24,
            "high": 1e-22
          },
          {
            "name": "x1",
            "low": -3.1415926535897932, # PI
            # "low": -3.141592653589793,
            "high": 3.1415926535897932 # PI
            # "high": 3.141592653589793
          }
        ],
        "id": 4
      },
      # {
      #   "var_name": "x1",
      #   "var_display_name": "theta",
      #   "order_derivative": 2,
      #   "descriptor": "positive",
      #   "derivative": "-x0**2*(1.63742112993001e-13*x0*sin(x1)**2/(x0*(cos(x1) - 1) - 8.18710564965003e-14) + 8.18710564965003e-14*cos(x1))/(x0*(cos(x1) - 1) - 8.18710564965003e-14)**2",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e-24,
      #       "high": 1e-22
      #     },
      #     {
      #       "name": "x1",
      #       "low": -3.1415926535897932, # PI
      #       # "low": -3.141592653589793,
      #       "high": -1.5707374215126038
      #     }
      #   ],
      #   "id": 5
      # },
      # {
      #   "var_name": "x1",
      #   "var_display_name": "theta",
      #   "order_derivative": 2,
      #   "descriptor": "negative",
      #   "derivative": "-x0**2*(1.63742112993001e-13*x0*sin(x1)**2/(x0*(cos(x1) - 1) - 8.18710564965003e-14) + 8.18710564965003e-14*cos(x1))/(x0*(cos(x1) - 1) - 8.18710564965003e-14)**2",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e-24,
      #       "high": 1e-22
      #     },
      #     {
      #       "name": "x1",
      #       "low": -1.5707374215126038,
      #       "high": 1.5707963267948966, # 0.5pi 
      #       # "high": 1.5707744359970093
      #     }
      #   ],
      #   "id": 6
      # },
      # {
      #   "var_name": "x1",
      #   "var_display_name": "theta",
      #   "order_derivative": 2,
      #   "descriptor": "positive",
      #   "derivative": "-x0**2*(1.63742112993001e-13*x0*sin(x1)**2/(x0*(cos(x1) - 1) - 8.18710564965003e-14) + 8.18710564965003e-14*cos(x1))/(x0*(cos(x1) - 1) - 8.18710564965003e-14)**2",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 1e-24,
      #       "high": 1e-22
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1.5707963267948966, # 0.5pi 
      #       # "low": 1.5707744359970093,
      #       "high": 3.1415926535897932 # PI
      #       # "high": 3.141592653589793
      #     }
      #   ],
      #   "id": 7
      # }
    ]
  },
  {
    "EquationName": "FeynmanBonus9",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "-5.24444281156413e-83*x0**2*x1**2*(x0 + x1)/x2**5",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x2",
            "low": 100000000.0,
            "high": 10000000000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "m1",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-5.24444281156413e-83*x0**2*x1**2/x2**5 - 1.04888856231283e-82*x0*x1**2*(x0 + x1)/x2**5",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x2",
            "low": 100000000.0,
            "high": 10000000000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "m2",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-5.24444281156413e-83*x0**2*x1**2/x2**5 - 1.04888856231283e-82*x0**2*x1*(x0 + x1)/x2**5",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x2",
            "low": 100000000.0,
            "high": 10000000000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x2",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "2.62222140578207e-82*x0**2*x1**2*(x0 + x1)/x2**6",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x2",
            "low": 100000000.0,
            "high": 10000000000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "m1",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-x1**2*(3.14666568693848e-82*x0 + 1.04888856231283e-82*x1)/x2**5",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x2",
            "low": 100000000.0,
            "high": 10000000000.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "m2",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-x0**2*(1.04888856231283e-82*x0 + 3.14666568693848e-82*x1)/x2**5",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x2",
            "low": 100000000.0,
            "high": 10000000000.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "r",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-1.57333284346924e-81*x0**2*x1**2*(x0 + x1)/x2**7",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x1",
            "low": 1e+23,
            "high": 1e+25
          },
          {
            "name": "x2",
            "low": 100000000.0,
            "high": 10000000000.0
          }
        ],
        "id": 6
      }
    ]
  },
  {
    "EquationName": "FeynmanBonus10",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "theta2",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-3.33564095198152e-9*x1*(-3.33564095198152e-9*x1 + cos(x0))*sin(x0)/(-3.33564095198152e-9*x1*cos(x0) + 1)**2 - sin(x0)/(-3.33564095198152e-9*x1*cos(x0) + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141593098640442
          },
          {
            "name": "x1",
            "low": 100000.0,
            "high": 10000000.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "theta2",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-3.33564095198152e-9*x1*(-3.33564095198152e-9*x1 + cos(x0))*sin(x0)/(-3.33564095198152e-9*x1*cos(x0) + 1)**2 - sin(x0)/(-3.33564095198152e-9*x1*cos(x0) + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 3.1415926535897932, # PI
            # "low": 3.141593098640442,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          },
          {
            "name": "x1",
            "low": 100000.0,
            "high": 10000000.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "3.33564095198152e-9*(-3.33564095198152e-9*x1 + cos(x0))*cos(x0)/(-3.33564095198152e-9*x1*cos(x0) + 1)**2 - 3.33564095198152e-9/(-3.33564095198152e-9*x1*cos(x0) + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          },
          {
            "name": "x1",
            "low": 100000.0,
            "high": 10000000.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "2.22530011210724e-17*((3.33564095198152e-9*x1 - cos(x0))*cos(x0)/(3.33564095198152e-9*x1*cos(x0) - 1) - 1)*cos(x0)/(3.33564095198152e-9*x1*cos(x0) - 1)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1.5707963267948966, # 0.5pi 
            # "high": 1.5707451701164246
          },
          {
            "name": "x1",
            "low": 100000.0,
            "high": 10000000.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "2.22530011210724e-17*((3.33564095198152e-9*x1 - cos(x0))*cos(x0)/(3.33564095198152e-9*x1*cos(x0) - 1) - 1)*cos(x0)/(3.33564095198152e-9*x1*cos(x0) - 1)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 1.5707963267948966, # 0.5pi 
            # "low": 1.5707451701164246,
            "high": 4.7123889803846898 # 1.5pi 
            # "high": 4.712393283843994
          },
          {
            "name": "x1",
            "low": 100000.0,
            "high": 10000000.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "v",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "2.22530011210724e-17*((3.33564095198152e-9*x1 - cos(x0))*cos(x0)/(3.33564095198152e-9*x1*cos(x0) - 1) - 1)*cos(x0)/(3.33564095198152e-9*x1*cos(x0) - 1)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 4.7123889803846898, # 1.5pi 
            # "low": 4.712393283843994,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          },
          {
            "name": "x1",
            "low": 100000.0,
            "high": 10000000.0
          }
        ],
        "id": 5
      }
    ]
  },
  {
    "EquationName": "FeynmanBonus11",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "4*x0*sin(x1/2)**2*sin(x2*x3/2)**2/(x1**2*sin(x3/2)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1e-11,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x3",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "I_0",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "4*sin(x1/2)**2*sin(x2*x3/2)**2/(x1**2*sin(x3/2)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1e-11,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x3",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 1
      },
      {
        "var_name": "x2",
        "var_display_name": "n",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "4*x0*x3*sin(x1/2)**2*sin(x2*x3/2)*cos(x2*x3/2)/(x1**2*sin(x3/2)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1e-11,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x3",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 2
      },
      {
        "var_name": "x0",
        "var_display_name": "I_0",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1e-11,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x3",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 3
      },
      {
        "var_name": "x2",
        "var_display_name": "n",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "-2*x0*x3**2*(sin(x2*x3/2)**2 - cos(x2*x3/2)**2)*sin(x1/2)**2/(x1**2*sin(x3/2)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.001,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1e-11,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": 1.0,
            "high": 100.0
          },
          {
            "name": "x3",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 4
      }
    ]
  },
  {
    "EquationName": "FeynmanBonus12",
    "Constraints": [
      # {
      #   "var_name": "",
      #   "var_display_name": "",
      #   "order_derivative": 0,
      #   "descriptor": "negative",
      #   "derivative": "x0*(-x0*x2**3*x4/(x2**2 - x4**2)**2 + 4*pi*x1*x3*x4)/(4*pi*x1*x2**2)",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": -0.1,
      #       "high": 0.1
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1e-12,
      #       "high": 1e-10
      #     },
      #     {
      #       "name": "x2",
      #       "low": 0.01,
      #       "high": 0.012366482522338629
      #     },
      #     {
      #       "name": "x3",
      #       "low": -10.0,
      #       "high": 10.0
      #     },
      #     {
      #       "name": "x4",
      #       "low": 0.01,
      #       "high": 1.0
      #     }
      #   ],
      #   "id": 0
      # },
      # {
      #   "var_name": "",
      #   "var_display_name": "",
      #   "order_derivative": 0,
      #   "descriptor": "positive",
      #   "derivative": "x0*(-x0*x2**3*x4/(x2**2 - x4**2)**2 + 4*pi*x1*x3*x4)/(4*pi*x1*x2**2)",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": -0.1,
      #       "high": 0.1
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1e-12,
      #       "high": 1e-10
      #     },
      #     {
      #       "name": "x2",
      #       "low": 0.012366482522338629,
      #       "high": 0.012368368916213512
      #     },
      #     {
      #       "name": "x3",
      #       "low": -10.0,
      #       "high": 10.0
      #     },
      #     {
      #       "name": "x4",
      #       "low": 0.01,
      #       "high": 1.0
      #     }
      #   ],
      #   "id": 1
      # },
      # {
      #   "var_name": "",
      #   "var_display_name": "",
      #   "order_derivative": 0,
      #   "descriptor": "negative",
      #   "derivative": "x0*(-x0*x2**3*x4/(x2**2 - x4**2)**2 + 4*pi*x1*x3*x4)/(4*pi*x1*x2**2)",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": -0.1,
      #       "high": 0.1
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1e-12,
      #       "high": 1e-10
      #     },
      #     {
      #       "name": "x2",
      #       "low": 0.012368368916213512,
      #       "high": 1.0
      #     },
      #     {
      #       "name": "x3",
      #       "low": -10.0,
      #       "high": 10.0
      #     },
      #     {
      #       "name": "x4",
      #       "low": 0.01,
      #       "high": 1.0
      #     }
      #   ],
      #   "id": 2
      # },
      # {
      #   "var_name": "x0",
      #   "var_display_name": "q",
      #   "order_derivative": 1,
      #   "descriptor": "positive",
      #   "derivative": "-x0*x2*x4/(4*pi*x1*(x2**2 - x4**2)**2) + (-x0*x2**3*x4/(x2**2 - x4**2)**2 + 4*pi*x1*x3*x4)/(4*pi*x1*x2**2)",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": -0.1,
      #       "high": 0.0
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1e-12,
      #       "high": 1e-10
      #     },
      #     {
      #       "name": "x2",
      #       "low": 0.01,
      #       "high": 1.0
      #     },
      #     {
      #       "name": "x3",
      #       "low": -10.0,
      #       "high": 10.0
      #     },
      #     {
      #       "name": "x4",
      #       "low": 0.01,
      #       "high": 1.0
      #     }
      #   ],
      #   "id": 3
      # },
      # {
      #   "var_name": "x0",
      #   "var_display_name": "q",
      #   "order_derivative": 1,
      #   "descriptor": "negative",
      #   "derivative": "-x0*x2*x4/(4*pi*x1*(x2**2 - x4**2)**2) + (-x0*x2**3*x4/(x2**2 - x4**2)**2 + 4*pi*x1*x3*x4)/(4*pi*x1*x2**2)",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": 0.0,
      #       "high": 0.1
      #     },
      #     {
      #       "name": "x1",
      #       "low": 1e-12,
      #       "high": 1e-10
      #     },
      #     {
      #       "name": "x2",
      #       "low": 0.01,
      #       "high": 1.0
      #     },
      #     {
      #       "name": "x3",
      #       "low": -10.0,
      #       "high": 10.0
      #     },
      #     {
      #       "name": "x4",
      #       "low": 0.01,
      #       "high": 1.0
      #     }
      #   ],
      #   "id": 4
      # },
      {
        "var_name": "x1",
        "var_display_name": "epsilon",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*x3*x4/(x1*x2**2) - x0*(-x0*x2**3*x4/(x2**2 - x4**2)**2 + 4*pi*x1*x3*x4)/(4*pi*x1**2*x2**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1e-12,
            "high": 1e-10
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x3",
        "var_display_name": "Volt",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x0*x4/x2**2",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 1e-12,
            "high": 1e-10
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x3",
        "var_display_name": "Volt",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*x4/x2**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1e-12,
            "high": 1e-10
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 7
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-x2*x4/(2*pi*x1*(x2**2 - x4**2)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1e-12,
            "high": 1e-10
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 8
      },
      {
        "var_name": "x1",
        "var_display_name": "epsilon",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-x0*x4*(2*x3 + (x0*x2**3/(x2**2 - x4**2)**2 - 4*pi*x1*x3)/(2*pi*x1))/(x1**2*x2**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1e-12,
            "high": 1e-10
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 9
      },
      {
        "var_name": "x3",
        "var_display_name": "Volt",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1e-12,
            "high": 1e-10
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 10
      },
      {
        "var_name": "x4",
        "var_display_name": "d",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-3*x0**2*x2*x4*(2*x4**2/(x2**2 - x4**2) + 1)/(pi*x1*(x2**2 - x4**2)**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 1e-12,
            "high": 1e-10
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x4",
            "low": 0.01,
            "high": 1.0
          }
        ],
        "id": 11
      }
    ]
  },
  {
    "EquationName": "FeynmanBonus13",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "negative",
        "derivative": "28235825615.541*x0/(pi*sqrt(x1**2 - 2*x1*x2*cos(x3) + x2**2))",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141592653589793
          }
        ],
        "id": 0
      },
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "28235825615.541*x0/(pi*sqrt(x1**2 - 2*x1*x2*cos(x3) + x2**2))",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141592653589793
          }
        ],
        "id": 1
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "28235825615.541/(pi*sqrt(x1**2 - 2*x1*x2*cos(x3) + x2**2))",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141592653589793
          }
        ],
        "id": 2
      },
      {
        "var_name": "x3",
        "var_display_name": "alpha",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-28235825615.541*x0*x1*x2*sin(x3)/(pi*(x1**2 - 2*x1*x2*cos(x3) + x2**2)**(3/2))",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141592653589793
          }
        ],
        "id": 3
      },
      {
        "var_name": "x3",
        "var_display_name": "alpha",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-28235825615.541*x0*x1*x2*sin(x3)/(pi*(x1**2 - 2*x1*x2*cos(x3) + x2**2)**(3/2))",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141592653589793
          }
        ],
        "id": 4
      },
      {
        "var_name": "x0",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -0.1,
            "high": 0.1
          },
          {
            "name": "x1",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141592653589793
          }
        ],
        "id": 5
      }
    ]
  },
  {
    "EquationName": "FeynmanBonus14",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "Ef",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141592653589793
          },
          {
            "name": "x2",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x3",
            "low": 0.01,
            "high": 1.0
          },
          {
            "name": "x4",
            "low": 0.1,
            "high": 10.0
          }
        ],
        "id": 0
      }
    ]
  },
  {
    "EquationName": "FeynmanBonus15",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x1*sqrt(1 - 1.11265005605362e-17*x0**2)/(3.33564095198152e-9*x0*cos(x2) + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000.0,
            "high": 10000000.0
          },
          {
            "name": "x1",
            "low": 1000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 0
      },
      {
        "var_name": "x1",
        "var_display_name": "omega",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "sqrt(1 - 1.11265005605362e-17*x0**2)/(3.33564095198152e-9*x0*cos(x2) + 1)",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000.0,
            "high": 10000000.0
          },
          {
            "name": "x1",
            "low": 1000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 1
      },
      {
        "var_name": "x2",
        "var_display_name": "theta",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "3.33564095198152e-9*x0*x1*sqrt(1 - 1.11265005605362e-17*x0**2)*sin(x2)/(3.33564095198152e-9*x0*cos(x2) + 1)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000.0,
            "high": 10000000.0
          },
          {
            "name": "x1",
            "low": 1000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 3.1415926535897932 # PI
            # "high": 3.141624689102173
          }
        ],
        "id": 2
      },
      {
        "var_name": "x2",
        "var_display_name": "theta",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "3.33564095198152e-9*x0*x1*sqrt(1 - 1.11265005605362e-17*x0**2)*sin(x2)/(3.33564095198152e-9*x0*cos(x2) + 1)**2",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000.0,
            "high": 10000000.0
          },
          {
            "name": "x1",
            "low": 1000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x2",
            "low": 3.1415926535897932, # PI
            # "low": 3.141624689102173,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 3
      },
      {
        "var_name": "x1",
        "var_display_name": "omega",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 100000.0,
            "high": 10000000.0
          },
          {
            "name": "x1",
            "low": 1000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 4
      }
    ]
  },
  {
    "EquationName": "FeynmanBonus16",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "x1*x4 + 8.98755178736818e+16*sqrt(x3**2 + 1.11265005605362e-17*(x0 - x1*x2)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-07,
            "high": 1e-07
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x3",
        "var_display_name": "m",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "8.98755178736818e+16*x3/sqrt(x3**2 + 1.11265005605362e-17*(x0 - x1*x2)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-07,
            "high": 1e-07
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x4",
        "var_display_name": "Volt",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x1",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-07,
            "high": 1e-07
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 0.0
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x4",
        "var_display_name": "Volt",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x1",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-07,
            "high": 1e-07
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "p",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "(-1.11265005605362e-17*(x0 - x1*x2)**2/(x3**2 + 1.11265005605362e-17*(x0 - x1*x2)**2) + 1.0)/sqrt(x3**2 + 1.11265005605362e-17*(x0 - x1*x2)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-07,
            "high": 1e-07
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "q",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "x2**2*(-1.11265005605362e-17*(x0 - x1*x2)**2/(x3**2 + 1.11265005605362e-17*(x0 - x1*x2)**2) + 1.0)/sqrt(x3**2 + 1.11265005605362e-17*(x0 - x1*x2)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-07,
            "high": 1e-07
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x2",
        "var_display_name": "A_vec",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "x1**2*(-1.11265005605362e-17*(x0 - x1*x2)**2/(x3**2 + 1.11265005605362e-17*(x0 - x1*x2)**2) + 1.0)/sqrt(x3**2 + 1.11265005605362e-17*(x0 - x1*x2)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-07,
            "high": 1e-07
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x3",
        "var_display_name": "m",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "8.98755178736818e+16*(-x3**2/(x3**2 + 1.11265005605362e-17*(x0 - x1*x2)**2) + 1)/sqrt(x3**2 + 1.11265005605362e-17*(x0 - x1*x2)**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-07,
            "high": 1e-07
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 7
      },
      {
        "var_name": "x4",
        "var_display_name": "Volt",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1e-07,
            "high": 1e-07
          },
          {
            "name": "x1",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x2",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x3",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 8
      }
    ]
  },
  {
    "EquationName": "FeynmanBonus17",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "(x0**2*x2**2*x3**2*(x3*x4/x5 + 1) + x1**2)/(2*x0)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x1",
            "low": -1e-07,
            "high": 1e-07
          },
          {
            "name": "x2",
            "low": -100000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x3",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "m",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x2**2*x3**2*(x3*x4/x5 + 1) - (x0**2*x2**2*x3**2*(x3*x4/x5 + 1) + x1**2)/(2*x0**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x1",
            "low": -1e-07,
            "high": 1e-07
          },
          {
            "name": "x2",
            "low": -100000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x3",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "p",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x1/x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x1",
            "low": -1e-07,
            "high": 0.0
          },
          {
            "name": "x2",
            "low": -100000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x3",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "p",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x1/x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x1",
            "low": 0.0,
            "high": 1e-07
          },
          {
            "name": "x2",
            "low": -100000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x3",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 3
      },
      {
        "var_name": "x4",
        "var_display_name": "alpha",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "x0*x2**2*x3**3/(2*x5)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x1",
            "low": -1e-07,
            "high": 1e-07
          },
          {
            "name": "x2",
            "low": -100000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x3",
            "low": -1e-09,
            "high": 0.0
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 4
      },
      {
        "var_name": "x4",
        "var_display_name": "alpha",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "x0*x2**2*x3**3/(2*x5)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x1",
            "low": -1e-07,
            "high": 1e-07
          },
          {
            "name": "x2",
            "low": -100000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x3",
            "low": 0.0,
            "high": 1e-09
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 5
      },
      {
        "var_name": "x0",
        "var_display_name": "m",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "(-x2**2*x3**2*(x3*x4/x5 + 1) + (x0**2*x2**2*x3**2*(x3*x4/x5 + 1) + x1**2)/x0**2)/x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x1",
            "low": -1e-07,
            "high": 1e-07
          },
          {
            "name": "x2",
            "low": -100000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x3",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 6
      },
      {
        "var_name": "x1",
        "var_display_name": "p",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "1/x0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x1",
            "low": -1e-07,
            "high": 1e-07
          },
          {
            "name": "x2",
            "low": -100000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x3",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 7
      },
      {
        "var_name": "x4",
        "var_display_name": "alpha",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": 1e-30,
            "high": 1e-28
          },
          {
            "name": "x1",
            "low": -1e-07,
            "high": 1e-07
          },
          {
            "name": "x2",
            "low": -100000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x3",
            "low": -1e-09,
            "high": 1e-09
          },
          {
            "name": "x4",
            "low": -10.0,
            "high": 10.0
          },
          {
            "name": "x5",
            "low": 1e-11,
            "high": 1e-09
          }
        ],
        "id": 8
      }
    ]
  },
  {
    "EquationName": "FeynmanBonus18",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "k_f",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "5.04971595562541e+26/(pi*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "-1.00994319112508e+27*x0/(pi*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-1.00994319112508e+27*x0/(pi*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x2",
        "var_display_name": "H_G",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "11237133482.1629*x2/pi",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 0.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x2",
        "var_display_name": "H_G",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "11237133482.1629*x2/pi",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 100.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x0",
        "var_display_name": "k_f",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "3.02982957337525e+27*x0/(pi*x1**4)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          }
        ],
        "id": 6
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "3.02982957337525e+27*x0/(pi*x1**4)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          }
        ],
        "id": 7
      },
      {
        "var_name": "x2",
        "var_display_name": "H_G",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "11237133482.1629/pi",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          }
        ],
        "id": 8
      }
    ]
  },
  {
    "EquationName": "FeynmanBonus19",
    "Constraints": [
      {
        "var_name": "x0",
        "var_display_name": "k_f",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "-1.51281945542276e+43/(pi*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 0
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "3.02563891084552e+43*x0/(pi*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "3.02563891084552e+43*x0/(pi*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 2
      },
      {
        "var_name": "x3",
        "var_display_name": "alpha",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "3.36647730375027e+26*x2**2/pi",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 3
      },
      {
        "var_name": "x0",
        "var_display_name": "k_f",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 4
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "-9.07691673253655e+43*x0/(pi*x1**4)",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 0.0
          },
          {
            "name": "x1",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 5
      },
      {
        "var_name": "x1",
        "var_display_name": "r",
        "order_derivative": 2,
        "descriptor": "negative",
        "derivative": "-9.07691673253655e+43*x0/(pi*x1**4)",
        "sample_space": [
          {
            "name": "x0",
            "low": 0.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 6
      },
      # {
      #   "var_name": "x2",
      #   "var_display_name": "H_G",
      #   "order_derivative": 2,
      #   "descriptor": "negative",
      #   "derivative": "1872855580.36049*(3.59502071494727e+17*x3 - 1.79751035747364e+17)/pi",
      #   "sample_space": [
      #     {
      #       "name": "x0",
      #       "low": -1000.0,
      #       "high": 1000.0
      #     },
      #     {
      #       "name": "x1",
      #       "low": 100000000.0,
      #       "high": 10000000000.0
      #     },
      #     {
      #       "name": "x2",
      #       "low": -100.0,
      #       "high": 100.0
      #     },
      #     {
      #       "name": "x3",
      #       "low": -10.0,
      #       "high": 0.5000261962413788
      #     }
      #   ],
      #   "id": 7
      # },
      {
        "var_name": "x2",
        "var_display_name": "H_G",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "1872855580.36049*(3.59502071494727e+17*x3 - 1.79751035747364e+17)/pi",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          },
          {
            "name": "x3",
            "low": 0.5000261962413788,
            "high": 10.0
          }
        ],
        "id": 8
      },
      {
        "var_name": "x3",
        "var_display_name": "alpha",
        "order_derivative": 2,
        "descriptor": "zero",
        "derivative": "0",
        "sample_space": [
          {
            "name": "x0",
            "low": -1000.0,
            "high": 1000.0
          },
          {
            "name": "x1",
            "low": 100000000.0,
            "high": 10000000000.0
          },
          {
            "name": "x2",
            "low": -100.0,
            "high": 100.0
          },
          {
            "name": "x3",
            "low": -10.0,
            "high": 10.0
          }
        ],
        "id": 9
      }
    ]
  },
  {
    "EquationName": "FeynmanBonus20",
    "Constraints": [
      {
        "var_name": "",
        "var_display_name": "",
        "order_derivative": 0,
        "descriptor": "positive",
        "derivative": "7.83707760458308e-29*x0**2*(x0/x1 - sin(x2)**2 + x1/x0)/(pi*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x1",
            "low": 1000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 0
      },
      {
        "var_name": "x0",
        "var_display_name": "omega_0",
        "order_derivative": 1,
        "descriptor": "positive",
        "derivative": "7.83707760458308e-29*x0**2*(1/x1 - x1/x0**2)/(pi*x1**2) + 1.56741552091662e-28*x0*(x0/x1 - sin(x2)**2 + x1/x0)/(pi*x1**2)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x1",
            "low": 1000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 1
      },
      {
        "var_name": "x1",
        "var_display_name": "omega",
        "order_derivative": 1,
        "descriptor": "negative",
        "derivative": "7.83707760458308e-29*x0**2*(-x0/x1**2 + 1/x0)/(pi*x1**2) - 1.56741552091662e-28*x0**2*(x0/x1 - sin(x2)**2 + x1/x0)/(pi*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x1",
            "low": 1000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 2
      },
      {
        "var_name": "x1",
        "var_display_name": "omega",
        "order_derivative": 2,
        "descriptor": "positive",
        "derivative": "x0**2*(4.70224656274985e-28*x0/x1**2 + (4.70224656274985e-28*x0/x1 - 4.70224656274985e-28*sin(x2)**2 + 4.70224656274985e-28*x1/x0)/x1 - 3.13483104183323e-28/x0)/(pi*x1**3)",
        "sample_space": [
          {
            "name": "x0",
            "low": 1000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x1",
            "low": 1000000000.0,
            "high": 100000000000.0
          },
          {
            "name": "x2",
            "low": 0.0,
            "high": 6.2831853071795864 # 2pi 
            # "high": 6.283185307179586
          }
        ],
        "id": 3
      }
    ]
  }
]