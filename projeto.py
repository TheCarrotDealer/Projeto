from graphics import * 
from classes import *

def implementação1():

    win = GraphWin("Projeto Ai implementação1", 600, 600)
    win.setCoords(0, 0, 600, 600)
    win.setBackground("green")
    body = Robot(win,10,10)
    pontoderecolha1 = Point(0,570)
    pontoderecolha2 = Point(30,600)
    pontoderecolha3 = Point(570,300)
    pontoderecolha4 = Point(600,330)
    pontoderecolha = Recolha(pontoderecolha1,pontoderecolha2,pontoderecolha3,pontoderecolha4,win)
    x=1 
    y=1
    counter = 0
    pontoobs = Point(270,270)
    pontoobs1 = Point(330,330)
    obst = Obstaculo(pontoobs,pontoobs1,win)
    macacentro = win.getMouse()
    maca = Maça(win,macacentro)
    while counter == 0:
        update(30)
        if body.centre.getX() > (obst.obscentro.getX()-40) and body.centre.getY() > (obst.obscentro.getY()-40) and body.centre.getX() < (obst.obscentro.getX()+40) and body.centre.getY() < (obst.obscentro.getY()+40) :
            body.movimentoobst(obst.obscentro,maca.centro)    
        if body.centre.getX() == maca.centro.getX():
            x=0
        if body.centre.getX() == maca.centro.getX() and body.centre.getY() > maca.centro.getY():
            x=0
            y=-1
        if body.centre.getY() == maca.centro.getY():
            y=0
        if body.centre.getY() == maca.centro.getY() and body.centre.getX() > maca.centro.getX():
            y=0
            x=-1
        if body.centre.getY() == maca.centro.getY() and body.centre.getX() == maca.centro.getX():
            counter = 1
            maca.existnt()
        
        body.mover(x,y)
    while counter == 1:
        update(30)
        distrecolha1 = (pontoderecolha.box1centro.getX()-body.centre.getX())**2 + (pontoderecolha.box1centro.getY()-body.centre.getY())**2
        distrecolha2 = (pontoderecolha.box2centro.getX()-body.centre.getX())**2 + (pontoderecolha.box2centro.getY()-body.centre.getY())**2
        if distrecolha1 <= distrecolha2:
            if body.centre.getX() > (obst.obscentro.getX()-40) and body.centre.getY() > (obst.obscentro.getY()-40) and body.centre.getX() < (obst.obscentro.getX()+40) and body.centre.getY() < (obst.obscentro.getY()+40) :
                body.movimentoobst(obst.obscentro,pontoderecolha.box1centro)
            x=-1
            y=1
            if body.centre.getX() == pontoderecolha.box1centro.getX():
                x=0
            if body.centre.getX() == pontoderecolha.box1centro.getX() and body.centre.getY() > pontoderecolha.box1centro.getY():
                x=0
                y=-1
            if body.centre.getY() == pontoderecolha.box1centro.getY():
                y=0
            if body.centre.getY() == pontoderecolha.box1centro.getY() and body.centre.getX() < pontoderecolha.box1centro.getX():
                y=0
                x=-x
            if body.centre.getY() == pontoderecolha.box1centro.getY() and body.centre.getX() == pontoderecolha.box1centro.getX():
                print("homens")
                
        
        if distrecolha1 > distrecolha2:
            if body.centre.getX() > (obst.obscentro.getX()-40) and body.centre.getY() > (obst.obscentro.getY()-40) and body.centre.getX() < (obst.obscentro.getX()+40) and body.centre.getY() < (obst.obscentro.getY()+40) :
                body.movimentoobst(obst.obscentro,pontoderecolha.box2centro)
            x=1
            y=1
            if body.centre.getY() > pontoderecolha.box2centro.getY():
                y=-1
            if body.centre.getX() == pontoderecolha.box2centro.getX():
                x=0
            if body.centre.getX() == pontoderecolha.box2centro.getX() and body.centre.getY() > pontoderecolha.box2centro.getY():
                x=0
                y=-1
            if body.centre.getY() == pontoderecolha.box2centro.getY():
                y=0
            if body.centre.getY() == pontoderecolha.box2centro.getY() and body.centre.getX() > pontoderecolha.box2centro.getX():
                y=0
                x=-1
            if body.centre.getY() == pontoderecolha.box2centro.getY() and body.centre.getX() == pontoderecolha.box2centro.getX():
                print("homens")
              

        body.mover(x,y)
def implementação2():
    pass
def implementação3():
    pass
def implementação4():
    pass
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
    click = win1.getMouse()
    while True:
        if implementacao1.clicked(click):
            implementação1()
        if implementacao2.clicked(click):
            implementação2()
        if implementacao3.clicked(click):
            implementação3()
        if implementacao4.clicked(click):
            implementação4()
menu()