
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

def main():

    win = GraphWin("Projeto Ai apanhar maças", 600, 600)
    win.setCoords(0, 0, 600, 600)
    win.setBackground("green")
    body = Robot(win,10,10)
    macacentro = win.getMouse()
    maca = Maça(win,macacentro)
    print(maca.centro.getX())
    x=1
    y=1
    counter = 0
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
        y=1
        x=1
        body.mover(x,y)
main()