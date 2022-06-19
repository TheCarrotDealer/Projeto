from graphics import * 
from classes import *
from maças import *
def implementação4():
        win2 = GraphWin("Projeto Ai implementação4", 600, 600)
        win2.setCoords(0, 0, 600, 600)
        win2.setBackground("chartreuse3")
        bateriaponto1 = Point(570,570)
        bateriaponto2 = Point(600,600)
        bateria = baterystation(bateriaponto1,bateriaponto2,win2)
        pontoderecolha1 = Point(0,570)
        pontoderecolha2 = Point(30,600)
        pontoderecolha3 = Point(570,300)
        pontoderecolha4 = Point(600,330)
        pontoderecolha = Recolha(pontoderecolha1,pontoderecolha2,pontoderecolha3,pontoderecolha4,win2)
        counter = 0


        body = Robot(win2,10,10)
        file = open("fileprojeto.txt","r")
        body.file(file)
        for i in body.obstgrouppedras:
            thex = i.getX() -30
            they = i.getY() -30
            the1x = i.getX() +30
            the1y = i.getY() +30
            i = Obstaculo(Point(thex,they),Point(the1x,the1y),win2)
        for a in body.obstgrouparvores:
            a = Arvore(win2,a,30)

        
        grouparvores = body.obstgrouparvores 
        grouppedras = body.obstgrouppedras
        quitcounter, maçasgroup, maçasgroupcentre = multiplemaças(win2,grouparvores,grouppedras)
        while  quitcounter == 0:
            for l in maçasgroupcentre:
                counter = 0
                for i in range(2):
                    update(1)
                while counter == 0:
                    update(50)
                    body.moveobjetive(l)
                    body.countbatery(bateria.centro)
                    objective = l
                    if body.bateryactive == 1:
                        objective = bateria.centro
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
                    body.countbatery(bateria.centro)
                    objective = pontoderecolha.box1centro
                    if body.bateryactive == 1:
                        objective = bateria.centro
                    body.dodgeeverything(grouparvores,grouppedras,objective) 
                    if body.centre.getY() == pontoderecolha.box1centro.getY() and body.centre.getX() == pontoderecolha.box1centro.getX():
                        quitcounter, maçasgroup, maçasgroupcentre = multiplemaças(win2,grouparvores,grouppedras)
                        counter = 0
                if distrecolha1 > distrecolha2:
                    body.moveobjetive(pontoderecolha.box2centro)
                    body.countbatery(bateria.centro)
                    objective = pontoderecolha.box2centro
                    if body.bateryactive == 1:
                        objective = bateria.centro
                    body.dodgeeverything(grouparvores,grouppedras,objective)
                    if body.centre.getY() == pontoderecolha.box2centro.getY() and body.centre.getX() == pontoderecolha.box2centro.getX():
                        quitcounter, maçasgroup, maçasgroupcentre = multiplemaças(win2,grouparvores,grouppedras)
                        counter = 0
                body.mover(body.x,body.y)
        win2.close()