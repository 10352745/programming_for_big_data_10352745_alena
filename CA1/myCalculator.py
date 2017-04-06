# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:31:56 2017

@author: Alena

"""
import math

while True:

    def sum(n1, n2):
        plus = n1+n2
        return plus
    
    def substract(n1, n2):
        minus = n1-n2
        return minus
    
    def multiple(n1, n2):
        by = n1*n2
        return by
    
    def divide (n1, n2):
        if n2 ==0:
            return "Error"
        over = n1/float(n2)
        return over
    
    def exponent(n1, n2):
        exp = n1**n2
        return exp
    
    def square(n):
        square = n*n
        return square  
    
    def sqroot(n):
        sqroot = math.sqrt(n)
        return sqroot
    
    def perc(n1, n2):
        perc = (n1 /100)*n2
        return perc
    
    def sin(n):
        sin =math.sin(math.radians(n))
        return float(sin)
    
    def cos(n):
        cos =math.cos(math.radians(n))
        return float(cos)
    
    if "Q" == raw_input("This is a simle calculator.\n To continue press ENTER or Q to Quit the program\n"):
        break
    func = raw_input("Please input operation: '+', '-','*', '/','**','sq', 'sqr','sin','cos','%'\n")
    
    if func =="+":
        n1 = int (raw_input("enter number 1\n"))
        n2 = int(raw_input ("enter number 2\n"))
        plus = sum(n1,n2)
        print plus
    elif func =="-":
        n1 = int (raw_input("enter number 1\n"))
        n2 = int(raw_input ("enter number 2\n"))
        minus = substract(n1,n2)
        print minus
    elif func =="*":
        n1 = int (raw_input("enter number 1\n"))
        n2 = int(raw_input ("enter number 2\n"))
        by = multiple(n1,n2)
        print by
    elif func =="/":
        n1 = int (raw_input("enter number 1\n"))
        n2 = int(raw_input ("enter number 2\n"))
        over = divide(n1,n2)
        print  over
    elif func =="**":
        n1 = int (raw_input("enter number 1\n"))
        n2 = int(raw_input ("enter number 2\n"))
        exp = exponent(n1,n2)
        print exp
    elif func =="sq":
        n1 = int (raw_input("enter number 1\n"))
        sq = square(n1)
        print  sq
    elif func =="sqr":
         n1 = int (raw_input("enter number 1\n"))
         sqr = sqroot(n1)
         print sqr
    elif func =="perc":
        n1 = int (raw_input("enter number 1\n"))
        n2 = int (raw_input("enter %"))
        print perc(n1, n2)
    elif func =="cos":
        n1 = float (raw_input("enter number "))
        print cos(n1)
    elif func =="sin":
        n1 = float (raw_input("enter number "))
        print sin(n1)
        
    else:
        print "Invalid selection"
        break
print "Bye"