# Projeto feito pelo grupo 69
# 102680 Luís Alberto Canha Abreu Gomes Gonçalves
# 103545 Rúben Nelson da Silva Vieira Alves
from graphics import * 
from classes import *
from macas import *
from outrasclasses import *
def implementação1():

    #cria uma janela
    win = GraphWin("Projeto Ai implementação1", 600, 600)
    win.setCoords(0, 0, 600, 600)
    
    #dá set up aos itens importantes para o funcionamento da função
    bateria, pontoderecolha = baseline(win)

    #cria o obstáculo
    a = Point (300, 300)

    arvore = Arvore(win,a)
    
    #cria o robo
    body = Robot(win,10,10)

    grouparvores = [arvore.centre]
    grouppedras = []

    #processo de movimentos 
    moving(win,grouparvores,grouppedras,body,bateria,pontoderecolha,0,0,0)#e define que não é para contar a bateria

    win.close()