#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 18:10:55 2020
Miriam Stevens
@author: steve276

BE65100 - ThinkPython - Exercise 4.2

This program contains a set of generalized functions and refactors them to draw
the flowers in ThinkPython exercise 4.2.
"""

import turtle

import math

spud = turtle.Turtle()

def polyline(t, n, length, angle):
    """Draws n line segments with the given length and angle (in degrees)
    between them. t is a turtle.
    """
    for i in range(n):
        t.fd(length)                       #move turtle forward
        t.lt(angle)                        #turn turtle to left
        
        
def polygon(t, n, length):
    """Draws an n sided, polygon with exterior angles of 360/n and with the
    given length.
    """
    angle = 360.0 /n
    polyline(t, n, length, angle)
    
    
def arc(t, r, angle):
    """Draws an arc of a length that is a fraction of a circle (angle/360)
    with radius r.
    """
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length / 3) + 1               #ensures arc length is at least 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
    

def draw_petal(t, r, angle):
    """Draws a petal from two arcs. Turtle moves with pen down (pd)."""
    for i in range(2):
        t.pd()
        arc(t, r, angle)                       
        t.lt(180.0-angle) 
        
def draw_flower(t, n, r, angle):
    """Draws n number of arcs to form a flower."""
    for i in range(n):
        draw_petal(t, r, angle)
        t.lt(360.0/n)
        
def move(t, d):
    """Moves turtle to new location with pen up."""
    t.pu()
    t.fd(d)
        
move(spud,-150)
draw_flower(spud, 7, 100, (360.0/7))

move(spud,150)
draw_flower(spud, 10, 60, (360.0/5))

move(spud,150)
draw_flower(spud, 20, 200, (360.0/20))

spud.hideturtle()
turtle.mainloop()




              

#def draw_flower
    

        

