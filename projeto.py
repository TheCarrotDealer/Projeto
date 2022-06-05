from graphics import * 
from classes import *

def main():

    win = GraphWin("Projeto Ai apanhar maças", 600, 600)
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
        if body.centre.getX() > (obst.obscentro.getX()-40) and body.centre.getY() > (obst.obscentro.getY()-40) and body.centre.getX() < (obst.obscentro.getX()+40) and body.centre.getY() < (obst.obscentro.getY()+40) :
            pass
                
            
        update(30)
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
main()
