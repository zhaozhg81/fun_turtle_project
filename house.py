#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 19:53:31 2021

@author: zhaozhg
"""

import turtle
from math import tan, sin, pi
from turtle_draw_shape import turtle_draw_shape


class house:
    house_width=1000
    house_height=500
    door_width = 100
    door_height= 200
    start_x=-500
    start_y=-400
    
    def __init__(self, turtlename, turtle_plot, start_x, start_y, house_width, house_height):
        self.myturtle=turtlename
        self.myplot=turtle_plot
        self.myturtle.up()
        self.start_x = start_x
        self.start_y = start_y
        self.house_width=house_width
        self.house_height=house_height
        
        
            
    def frame(self, width, color, start_x, start_y, house_width, house_height):
        self.myplot.plot_rectangular(width, color, start_x, start_y, house_height, house_width)
        self.rest()
        
    def door(self, width, color_border, color_fill, start_x, start_y, door_height, door_width):
        self.myplot.plot_fillable_rectangular(width, color_border, color_fill, start_x, start_y, door_height, door_width)

    def roof(self, width, color, start_x, start_y, angle, roof_length):
        self.myplot.plot_upside_v( width, color, start_x, start_y, 180-angle, roof_length)        
        self.myturtle.left(angle)
        
        gaps = 5
        roof_gap = self.house_width/2/sin(angle*pi/180)/gaps
        
        for i in range(gaps):
            self.myturtle.forward( self.house_width/2/tan(angle*pi/180) * (gaps-i)/gaps )    
            self.myturtle.backward( self.house_width/2/tan(angle*pi/180) * (gaps-i)/gaps )    
            self.myturtle.right(angle)
            self.myturtle.forward(roof_gap)
            self.myturtle.left(angle)
        self.myturtle.right(angle)
        self.myturtle.backward( gaps*roof_gap)
        self.myturtle.left(angle)
        for i in range(gaps):
            self.myturtle.forward( self.house_width/2/tan(angle*pi/180) * (gaps-i)/gaps )    
            self.myturtle.backward( self.house_width/2/tan(angle*pi/180) * (gaps-i)/gaps )    
            self.myturtle.left(angle)
            self.myturtle.forward(roof_gap)
            self.myturtle.right(angle)
        self.myturtle.left(angle)
        self.myturtle.backward( gaps*roof_gap)
        self.myturtle.right(angle)
        
    def rest(self):          
        self.myturtle.up()
        self.myturtle.goto(-600,300)
        self.myturtle.setheading(90)

    def final_rest(self, pos_x,pos_y):
        self.myturtle.up()
        self.myturtle.goto(pos_x,pos_y)
        self.myturtle.setheading(90)
    
    def plot_house(self):
        angle = 60
        self.frame(5, 'blue', self.start_x, self.start_y, self.house_width, self.house_height)
        self.door(5,'black','red', self.start_x + self.house_width/4 - self.door_width/2, self.start_y, self.door_height, self.door_width)
        self.door(5,'black','blue', self.start_x + self.house_width*3/4 - self.door_width/2, self.start_y, self.door_height, self.door_width)
        self.roof(5,'brown', self.start_x + self.house_width/2, self.start_y + self.house_height + self.house_width/2/tan(angle*pi/180),angle, self.house_width/2/sin(angle*pi/180)*1.2 )
        
def main():
    house_width= 1000
    house_height=500
    start_x=-500
    start_y=-400
    turtle_width=5
    
    turtlescreen = turtle.getscreen()
    myturtle = turtle.Turtle()
    myturtle.shape('turtle')
    myturtle.width(5)    
    myplot = turtle_draw_shape(myturtle)
    myhouse = house(myturtle, myplot, start_x, start_y, house_width, house_height)
    

    myhouse.plot_house()
    
if __name__=="__main__":
    main()
