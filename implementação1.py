from graphics import * 
from classes import *
from maças import *
from outrasclasses import *
def implementação1():
    win = GraphWin("Projeto Ai implementação1", 600, 600)
    win.setCoords(0, 0, 600, 600)
    bateria, pontoderecolha = baseline(win)

    a = Point (300, 300)

    arvore = Arvore(win,a,30)

    body = Robot(win,10,10)

    grouparvores = [arvore.centre]
    grouppedras = []

    moving(win,grouparvores,grouppedras,body,bateria,pontoderecolha,0)

    win.close()