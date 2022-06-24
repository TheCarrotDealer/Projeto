# Projeto feito pelo grupo 69
# 102680 Luís Alberto Canha Abreu Gomes Gonçalves
# 103545 Rúben Nelson da Silva Vieira Alves
from graphics import * 
from classes import *
from outrasclasses import *
def multiplemaças(win2,grouparvores,grouppedras,maçafile,on):
    if on == 0:
        #cria os botões 
        pointstart = Point(510,0)
        pointstart1 = Point(550,30)
        startbutton = butão(win2,pointstart,pointstart1,"Start")

        pointquit = Point(560,0)
        pointquit1 = Point(600,30)
        quitbutton = butão(win2,pointquit,pointquit1,"Quit")

        quitcounter = 0

        #grupos de maças 
        maçasgroup = []
        maçasgroupcentre = []

        #criação do texto para iniciar a implementação
        text2 = Text(Point(300,450),"clique no ecrã")
        text2.draw(win2)
        macacentro = win2.getMouse()
        text2.undraw()
        macacount = 0


        while macacount == 0:
                checkcounter = 0

                #criação de um ponto que possivélmente será uma maça
                macacentro = win2.getMouse()
                text1 = Text(Point(300,450),"coloque noutro lugar")

                #verifica se a localização da maça é válida 
                for i in grouparvores:
                    if (macacentro.getX() - i.getX())**2 + (macacentro.getY() - i.getY())**2 <= 40**2:
                        checkcounter = checkcounter + 1
                for i in grouppedras:
                    if i.getX() - 40 < macacentro.getX() <  i.getX() + 40 and  i.getY() - 40 < macacentro.getY() <  i.getY() + 40:
                        checkcounter = checkcounter + 1

                text1.draw(win2)

                #caso não o utilizador entra num loop até colocar uma maça válida
                while checkcounter > 0:
                    macacentro = win2.getMouse()
                    text1.undraw()
                    text1 = Text(Point(300,450),"coloque noutro lugar")
                    checkcounter = 0

                    for i in grouparvores:
                        if (macacentro.getX() - i.getX())**2 + (macacentro.getY() - i.getY())**2 <= 40**2:
                            checkcounter = checkcounter + 1
                    for i in grouppedras:
                        if i.getX() - 40 < macacentro.getX() <  i.getX() + 40 and  i.getY() - 40 < macacentro.getY() <  i.getY() + 40:
                            checkcounter = checkcounter + 1

                    text1.draw(win2)
                text1.undraw()


                if startbutton.clicked(macacentro):
                    #caso haja maças a fase de adição de maças acaba
                    if maçasgroupcentre != []:
                        macacount = 1
                    #caso n haja maças a fase de adição continua
                    if maçasgroupcentre == []:
                        print("adicione maças")


                elif quitbutton.clicked(macacentro):
                    #sai da janela
                    quitcounter = 1
                    macacount = 1

                else: 
                    if maçasgroupcentre == []:
                        #cria a maça
                        maca = Maça(win2,macacentro)
                        maçasgroup.append(maca)
                        maçasgroupcentre.append(maca.centro)
                    else:
                        specialcounter = 0 #serve para verificar se está em cima da maça
                        #verifica se a maça não coincide com outra maça 
                        for i in maçasgroupcentre:
                            if (macacentro.getX() - i.getX())**2 + (macacentro.getY() - i.getY())**2 <= 10**2:
                                specialcounter = specialcounter +1

                        if specialcounter == 0:
                            #caso não coincida cria a maça
                            maca = Maça(win2,macacentro)
                            maçasgroup.append(maca)
                            maçasgroupcentre.append(maca.centro)
                        else:
                            print("maça demasiado perto")

        #dá return ao movimento de saida da janela e ás listas das maças e os seus centros
        return quitcounter, maçasgroup, maçasgroupcentre

    if on == 1:

        #cria os botões 
        pointstart = Point(510,0)
        pointstart1 = Point(550,30)
        startbutton = butão(win2,pointstart,pointstart1,"Start")

        pointquit = Point(560,0)
        pointquit1 = Point(600,30)
        quitbutton = butão(win2,pointquit,pointquit1,"Quit")

        quitcounter = 0

        #grupos de maças 
        maçasgroup = []
        maçasgroupcentre = []

        for l in maçafile.readlines(): #lê o file inserido
            l = str(l)
            try:
                x , y = l.split(" ")
                x = int(x)
                y = int(y)
                counter = 0
                macacentro= Point(x,y)
                # verifica se o ponto da maça não coincide com obstáculos
                for i in grouparvores:
                    if (macacentro.getX() - i.getX())**2 + (macacentro.getY() - i.getY())**2 <= 40**2:
                        counter = counter + 1
                for i in grouppedras:
                    if i.getX() - 40 < macacentro.getX() <  i.getX() + 40 and  i.getY() - 40 < macacentro.getY() <  i.getY() + 40:
                        counter = counter + 1
                if counter == 0:
                    if maçasgroupcentre == []:
                        #cria a maça
                        maca = Maça(win2,macacentro)
                        maçasgroup.append(maca)
                        maçasgroupcentre.append(maca.centro)
                    else:
                        specialcounter = 0
                        #verifica se a maça não coincide com outra maça 
                        for i in maçasgroupcentre:
                            if (macacentro.getX() - i.getX())**2 + (macacentro.getY() - i.getY())**2 <= 10**2:
                                specialcounter = specialcounter +1

                        if specialcounter == 0:
                            #caso não coincida cria a maça
                            maca = Maça(win2,macacentro)
                            maçasgroup.append(maca)
                            maçasgroupcentre.append(maca.centro)
                        else:
                            print("maça demasiado perto")    
                else:
                    print(" maça dentro de obstáculos")
                        
            except ValueError:
                print("failed")
        while True:
            click = win2.getMouse()

            if quitbutton.clicked(click):
                quitcounter = 1
                break
            if startbutton.clicked(click):
                break
        #dá return ao movimento de saida da janela e ás listas das maças e os seus centros
        return quitcounter, maçasgroup, maçasgroupcentre



