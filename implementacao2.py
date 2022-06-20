from graphics import * 
from classes import *
from macas import *
from outrasclasses import *
def implementação2():
        win2 = GraphWin("Projeto Ai implementação2", 600, 600)
        win2.setCoords(0, 0, 600, 600)
        bateria, pontoderecolha = baseline(win2)
        pontopedra1 = Point(120,420)
        pontopedra2 = Point(420,120)
        pontopedra12 = Point(180,480)
        pontopedra22 = Point(480,180)
        pedra1 = Obstaculo(pontopedra1,pontopedra12,win2,1)
        pedra2 = Obstaculo(pontopedra2,pontopedra22,win2,0)
        arvore2 = Arvore(win2,Point (150, 150),30)
        arvore3 = Arvore(win2,Point (450, 450),30)
        arvore = Arvore(win2,Point (300, 300),30)
        grouppedras = []
        grouparvores = []
        for i in [arvore.centre,arvore2.centre,arvore3.centre]:
            grouparvores.append(i)
        for i in [pedra1.obscentro,pedra2.obscentro]:
            grouppedras.append(i)
        body = Robot(win2,10,10)
        moving(win2,grouparvores,grouppedras,body,bateria,pontoderecolha,1)
        win2.close()