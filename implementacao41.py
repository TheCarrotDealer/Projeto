from graphics import * 
from classes import *
from macas import *
from outrasclasses import *
def implementação41():

        #cria uma janela
        win2 = GraphWin("Projeto Ai implementação4", 600, 600)
        win2.setCoords(0, 0, 600, 600)

        #dá set up aos itens importantes para o funcionamento da função
        bateria, pontoderecolha = baseline(win2)

        #cria o robo
        body = Robot(win2,10,10)

        #lê o file
        file = open("fileprojeto.txt","r")
        body.file(file)
        macafile= open("maçasfile.txt","r")

        for i in body.obstgrouppedras: #transforma os pontos designados para pedras em pedras
            thex = i.getX() -30
            they = i.getY() -30
            the1x = i.getX() +30
            the1y = i.getY() +30
            i = Obstaculo(Point(thex,they),Point(the1x,the1y),win2,1)

        for l in body.obstgrouparbustos: #transforma os pontos designados para arbustos em arbustos
            thex = l.getX() -30
            they = l.getY() -30
            the1x = l.getX() +30
            the1y = l.getY() +30
            body.obstgrouppedras.append(l) #adiciona os arbustos ao grupo de pedras por terem hitboxes iguais 

            l = Obstaculo(Point(thex,they),Point(the1x,the1y),win2,0)
        for a in body.obstgrouparvores: #transforma os pontos designados para arvores em arvores
            a = Arvore(win2,a)

        grouparvores = body.obstgrouparvores 
        grouppedras = body.obstgrouppedras

        #processo de movimentos 
        moving(win2,grouparvores,grouppedras,body,bateria,pontoderecolha,1,macafile,1)

        win2.close()