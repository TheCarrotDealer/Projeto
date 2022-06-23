from random import *
from graphics import * 
from math import *

class Robot:
    
    def __init__(self,win,ax,bx): 
        #Aqui é criado o corpo do robo em si 
        self.body= Circle(Point(ax,bx),10)
        self.bodybatery= Circle(Point(ax,bx),5)
        self.body.setFill("white")
        self.body.draw(win)
        self.bodybatery.setFill("light green")
        self.bodybatery.draw(win)
        self.centre = Point(ax,bx) #cria o seu centro 
        self.batery = 0 # cria a vareavel da bateria

    def mover(self,dx,dy):
        #esta função faz mover o robo e o seu centro
        self.bodybatery.move(dx,dy)
        self.body.move(dx,dy)
        self.centre.move(dx,dy)
        self.batery = self.batery + 1 #aumenta a bateria

    def distancias(self,ponto3,ponto4):
        #arredonda as entradas de pontos, ponto3 será de um obstáculo e o ponto4 a localização da maça
        true1x = round(ponto3.getX())
        true1y = round(ponto3.getY())
        true2x = round(ponto4.getX())
        true2y = round(ponto4.getY())

        #se o obstáculo tiver uma hitbox quadrada aqui é calculada a distancia do centro do robo aos cantos da hitbox do obstáculo
        self.distesq = (self.centre.getX()-40-true1x)**2 + (self.centre.getY()-true1y)**2
        self.distinf = (self.centre.getX()-true1x)**2 + (self.centre.getY()-40-true1y)**2
        self.distsup = (self.centre.getX()-true1x)**2 + (self.centre.getY()+40-true1y)**2
        self.distdir = (self.centre.getX()+40-true1x)**2 + (self.centre.getY()-true1y)**2

        #se o obstáculo tiver uma hitbox circular aqui é calculada a distancia do centro da maça aos cantos da hitbox do obstáculo 
        # ( como é um circulo será os estremos do circulo nas coordenadas x e y)
        self.distesqmaca = (true2x-40-true1x)**2 + (true2y-true1y)**2
        self.distinfmaca = (true2x-true1x)**2 + (true2y-40-true1y)**2
        self.distsupmaca = (true2x-true1x)**2 + (true2y+40-true1y)**2
        self.distdirmaca = (true2x+40-true1x)**2 + (true2y-true1y)**2

        #se o obstáculo tiver uma hitbox quadrada aqui é calculada a distancia do centro da maça aos cantos da hitbox do obstáculo
        self.distcantoinfesqqmaca = (true1x-40-true2x)**2 + (true1y-40-true2y)**2
        self.distcantoinfdirmaca = (true1x+40-true2x)**2 + (true1y-40-true2y)**2
        self.distcantosupesqmaca = (true1x-40-true2x)**2 + (true1y+40-true2y)**2
        self.distcantosupdirmaca = (true1x+40-true2x)**2 + (true1y+40-true2y)**2

    # Temos aqui uma série de funções que designam movimentos específicos para o robo fazer quando entra em contacto com o obstáculo quadrado
    # para se desviar deste e conseguir se deslocar para o seu objetivo
    def A1C2(self,ponto2):
        # o robo desloca-se do local onde está na parede para o canto designado
        true1x = round(self.centre.getX())
        true2x = round(ponto2.getX())
        true2x = true2x - 40
        a = (true1x - true2x) #calcula quanto tem de se mover
        for i in range(a):
            update(50)
            self.mover(-1,0)

    def A1C3(self,ponto1,ponto2):# escolhe da esquina que devia se movimentar
        self.distancias(ponto1,ponto2) 
        #com as distâncias vê qual é o percurso mais rápido para se derigir 
        if self.distcantoinfesqqmaca < self.distcantosupdirmaca: 
            for i in range(80):
                update(50)
                self.mover(-1,0)
        if self.distcantoinfesqqmaca >= self.distcantosupdirmaca:
            for i in range(80):
                update(50)
                self.mover(0,1)

    def A1B3(self,ponto2): # o robo desloca-se do local onde está na parede para o canto designado
        true1x = round(self.centre.getY())
        true2x = round(ponto2.getY())
        true2x = true2x + 40
        a = (true2x - true1x)
        for i in range(a):
            update(50)
            self.mover(0,1)

    def A2B1(self,ponto1): # o robo desloca-se do local onde está na parede para o canto designado
        true1x = round(self.centre.getY())
        true2x = round(ponto1.getY())
        a = (true2x - true1x) + 40
        for i in range(a):
            update(50)
            self.mover(0,1)

    def A2C1(self): #desloca-se da esquina onde está para a esquina designada
        for i in range(80):
            update(50)
            self.mover(0,1)

    def A2C2(self,ponto1,ponto2): #estando o objetivo no lado oposto á maça é calculado para que lado o robo deverá ir
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

    def A2C3(self): #desloca-se da esquina onde está para a esquina designada
        for i in range(80):
            update(50)
            self.mover(0,1)

    def A2B3(self,ponto1): # o robo desloca-se do local onde está na parede para o canto designado
        true1x = round(self.centre.getY())
        true2x = round(ponto1.getY())
        a = (true2x - true1x) + 40
        for i in range(a):
            update(50)
            self.mover(0,1)

    def A3B1(self,ponto1): # o robo desloca-se do local onde está na parede para o canto designado
        true1x = round(self.centre.getY())
        true2x = round(ponto1.getY())
        a = (true2x - true1x) + 40
        for i in range(a):
            update(50)
            self.mover(0,1)

    def A3C1(self,ponto1,ponto2): # escolhe da esquina que devia se movimentar
        self.distancias(ponto1,ponto2)
        if self.distcantosupesqmaca < self.distcantoinfdirmaca:
            for i in range(80):
                update(50)
                self.mover(0,1)
        if self.distcantosupesqmaca >= self.distcantoinfdirmaca:
            for i in range(80):
                update(50)
                self.mover(1,0)

    def A3C2(self,ponto1): # o robo desloca-se do local onde está na parede para o canto designado
        true1x = round(self.centre.getX())
        true2x = round(ponto1.getX())
        a= true2x - true1x + 40
        for i in range(a):
            update(50)
            self.mover(1,0)

    def B1A2(self,ponto1): # o robo desloca-se do local onde está na parede para o canto designado
        true1x = round(self.centre.getX())
        true2x = round(ponto1.getX())
        true2x = true2x - 40
        a = (true1x - true2x)
        for i in range(a):
            update(50)
            self.mover(-1,0)

    def B1A3(self): #desloca-se da esquina onde está para a esquina designada
        for i in range(80):
            update(50)
            self.mover(-1,0)

    def B1B3(self,ponto1,ponto2): #estando o objetivo no lado oposto á maça é calculado para que lado o robo deverá ir
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

    def B1C3(self): #desloca-se da esquina onde está para a esquina designada
        for i in range(80):
            update(50)
            self.mover(-1,0)

    def B1C2(self,ponto1): # o robo desloca-se do local onde está na parede para o canto designado
        true1x = round(self.centre.getX())
        true2x = round(ponto1.getX())
        true2x = true2x - 40
        a = (true1x - true2x)
        for i in range(a):
            update(50)
            self.mover(-1,0)

    def B3A2(self,ponto1): # o robo desloca-se do local onde está na parede para o canto designado
        true1x = round(self.centre.getX())
        true2x = round(ponto1.getX())
        a= true2x - true1x + 40
        for i in range(a):
            update(50)
            self.mover(1,0)

    def B3A1(self): #desloca-se da esquina onde está para a esquina designada
        for i in range(80):
            update(50)
            self.mover(1,0)

    def B3B1(self,ponto1,ponto2): #estando o objetivo no lado oposto á maça é calculado para que lado o robo deverá ir
        self.distancias(ponto1,ponto2)
        true1x = round(self.centre.getY())
        true2x = round(ponto1.getY())
        #desloca-se para a esquina que o dará o percurso mais curto
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
        for i in range(80): # estando já na esquina este desloca-se da esquina onde está para a esquina designada
            update(50)
            self.mover(1,0)

    def B3C1(self): #desloca-se da esquina onde está para a esquina designada
        for i in range(80):
            update(50)
            self.mover(1,0)

    def B3C2(self,ponto1): # o robo desloca-se do local onde está na parede para o canto designado
        true1x = round(self.centre.getX())
        true2x = round(ponto1.getX())
        a= true2x - true1x + 40
        for i in range(a):
            update(50)
            self.mover(1,0)

    def C1A2(self,ponto1): # o robo desloca-se do local onde está na parede para o canto designado
        true1x = round(self.centre.getX())
        true2x = round(ponto1.getX())
        true2x = true2x - 40
        a = (true1x - true2x)
        for i in range(a):
            update(50)
            self.mover(-1,0)

    def C1A3(self,ponto1,ponto2): # escolhe da esquina que devia se movimentar
        self.distancias(ponto1,ponto2)
        if self.distcantosupesqmaca < self.distcantoinfdirmaca:
            for i in range(80):
                update(50)
                self.mover(-1,0)
        if self.distcantosupesqmaca >= self.distcantoinfdirmaca:
            for i in range(80):
                update(50)
                self.mover(0,-1)

    def C1B3(self,ponto1): # o robo desloca-se do local onde está na parede para o canto designado
        true1x = round(self.centre.getY())
        true2x = round(ponto1.getY())
        true2x = true2x - 40
        a= true1x - true2x
        for i in range(a):
            update(50)
            self.mover(0,-1)

    def C2B1(self,ponto1): # o robo desloca-se do local onde está na parede para o canto designado
        true1x = round(self.centre.getY())
        true2x = round(ponto1.getY())
        true2x = true2x - 40
        a= true1x - true2x
        for i in range(a):
            update(50)
            self.mover(0,-1)

    def C2A1(self): #desloca-se da esquina onde está para a esquina designada
        for i in range(80):
            update(50)
            self.mover(0,-1)

    def C2A2(self,ponto1,ponto2): #estando o objetivo no lado oposto á maça é calculado para que lado o robo deverá ir
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

    def C2A3(self): #desloca-se da esquina onde está para a esquina designada
        for i in range(80):
            update(50)
            self.mover(0,-1)

    def C2B3(self,ponto1): # o robo desloca-se do local onde está na parede para o canto designado
        true1x = round(self.centre.getY())
        true2x = round(ponto1.getY())
        true2x = true2x - 40
        a= true1x - true2x
        for i in range(a):
            update(50)
            self.mover(0,-1)

    def C3B1(self,ponto1): # o robo desloca-se do local onde está na parede para o canto designado
        true1x = round(self.centre.getY())
        true2x = round(ponto1.getY())
        true2x = true2x - 40
        a= true1x - true2x
        for i in range(a):
            update(50)
            self.mover(0,-1)

    def C3A1(self,ponto1,ponto2): # escolhe da esquina que devia se movimentar
        self.distancias(ponto1,ponto2)
        if self.distcantoinfesqqmaca < self.distcantosupdirmaca:
            for i in range(80):
                update(50)
                self.mover(0,-1)
        if self.distcantoinfesqqmaca >= self.distcantosupdirmaca:
            for i in range(80):
                update(50)
                self.mover(1,0) 

    def C3A2(self,ponto1): # o robo desloca-se do local onde está na parede para o canto designado
        true1x = round(self.centre.getX())
        true2x = round(ponto1.getX())
        a= true2x - true1x + 40
        for i in range(a):
            update(50)
            self.mover(1,0)

    def movimentoobst(self,ponto1,ponto2):
        # verifica se o robo está dentro da hitbox quadrada do obstáculo

        if self.centre.getX() > (ponto1.getX()-40) and self.centre.getY() > (ponto1.getY()-40) and self.centre.getX() < (ponto1.getX()+40) and self.centre.getY() < (ponto1.getY()+40) :
            
            #verificada a posição do objetivo em relação ao obstáculo

            if ponto1.getX() - 40 >= ponto2.getX() and ponto1.getY() + 40 <= ponto2.getY(): #zona da maça A1

                # caso o objetivo esteja nesta posição, o robo ao ter tocado só poderá estar numa de algumas posições
                # em relação ao obstáculo e aqui é verificado qual delas é a que o robo se encontra para realizar o movimento nessesário 

                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and self.centre.getY() <= ponto1.getY() - 39: #zona do robo C2
                    self.A1C2(ponto1) 

                if self.centre.getX() >= ponto1.getX() + 39 and self.centre.getY() <= ponto1.getY() - 39: #zona do robo C3
                    self.A1C3(ponto1,ponto2)

                if self.centre.getX() >= ponto1.getX() + 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39: #zona do robo B3
                    self.A1B3(ponto1)

            if ponto1.getX() - 40 <= ponto2.getX() <= ponto1.getX() + 40  and ponto1.getY() + 40 <= ponto2.getY(): #zona da maça A2

                if self.centre.getX() <= ponto1.getX() - 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39: #zona do robo B1
                    self.A2B1(ponto1)

                if self.centre.getX() <= ponto1.getX() - 39 and self.centre.getY() <= ponto1.getY() - 39: #zona do robo C1
                    self.A2C1()

                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and self.centre.getY() <= ponto1.getY() - 39: #zona do robo C2
                    self.A2C2(ponto1,ponto2)

                if self.centre.getX() >= ponto1.getX() + 39 and self.centre.getY() <= ponto1.getY() - 39: #zona do robo C3
                    self.A2C3()

                if self.centre.getX() >= ponto1.getX() + 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39: #zona do robo B3
                    self.A2B3(ponto1)

            if ponto1.getX() + 40 < ponto2.getX() and ponto1.getY() + 40 < ponto2.getY(): #zona da maça A3

                if self.centre.getX() <= ponto1.getX() - 39 and self.centre.getY() <= ponto1.getY() - 39: #zona do robo C1
                    self.A3C1(ponto1,ponto2)

                if self.centre.getX() <= ponto1.getX() - 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39: #zona do robo B1
                    self.A3B1(ponto1)

                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and self.centre.getY() <= ponto1.getY() - 39: #zona do robo C2
                    self.A3C2(ponto1)

            if ponto1.getX() - 40 > ponto2.getX() and ponto1.getY() - 40 < ponto2.getY() < ponto1.getY() + 40: #zona da maça B1

                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and self.centre.getY() <= ponto1.getY() - 39: #zona do robo C2
                    self.B1C2(ponto1)

                if self.centre.getX() >= ponto1.getX() + 39 and self.centre.getY() <= ponto1.getY() - 39: #zona do robo C3
                    self.B1C3()

                if self.centre.getX() >= ponto1.getX() + 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39: #zona do robo B3
                    self.B1B3(ponto1,ponto2)

                if self.centre.getX() >= ponto1.getX() + 39 and ponto1.getY() + 39 < self.centre.getY(): #zona do robo A3
                    self.B1A3()

                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and ponto1.getY() + 38 < self.centre.getY(): #zona do robo A2
                    self.B1A2(ponto1)

            if ponto1.getX() + 40 < ponto2.getX() and ponto1.getY() - 40 < ponto2.getY() < ponto1.getY() + 40: #zona da maça B3

                if self.centre.getX() < ponto1.getX() - 39 and ponto1.getY() + 38 < self.centre.getY(): #zona do robo A1
                    self.B3A1()

                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and ponto1.getY() + 38 < self.centre.getY(): #zona do robo A2
                    self.B3A2(ponto1)

                if self.centre.getX() <= ponto1.getX() - 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39: #zona do robo B1
                    self.B3B1(ponto1,ponto2)

                if self.centre.getX() <= ponto1.getX() - 39 and self.centre.getY() <= ponto1.getY() - 39: #zona do robo C1
                    self.B3C1()

                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and self.centre.getY() <= ponto1.getY() - 39: #zona do robo C2
                    self.B3C2(ponto1)

            if ponto1.getX() - 40 > ponto2.getX() and ponto1.getY() - 40 > ponto2.getY(): #zona da maça C1

                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and ponto1.getY() + 38 < self.centre.getY(): #zona do robo A2
                    self.C1A2(ponto1)

                if self.centre.getX() >= ponto1.getX() + 39 and ponto1.getY() + 39 < self.centre.getY(): #zona do robo A3
                    self.C1A3(ponto1,ponto2)

                if self.centre.getX() >= ponto1.getX() + 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39: #zona do robo B3
                    self.C1B3(ponto1)

            if ponto1.getX() - 40 < ponto2.getX() < ponto1.getX() + 40 and ponto1.getY() - 40 > ponto2.getY(): #zona da maça C2

                if self.centre.getX() <= ponto1.getX() - 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39: #zona do robo B1
                    self.C2B1(ponto1)

                if self.centre.getX() < ponto1.getX() - 39 and ponto1.getY() + 39 < self.centre.getY(): #zona do robo A1
                    self.C2A1()

                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and ponto1.getY() + 38 < self.centre.getY(): #zona do robo A2
                    self.C2A2(ponto1,ponto2)

                if self.centre.getX() >= ponto1.getX() + 39 and ponto1.getY() + 39 < self.centre.getY(): #zona do robo A3
                    self.C2A3()

                if self.centre.getX() >= ponto1.getX() + 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39: #zona do robo B3
                    self.C2B3(ponto1)

            if ponto1.getX() + 40 < ponto2.getX() and ponto1.getY() - 40 > ponto2.getY(): #zona da maça C3

                if self.centre.getX() <= ponto1.getX() - 39 and ponto1.getY() - 39 < self.centre.getY() < ponto1.getY() + 39: #zona do robo B1
                    self.C3B1(ponto1)

                if self.centre.getX() < ponto1.getX() - 39 and ponto1.getY() + 39 < self.centre.getY(): #zona do robo A1
                    self.C3A1(ponto1,ponto2)

                if ponto1.getX() - 39 <= self.centre.getX() <= ponto1.getX() + 39 and ponto1.getY() + 38 < self.centre.getY(): #zona do robo A2
                    self.C3A2(ponto1)

    def moveobjetive(self,ponto1):
        #sendo o ponto1 o objetivo aqui é verificado a localização desse objetivo em comparação com o centro do robo

        if self.centre.getX() < ponto1.getX():
            self.x = 1 #aqui é alterado a direção do robo para que este vá na direção do objetivo

        if self.centre.getX() > ponto1.getX():
            self.x = -1

        if self.centre.getY() < ponto1.getY():
            self.y = 1

        if self.centre.getY() > ponto1.getY():
            self.y = -1

        #aqui vemos que quando eles partilharem uma coordenada o robo já não tem de se mover em relação a essa coordenada, assim ele acaba por ir em direção para o objetivo
        if self.centre.getX() == ponto1.getX():
            self.x = 0

        if self.centre.getY() == ponto1.getY():
            self.y = 0

    # Temos aqui uma série de funções que designam movimentos específicos para o robo fazer quando entra em contacto com o obstáculo circular
    # para se desviar deste e conseguir se deslocar para o seu objetivo

    def circA1A2(self): #muda a direção do movimento para sair da zona do circulo (em direção ao seu objetivo)
        self.x = 0
        self.y = 1

    def circA1B1(self):#muda a direção do movimento para sair da zona do circulo
        self.x = -1
        self.y = 0

    def circA1B2(self,ponto1,ponto2): # a partir das distâncias verifica para que lado o robo deverá se deslocar para mais rápidamente ultrapassar o obstáculo
        self.distancias(ponto1,ponto2)
        if self.distsupmaca + self.distdir  > self.distesqmaca + self.distinf:
            #muda a direção do movimento para sair da zona do circulo
            self.x = 1
            self.y = 0
        if self.distsupmaca + self.distdir  <= self.distesqmaca + self.distinf:
            self.x = 0
            self.y = -1

    def circA1A1(self):#muda a direção do movimento para sair da zona do circulo
        self.x = -1
        self.y = 1

    def circA2A1(self):#muda a direção do movimento para sair da zona do circulo
        self.x = 0
        self.y = 1

    def circA2B1(self,ponto1,ponto2): # a partir das distâncias verifica para que lado o robo deverá se deslocar para mais rápidamente ultrapassar o obstáculo
        self.distancias(ponto1,ponto2)
        if self.distsupmaca + self.distesq  > self.distdirmaca + self.distinf:
            self.x = -1
            self.y = 0
        if self.distsupmaca + self.distesq  <= self.distdirmaca + self.distinf:
            self.x = 0
            self.y = -1

    def circA2B2(self):#muda a direção do movimento para sair da zona do circulo
        self.x = 1
        self.y = 0

    def circA2A2(self):#muda a direção do movimento para sair da zona do circulo
        self.x = 1
        self.y = 1

    def circB1A1(self):#muda a direção do movimento para sair da zona do circulo
        self.x = -1
        self.y = 0

    def circB1A2(self,ponto1,ponto2): # a partir das distâncias verifica para que lado o robo deverá se deslocar para mais rápidamente ultrapassar o obstáculo
        self.distancias(ponto1,ponto2)
        if self.distsup + self.distesqmaca  > self.distdir + self.distinfmaca:
            self.x = 0
            self.y = 1
        if self.distsup + self.distesqmaca  <= self.distdir + self.distinfmaca:
            self.x = 1
            self.y = 0

    def circB1B2(self):#muda a direção do movimento para sair da zona do circulo
        self.x = 0
        self.y = -1

    def circB1B1(self):#muda a direção do movimento para sair da zona do circulo
        self.x = -1
        self.y = -1

    def circB2A1(self,ponto1,ponto2): # a partir das distâncias verifica para que lado o robo deverá se deslocar para mais rápidamente ultrapassar o obstáculo
        self.distancias(ponto1,ponto2)
        if self.distsup + self.distdirmaca  > self.distesq + self.distinfmaca:
            self.x = 0
            self.y = 1
        if self.distsup + self.distdirmaca  <= self.distesq + self.distinfmaca:
            self.x = -1
            self.y = 0

    def circB2A2(self):#muda a direção do movimento para sair da zona do circulo
        self.x = 1
        self.y = 0

    def circB2B1(self):#muda a direção do movimento para sair da zona do circulo
        self.x = 0
        self.y = -1

    def circB2B2(self):#muda a direção do movimento para sair da zona do circulo
        self.x = 1
        self.y = -1

    def movearvore(self,ponto1,ponto2):
        # verifica se o robo está dentro da hitbox circular do obstáculo
        if (self.centre.getX() - ponto1.getX())**2 + (self.centre.getY() - ponto1.getY())**2 <= 40**2:
            #verificada a posição do objetivo em relação ao obstáculo

            if ponto2.getX() <= ponto1.getX() and ponto2.getY() >= ponto1.getY(): #zona da maça A1
                # caso o objetivo esteja nesta posição, o robo ao ter tocado só poderá estar numa de algumas posições
                # em relação ao obstáculo e aqui é verificado qual delas é a que o robo se encontra para realizar o movimento nessesário
                # para se desviar do obstáculo 

                if self.centre.getX() <= ponto1.getX() and self.centre.getY() >= ponto1.getY(): #zona do robo A1
                    self.circA1A1()

                if self.centre.getX() < ponto1.getX() and self.centre.getY() < ponto1.getY():#zona do robo B1
                    self.circA1B1()

                if self.centre.getX() >= ponto1.getX() and self.centre.getY() <= ponto1.getY(): #zona do robo B2
                    self.circA1B2(ponto1,ponto2)

                if self.centre.getX() > ponto1.getX() and self.centre.getY() > ponto1.getY(): #zona do robo A2
                    self.circA1A2()

            if ponto2.getX() < ponto1.getX() and ponto2.getY() < ponto1.getY(): #zona da maça B1

                if self.centre.getX() <= ponto1.getX() and self.centre.getY() >= ponto1.getY():#zona do robo A1
                    self.circB1A1()

                if self.centre.getX() < ponto1.getX() and self.centre.getY() < ponto1.getY():#zona do robo B1
                    self.circB1B1()

                if self.centre.getX() >= ponto1.getX() and self.centre.getY() <= ponto1.getY():#zona do robo B2
                    self.circB1B2()

                if self.centre.getX() > ponto1.getX() and self.centre.getY() > ponto1.getY():#zona do robo A2
                    self.circB1A2(ponto1,ponto2)

            if ponto2.getX() >= ponto1.getX() and ponto2.getY() <= ponto1.getY(): #zona da maça B2

                if self.centre.getX() <= ponto1.getX() and self.centre.getY() >= ponto1.getY():#zona do robo A1
                    self.circB2A1(ponto1,ponto2)

                if self.centre.getX() < ponto1.getX() and self.centre.getY() < ponto1.getY(): #zona do robo B1
                    self.circB2B1()

                if self.centre.getX() >= ponto1.getX() and self.centre.getY() <= ponto1.getY():#zona do robo B2
                    self.circB2B2()

                if self.centre.getX() > ponto1.getX() and self.centre.getY() > ponto1.getY():#zona do robo A2
                    self.circB2A2()

            if ponto2.getX() > ponto1.getX() and ponto2.getY() > ponto1.getY(): #zona da maça A2

                if self.centre.getX() <= ponto1.getX() and self.centre.getY() >= ponto1.getY():#zona do robo A1
                    self.circA2A1()

                if self.centre.getX() < ponto1.getX() and self.centre.getY() < ponto1.getY():#zona do robo B1
                    self.circA2B1(ponto1,ponto2)

                if self.centre.getX() >= ponto1.getX() and self.centre.getY() <= ponto1.getY():#zona do robo B2
                    self.circA2B2()

                if self.centre.getX() > ponto1.getX() and self.centre.getY() > ponto1.getY():#zona do robo A2
                    self.circA2A2()


    def countbatery(self,ponto1,on):
        #aqui é verificada a bateria e designada a cor do centro do robo
        self.bateryactive = 0 #aqui temos a verificação se o robo está sem bateria ou não
        if self.batery >= 0:
            self.bodybatery.setFill("light green")
        if on == 1: #sendo a variavel on responsável por identificar se temos a bateria em conta ou não
            if self.batery >= 400:
                self.bodybatery.setFill("yellow")
            if self.batery >= 800:
                self.bodybatery.setFill("red")
            if self.batery >= 1200: #aqui temos o limite da bateria 
                self.moveobjetive(ponto1) #muda o objetivo do robo para o centro da estação de recarga
                self.bateryactive = 1 #confirma que está sem bateria
                if self.centre.getX() == ponto1.getX() and self.centre.getY() == ponto1.getY(): #quando chega ao centro do centro de recarga espera 2 segundos e renicia a bateria
                    for i in range(2):
                        update(1)
                    self.batery=0
        else:
            pass

    def randompoint(self): #randomiza pontos
        x = randrange(61, 540)
        y = randrange(61, 540)
        first = Point(x,y)
        return first

    def random(self,numb):
        self.numbarvores = randrange(0,numb+1) #randomiza o numero de objetos com hitbox circular, a partir do numero de obstáculos pedidos
        print(self.numbarvores)
        self.numbpedras = numb - self.numbarvores #numero de objetos com hitbox quadrada
        print(self.numbpedras)

        #grupos onde os centros dos obstáculos são guardados
        self.obstgrouparvores = []
        self.obstgrouppedras = []
        self.obstgroup = []

        if self.numbarvores ==0: #se só tivermos circulos
            #randomiza um ponto e adiciona-o ás listas
            first = self.randompoint()
            self.obstgrouppedras.append(first)
            self.obstgroup.append(first)

            for i in range(numb-1): #cria os pontos pedidos
                counter = 1
                while counter ==1:
                    i = self.randompoint()
                    counter = 0 
                    for a in self.obstgroup:#verifica se os pontos estáo demasiado pertos
                        if sqrt((i.getX() - a.getX())**2 + (i.getY() - a.getY())**2) < 120:
                            counter = counter + 1
                if counter == 0: #se o ponto for válido, é adicionado ás listas
                    self.obstgrouppedras.append(i)
                    self.obstgroup.append(i)


        if 0 < self.numbarvores < numb: # se tivermos árvores e circulos
            first = self.randompoint()
            self.obstgrouparvores.append(first)
            self.obstgroup.append(first)

            for i in range(self.numbarvores - 1): #para o numero de árvores cria pontos random, tal que estes não criem objetos que se intersetam 
                counter = 1
                while counter ==1:
                    i = self.randompoint()
                    counter = 0 
                    for a in self.obstgroup:
                        if sqrt((i.getX() - a.getX())**2 + (i.getY() - a.getY())**2) < 120:
                            counter = counter + 1
                if counter == 0:
                    self.obstgrouparvores.append(i)
                    self.obstgroup.append(i)


            for i in range(self.numbpedras): #repete o processo para as pedras
                counter = 1
                while counter ==1:
                    i = self.randompoint()
                    counter = 0 
                    for a in self.obstgroup:
                        if sqrt((i.getX() - a.getX())**2 + (i.getY() - a.getY())**2) < 120:
                            counter = counter + 1
                if counter == 0:
                    self.obstgrouppedras.append(i)
                    self.obstgroup.append(i)


        if self.numbarvores == numb: #o mesmo processo mas para só arvores
            first = self.randompoint()
            self.obstgrouparvores.append(first)
            self.obstgroup.append(first)
            for i in range(numb-1):
                counter = 1
                while counter ==1:
                    i = self.randompoint()
                    counter = 0 
                    for a in self.obstgroup:
                        if sqrt((i.getX() - a.getX())**2 + (i.getY() - a.getY())**2) < 120:
                            counter = counter + 1
                if counter == 0:
                    self.obstgrouparvores.append(i)
                    self.obstgroup.append(i)


    def file(self,file):
        #cria os grupos de obstáculos
        self.obstgrouparvores = []
        self.obstgrouparbustos = []
        self.obstgrouppedras = []
        self.obstaculos = []
        counter = 0
        for i in file.readlines(): #lê o file inserido
            i = str(i)
            try:
                x , y , ob = i.split(" ")
                x = int(x)
                y = int(y)
                counter = 0
                # verifica se o ponto do obstáculo inserido é válido
                for l in self.obstaculos: # se está demasiado perto de outros obstáculos 
                    if sqrt((x - l.getX())**2 + (y - l.getY())**2) < 120:
                        counter = counter + 1 
                        print("Obstáculo demasiado perto de outros objetos")
                    if x<= 21 or 570 < x or y<= 21 or 570 < y: # se está demasiado perto das bordas
                        counter = counter + 1 
                        print("Obstáculo demasiado perto das bordas onde se localizam objetivos")
                self.obstaculos.append(Point(x,y))
                if counter == 0:
                    ob = int(ob) #se o ponto for válido verifica se o ponto é um arbusto, uma arvore ou uma pedra
                    if ob == 1:
                        self.obstgrouppedras.append(Point(x,y))
                    elif ob == 2:
                        self.obstgrouparvores.append(Point(x,y))
                    elif ob == 3:
                        self.obstgrouparbustos.append(Point(x,y))
                    else:
                        print("Tipo de obstáculo inválido")
                else:
                    print("Obstáculo inválido")
                        
            except ValueError:
                break

    def dodgeeverything(self,grouparvores,grouppedras,objective): # agrupa as funções para o robo se desviar de quadrados e de circulos 
        for i in grouparvores: #verifica para todos os circulos
            self.movearvore(i,objective) 
        for i in grouppedras: #verifica para todos os quadrados
            self.movimentoobst(i,objective) 

