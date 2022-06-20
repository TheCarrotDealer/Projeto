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
   
    quitbutton = butão(win1,Point(250,500),Point(350,550),"quit")
    implementacao1 = butão(win1,Point(30,30),Point(170,70),"implementação 1")
    implementacao2 = butão(win1,Point( 200,30),Point(350,70),"implementação 2")
    implementacao3 = butão(win1,Point( 380,30),Point(520,70),"implementação 3")
    implementacao4 = butão(win1,Point( 230,130),Point(370,170),"implementação 4")
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