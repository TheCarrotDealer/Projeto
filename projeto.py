from graphics import * 
from classes import *
from random import *
from outrasclasses import *
from implementacao1 import *
from implementacao2 import *
from implementacao3 import *
from implementacao4 import *
def menu():
    win1 = GraphWin("Projeto Ai Menu", 1000, 550)
    win1.setCoords(0, 0, 1000, 550)

    menubackround = Image(Point(500,275),"menubackround.png")
    menubackround.draw(win1)
    title = Image(Point(200,500),"title.png")
    title.draw(win1)

    buttoneasteregg = butão(win1,Point(230,480),Point(250,505)," ")
    red = Rectangle(Point(230,480),Point(250,505))
    red.setOutline("red")
    red.setFill("red")
    red.draw(win1)
   
    quitbutton = butão(win1,Point(870,30),Point(970,70),"Quit")
    implementacao1 = butão(win1,Point(830,475),Point(970,525),"Implementação 1")
    implementacao2 = butão(win1,Point( 830,400),Point(970,450),"Implementação 2")
    implementacao3 = butão(win1,Point( 830,325),Point(970,375),"Implementação 3")
    implementacao4 = butão(win1,Point( 830,250),Point(970,300),"Implementação 4")
    while True:
        click = win1.getMouse()
        if buttoneasteregg.clicked(click):
            a= Text(Point(randrange(10,990),randrange(540)),"apple")
            a.draw(win1)
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
            break
    win1.close()
menu()