#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 17:53:34 2021

@author: zhaozhg
"""

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
        self.myturtle.up()
        
        ## Plot the tyre
        (x_cur,y_cur) = self.myturtle.pos()
        radius_outer = carriage_length/8
        radius_inner = carriage_length/16
        self.tyre(width, color, x_cur + carriage_length/4, y_cur, radius_inner, radius_outer)
        self.tyre(width, color, x_cur + carriage_length*3/4, y_cur, radius_inner, radius_outer)
        
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
        
        self.myturtle.forward(loca_width)
        self.myturtle.right(90)
        self.myturtle.forward(loca_length*3/4)
        ## Draw a chimney
        self.myturtle.left(90)
        self.myturtle.forward(loca_width/20)
        self.myturtle.right(90)
        self.myturtle.forward(loca_length/8)
        self.myturtle.right(90)
        self.myturtle.forward(loca_width/20)
        self.myturtle.left(90)
        self.myturtle.backward(loca_length/8)
        self.myturtle.forward(loca_length/4)
        self.myturtle.right(90)
        self.myturtle.forward(loca_width)
        self.myturtle.right(90)
        self.myturtle.forward(loca_length)
        self.myturtle.right(90)
        self.myturtle.up()

        ## Plot the tyre
        (x_cur,y_cur) = self.myturtle.pos()
        radius_outer = loca_length/8*2/3
        radius_inner = loca_length/16*2/3
        self.tyre(width, 'red', x_cur + loca_length/4, y_cur, radius_inner, radius_outer)
        self.tyre(width, 'red', x_cur + loca_length*3/4, y_cur, radius_inner, radius_outer)
        
        ## Plot the window
        self.window(width,'orange',x_cur + loca_length*1/2, y_cur+loca_width/2, loca_width/4)
        self.window(width,'orange',x_cur + loca_length*3/4, y_cur+loca_width/2, loca_width/4)
        
    def window(self, width, color, start_x, start_y, window_width):
        self.myturtle.up()
        self.myturtle.setheading(90)
        self.myturtle.width(width)
        self.myturtle.color(color)
        self.myturtle.goto(start_x, start_y)
        self.myturtle.down()
        for i in range(4):
            self.myturtle.forward(window_width)
            self.myturtle.right(90)
        self.myturtle.up()
        self.rest()
        

    def tyre(self, width, color, center_x, center_y, radius_inner, radius_outer):
        self.myturtle.setheading(90)
        self.myturtle.color(color)
        self.myturtle.width(width)
        self.myturtle.up()
        self.myturtle.goto(center_x,center_y) ## Go to the center of the tyre
        self.myturtle.up()
        self.myturtle.color(color)
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
        self.rest()


    def rest(self):
        self.myturtle.up()
        self.myturtle.goto(-600,300)
        self.myturtle.setheading(90)
    


def main():
    carriage_width=100
    carriage_length=200
    start_x=-600
    start_y=-200
    myturtle = turtle.getscreen()
    myturtle = turtle.Turtle()
    myturtle.shape('turtle')
    myturtle.width(5)
    mytrain = train(myturtle)
    mytrain.track(5,'black',start_x-50, start_y - carriage_length/8, carriage_length*6 )
    colors=("blue","green","yellow","black")
    for i in range(4):
        mytrain.carriage(5,colors[i],start_x+carriage_length*21/20*i,start_y,carriage_width,carriage_length)
    
    mytrain.locamotive(5, 'red', start_x + 4*carriage_length*21/20, start_y, carriage_width*1.5, carriage_length*1.5)

    
if __name__=="__main__":
    main()
