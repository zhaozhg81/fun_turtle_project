#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 16:22:33 2021

@author: zhaozhg
"""
##
##
## In this class, we introduce the concept of "variable" and use variable in the code.
##
##

import turtle

turtlescreen = turtle.getscreen()

irene = turtle.Turtle()
irene.shape('turtle')

width = 400
height = 300
color='blue'

irene.color(color)
irene.up()
irene.goto(0,0)
irene.left(270)
irene.forward(width/2)
irene.down()
irene.left(90)
irene.forward(width/2)
irene.left(90)
irene.forward(height)
irene.left(90)
irene.forward(width)
irene.left(90)
irene.forward(height)
irene.left(90)
irene.forward(width/2)
irene.up()
irene.backward(width/2)
irene.right(90)
irene.down()
irene.circle(width/2,180)
irene.right(90)
irene.circle(height/2,180)
irene.right(90)
irene.circle(width/2,180)
irene.right(90)
irene.circle(height/2,180)

