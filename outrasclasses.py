from graphics import * 
from classes import *
class Maça:
    def __init__(self,win,ponto):
        poentox = round(ponto.getX())
        poentoy = round(ponto.getY())
        self.corpo = Image(Point(poentox,poentoy),"basketapples.png")
        self.corpo.draw(win)
        self.centro = Point(poentox,poentoy)
    def existnt(self):
        self.corpo.undraw()
class Recolha:
    def __init__(self,ponto1,ponto2,ponto3,ponto4,win):
        true1x = round(ponto1.getX())
        true1y = round(ponto1.getY())
        true2x = round(ponto2.getX())
        true2y = round(ponto2.getY())
        true3x = round(ponto3.getX())
        true3y = round(ponto3.getY())
        true4x = round(ponto4.getX())
        true4y = round(ponto4.getY())
        self.box1centro = Point((true1x + true2x)/2,(true1y + true2y)/2)
        self.box2centro = Point((true3x + true4x)/2,(true3y + true4y)/2)
        self.box1 = Image(self.box1centro,"buraco.png")
        self.box2 = Image(self.box2centro,"buraco.png")
        self.box1.draw(win)
        self.box2.draw(win)
class Obstaculo:
    def __init__(self,ponto1,ponto2,win,type):
        true1x = round(ponto1.getX())
        true1y = round(ponto1.getY())
        true2x = round(ponto2.getX())
        true2y = round(ponto2.getY())
        self.obscentro = Point((true1x + true2x)/2,(true1y + true2y)/2)
        if type == 1:
            self.obs = Image(self.obscentro,"rock.png")
        else:
            self.obs = Image(self.obscentro,"bush.png")
        self.obs.draw(win)
class Arvore:
    def __init__(self, win, ponto1, raio):
        self.centre = ponto1
        self.arvore = Image(self.centre,"arvore.png")
        self.arvore.draw(win)
class butão: 
    def __init__(self,win1,point1,point2,lable):
        self.leftcorner = point1
        self.rightcorner = point2
        x = round((point1.getX() + point2.getX())/2)
        y = round((point1.getY() + point2.getY())/2)
        self.centre = Point(x,y)
        self.button = Rectangle(point1,point2)
        self.button.setFill("lightgray")
        self.button.draw(win1)
        self.lable = Text(self.centre,lable)
        self.lable.draw(win1)
    def clicked(self,point):
        self.active = True
        return (self.active and self.leftcorner.getX() < point.getX() < self.rightcorner.getX() and self.leftcorner.getY() < point.getY()< self.rightcorner.getY())    
class baterystation:
    def __init__(self,ponto1,ponto2,win):
        true1x = round(ponto1.getX())
        true1y = round(ponto1.getY())
        true2x = round(ponto2.getX())
        true2y = round(ponto2.getY())
        self.obs = Rectangle(Point(true1x,true1y),Point(true2x,true2y))
        self.centro = Point((true1x + true2x)/2,(true1y + true2y)/2)
        self.obs.setFill("chocolate4")
        self.obs.draw(win)