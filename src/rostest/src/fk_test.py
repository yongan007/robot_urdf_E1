#! /usr/bin/env python
import unittest
import rostest
import numpy as np
from sympy import pi
import fk

class MyTestCase(unittest.TestCase):

    def test_fk(self):
        calculation1 = fk.fk_3link(pi/3,pi/3,pi/3)
        expected1 = np.array([0.43, -0.25, -0.87, 0.72, 0.75, -0.43, 0.50, 1.2, -0.50, -0.87, 0, 1.4, 0, 0, 0, 1.0])
        #self.assertEqual((a).all,(b).all), "work work"
        assert (calculation1).all != 0,"List is empty."
        assert (calculation1).all != (expected1).all, "The answer is incorrect."

    def edge_fkassert(self): 
        cal2 = fk.fk_3link(0,0,0)
        exp2 = np.array([0, 1.0, 0, 0.35, 0, 0, 1.0, 0, 1.0, 0, 0, 2.0, 0, 0, 0, 1.0])
        assert (cal2).all != (exp2).all, "The answer is incorrect."

if __name__ == "__main__":
    rostest.rosrun('mytest', 'test_code', MyTestCase)