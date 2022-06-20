from graphics import * 
from classes import *
win1 = GraphWin("Projeto Ai Menu", 600, 600)
win1.setCoords(0, 0, 600, 600)

oval = Oval(Point(30,60),Point(50,30))

circle = Circle(Point(30,30),10)
circle.draw(win1)

body= Robot(win1,10,10)
while True:
    update(30)
    
    body.mover(1,1)
    if ((body.centre.getX()-30)**2)/20 + ((body.centre.getY()-30)**2)/20 < 1:
        print("homens")
