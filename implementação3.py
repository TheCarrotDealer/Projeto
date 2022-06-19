from graphics import * 
from classes import *
from maças import *
def implementação3():
        win2 = GraphWin("Projeto Ai implementação3", 600, 600)
        win2.setCoords(0, 0, 600, 600)
        win2.setBackground("chartreuse3")
        bateria, pontoderecolha = baseline(win2)
        body = Robot(win2,10,10)
        body.random(5)
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
        
        on = 1

        moving(win2,grouparvores,grouppedras,body,bateria,pontoderecolha,on)
        win2.close()