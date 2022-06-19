from graphics import * 
from classes import *
from maças import *
def implementação1():
    win = GraphWin("Projeto Ai implementação1", 600, 600)
    win.setCoords(0, 0, 600, 600)
    win.setBackground("chartreuse3")

    
    a = Point (300, 300)
    arvore = Arvore(win,a,30)


    pontoderecolha1 = Point(0,570)
    pontoderecolha2 = Point(30,600)
    pontoderecolha3 = Point(570,300)
    pontoderecolha4 = Point(600,330)
    pontoderecolha = Recolha(pontoderecolha1,pontoderecolha2,pontoderecolha3,pontoderecolha4,win)
    body = Robot(win,10,10)
    grouparvores = [arvore.centre]
    grouppedras = []
    quitcounter, maçasgroup, maçasgroupcentre = multiplemaças(win,grouparvores,grouppedras)
    while  quitcounter == 0:
        for l in maçasgroupcentre:
            counter = 0
            for i in range(2):
                update(1)
            while counter == 0:
                update(50)
                body.moveobjetive(l)
                objective = l
                body.dodgeeverything(grouparvores,grouppedras,objective)
                if body.centre.getY() == l.getY() and body.centre.getX() == l.getX():
                    counter = 1
                    for p in maçasgroup:
                        if body.centre.getY() == p.centro.getY() and body.centre.getX() == p.centro.getX():
                            p.existnt()
                    for i in range(2):
                        update(1)
                body.mover(body.x,body.y)
        while counter == 1:
            update(50)
            distrecolha1 = (pontoderecolha.box1centro.getX()-body.centre.getX())**2 + (pontoderecolha.box1centro.getY()-body.centre.getY())**2
            distrecolha2 = (pontoderecolha.box2centro.getX()-body.centre.getX())**2 + (pontoderecolha.box2centro.getY()-body.centre.getY())**2
            if distrecolha1 <= distrecolha2:
                body.moveobjetive(pontoderecolha.box1centro)
                objective = pontoderecolha.box1centro
                body.dodgeeverything(grouparvores,grouppedras,objective) 
                if body.centre.getY() == pontoderecolha.box1centro.getY() and body.centre.getX() == pontoderecolha.box1centro.getX():
                    quitcounter, maçasgroup, maçasgroupcentre = multiplemaças(win,grouparvores,grouppedras)
                    counter = 0
            if distrecolha1 > distrecolha2:
                body.moveobjetive(pontoderecolha.box2centro)
                objective = pontoderecolha.box2centro
                body.dodgeeverything(grouparvores,grouppedras,objective)
                if body.centre.getY() == pontoderecolha.box2centro.getY() and body.centre.getX() == pontoderecolha.box2centro.getX():
                    quitcounter, maçasgroup, maçasgroupcentre = multiplemaças(win,grouparvores,grouppedras)
                    counter = 0
            body.mover(body.x,body.y)
    win.close()