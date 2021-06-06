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
def draw(rad):
  for i in range(2):
    # two arcs
    turtle.circle(rad,90)
    turtle.circle(rad//2,90)
  



import turtle

width=5

olivia = turtle.Turtle()
olivia = turtle.Turtle()

olivia.shape('turtle')
olivia.shapesize(5)
olivia.color('red')
olivia.width(width)

andrew = turtle.Turtle()
andrew.shape('turtle')
andrew.shapesize(5)
andrew.width(width)
andrew.color('yellow')

irene = turtle.Turtle()
irene.shape('turtle')
irene.shapesize(5)
irene.width(width)
irene.color('blue')


## Getting to the starting point
olivia.up()
olivia.goto(-600,-200)
olivia.down()

## Draw two wheels
olivia.forward(200)
olivia.right(90)
olivia.circle(75,540)
olivia.right(90)
olivia.forward(400)
olivia.right(90)
olivia.circle(75,540)

## Draw the two circles in side the wheel
## Getting to the starting point
andrew.up()
andrew.goto(-400,-200)
andrew.down()
andrew.up()
andrew.forward(50)
andrew.right(90)
andrew.down()
andrew.circle(25)
andrew.left(90)
andrew.up()
andrew.forward(550)
andrew.down()
andrew.right(90)
andrew.circle(25)
andrew.left(90)
andrew.up()
andrew.forward(100)

    
olivia.right(90)
olivia.forward(300)
olivia.left(120)
olivia.forward(400)

## Draw the front    
olivia.right(-60)
olivia.forward(200)
olivia.right(30)
olivia.forward(50)

## plot a ladder
olivia.forward(450)
olivia.backward(450)
olivia.right(-30)
olivia.forward(150)
olivia.right(30)
olivia.forward(450)
olivia.backward(450)

## plot ladder steps
for i in range(9):
    olivia.forward(50)
    olivia.right(150)
    olivia.forward(150)
    olivia.backward(150)
    olivia.right(-150)

olivia.backward(450)

## plot the top
olivia.right(-30)
olivia.forward(150)
olivia.right(-30)
olivia.forward(50)
olivia.right(30)
olivia.backward(400)
olivia.forward(400)
olivia.forward(220)
olivia.right(-60)
olivia.forward(400)
olivia.right(-120)
olivia.forward(200)
olivia.up()

olivia.right(-90)
olivia.forward(300)

olivia.up()

irene.up()
irene.goto( -400,100 )
irene.left(90)
irene.down()

for i in range(4):
    irene.right(90)
    irene.forward(100)
    
irene.right(90)
irene.up()
irene.forward(300)
irene.down()

for i in range(4):
    irene.right(90)
    irene.forward(100)


irene.up()  
irene.forward(200)
irene.down()
for i in range(4):
    irene.right(90)
    irene.forward(100)
irene.up()


irene.up()
irene.forward(200)
irene.down()
for i in range(4):
    irene.right(90)
    irene.forward(100)
irene.up()

olivia.goto(-750,300)
irene.goto(-650,300)    
irene.left(90)
andrew.goto(-550, 300)
andrew.left(90)
    
