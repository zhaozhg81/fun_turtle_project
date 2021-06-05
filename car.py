#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 19:17:45 2021

@author: zhaozhg
"""


import turtle


t = turtle.Turtle()
t.shape('turtle')
t.shapesize(5)
t.color('red')

t.up()
t.goto(-600,-200)
t.down()

t.forward(200)
t.right(90)
t.circle(75,540)
t.right(90)
t.forward(400)
t.right(90)
t.circle(75,540)

t.right(90)
t.forward(300)
t.right(-120)
t.forward(400)

t.right(-60)
t.forward(200)
t.right(30)
t.forward(50)
t.right(-30)
t.forward(300)
t.right(-30)
t.forward(50)
t.right(30)
t.backward(400)
t.forward(400)
t.forward(220)
t.right(-60)
t.forward(400)
t.right(-120)
t.forward(200)
t.up()

t.right(-90)
t.forward(300)

t.down()
for i in range(4):
    t.right(90)
    t.forward(100)
    
t.right(90)
t.up()
t.forward(300)
t.down()
for i in range(4):
    t.right(90)
    t.forward(100)


t.up()
t.forward(200)
t.down()
for i in range(4):
    t.right(90)
    t.forward(100)
t.up()


t.up()
t.forward(200)
t.down()
for i in range(4):
    t.right(90)
    t.forward(100)
t.up()

t.goto(1000,1000)