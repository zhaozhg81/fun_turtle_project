#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 17:53:34 2021

@author: zhaozhg
"""

import turtle
from turtle_draw_shape import turtle_draw_shape
import math

class train:
    def __init__(self, turtlename):
        self.myturtle=turtlename
        self.myturtle.up()

    def carriage(self, width, color, start_x, start_y, carriage_width, carriage_length):
        self.myturtle.goto( start_x, start_y)
        self.myturtle.width(width)
        self.myturtle.color(color)
        
        ## Plot the frame
        ## The length of the connector is carriage_length/20
        ## The width of the connector is carriage_width/6
        self.myturtle.down()
        self.myturtle.begin_fill()
        self.myturtle.setheading(90)
        self.myturtle.forward(carriage_width)
        self.myturtle.right(90)
        self.myturtle.forward(carriage_length)
        self.myturtle.right(90)
        self.myturtle.forward(carriage_width*5/12)
        self.myturtle.left(90)
        self.myturtle.forward(carriage_length/20)
        self.myturtle.right(90)
        self.myturtle.forward(carriage_width/6)
        self.myturtle.right(90)
        self.myturtle.forward(carriage_length/20)
        self.myturtle.left(90)
        self.myturtle.backward(carriage_width*1/6)
        self.myturtle.forward(carriage_width*1/6)
        self.myturtle.forward(carriage_width*5/12)
        self.myturtle.right(90)
        self.myturtle.forward(carriage_length)
        self.myturtle.right(90)
        self.myturtle.end_fill()
        self.myturtle.up()
        
        ## Plot the tyre
        (x_cur,y_cur) = self.myturtle.pos()
        radius_outer = carriage_length/8
        radius_inner = carriage_length/16
        self.tyre(width, color, x_cur + carriage_length/4, y_cur, radius_inner, radius_outer)
        self.tyre(width, color, x_cur + carriage_length*3/4, y_cur, radius_inner, radius_outer)
        
        self.rest()
        
    def track(self, width, color, start_x, start_y, track_length):
        self.myturtle.up()
        self.myturtle.width(width)
        self.myturtle.color(color)
        self.myturtle.goto(start_x,start_y)
        self.myturtle.setheading(0)
        self.myturtle.down()
        self.myturtle.forward(track_length)
        self.rest()
        
    def locamotive(self, width, color, start_x, start_y, loca_width, loca_length):
        self.myturtle.goto( start_x, start_y)
        self.myturtle.width(width)
        self.myturtle.color(color)
        self.myturtle.down()
        self.myturtle.setheading(90)
        self.myturtle.begin_fill()
        self.myturtle.forward(loca_width)
        self.myturtle.right(90)
        self.myturtle.forward(loca_length*3/4)
        ## Draw a chimney
        self.myturtle.left(90)
        self.myturtle.forward(loca_width/10)
        self.myturtle.right(90)
        self.myturtle.forward(loca_length/8)
        self.myturtle.right(90)
        self.myturtle.forward(loca_width/10)
        self.myturtle.left(90)
        self.myturtle.backward(loca_length/8)
        self.myturtle.forward(loca_length/4)
        self.myturtle.right(90)
        self.myturtle.forward(loca_width)
        self.myturtle.right(90)
        self.myturtle.forward(loca_length)
        self.myturtle.right(90)
        self.myturtle.end_fill()
        self.myturtle.up()

        ## Plot the tyre
        (x_cur,y_cur) = self.myturtle.pos()
        radius_outer = loca_length/8*2/3
        radius_inner = loca_length/16*2/3
        self.tyre(width, 'red', x_cur + loca_length/4, y_cur, radius_inner, radius_outer)
        self.tyre(width, 'red', x_cur + loca_length*3/4, y_cur, radius_inner, radius_outer)
        
        ## Plot the window
        self.window(width,'white',x_cur + loca_length*1/2, y_cur+loca_width/2, loca_width/4, True)
        self.window(width,'white',x_cur + loca_length*3/4, y_cur+loca_width/2, loca_width/4, True)
        
        self.rest()
        
    def window(self, width, color, start_x, start_y, window_width, fill):
        self.myturtle.up()
        self.myturtle.setheading(90)
        self.myturtle.width(width)
        self.myturtle.color(color)
        self.myturtle.goto(start_x, start_y)
        self.myturtle.down()
        if fill == True:
            self.myturtle.begin_fill()
        for i in range(4):
            self.myturtle.forward(window_width)
            self.myturtle.right(90)
        if fill==True:
            self.myturtle.end_fill()
        self.myturtle.up()
        

    def tyre(self, width, color, center_x, center_y, radius_inner, radius_outer):
        self.myturtle.setheading(90)
        self.myturtle.color(color)
        self.myturtle.width(width)
        self.myturtle.up()
        self.myturtle.goto(center_x,center_y) ## Go to the center of the tyre
        self.myturtle.up()
        self.myturtle.color('black')
        self.myturtle.goto( center_x+radius_outer, center_y)
        self.myturtle.down()
        self.myturtle.begin_fill()
        self.myturtle.circle(radius_outer)
        self.myturtle.end_fill()
        ## Inner circle
        self.myturtle.up()
        self.myturtle.goto(center_x+radius_inner, center_y)
        self.myturtle.down()
        self.myturtle.color('grey')
        self.myturtle.begin_fill()
        self.myturtle.circle(radius_inner)
        self.myturtle.end_fill()
        
        self.myturtle.color(color)


    def rest(self):
        self.myturtle.up()
        self.myturtle.goto(-600,300)
        self.myturtle.setheading(90)

    def final_rest(self, pos_x,pos_y):
        self.myturtle.up()
        self.myturtle.goto(pos_x,pos_y)
        self.myturtle.setheading(90)
    

def main():
    carriage_width=90
    carriage_length=180
    start_x=-700
    start_y=-300
    turtlescreen = turtle.getscreen()
    myturtle = turtle.Turtle()
    myturtle.shape('turtle')
    myturtle.shapesize(2)
    myturtle.width(5)    
    myplot = turtle_draw_shape(myturtle)
    
    ## Plot the background 
    myplot.plot_fillable_rec('chartreuse4',-1000, -500, 400, 2000)
    myplot.plot_fillable_rec('DeepSkyBlue',-1000, -100, 600, 2000)

    mytrain = train(myturtle)
    ## Plot the track
    mytrain.track(5,'black',start_x-50, start_y - carriage_length/8, carriage_length* 8)
    
    ## Plot the carriages
    colors=("purple","blue","green","yellow","orange")
    for i in range(5):
        mytrain.carriage(5,colors[i],start_x+carriage_length*21/20*i,start_y,carriage_width,carriage_length)
    
    ## Plot the locamotives
    mytrain.locamotive(5, 'red', start_x + 5*carriage_length*21/20, start_y, carriage_width*1.5, carriage_length*1.5)
    
    ## Plot the smoke
    for i in range(10):
        myplot.plot_oval( 2,'grey', start_x + (6.1)*carriage_length*21/20 - carriage_length/5*i*i/3 ,start_y +carriage_width*1.5*1.2 + carriage_width/4*i, (i+1)*carriage_width*1.5/25, (i+1)*carriage_width*1.5/25/2, 0, True)    
    myplot.rest()
    
    ## plot the sun
    myplot.plot_sun(4,'red',start_x + 7.5*carriage_length*21/20, 325, 50)
    
    mytrain.final_rest(-600,500)
    
    turtlescreen.getcanvas().postscript(file="train.eps")

if __name__=="__main__":
    main()
