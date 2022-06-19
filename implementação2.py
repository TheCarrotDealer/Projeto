from graphics import * 
from classes import *
from maças import *
def implementação2():
        win2 = GraphWin("Projeto Ai implementação2", 600, 600)
        win2.setCoords(0, 0, 600, 600)
        win2.setBackground("chartreuse3")
        bateria, pontoderecolha = baseline(win2)
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

        on = 1

        moving(win2,grouparvores,grouppedras,body,bateria,pontoderecolha,on)
        win2.close()