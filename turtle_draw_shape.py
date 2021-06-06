#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 11:42:06 2021

@author: zhaozhg
"""

class turtle_draw_shape:
    def __init__(self, turtlename):
        self.myturtle=turtlename
        self.myturtle.up()
        
    def plot_oval(self, width, color, start_x, start_y, a, b, angle, fill ):               # Horizontal Oval
        self.myturtle.up()
        self.myturtle.width(width)
        self.myturtle.color(color)
        self.myturtle.setheading(0)
        self.myturtle.right(angle)
        self.myturtle.goto(start_x,start_y)
        self.myturtle.down()
        if fill == True:
            self.myturtle.begin_fill()
        for loop in range(2):        
            self.myturtle.circle(a,90)
            self.myturtle.circle(b,90)
        if fill == True :
            self.myturtle.end_fill()
        
    def plot_sun(self, width, color, start_x, start_y, radius):
        self.myturtle.up()
        self.myturtle.width(width)
        self.myturtle.color(color)
        self.myturtle.setheading(90)        
        self.myturtle.goto(start_x,start_y)
        self.myturtle.down()
        self.myturtle.begin_fill()
        self.myturtle.circle(radius)
        self.myturtle.end_fill()
        self.myturtle.up()
        self.rest()
        
    def plot_fillable_rec(self, color, start_x, start_y, rec_width, rec_leng):
        self.myturtle.up()
        self.myturtle.color(color)
        self.myturtle.setheading(90)        
        self.myturtle.goto(start_x,start_y)
        self.myturtle.down()
        self.myturtle.begin_fill()
        for i in range(2):
            self.myturtle.forward( rec_width) 
            self.myturtle.right(90)
            self.myturtle.forward( rec_leng )
            self.myturtle.right(90)
        
        self.myturtle.end_fill()
        self.rest()

    def plot_plain_rec(self, color, start_x, start_y, rec_width, rec_leng):
        self.myturtle.up()
        self.myturtle.color(color)
        self.myturtle.setheading(90)        
        self.myturtle.goto(start_x,start_y)
        self.myturtle.down()        
        for i in range(2):
            self.myturtle.forward( rec_width) 
            self.myturtle.right(90)
            self.myturtle.forward( rec_leng )
            self.myturtle.right(90)
        self.myturtle.rest()

            
    def rest(self):
        self.myturtle.up()
        self.myturtle.goto(-600,300)
        self.myturtle.setheading(90)
        
        