def myFunc(e):
    #retorna os valores das distancias das listas
    return e['distance']

def moving(win2,grouparvores,grouppedras,body,bateria,pontoderecolha,on,file,onfile):
        #reune os acontecimentos todos dentro das implementações 

        counter = 0

        #busca a ação de quit e as listas de maças
        quitcounter, maçasgroup, maçasgroupcentre = multiplemaças(win2,grouparvores,grouppedras,file,onfile)

        while quitcounter == 0:
            for i in range(2):
                update(1)

            
            objetivomacasgroup = []
            for a in maçasgroupcentre:

                #calcula as distâncias do centro a cada maça
                b = (body.centre.getX()-a.getX())**2 + (body.centre.getY()-a.getY())**2 

                #adiciona a uma lista e organiza os pontos dos centros das maças consoante as distancias 
                objetivomacasgroup .append( {'a':a,'distance':b})
                objetivomacasgroup .sort(key=myFunc)

            #apaga a lista das maças já que os pontos já estão organizados em outra lista    
            maçasgroupcentre = []

            #busca os pontos já organizados das maças e adiciona-os á lista das maças
            for a in objetivomacasgroup:
                b = a['a']
                maçasgroupcentre.append(b)

            while not maçasgroupcentre == []:
                counter = 0
                while counter == 0:
                    #direciona-se ao ponto mais próximo do robo
                    l = maçasgroupcentre[0]
                    update(50)

                    #direciona-se a ele
                    body.moveobjetive(l)
                    #caso o robo fique sem bateria direciona-se para a estação de carregamento
                    body.countbatery(bateria.centro,on)
                    objective = l

                    #define o objetivo no desvio de obstáculos
                    if body.bateryactive == 1:
                        objective = bateria.centro

                    #desvia-se dos obstáculos de forma a chegar ao seu objetive da maneira mais rápida    
                    body.dodgeeverything(grouparvores,grouppedras,objective)

                    #caso chegue ao seu objetivo
                    if body.centre.getY() == l.getY() and body.centre.getX() == l.getX():
                        counter = 1

                        for p in maçasgroup:
                            #verifica qual das maças apanhou
                            if body.centre.getY() == p.centro.getY() and body.centre.getX() == p.centro.getX():
                                #apaga a maça 
                                p.existnt()
                                maçasgroupcentre.remove(l)

                                #reorganiza as maças
                                objetivomacasgroup = []
                                for a in maçasgroupcentre:
                                    b = (body.centre.getX()-a.getX())**2 + (body.centre.getY()-a.getY())**2 
                                    objetivomacasgroup.append( {'a':a,'distance':b})
                                    objetivomacasgroup.sort(key=myFunc)
                                maçasgroupcentre = []
                                for a in objetivomacasgroup:
                                    b = a['a']
                                    maçasgroupcentre.append(b)  

                    body.mover(body.x,body.y)


            for i in range(2):
                update(1)

            #quando as maças forem todas recolhidas proseguimos para a fase seguinte
            while counter == 1:
                update(50)

                #calcula e escolhe o ponto de recolha mais perto
                distrecolha1 = (pontoderecolha.box1centro.getX()-body.centre.getX())**2 + (pontoderecolha.box1centro.getY()-body.centre.getY())**2
                distrecolha2 = (pontoderecolha.box2centro.getX()-body.centre.getX())**2 + (pontoderecolha.box2centro.getY()-body.centre.getY())**2


                if distrecolha1 <= distrecolha2:

                    #direciona-se a ele
                    body.moveobjetive(pontoderecolha.box1centro)
                    #caso o robo fique sem bateria direciona-se para a estação de carregamento
                    body.countbatery(bateria.centro,on)
                    #define o objetivo no desvio de obstáculos
                    objective = pontoderecolha.box1centro
                    if body.bateryactive == 1:
                        objective = bateria.centro

                    #desvia-se dos obstáculos de forma a chegar ao seu objetive da maneira mais rápida
                    body.dodgeeverything(grouparvores,grouppedras,objective) 
                    if body.centre.getY() == pontoderecolha.box1centro.getY() and body.centre.getX() == pontoderecolha.box1centro.getX():
                        #cria maças e recomeça a fase de busca de maças
                        if onfile == 1: #se as maças vierem de um file feicha o programa
                            quitcounter = 1
                        else:
                            quitcounter, maçasgroup, maçasgroupcentre = multiplemaças(win2,grouparvores,grouppedras,file,onfile)
                        counter = 0


                if distrecolha1 > distrecolha2:

                    #direciona-se a ele
                    body.moveobjetive(pontoderecolha.box2centro)
                    #caso o robo fique sem bateria direciona-se para a estação de carregamento
                    body.countbatery(bateria.centro,on)

                    #define o objetivo no desvio de obstáculos
                    objective = pontoderecolha.box2centro
                    if body.bateryactive == 1:
                        objective = bateria.centro

                    #desvia-se dos obstáculos de forma a chegar ao seu objetive da maneira mais rápida
                    body.dodgeeverything(grouparvores,grouppedras,objective)
                    if body.centre.getY() == pontoderecolha.box2centro.getY() and body.centre.getX() == pontoderecolha.box2centro.getX():
                        #cria maças e recomeça a fase de busca de maças
                        if onfile == 1:#se as maças vierem de um file feicha o programa
                            quitcounter = 1
                        else:
                            quitcounter, maçasgroup, maçasgroupcentre = multiplemaças(win2,grouparvores,grouppedras,file,onfile)
                        counter = 0
                #move o robo em relação ás condições todas         
                body.mover(body.x,body.y)

def baseline(win2):

    #criação dos itens comuns em todas as implementações

    #backround
    backround = Image(Point(300,300),"sprites/backround.png")
    backround.draw(win2)

    #bateria
    bateriaponto1 = Point(570,570)
    bateriaponto2 = Point(600,600)
    bateria = baterystation(bateriaponto1,bateriaponto2,win2)

    #pontos de recolha
    pontoderecolha1 = Point(0,570)
    pontoderecolha2 = Point(50,600)
    pontoderecolha3 = Point(550,300)
    pontoderecolha4 = Point(600,330)
    pontoderecolha = Recolha(pontoderecolha1,pontoderecolha2,pontoderecolha3,pontoderecolha4,win2)

    return bateria, pontoderecolha