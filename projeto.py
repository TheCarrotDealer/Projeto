from graphics import * 
from classes import *
from outrasclasses import *
from implementacao1 import *
from implementacao2 import *
from implementacao3 import *
from implementacao4 import *
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
    point9 = Point(250,500)
    point10 = Point(350,550)
    quitbutton = butão(win1,point9,point10,"quit")
    implementacao1 = butão(win1,point1,point2,"implementação 1")
    implementacao2 = butão(win1,point3,point4,"implementação 2")
    implementacao3 = butão(win1,point5,point6,"implementação 3")
    implementacao4 = butão(win1,point7,point8,"implementação 4")
    while True:
        click = win1.getMouse()
        if implementacao1.clicked(click):
            win1.close()
            implementação1()
            menu()
        if implementacao2.clicked(click):
            win1.close()
            implementação2()
            menu()
        if implementacao3.clicked(click):
            win1.close()
            implementação3()
            menu()
        if implementacao4.clicked(click):
            win1.close()
            implementação4()
            menu()
        if quitbutton.clicked(click):
            win1.close()
            break
menu()