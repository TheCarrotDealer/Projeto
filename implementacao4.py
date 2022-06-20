from graphics import * 
from classes import *
from macas import *
from outrasclasses import *
def implementação4():
        win2 = GraphWin("Projeto Ai implementação4", 600, 600)
        win2.setCoords(0, 0, 600, 600)
        bateria, pontoderecolha = baseline(win2)
        body = Robot(win2,10,10)
        file = open("fileprojeto.txt","r")
        body.file(file)
        for i in body.obstgrouppedras:
            thex = i.getX() -30
            they = i.getY() -30
            the1x = i.getX() +30
            the1y = i.getY() +30
            i = Obstaculo(Point(thex,they),Point(the1x,the1y),win2,1)
        for l in body.obstgrouparbustos:
            thex = l.getX() -30
            they = l.getY() -30
            the1x = l.getX() +30
            the1y = l.getY() +30
            body.obstgrouppedras.append(l)
            l = Obstaculo(Point(thex,they),Point(the1x,the1y),win2,0)
        for a in body.obstgrouparvores:
            a = Arvore(win2,a,30)
        grouparvores = body.obstgrouparvores 
        grouppedras = body.obstgrouppedras
        moving(win2,grouparvores,grouppedras,body,bateria,pontoderecolha,1)
        win2.close()