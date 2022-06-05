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


def main():

    win = GraphWin("Projeto Ai apanhar maças", 600, 600)
    win.setCoords(0, 0, 600, 600)
    win.setBackground("green")
    body = Robot(win,10,10)
    macacentro = win.getMouse()
    maca = Maça(win,macacentro)
    pontoderecolha1 = Point(0,570)
    pontoderecolha2 = Point(30,600)
    pontoderecolha3 = Point(570,300)
    pontoderecolha4 = Point(600,330)
    pontoderecolha = Recolha(pontoderecolha1,pontoderecolha2,pontoderecolha3,pontoderecolha4,win)
    x=1
    y=1
    counter = 0
    pontoobs = Point(270,270)
    pontoobs1 = Point(330,330)
    obst = Obstaculo(pontoobs,pontoobs1,win)
    while counter == 0:
        update(30)
        if body.centre.getX() == maca.centro.getX():
            x=0
        if body.centre.getX() == maca.centro.getX() and body.centre.getY() > maca.centro.getY():
            x=0
            y=-1
        if body.centre.getY() == maca.centro.getY():
            y=0
        if body.centre.getY() == maca.centro.getY() and body.centre.getX() > maca.centro.getX():
            y=0
            x=-1
        if body.centre.getY() == maca.centro.getY() and body.centre.getX() == maca.centro.getX():
            counter = 1
            maca.existnt()
        
        body.mover(x,y)
    while counter == 1:
        update(30)
        distrecolha1 = (pontoderecolha.box1centro.getX()-body.centre.getX())**2 + (pontoderecolha.box1centro.getY()-body.centre.getY())**2
        distrecolha2 = (pontoderecolha.box2centro.getX()-body.centre.getX())**2 + (pontoderecolha.box2centro.getY()-body.centre.getY())**2
        if distrecolha1 <= distrecolha2:
            x=-1
            y=1
            if body.centre.getX() == pontoderecolha.box1centro.getX():
                x=0
            if body.centre.getX() == pontoderecolha.box1centro.getX() and body.centre.getY() > pontoderecolha.box1centro.getY():
                x=0
                y=-1
            if body.centre.getY() == pontoderecolha.box1centro.getY():
                y=0
            if body.centre.getY() == pontoderecolha.box1centro.getY() and body.centre.getX() < pontoderecolha.box1centro.getX():
                y=0
                x=-x
            if body.centre.getY() == pontoderecolha.box1centro.getY() and body.centre.getX() == pontoderecolha.box1centro.getX():
                print("homens")
                
        
        if distrecolha1 > distrecolha2:
            x=1
            y=1
            if body.centre.getY() > pontoderecolha.box2centro.getY():
                y=-1
            if body.centre.getX() == pontoderecolha.box2centro.getX():
                x=0
            if body.centre.getX() == pontoderecolha.box2centro.getX() and body.centre.getY() > pontoderecolha.box2centro.getY():
                x=0
                y=-1
            if body.centre.getY() == pontoderecolha.box2centro.getY():
                y=0
            if body.centre.getY() == pontoderecolha.box2centro.getY() and body.centre.getX() > pontoderecolha.box2centro.getX():
                y=0
                x=-1
            if body.centre.getY() == pontoderecolha.box2centro.getY() and body.centre.getX() == pontoderecolha.box2centro.getX():
                print("homens")
              

        body.mover(x,y)
main()
