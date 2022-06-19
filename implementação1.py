from graphics import * 
from classes import *
from maças import *
def implementação1():
    win = GraphWin("Projeto Ai implementação1", 600, 600)
    win.setCoords(0, 0, 600, 600)
    win.setBackground("chartreuse3")


    a = Point (300, 300)
    arvore = Arvore(win,a,30)

    bateria, pontoderecolha = baseline(win)

    body = Robot(win,10,10)

    on = 0

    grouparvores = [arvore.centre]
    grouppedras = []
    
    moving(win,grouparvores,grouppedras,body,bateria,pontoderecolha,on)

    win.close()