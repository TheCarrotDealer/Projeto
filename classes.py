from random import *
from graphics import * 
from math import *
class Robot:
    def __init__(self,win,ax,bx): 
        self.body= Circle(Point(ax,bx),10)
        self.bodybatery= Circle(Point(ax,bx),5)
        self.body.setFill("white")
        self.body.draw(win)
        self.bodybatery.setFill("light green")
        self.bodybatery.draw(win)
        self.centre = Point(ax,bx)
        self.batery = 0
    def mover(self,dx,dy):
        self.bodybatery.move(dx,dy)
        self.body.move(dx,dy)
        self.centre.move(dx,dy)
        self.batery = self.batery + 1
    def distancias(self,ponto3,ponto4):
        true1x = round(ponto3.getX())
        true1y = round(ponto3.getY())
        true2x = round(ponto4.getX())
        true2y = round(ponto4.getY())
        self.distesq = (self.centre.getX()-40-true1x)**2 + (self.centre.getY()-true1y)**2
        self.distinf = (self.centre.getX()-true1x)**2 + (self.centre.getY()-40-true1y)**2
        self.distsup = (self.centre.getX()-true1x)**2 + (self.centre.getY()+40-true1y)**2
        self.distdir = (self.centre.getX()+40-true1x)**2 + (self.centre.getY()-true1y)**2
        self.distesqmaca = (true2x-40-true1x)**2 + (true2y-true1y)**2
        self.distinfmaca = (true2x-true1x)**2 + (true2y-40-true1y)**2
        self.distsupmaca = (true2x-true1x)**2 + (true2y+40-true1y)**2
        self.distdirmaca = (true2x+40-true1x)**2 + (true2y-true1y)**2
        self.distcantoinfesqqmaca = (true1x-40-true2x)**2 + (true1y-40-true2y)**2
        self.distcantoinfdirmaca = (true1x+40-true2x)**2 + (true1y-40-true2y)**2
        self.distcantosupesqmaca = (true1x-40-true2x)**2 + (true1y+40-true2y)**2
        self.distcantosupdirmaca = (true1x+40-true2x)**2 + (true1y+40-true2y)**2
    def A1C2(self,ponto2):
        true1x = round(self.centre.getX())
        true2x = round(ponto2.getX())
        true2x = true2x - 40
        a = (true1x - true2x)
        for i in range(a):
            update(50)
            self.mover(-1,0)
    def A1C3(self,ponto1,ponto2):
        self.distancias(ponto1,ponto2)
        if self.distcantoinfesqqmaca < self.distcantosupdirmaca:
            for i in range(80):
                update(50)
                self.mover(-1,0)
        if self.distcantoinfesqqmaca >= self.distcantosupdirmaca:
            for i in range(80):
                update(50)
                self.mover(0,1)
    def A1B3(self,ponto2):
        true1x = round(self.centre.getY())
        true2x = round(ponto2.getY())
        true2x = true2x + 40
        a = (true2x - true1x)
        for i in range(a):
            update(50)
            self.mover(0,1)
    def A2B1(self,ponto1):
        true1x = round(self.centre.getY())
        true2x = round(ponto1.getY())
        a = (true2x - true1x) + 40
        for i in range(a):
            update(50)
            self.mover(0,1)
    def A2C1(self):
        for i in range(80):
            update(50)
            self.mover(0,1)
    def A2C2(self,ponto1,ponto2):
        self.distancias(ponto1,ponto2)
        true1x = round(self.centre.getX())
        true2x = round(ponto1.getX())
        if  self.distcantosupesqmaca < self.distcantosupdirmaca:
            true2x = true2x - 40
            a = (true1x - true2x)
            for i in range(a):
                update(50)
                self.mover(-1,0)
        if  self.distcantosupesqmaca >= self.distcantosupdirmaca:
            a= true2x - true1x + 40
            for i in range(a):
                update(50)
                self.mover(1,0)
        for i in range(80):
            update(50)
            self.mover(0,1)
    def A2C3(self):
        for i in range(80):
            update(50)
            self.mover(0,1)
    def A2B3(self,ponto1):
        true1x = round(self.centre.getY())
        true2x = round(ponto1.getY())
        a = (true2x - true1x) + 40
        for i in range(a):
            update(50)
            self.mover(0,1)
    def A3B1(self,ponto1):
        true1x = round(self.centre.getY())
        true2x = round(ponto1.getY())
        a = (true2x - true1x) + 40
        for i in range(a):
            update(50)
            self.mover(0,1)
    def A3C1(self,ponto1,ponto2):
        self.distancias(ponto1,ponto2)
        if self.distcantosupesqmaca < self.distcantoinfdirmaca:
            for i in range(80):
                update(50)
                self.mover(0,1)
        if self.distcantosupesqmaca >= self.distcantoinfdirmaca:
            for i in range(80):
                update(50)
                self.mover(1,0)
    def A3C2(self,ponto1):
        true1x = round(self.centre.getX())
        true2x = round(ponto1.getX())
        a= true2x - true1x + 40
        for i in range(a):
            update(50)
            self.mover(1,0)
    def B1A2(self,ponto1):
        true1x = round(self.centre.getX())
        true2x = round(ponto1.getX())
        true2x = true2x - 40
        a = (true1x - true2x)
        for i in range(a):
            update(50)
            self.mover(-1,0)
    def B1A3(self):
        for i in range(80):
            update(50)
            self.mover(-1,0)
    def B1B3(self,ponto1,ponto2):
        self.distancias(ponto1,ponto2)
        true1x = round(self.centre.getY())
        true2x = round(ponto1.getY())
        if  self.distcantosupesqmaca < self.distcantoinfesqqmaca:
            true2x = true2x + 40
            a = (true2x - true1x)
            for i in range(a):
                update(50)
                self.mover(0,1)
        if  self.distcantosupesqmaca >= self.distcantoinfesqqmaca:
            true2x = true2x - 40
            a= true1x - true2x
            for i in range(a):
                update(50)
                self.mover(0,-1)
        for i in range(80):
            update(50)
            self.mover(-1,0)
    def B1C3(self):
        for i in range(80):
            update(50)
            self.mover(-1,0)
    def B1C2(self,ponto1):
        true1x = round(self.centre.getX())
        true2x = round(ponto1.getX())
        true2x = true2x - 40
        a = (true1x - true2x)
        for i in range(a):
            update(50)
            self.mover(-1,0)
    def B3A2(self,ponto1):
        true1x = round(self.centre.getX())
        true2x = round(ponto1.getX())
        a= true2x - true1x + 40
        for i in range(a):
            update(50)
            self.mover(1,0)
    def B3A1(self):
        for i in range(80):
            update(50)
            self.mover(1,0)
    def B3B1(self,ponto1,ponto2):
        self.distancias(ponto1,ponto2)
        true1x = round(self.centre.getY())
        true2x = round(ponto1.getY())
        if  self.distcantosupdirmaca < self.distcantoinfdirmaca:
            true2x = true2x + 40
            a = (true2x - true1x)
            for i in range(a):
                update(50)
                self.mover(0,1)
        if  self.distcantosupdirmaca >= self.distcantoinfdirmaca:
            true2x = true2x - 40
            a= true1x - true2x
            for i in range(a):
                update(50)
                self.mover(0,-1)
        for i in range(80):
            update(50)
            self.mover(1,0)
    def B3C1(self):
        for i in range(80):
            update(50)
            self.mover(1,0)
    def B3C2(self,ponto1):
        true1x = round(self.centre.getX())
        true2x = round(ponto1.getX())
        a= true2x - true1x + 40
        for i in range(a):
            update(50)
            self.mover(1,0)
    def C1A2(self,ponto1):
        true1x = round(self.centre.getX())
        true2x = round(ponto1.getX())
        true2x = true2x - 40
        a = (true1x - true2x)
        for i in range(a):
            update(50)
            self.mover(-1,0)
    def C1A3(self,ponto1,ponto2):
        self.distancias(ponto1,ponto2)
        if self.distcantosupesqmaca < self.distcantoinfdirmaca:
            for i in range(80):
                update(50)
                self.mover(-1,0)
        if self.distcantosupesqmaca >= self.distcantoinfdirmaca:
            for i in range(80):
                update(50)
                self.mover(0,-1)
    def C1B3(self,ponto1):
        true1x = round(self.centre.getY())
        true2x = round(ponto1.getY())
        true2x = true2x - 40
        a= true1x - true2x
        for i in range(a):
            update(50)
            self.mover(0,-1)
    def C2B1(self,ponto1):
        true1x = round(self.centre.getY())
        true2x = round(ponto1.getY())
        true2x = true2x - 40
        a= true1x - true2x
        for i in range(a):
            update(50)
            self.mover(0,-1)
    def C2A1(self):
        for i in range(80):
            update(50)
            self.mover(0,-1)
    def C2A2(self,ponto1,ponto2):
        self.distancias(ponto1,ponto2)
        true1x = round(self.centre.getX())
        true2x = round(ponto1.getX())
        if  self.distcantoinfesqqmaca < self.distcantoinfdirmaca:
            true2x = true2x - 40
            a = (true1x - true2x)
            for i in range(a):
                update(50)
                self.mover(-1,0)
        if  self.distcantoinfesqqmaca >= self.distcantoinfdirmaca:
            a= true2x - true1x + 40
            for i in range(a):
                update(50)
                self.mover(1,0)
        for i in range(80):
            update(50)
            self.mover(0,-1)
    def C2A3(self):
        for i in range(80):
            update(50)
            self.mover(0,-1)
    def C2B3(self,ponto1):
        true1x = round(self.centre.getY())
        true2x = round(ponto1.getY())
        true2x = true2x - 40
        a= true1x - true2x
        for i in range(a):
            update(50)
            self.mover(0,-1)
    def C3B1(self,ponto1):
        true1x = round(self.centre.getY())
        true2x = round(ponto1.getY())
        true2x = true2x - 40
        a= true1x - true2x
        for i in range(a):
            update(50)
            self.mover(0,-1)
    def C3A1(self,ponto1,ponto2):
        self.distancias(ponto1,ponto2)
        if self.distcantoinfesqqmaca < self.distcantosupdirmaca:
            for i in range(80):
                update(50)
                self.mover(0,-1)
        if self.distcantoinfesqqmaca >= self.distcantosupdirmaca:
            for i in range(80):
                update(50)
                self.mover(1,0) 
    def C3A2(self,ponto1):
        true1x = round(self.centre.getX())
        true2x = round(ponto1.getX())
        a= true2x - true1x + 40
        for i in range(a):
            update(50)
            self.mover(1,0)
    def movimentoobst(self,ponto1,ponto2):
        if self.centre.getX() > (ponto1.getX()-40) and self.centre.getY() > (ponto1.getY()-40) and self.centre.getX() < (ponto1.getX()+40) and self.centre.getY() < (ponto1.getY()+40) :
            if ponto1.getX() - 40 >= ponto2.getX() and ponto1.getY() + 40 <= ponto2.getY():
                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and self.centre.getY() <= ponto1.getY() - 39:
                    self.A1C2(ponto1)
                if self.centre.getX() >= ponto1.getX() + 39 and self.centre.getY() <= ponto1.getY() - 39:
                    self.A1C3(ponto1,ponto2)
                if self.centre.getX() >= ponto1.getX() + 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39:
                    self.A1B3(ponto1)
            if ponto1.getX() - 40 <= ponto2.getX() <= ponto1.getX() + 40  and ponto1.getY() + 40 <= ponto2.getY():
                if self.centre.getX() <= ponto1.getX() - 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39:
                    self.A2B1(ponto1)
                if self.centre.getX() <= ponto1.getX() - 39 and self.centre.getY() <= ponto1.getY() - 39:
                    self.A2C1()
                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and self.centre.getY() <= ponto1.getY() - 39:
                    self.A2C2(ponto1,ponto2)
                if self.centre.getX() >= ponto1.getX() + 39 and self.centre.getY() <= ponto1.getY() - 39:
                    self.A2C3()
                if self.centre.getX() >= ponto1.getX() + 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39:
                    self.A2B3(ponto1)
            if ponto1.getX() + 40 < ponto2.getX() and ponto1.getY() + 40 < ponto2.getY():
                if self.centre.getX() <= ponto1.getX() - 39 and self.centre.getY() <= ponto1.getY() - 39:
                    self.A3C1(ponto1,ponto2)
                if self.centre.getX() <= ponto1.getX() - 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39:
                    self.A3B1(ponto1)
                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and self.centre.getY() <= ponto1.getY() - 39:
                    self.A3C2(ponto1)
            if ponto1.getX() - 40 > ponto2.getX() and ponto1.getY() - 40 < ponto2.getY() < ponto1.getY() + 40:
                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and self.centre.getY() <= ponto1.getY() - 39:
                    self.B1C2(ponto1)
                if self.centre.getX() >= ponto1.getX() + 39 and self.centre.getY() <= ponto1.getY() - 39:
                    self.B1C3()
                if self.centre.getX() >= ponto1.getX() + 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39:
                    self.B1B3(ponto1,ponto2)
                if self.centre.getX() >= ponto1.getX() + 39 and ponto1.getY() + 39 < self.centre.getY():
                    self.B1A3()
                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and ponto1.getY() + 38 < self.centre.getY():
                    self.B1A2(ponto1)
            if ponto1.getX() + 40 < ponto2.getX() and ponto1.getY() - 40 < ponto2.getY() < ponto1.getY() + 40:
                if self.centre.getX() < ponto1.getX() - 39 and ponto1.getY() + 38 < self.centre.getY():
                    self.B3A1()
                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and ponto1.getY() + 38 < self.centre.getY():
                    self.B3A2(ponto1)
                if self.centre.getX() <= ponto1.getX() - 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39:
                    self.B3B1(ponto1,ponto2)
                if self.centre.getX() <= ponto1.getX() - 39 and self.centre.getY() <= ponto1.getY() - 39:
                    self.B3C1()
                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and self.centre.getY() <= ponto1.getY() - 39:
                    self.B3C2(ponto1)
            if ponto1.getX() - 40 > ponto2.getX() and ponto1.getY() - 40 > ponto2.getY():
                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and ponto1.getY() + 38 < self.centre.getY():
                    self.C1A2(ponto1)
                if self.centre.getX() >= ponto1.getX() + 39 and ponto1.getY() + 39 < self.centre.getY():
                    self.C1A3(ponto1,ponto2)
                if self.centre.getX() >= ponto1.getX() + 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39:
                    self.C1B3(ponto1)
            if ponto1.getX() - 40 < ponto2.getX() < ponto1.getX() + 40 and ponto1.getY() - 40 > ponto2.getY():
                if self.centre.getX() <= ponto1.getX() - 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39:
                    self.C2B1(ponto1)
                if self.centre.getX() < ponto1.getX() - 39 and ponto1.getY() + 39 < self.centre.getY():
                    self.C2A1()
                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and ponto1.getY() + 38 < self.centre.getY():
                    self.C2A2(ponto1,ponto2)
                if self.centre.getX() >= ponto1.getX() + 39 and ponto1.getY() + 39 < self.centre.getY():
                    self.C2A3()
                if self.centre.getX() >= ponto1.getX() + 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39:
                    self.C2B3(ponto1)
            if ponto1.getX() + 40 < ponto2.getX() and ponto1.getY() - 40 > ponto2.getY():
                if self.centre.getX() <= ponto1.getX() - 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39:
                    self.C3B1(ponto1)
                if self.centre.getX() < ponto1.getX() - 39 and ponto1.getY() + 39 < self.centre.getY():
                    self.C3A1(ponto1,ponto2)
                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and ponto1.getY() + 38 < self.centre.getY():
                    self.C3A2(ponto1)
    def moveobjetive(self,ponto1):
        if self.centre.getX() < ponto1.getX():
            self.x = 1
        if self.centre.getX() > ponto1.getX():
            self.x = -1
        if self.centre.getY() < ponto1.getY():
            self.y = 1
        if self.centre.getY() > ponto1.getY():
            self.y = -1
        if self.centre.getX() == ponto1.getX():
            self.x = 0
        if self.centre.getY() == ponto1.getY():
            self.y = 0
    def circA1A2(self):
        self.x = 0
        self.y = 1
    def circA1B1(self):
        self.x = -1
        self.y = 0
    def circA1B2(self,ponto1,ponto2):
        self.distancias(ponto1,ponto2)
        if self.distsupmaca + self.distdir  > self.distesqmaca + self.distinf:
            self.x = 1
            self.y = 0
        if self.distsupmaca + self.distdir  <= self.distesqmaca + self.distinf:
            self.x = 0
            self.y = -1
    def circA1A1(self):
        self.x = -1
        self.y = 1
    def circA2A1(self):
        self.x = 0
        self.y = 1
    def circA2B1(self,ponto1,ponto2):
        self.distancias(ponto1,ponto2)
        if self.distsupmaca + self.distesq  > self.distdirmaca + self.distinf:
            self.x = -1
            self.y = 0
        if self.distsupmaca + self.distesq  <= self.distdirmaca + self.distinf:
            self.x = 0
            self.y = -1
    def circA2B2(self):
        self.x = 1
        self.y = 0
    def circA2A2(self):
        self.x = 1
        self.y = 1
    def circB1A1(self):
        self.x = -1
        self.y = 0
    def circB1A2(self,ponto1,ponto2):
        self.distancias(ponto1,ponto2)
        if self.distsup + self.distesqmaca  > self.distdir + self.distinfmaca:
            self.x = 0
            self.y = 1
        if self.distsup + self.distesqmaca  <= self.distdir + self.distinfmaca:
            self.x = 1
            self.y = 0
    def circB1B2(self):
        self.x = 0
        self.y = -1
    def circB1B1(self):
        self.x = -1
        self.y = -1
    def circB2A1(self,ponto1,ponto2):
        self.distancias(ponto1,ponto2)
        if self.distsup + self.distdirmaca  > self.distesq + self.distinfmaca:
            self.x = 0
            self.y = 1
        if self.distsup + self.distdirmaca  <= self.distesq + self.distinfmaca:
            self.x = -1
            self.y = 0
    def circB2A2(self):
        self.x = 1
        self.y = 0
    def circB2B1(self):
        self.x = 0
        self.y = -1
    def circB2B2(self):
        self.x = 1
        self.y = -1
    def movearvore(self,ponto1,ponto2):
        if (self.centre.getX() - ponto1.getX())**2 + (self.centre.getY() - ponto1.getY())**2 <= 40**2:
            if ponto2.getX() <= ponto1.getX() and ponto2.getY() >= ponto1.getY():
                if self.centre.getX() <= ponto1.getX() and self.centre.getY() >= ponto1.getY():
                    self.circA1A1()
                if self.centre.getX() < ponto1.getX() and self.centre.getY() < ponto1.getY():
                    self.circA1B1()
                if self.centre.getX() >= ponto1.getX() and self.centre.getY() <= ponto1.getY():
                    self.circA1B2(ponto1,ponto2)
                if self.centre.getX() > ponto1.getX() and self.centre.getY() > ponto1.getY():
                    self.circA1A2()
            if ponto2.getX() < ponto1.getX() and ponto2.getY() < ponto1.getY():
                if self.centre.getX() <= ponto1.getX() and self.centre.getY() >= ponto1.getY():
                    self.circB1A1()
                if self.centre.getX() < ponto1.getX() and self.centre.getY() < ponto1.getY():
                    self.circB1B1()
                if self.centre.getX() >= ponto1.getX() and self.centre.getY() <= ponto1.getY():
                    self.circB1B2()
                if self.centre.getX() > ponto1.getX() and self.centre.getY() > ponto1.getY():
                    self.circB1A2(ponto1,ponto2)
            if ponto2.getX() >= ponto1.getX() and ponto2.getY() <= ponto1.getY():
                if self.centre.getX() <= ponto1.getX() and self.centre.getY() >= ponto1.getY():
                    self.circB2A1(ponto1,ponto2)
                if self.centre.getX() < ponto1.getX() and self.centre.getY() < ponto1.getY():
                    self.circB2B1()
                if self.centre.getX() >= ponto1.getX() and self.centre.getY() <= ponto1.getY():
                    self.circB2B2()
                if self.centre.getX() > ponto1.getX() and self.centre.getY() > ponto1.getY():
                    self.circB2A2()
            if ponto2.getX() > ponto1.getX() and ponto2.getY() > ponto1.getY():
                if self.centre.getX() <= ponto1.getX() and self.centre.getY() >= ponto1.getY():
                    self.circA2A1()
                if self.centre.getX() < ponto1.getX() and self.centre.getY() < ponto1.getY():
                    self.circA2B1(ponto1,ponto2)
                if self.centre.getX() >= ponto1.getX() and self.centre.getY() <= ponto1.getY():
                    self.circA2B2()
                if self.centre.getX() > ponto1.getX() and self.centre.getY() > ponto1.getY():
                    self.circA2A2()
    def countbatery(self,ponto1,on):
        self.bateryactive = 0
        if self.batery >= 0:
            self.bodybatery.setFill("light green")
        if on == 1:
            if self.batery >= 1500:
                self.bodybatery.setFill("yellow")
            if self.batery >= 3000:
                self.bodybatery.setFill("red")
            if self.batery >= 4800:
                self.moveobjetive(ponto1)
                self.bateryactive = 1
                if self.centre.getX() == ponto1.getX() and self.centre.getY() == ponto1.getY():
                    for i in range(2):
                        update(1)
                    self.batery=0
        else:
            pass
    def random(self,numb):
        self.numbarvores = randrange(0,numb+1)
        print(self.numbarvores)
        self.numbpedras = numb - self.numbarvores 
        print(self.numbpedras)
        self.obstgrouparvores = []
        self.obstgrouppedras = []
        self.obstgroup = []
        if self.numbarvores ==0:
            x = randrange(61, 540)
            y = randrange(61, 540)
            first = Point(x,y)
            self.obstgrouppedras.append(first)
            self.obstgroup.append(first)
            for i in range(numb-1):
                x = randrange(61, 540)
                y = randrange(61, 540)
                i = Point(x,y)
                counter = 1
                while counter ==1:
                    x = randrange(61, 540)
                    y = randrange(61, 540)
                    i = Point(x,y)
                    counter = 0 
                    for a in self.obstgroup:
                        if sqrt((i.getX() - a.getX())**2 + (i.getY() - a.getY())**2) < 120:
                            counter = counter + 1
                if counter == 0:
                    self.obstgrouppedras.append(i)
                    self.obstgroup.append(i)
        if 0 < self.numbarvores < numb:
            x = randrange(61, 540)
            y = randrange(61, 540)
            first = Point(x,y)
            self.obstgrouparvores.append(first)
            self.obstgroup.append(first)
            for i in range(self.numbarvores - 1):
                x = randrange(61, 540)
                y = randrange(61, 540)
                i = Point(x,y)
                counter = 1
                while counter ==1:
                    x = randrange(61, 540)
                    y = randrange(61, 540)
                    i = Point(x,y)
                    counter = 0 
                    for a in self.obstgroup:
                        if sqrt((i.getX() - a.getX())**2 + (i.getY() - a.getY())**2) < 120:
                            counter = counter + 1
                if counter == 0:
                    self.obstgrouparvores.append(i)
                    self.obstgroup.append(i)
            for i in range(self.numbpedras):
                x = randrange(61, 540)
                y = randrange(61, 540)
                i = Point(x,y)
                counter = 1
                while counter ==1:
                    x = randrange(61, 540)
                    y = randrange(61, 540)
                    i = Point(x,y)
                    counter = 0 
                    for a in self.obstgroup:
                        if sqrt((i.getX() - a.getX())**2 + (i.getY() - a.getY())**2) < 120:
                            counter = counter + 1
                if counter == 0:
                    self.obstgrouppedras.append(i)
                    self.obstgroup.append(i)
        if self.numbarvores == numb:
            x = randrange(61, 540)
            y = randrange(61, 540)
            first = Point(x,y)
            self.obstgrouparvores.append(first)
            self.obstgroup.append(first)
            for i in range(numb-1):
                x = randrange(61, 540)
                y = randrange(61, 540)
                i = Point(x,y)
                counter = 1
                while counter ==1:
                    x = randrange(61, 540)
                    y = randrange(61, 540)
                    i = Point(x,y)
                    counter = 0 
                    for a in self.obstgroup:
                        if sqrt((i.getX() - a.getX())**2 + (i.getY() - a.getY())**2) < 120:
                            counter = counter + 1
                if counter == 0:
                    self.obstgrouparvores.append(i)
                    self.obstgroup.append(i)


    def file(self,file):
        self.obstgrouparvores = []
        self.obstgrouparbustos = []
        self.obstgrouppedras = []
        self.obstaculos = []
        counter = 0
        for i in file.readlines():
            i = str(i)
            try:
                x , y , ob = i.split(" ")
                x = int(x)
                y = int(y)
                if self.obstaculos == []:
                    self.obstaculos.append(Point(x,y))
                else:
                    counter = 0
                    for l in self.obstaculos:
                        if sqrt((x - l.getX())**2 + (y - l.getY())**2) < 120:
                            counter = counter + 1 
                    if counter == 0:
                        self.obstaculos.append(Point(x,y))
                    else:
                        print("obstáculo demasiado perto do obsjetivo")
                        


                ob = int(ob)
                ponto = Point(x,y)
                if ob == 1:
                    self.obstgrouppedras.append(ponto)
                elif ob == 2:
                    self.obstgrouparvores.append(ponto)
                elif ob == 3:
                    self.obstgrouparbustos.append(ponto)
                else:
                    print("tipo de obstáculo inválido")

            except ValueError:
                break
    def dodgeeverything(self,grouparvores,grouppedras,objective):
        for i in grouparvores:
            self.movearvore(i,objective) 
        for i in grouppedras:
            self.movimentoobst(i,objective) 

