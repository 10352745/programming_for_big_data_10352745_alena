# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from myCalculator import *

import unittest

class TestCalculator(unittest.TestCase):
    def testAdd1(self):
        self.assertEqual(sum(2,2),4)
    def testAdd2(self):
        self.assertEqual(sum(6,3),9)
    def testAdd3(self):
        self.assertEqual(sum(5,3),8)
        
    def testSubstract1(self):
        self.assertEqual(substract(2,2),0)
    def testSubstract2(self):
        self.assertEqual(substract(6,3),3)
    def testSubstract3(self):
        self.assertEqual(substract(5,3),2)
        
    def testMultiple1(self):
        result = multiple(2,2)
        self.assertEqual(result, 4)
        
        self.assertEqual(multiple(2,2),4)
    def testMultiple2(self):
        self.assertEqual(multiple(6,3),18)
    def testMultiple3(self):
        self.assertEqual(multiple(5,3),15)
        
    def testDivide(self):
        # 4/1=4
        #4/2=2
        #2/2=1
        #0/1=0
        #4/3 = 1.25
        self.assertEqual(divide(4,1),4)
        self.assertEqual(divide(4,2),2)
        self.assertEqual(divide(2,2),1)
        self.assertEqual(divide(0,1),0)
        self.assertEqual(divide(5,4),1.25)

    def testExponent(self):
        # 1**1=1
        #2**2 =4
        #4**2=16
                
        self.assertEqual(exponent(1,1),1)
        self.assertEqual(exponent(2,2),4)
        self.assertEqual(exponent(4,2),16)
        
    def testSquare(self):
        # 4*4 =16
        # 2*2 = 4.0
        # 9*9 =81.0 
        self.assertEqual(square(4),16.0)
        self.assertEqual(square(2),4.0)
        self.assertEqual(square(9),81.0) 
        
    def testSqRoot(self):
        # 4**0,5 =2.0
        # 16**0,5 = 4.0
        # 81**0,5 =9.0 
        self.assertEqual(sqroot(4),2.0)
        self.assertEqual(sqroot(16),4.0)
        self.assertEqual(sqroot(81),9.0) 
        
    def testPercentage(self):
        # 10% of 100 =10
        # 5% of 100 = 5
        # 3% of 10 =3
        self.assertEqual(perc(100,10),10)
        self.assertEqual(perc(100,5),5)
       
    def testSin(self):
        #sin  = -0.50636564
        #sin 5 = -0.95892427
        self.assertEqual(round(sin(30), 2),0.5)
        self.assertEqual(sin(90),1)
        
    def testCos(self):
        #sin 100 = -0.50636564
        #sin 5 = -0.95892427
        self.assertEqual(round(cos(60),2),0.5)
        self.assertEqual(round(cos(90),2),0)
                
if __name__=="__main__":
    unittest.main()