from graphics import * 
from classes import *
from implementação1 import *
from implementação2 import *
from implementação3 import *
from implementação4 import *
def menu():
    win1 = GraphWin("Projeto Ai Menu", 600, 600)
    win1.setCoords(0, 0, 600, 600)
    point1 = Point(30,30)
    point2 = Point(170,70)
    point3 = Point( 200,30)
    point4 = Point(350,70)
    point5 = Point( 380,30)
    point6 = Point(520,70)
    point7 = Point( 230,130)
    point8 = Point(370,170)
    implementacao1 = butão(win1,point1,point2,"implementação 1")
    implementacao2 = butão(win1,point3,point4,"implementação 2")
    implementacao3 = butão(win1,point5,point6,"implementação 3")
    implementacao4 = butão(win1,point7,point8,"implementação 4")
    while True:
        click = win1.getMouse()
        if implementacao1.clicked(click):
            implementação1()
        if implementacao2.clicked(click):
            implementação2()
        if implementacao3.clicked(click):
            implementação3()
        if implementacao4.clicked(click):
            implementação4()
menu()