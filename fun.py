#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 12:32:24 2021

@author: zhaozhg
"""

import turtle
import math


andrew = turtle.Turtle()
irene = turtle.Turtle()

andrew.shape("turtle")
irene.shape("turtle")

andrew.shapesize(5)
irene.shapesize(5)

andrew.color('orange')
irene.color('blue')
andrew.forward(400)
irene.circle(10)
for i in range(6):
    andrew.circle(10*i)
    irene.circle(10*i)
    irene.right(90)
irene.forward(300)
irene.right(90)
irene.forward(200)
andrew.right(90)
andrew.forward(200)
andrew.circle(25)
for i in range(3):
    irene.circle(20*i)

irene.goto(100,100)
irene.goto(200,100)
irene.goto(200,300)
irene.goto(400,300)
irene.goto(400,500)
irene.goto(400,400)
irene.goto(600,400)
irene.goto(800,400)
irene.goto(800,450)
irene.goto(400,400)
irene.goto(100,100)