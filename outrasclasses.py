from graphics import * 
from classes import *

class Maça:

    def __init__(self,win,ponto): # cria o objeto "maça" a partir de um ponto e desenha-a
        poentox = round(ponto.getX()) # arredonda as suas coordenadas para evitar erros
        poentoy = round(ponto.getY())
        self.corpo = Image(Point(poentox,poentoy),"basketapples.png")
        self.corpo.draw(win)
        self.centro = Point(poentox,poentoy) #cria o seu centro

    def existnt(self): #apaga a maça
        self.corpo.undraw()

class Recolha:
    def __init__(self,ponto1,ponto2,ponto3,ponto4,win): #cria pontos de recolha
        true1x = round(ponto1.getX())
        true1y = round(ponto1.getY())
        true2x = round(ponto2.getX())
        true2y = round(ponto2.getY())
        true3x = round(ponto3.getX())
        true3y = round(ponto3.getY())
        true4x = round(ponto4.getX())
        true4y = round(ponto4.getY())

        self.box1centro = Point((true1x + true2x)/2,(true1y + true2y)/2) #cria os seus centros
        self.box2centro = Point((true3x + true4x)/2,(true3y + true4y)/2)

        self.box1 = Image(self.box1centro,"buraco2.png") #desenha-os
        self.box2 = Image(self.box2centro,"buraco2.png")
        self.box1.draw(win)
        self.box2.draw(win)

class Obstaculo: #cria o osbtáculo pedra
    def __init__(self,ponto1,ponto2,win,type):
        true1x = round(ponto1.getX())
        true1y = round(ponto1.getY())
        true2x = round(ponto2.getX())
        true2y = round(ponto2.getY())

        self.obscentro = Point((true1x + true2x)/2,(true1y + true2y)/2) #cria o seu centro
        
        #verifica se é uma pedra ou um arbusto
        if type == 1:
            self.obs = Image(self.obscentro,"rock.png")
        else:
            self.obs = Image(self.obscentro,"bush.png")

        self.obs.draw(win)

class Arvore: #cria o obstaculo arvore
    def __init__(self, win, ponto1):
        self.centre = ponto1 #cria o seu centro

        self.arvore = Image(self.centre,"arvore.png")
        self.arvore.draw(win)

class butão: #cria um botão
    def __init__(self,win1,point1,point2,lable):
        self.leftcorner = point1
        self.rightcorner = point2
        x = round((point1.getX() + point2.getX())/2)
        y = round((point1.getY() + point2.getY())/2)

        self.centre = Point(x,y) #cria o seu centro

        #desenha-o
        self.button = Rectangle(point1,point2)
        self.button.setFill("lightgray")
        self.button.draw(win1)

        self.lable = Text(self.centre,lable)
        self.lable.draw(win1)

    def clicked(self,point):
        # verifica se foi clicado
        self.active = True
        return (self.active and self.leftcorner.getX() < point.getX() < self.rightcorner.getX() and self.leftcorner.getY() < point.getY()< self.rightcorner.getY())    

class baterystation: #cria a estação de carregamento
    def __init__(self,ponto1,ponto2,win):
        true1x = round(ponto1.getX())
        true1y = round(ponto1.getY())
        true2x = round(ponto2.getX())
        true2y = round(ponto2.getY())
        
        self.centro = Point((true1x + true2x)/2,(true1y + true2y)/2) #cria o seu centro

        self.obs = Image(self.centro,"bateria.png")
        self.obs.draw(win)