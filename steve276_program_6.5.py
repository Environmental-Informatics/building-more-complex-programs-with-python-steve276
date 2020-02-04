#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:54:44 2020
by Miriam Stevens
@author: steve276

ABE65100 - ThinkPython - Exercise 6.5

This program prompts the user for two values then computes the greatest
common divisor (GCD).

"""

def find_gcd(x,y):
    if x == y or y == 0:
        return x
    if x == 0:
        return y 
    elif x > y:
        a = x
        b = y
        print('a is',a,'and b is',b)
        if a % b == 0 :
            return b                         # this works
        else:
            r = a % b
            recurse = find_gcd((a % b),b)
            result = recurse((a % b), b)
            return result
  
    #          if b == 1:
 #               return a
    elif x < y:
        a = y
        b = x
        print('a is',a,'and b is',b)
        if a % b == 0 :
            return b
        else:
            r = a % b
            recurse = find_gcd((a % b),b)
            result = recurse((b % r), r)
            return result
        

def gcd():
    prompt_x = 'Choose a number for x.\n'
    x = input(prompt_x)
    
    prompt_y = 'Choose a number for y.\n'
    y = input(prompt_y) 
    
    find_gcd(int(x),int(y))
    
#currently only works if input x or y is gcd
    

