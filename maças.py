from graphics import * 
from classes import *
def multiplemaças(win2,grouparvores,grouppedras):
        pointstart = Point(540,0)
        pointstart1 = Point(570,30)
        startbutton = butão(win2,pointstart,pointstart1,"start")
        pointquit = Point(570,0)
        pointquit1 = Point(600,30)
        quitbutton = butão(win2,pointquit,pointquit1,"quit")
        quitcounter = 0
        maçasgroup = []
        maçasgroupcentre = []
        text2 = Text(Point(300,450),"clique no ecrã")
        text2.draw(win2)
        macacentro = win2.getMouse()
        text2.undraw()
        macacount = 0
        while macacount == 0:
                checkcounter = 0
                macacentro = win2.getMouse()
                text1 = Text(Point(300,450),"coloque noutro lugar")
                for i in grouparvores:
                    if (macacentro.getX() - i.getX())**2 + (macacentro.getY() - i.getY())**2 <= 40**2:
                        checkcounter = checkcounter + 1
                for i in grouppedras:
                    if i.getX() - 40 < macacentro.getX() <  i.getX() + 40 and  i.getY() - 40 < macacentro.getY() <  i.getY() + 40:
                        checkcounter = checkcounter + 1
                text1.draw(win2)
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
                    if maçasgroupcentre != []:
                        macacount = 1
                    if maçasgroupcentre == []:
                        pass
                elif quitbutton.clicked(macacentro):
                    quitcounter = 1
                    macacount = 1
                else: 
                    maca = Maça(win2,macacentro)
                    maçasgroup.append(maca)
                    maçasgroupcentre.append(maca.centro)
        return quitcounter, maçasgroup, maçasgroupcentre
def moving(win2,grouparvores,grouppedras,body,bateria,pontoderecolha,on):
        counter = 0
        quitcounter, maçasgroup, maçasgroupcentre = multiplemaças(win2,grouparvores,grouppedras)
        while quitcounter == 0:
            for l in maçasgroupcentre:
                counter = 0
                for i in range(2):
                    update(1)
                while counter == 0:
                    update(50)
                    body.moveobjetive(l)
                    body.countbatery(bateria.centro,on)
                    objective = l
                    if body.bateryactive == 1:
                        objective = bateria.centro
                    body.dodgeeverything(grouparvores,grouppedras,objective)
                    if body.centre.getY() == l.getY() and body.centre.getX() == l.getX():
                        counter = 1
                        for p in maçasgroup:
                            if body.centre.getY() == p.centro.getY() and body.centre.getX() == p.centro.getX():
                                p.existnt()
                        for i in range(2):
                            update(1)
                    body.mover(body.x,body.y)
            while counter == 1:
                update(50)
                distrecolha1 = (pontoderecolha.box1centro.getX()-body.centre.getX())**2 + (pontoderecolha.box1centro.getY()-body.centre.getY())**2
                distrecolha2 = (pontoderecolha.box2centro.getX()-body.centre.getX())**2 + (pontoderecolha.box2centro.getY()-body.centre.getY())**2
                if distrecolha1 <= distrecolha2:
                    body.moveobjetive(pontoderecolha.box1centro)
                    body.countbatery(bateria.centro,on)
                    objective = pontoderecolha.box1centro
                    if body.bateryactive == 1:
                        objective = bateria.centro
                    body.dodgeeverything(grouparvores,grouppedras,objective) 
                    if body.centre.getY() == pontoderecolha.box1centro.getY() and body.centre.getX() == pontoderecolha.box1centro.getX():
                        quitcounter, maçasgroup, maçasgroupcentre = multiplemaças(win2,grouparvores,grouppedras)
                        counter = 0
                if distrecolha1 > distrecolha2:
                    body.moveobjetive(pontoderecolha.box2centro)
                    body.countbatery(bateria.centro,on)
                    objective = pontoderecolha.box2centro
                    if body.bateryactive == 1:
                        objective = bateria.centro
                    body.dodgeeverything(grouparvores,grouppedras,objective)
                    if body.centre.getY() == pontoderecolha.box2centro.getY() and body.centre.getX() == pontoderecolha.box2centro.getX():
                        quitcounter, maçasgroup, maçasgroupcentre = multiplemaças(win2,grouparvores,grouppedras)
                        counter = 0
                body.mover(body.x,body.y)
def baseline(win2):
    bateriaponto1 = Point(570,570)
    bateriaponto2 = Point(600,600)
    bateria = baterystation(bateriaponto1,bateriaponto2,win2)
    pontoderecolha1 = Point(0,570)
    pontoderecolha2 = Point(30,600)
    pontoderecolha3 = Point(570,300)
    pontoderecolha4 = Point(600,330)
    pontoderecolha = Recolha(pontoderecolha1,pontoderecolha2,pontoderecolha3,pontoderecolha4,win2)
    return bateria, pontoderecolha