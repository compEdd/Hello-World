# Projeto baseado no turtle race da RaspberryPiProjects
# https://projects.raspberrypi.org/en/projects/turtle-race##
# Modificado por Ed Canto

from turtle import *
#from turtle import ScrolledCanvas, RawTurtle, TurtleScreen
from random import randint

#screen = TurtleScreen()
#screen = Screen()
setup(600, 600)
screensize(200, 500)
title('Welcome to the Final World Turtle Race')
color('white', 'white')
bgcolor('black')

penup()
goto(-200, 200)
#pendown()
speed(5)

for step in range(21):
	write(step, align='center')
	right(90)
	forward(10)
	pendown()
	forward(180)
	penup()
	backward(190)
	left(90)
	forward(20)

#speed(15)
penup()
goto(-200, 0)

ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-200, 170)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-200, 140)
bob.pendown()

fran = Turtle()
fran.color('green')
fran.shape('turtle')

fran.penup()
fran.goto(-200, 110)
fran.pendown()

eve = Turtle()
eve.color('violet')
eve.shape('turtle')

eve.penup()
eve.goto(-200, 80)
eve.pendown()

zen = Turtle()
zen.color('white')
zen.shape('turtle')

zen.penup()
zen.goto(-200, 50)
zen.pendown()

zig = Turtle()
zig.color('yellow')
zig.shape('turtle')

zig.penup()
zig.goto(-200, 20)
zig.pendown()

ada.speed(randint(10,15))
bob.speed(randint(10,15))
fran.speed(randint(10,15))
eve.speed(randint(10,15))
zen.speed(randint(10,15))
zig.speed(randint(10,15))


for turn in range(140):
	ada.forward(randint(1,5))
	bob.forward(randint(1,5))
	fran.forward(randint(1,5))
	eve.forward(randint(1,5))
	zen.forward(randint(1,5))
	zig.forward(randint(1,5))


ada.reset()
bob.reset()
fran.reset()
eve.reset()
zen.reset()
zig.reset()

ada.setpos(-200, 170)
bob.setpos(-200, 140)
fran.setpos(-200, 110)
eve.setpos(-200, 80)
zen.setpos(-200, 50)
zig.setpos(-200, 20)

ada.shape('square')
ada.color('white')
ada.penup()
ada.goto(-200, 170)
ada.pendown()

bob.shape('square')
bob.color('violet')
bob.penup()
bob.goto(-200, 140)
bob.pendown()

fran.shape('square')
fran.color('yellow')
fran.penup()
fran.goto(-200, 110)
fran.pendown()

eve.shape('square')
eve.color('red')
eve.penup()
eve.goto(-200, 80)
eve.pendown()

zen.shape('square')
zen.color('blue')
zen.penup()
zen.goto(-200, 50)
zen.pendown()

zig.shape('square')
zig.color('green')
zig.penup()
zig.goto(-200, 20)
zig.pendown()

for turn in range(140):
	ada.forward(randint(1,5))
	bob.forward(randint(1,5))
	fran.forward(randint(1,5))
	eve.forward(randint(1,5))
	zen.forward(randint(1,5))
	zig.forward(randint(1,5))
