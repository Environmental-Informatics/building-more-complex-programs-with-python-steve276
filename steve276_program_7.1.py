#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 19:25:09 2020
Miriam Stevens
@author: steve276

ABE65100 - ThinkPython - Excercise 7.1

This program uses 'while True' and 'for loop' iteration to compare Newton's 
square root algorithm with the square root function in the math module.

.....................

"""
import math

def prt_header():
    print('a   mysqrt(a)     math.sqrt(a)  diff')
    print('_   _________     ____________  ____')

#first try    
#def mysqrt(a):
#    a = float(a)
#    x = .625*a
#    alg = (x + a/x) / 2
#    math_alg = math.sqrt(a)
#    diff = abs(alg - math_alg)
#    print(a, end =" ") 
#    print('%.7f'%alg,"   ", end =" ")
#    print('%.11f'%math_alg, end =" ")
#    print(diff)
    
#def test_square_root(a):
#    prt_header()
#    mysqrt(a)
    
def mysqrt(a):
    a = float(a)
    x = .625*a                                 #reasonable value of x required by in prompt
    epsilon = 0.0000001
    while True:
        alg = (x + a/x) / 2
        if abs(alg-x) < epsilon:
#            print(x)
            break
        x = alg
            
    math_alg = math.sqrt(a)
    diff = abs(alg - math_alg)                 # abs of difference between squrt calculations
    print(a, end =" ")                         #prints base value for taking sqrt
    print('%.7f'%alg, "   ", end =" ")         #prints newton's sqrt algorithm
    print('%.7f'%math_alg, "   ", end =" ")    #prints sqrt calculation from math
    print(diff)    
    
def test_square_root():
    prt_header()
    for a in range (1, 10):                     #iterate 9 times for a={1-9}
        mysqrt(a)
 
