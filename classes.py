from graphics import * 
class Robot:
    def __init__(self,win,ax,bx): 
        self.body= Circle(Point(ax,bx),10)
        self.body.setFill("white")
        self.body.draw(win)
        self.centre = Point(ax,bx)
    def mover(self,dx,dy):
        self.body.move(dx,dy)
        self.centre.move(dx,dy)
    def distancias(self,ponto3,ponto4):
        true1x = round(ponto3.getX())
        true1y = round(ponto3.getY())
        true2x = round(ponto4.getX())
        true2y = round(ponto4.getY())
        distcantoinfesq = (self.centre.getX()-40-true1x)**2 + (self.centre.getY()-40-true1y)**2
        distcantoinfdir = (self.centre.getX()+40-true1x)**2 + (self.centre.getY()-40-true1y)**2
        distcantosupesq = (self.centre.getX()-40-true1x)**2 + (self.centre.getY()+40-true1y)**2
        distcantosupdir = (self.centre.getX()+40-true1x)**2 + (self.centre.getY()+40-true1y)**2
        distcantoinfesqqmaca = (self.centre.getX()-40-true2x)**2 + (self.centre.getY()-40-true2y)**2
        distcantoinfdirmaca = (self.centre.getX()+40-true2x)**2 + (self.centre.getY()-40-true2y)**2
        distcantosupesqmaca = (self.centre.getX()-40-true2x)**2 + (self.centre.getY()+40-true2y)**2
        distcantosupdirmaca = (self.centre.getX()+40-true2x)**2 + (self.centre.getY()+40-true2y)**2
    def A1C2(self,ponto1):
        pass
    def A1C3(self,ponto1):
        pass
    def A1B3(self):
        pass
    def A2B1(self):
        pass
    def A2C1(self):
        pass
    def A2C2(self):
        pass
    def A2C3(self):
        pass
    def A2B3(self):
        pass
    def A3B1(self):
        pass
    def A3C1(self):
        pass
    def A3C2(self):
        pass
    def B1A2(self):
        pass
    def B1A3(self):
        pass
    def B1B3(self):
        pass
    def B1C3(self):
        pass
    def B1C2(self):
        pass
    def B3A2(self):
        pass
    def B3A1(self):
        pass
    def B3B1(self):
        pass
    def B3C1(self):
        pass
    def B3C2(self):
        pass
    def C1A2(self):
        pass
    def C1A3(self):
        pass
    def C1B3(self):
        pass
    def C2B1(self):
        pass
    def C2A1(self):
        pass
    def C2A2(self):
        pass
    def C2A3(self):
        pass
    def C2B3(self):
        pass
    def C3B1(self):
        pass
    def C3A1(self):
        pass   
    def C3A2(self):
        pass
    def movimentoobst(self):
        pass

class Maça:
    def __init__(self,win,ponto):
        poentox = round(ponto.getX())
        poentoy = round(ponto.getY())
        self.corpo = Circle(ponto,10)
        self.corpo.setFill("red")
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
        self.box1 = Rectangle(Point(true1x,true1y),Point(true2x,true2y))
        self.box2 = Rectangle(Point(true3x,true3y),Point(true4x,true4y))
        self.box1.setFill("grey20")
        self.box2.setFill("grey20")
        self.box1.draw(win)
        self.box2.draw(win)
class Obstaculo:
    def __init__(self,ponto1,ponto2,win):
        true1x = round(ponto1.getX())
        true1y = round(ponto1.getY())
        true2x = round(ponto2.getX())
        true2y = round(ponto2.getY())
        self.obs = Rectangle(Point(true1x,true1y),Point(true2x,true2y))
        self.obscentro = Point((true1x + true2x)/2,(true1y + true2y)/2)
        self.obs.setFill("azure4")
        self.obs.draw(win)