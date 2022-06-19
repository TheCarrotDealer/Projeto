from graphics import * 
from classes import *
from maças import *
def implementação2():
        win2 = GraphWin("Projeto Ai implementação2", 600, 600)
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

        a = Point (300, 300)
        b = Point (450, 450)
        c = Point (150, 150)
        pontopedra1 = Point(120,420)
        pontopedra2 = Point(420,120)
        pontopedra12 = Point(180,480)
        pontopedra22 = Point(480,180)
        pedra1 = Obstaculo(pontopedra1,pontopedra12,win2)
        pedra2 = Obstaculo(pontopedra2,pontopedra22,win2)
        arvore2 = Arvore(win2,c,30)
        arvore3 = Arvore(win2,b,30)
        arvore = Arvore(win2,a,30)
        grouppedras = []
        grouparvores = []
        for i in [arvore.centre,arvore2.centre,arvore3.centre]:
            grouparvores.append(i)
        for i in [pedra1.obscentro,pedra2.obscentro]:
            grouppedras.append(i)


        
        body = Robot(win2,10,10)
        
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