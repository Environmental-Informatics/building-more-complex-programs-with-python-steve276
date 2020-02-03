#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:31:06 2020
by Miriam Stevens
@author: steve276

ABE65100 - ThinkPython - Exercise 5.2

This program uses nested conditionals and recursion to check whether Format's
Last Theorem is true for diferent user-input values.

"""
#part 1

def check_fermat(a,b,c,n):
    if n > 2:                                       # condition is boolean expression 'n > 2'
        if (a**n)+(b**n)==c**n:                     # nested conditional
            print('Holy smokes,Fermat was wrong!')
        else: 
            print("No, that doesn't work.")
#            print((a**n)+(b**n)==c**n,(a**n)+(b**n))
#            print("(a^n)+(b^n) =",(a**n)+(b**n),   # prints why it doesn't work
#                  "but c^n =",(c**n))
    if n <= 2:
        print("n is not greater than 2.")
#part 2
def help_check_fermat():
    prompt_a = 'Pick an integer, a.\n'              # defines the prompt
    fermat_a = input(prompt_a)                      # uses the prompt to gather user input
    
    prompt_b = 'Pick an integer, b.\n'
    fermat_b = input(prompt_b)
    
    prompt_c = 'Pick an integer, c.\n'
    fermat_c = input(prompt_c)
    
    prompt_n = 'Pick an integer, n, that is greater than 2.\n'
    fermat_n = input(prompt_n)
    
    check_fermat(int(fermat_a),int(fermat_b),int(fermat_c),int(fermat_n))
    # the above line takes user the user input and converts it to an integer
    # before using it as parameters in check_fermat function.
    


