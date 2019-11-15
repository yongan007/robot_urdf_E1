
### 3 Link Forward Kinematics ###

import numpy as np
from numpy import array
import sympy
from sympy import *
from sympy import symbols, cos, sin, pi, simplify, sqrt, atan2, pprint
from sympy.matrices import Matrix

def fk_3link(theta1,theta2,theta3):

    # Create symbols for DH param
    q1, q2, q3 = symbols('q1:4')                               # joint angles theta
    d1, d2, d3 = symbols('d1:4')                              # link offsets
    a0, a1, a2 = symbols('a0:3')                              # link lengths
    alpha0, alpha1, alpha2 = symbols('alpha0:3') # joint twist angles

    # DH Table
    dh = {alpha0:      0, a0:      0, d1:  0.75, q1:        q1,
          alpha1: -pi/2., a1:   0.35, d2:     0, q2: -pi/2.+q2,
          alpha2:      0, a2:   1.25, d3:     0, q3:        q3,}

    # Function to return homogeneous transform matrix

    def TF_Mat(alpha, a, d, q):
        TF = Matrix([[            cos(q),           -sin(q),           0,             a],
                     [ sin(q)*cos(alpha), cos(q)*cos(alpha), -sin(alpha), -sin(alpha)*d],
                     [ sin(q)*sin(alpha), cos(q)*sin(alpha),  cos(alpha),  cos(alpha)*d],
                     [                 0,                 0,           0,             1]])
        return TF

    ## Substiute DH_Table
    T0_1 = TF_Mat(alpha0, a0, d1, q1).subs(dh)
    T1_2 = TF_Mat(alpha1, a1, d2, q2).subs(dh)
    T2_3 = TF_Mat(alpha2, a2, d3, q3).subs(dh)

    #Homogeneous Transforms

    T0_2 = (T0_1 * T1_2) ## (Base) Link_0 to Link_2
    T0_3 = (T0_2 * T2_3) ## (Base) Link_0 to Link_3

    T0_3_value = N(T0_3.evalf(subs={q1: theta1, q2: theta2, q3: theta3}),2) #two digit output
    #print(T0_3 )
    print('T0_3= \n    ',T0_3_value)
    print("result:",np.array([T0_3_value]))

    #print("\nT_total Matrix : \n")
    print("\n")

    return np.array([T0_3_value])

#fk_3link(pi/3,pi/3,pi/3)

#fk_3link(0,0,0)

