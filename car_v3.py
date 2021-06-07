#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 09:14:37 2021

@author: zhaozhg
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 19:17:45 2021

@author: zhaozhg
"""


import turtle


class car:

    width=5

    def __init__(self, turtlename):
        self.myturtle=turtlename
        self.myturtle.up()
        
    def frame(self, width, color):
        self.myturtle.shape('turtle')
        self.myturtle.shapesize(5)
        self.myturtle.color(color)
        self.myturtle.width(width)
        ## Getting to the starting point
        self.myturtle.up()
        self.myturtle.goto(-600,-200)
        self.myturtle.down()
        ## Draw two bottom
        self.myturtle.forward(200)
        self.myturtle.up()
        self.myturtle.forward(150)
        self.myturtle.down()
        self.myturtle.forward(400)
        self.myturtle.up()
        self.myturtle.forward(150)
        self.myturtle.down()
        self.myturtle.forward(300)
        
        ## Draw the front
        self.myturtle.left(120)
        self.myturtle.forward(400)
        self.myturtle.left(60)
        self.myturtle.forward(200)
        self.myturtle.right(30)
        self.myturtle.forward(50)
        self.myturtle.right(-30)
        self.myturtle.forward(300)
        self.myturtle.right(-30)
        
        ## Draw the top
        self.myturtle.forward(50)
        self.myturtle.right(30)
        self.myturtle.backward(400)
        self.myturtle.forward(400)
        self.myturtle.forward(220)
        self.myturtle.right(-60)
        self.myturtle.forward(400)
        self.myturtle.right(-120)
        self.myturtle.forward(200)
        self.myturtle.up()
        
        self.myturtle.right(-90)
        self.myturtle.forward(300)
        
        self.myturtle.up()
        self.rest()
        
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
        self.rest()
        
    def window(self, width, color, start_x, start_y, length):
        self.myturtle.setheading(90)
        self.myturtle.shapesize(width)
        self.myturtle.color(color)
        self.myturtle.goto(start_x,start_y)
        self.myturtle.down()
        for i in range(4):
            self.myturtle.right(90)
            self.myturtle.forward(length)
        self.rest()
        
    def ladder(self, width, color, start_x, start_y, ladder_length, ladder_width, angle, number_steps):
        self.myturtle.setheading(180)
        self.myturtle.shapesize(width)
        self.myturtle.color(color)
        self.myturtle.goto(start_x, start_y)
        self.myturtle.down()
        self.myturtle.right(angle)
        self.myturtle.forward(ladder_length)
        self.myturtle.backward(ladder_length)
        self.myturtle.left(angle)
        self.myturtle.forward(ladder_width)
        self.myturtle.right(angle)
        self.myturtle.forward(ladder_length)
        self.myturtle.backward(ladder_length)
        for i in range(number_steps):
            self.myturtle.forward( ladder_length/number_steps)
            self.myturtle.left(angle)
            self.myturtle.backward(ladder_width)
            self.myturtle.forward(ladder_width)
            self.myturtle.right(angle)            
        self.rest()
        
    def rest(self):
        self.myturtle.up()
        self.myturtle.goto(-600,300)
        self.myturtle.setheading(90)
            
    def final_rest(self, pos_x,pos_y):
        self.myturtle.up()
        self.myturtle.goto(pos_x,pos_y)
        self.myturtle.setheading(90)
        

def main():
    myturtle = turtle.getscreen()
    myturtle = turtle.Turtle()
    myturtle.shapesize(2)
    mycar = car(myturtle)
    mycar.frame(5,'red')
    mycar.tyre(5,'grey',-325,-200,25,75)
    mycar.tyre(5,'grey',225,-200,25,75)
    for i in range(4):
        mycar.window(5, 'blue', -400+i*200, 100, 100)
        
    mycar.ladder(5,'black',150, 170, 450, 150, 20, 9 )
    
    mycar.final_rest(1000,1000)
    
if __name__=="__main__":
    main()
