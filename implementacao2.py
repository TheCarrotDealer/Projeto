# Projeto feito pelo grupo 69
# 102680 Luís Alberto Canha Abreu Gomes Gonçalves
# 103545 Rúben Nelson da Silva Vieira Alves
from graphics import * 
from classes import *
from macas import *
from outrasclasses import *
def implementação2():
        #cria uma janela
        win2 = GraphWin("Projeto Ai implementação2", 600, 600)
        win2.setCoords(0, 0, 600, 600)

        #dá set up aos itens importantes para o funcionamento da função
        bateria, pontoderecolha = baseline(win2)

        #cria os obstáculos
        pontopedra1 = Point(120,420)
        pontopedra2 = Point(420,120)
        pontopedra12 = Point(180,480)
        pontopedra22 = Point(480,180)
        pedra1 = Obstaculo(pontopedra1,pontopedra12,win2,1)
        pedra2 = Obstaculo(pontopedra2,pontopedra22,win2,0)
        arvore2 = Arvore(win2,Point (150, 150))
        arvore3 = Arvore(win2,Point (450, 450))
        arvore = Arvore(win2,Point (300, 300))

        #coloca os seus centros dentro das listas
        grouppedras = []
        grouparvores = []
        for i in [arvore.centre,arvore2.centre,arvore3.centre]:
            grouparvores.append(i)
        for i in [pedra1.obscentro,pedra2.obscentro]:
            grouppedras.append(i)

        #cria o robo
        body = Robot(win2,10,10)

        #processo de movimentos 
        moving(win2,grouparvores,grouppedras,body,bateria,pontoderecolha,1,0,0)
        win2.close()