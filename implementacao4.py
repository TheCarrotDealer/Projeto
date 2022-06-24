from graphics import * 
from classes import *
from macas import *
from outrasclasses import *
def implementação4():
        #cria uma janela
        win2 = GraphWin("Projeto Ai implementação4", 600, 600)
        win2.setCoords(0, 0, 600, 600)

        #dá set up aos itens importantes para o funcionamento da função
        bateria, pontoderecolha = baseline(win2)
        
        #cria o robo
        body = Robot(win2,10,10)

        #randomiza os centros de obstáculos
        body.random(5)

        #transforma os centros de obstáculos com hitbox quadrada em objetos
        for i in body.obstgrouppedras: 
            thex = i.getX() -30
            they = i.getY() -30
            the1x = i.getX() +30
            the1y = i.getY() +30

            #randomiza arbustos e arvores
            l = randrange(0,2)
            i = Obstaculo(Point(thex,they),Point(the1x,the1y),win2,l)

        #transforma os centros de obstáculos com hitbox circular em objetos
        for a in body.obstgrouparvores:
            a = Arvore(win2,a)

        grouparvores = body.obstgrouparvores 
        grouppedras = body.obstgrouppedras

        #processo de movimentos 
        moving(win2,grouparvores,grouppedras,body,bateria,pontoderecolha,1,0,0)
        
        win2.close()