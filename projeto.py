from graphics import * 
from classes import *

def implementação1():
    win = GraphWin("Projeto Ai implementação1", 600, 600)
    win.setCoords(0, 0, 600, 600)
    win.setBackground("chartreuse3")
    a = Point (300, 300)
    arvore = Arvore(win,a,30)
    pontoderecolha1 = Point(0,570)
    pontoderecolha2 = Point(30,600)
    pontoderecolha3 = Point(570,300)
    pontoderecolha4 = Point(600,330)
    pontoderecolha = Recolha(pontoderecolha1,pontoderecolha2,pontoderecolha3,pontoderecolha4,win)
    counter = 0
    body = Robot(win,10,10)
    pointquit = Point(570,0)
    pointquit1 = Point(600,30)
    quitbutton = butão(win,pointquit,pointquit1,"quit")
    checkcounter = 1
    macacentro = win.getMouse()
    text1 = Text(Point(300,450),"coloque noutro lugar")
    if (macacentro.getX() - arvore.centre.getX())**2 + (macacentro.getY() - arvore.centre.getY())**2 > 40**2:
        checkcounter = 0 
    text1.draw(win)
    while checkcounter > 0:
        macacentro = win.getMouse()
        text1.undraw()
        text1 = Text(Point(300,450),"coloque noutro lugar")
        if (macacentro.getX() - arvore.centre.getX())**2 + (macacentro.getY() - arvore.centre.getY())**2 > 40**2:
            checkcounter = 0
        
        text1.draw(win)
    text1.undraw()

    maca = Maça(win,macacentro)
    while not quitbutton.clicked(macacentro):
        while counter == 0:
            update(30)
            body.moveobjetive(maca.centro)
            body.movearvore(arvore.centre,maca.centro)    
            if body.centre.getY() == maca.centro.getY() and body.centre.getX() == maca.centro.getX():
                counter = 1
                maca.existnt()
            
            body.mover(body.x,body.y)
        while counter == 1:
            update(30)
            distrecolha1 = (pontoderecolha.box1centro.getX()-body.centre.getX())**2 + (pontoderecolha.box1centro.getY()-body.centre.getY())**2
            distrecolha2 = (pontoderecolha.box2centro.getX()-body.centre.getX())**2 + (pontoderecolha.box2centro.getY()-body.centre.getY())**2
            if distrecolha1 <= distrecolha2:
                body.moveobjetive(pontoderecolha.box1centro)
                body.movearvore(arvore.centre,pontoderecolha.box1centro) 
                if body.centre.getY() == pontoderecolha.box1centro.getY() and body.centre.getX() == pontoderecolha.box1centro.getX():
                    macacentro = win.getMouse()
                    maca = Maça(win,macacentro)
                    counter = 0
            if distrecolha1 > distrecolha2:
                body.moveobjetive(pontoderecolha.box2centro)
                body.movearvore(arvore.centre,pontoderecolha.box2centro) 
                if body.centre.getY() == pontoderecolha.box2centro.getY() and body.centre.getX() == pontoderecolha.box2centro.getX():
                    macacentro = win.getMouse()
                    maca = Maça(win,macacentro)
                    counter = 0
            body.mover(body.x,body.y)
    win.close()

def implementação2():
        win2 = GraphWin("Projeto Ai implementação2", 600, 600)
        win2.setCoords(0, 0, 600, 600)
        win2.setBackground("chartreuse3")
        a = Point (300, 300)
        b = Point (450, 450)
        c = Point (150, 150)
        pontopedra1 = Point(120,420)
        pontopedra2 = Point(420,120)
        pontopedra12 = Point(180,480)
        pontopedra22 = Point(480,180)
        bateriaponto1 = Point(570,570)
        bateriaponto2 = Point(600,600)
        bateria = baterystation(bateriaponto1,bateriaponto2,win2)
        pedra1 = Obstaculo(pontopedra1,pontopedra12,win2)
        pedra2 = Obstaculo(pontopedra2,pontopedra22,win2)
        arvore2 = Arvore(win2,c,30)
        arvore3 = Arvore(win2,b,30)
        arvore = Arvore(win2,a,30)
        grouppedras = []
        grouparvores = []
        for i in [arvore.centre,arvore2.centre,arvore3.centre]:
            grouparvores.append(i)
        for i in [pedra1.obscentro,pedra2.obscentro]:
            grouppedras.append(i)
        pontoderecolha1 = Point(0,570)
        pontoderecolha2 = Point(30,600)
        pontoderecolha3 = Point(570,300)
        pontoderecolha4 = Point(600,330)
        pontoderecolha = Recolha(pontoderecolha1,pontoderecolha2,pontoderecolha3,pontoderecolha4,win2)
        counter = 0
        body = Robot(win2,10,10)
        pointquit = Point(570,0)
        pointquit1 = Point(600,30)
        quitbutton = butão(win2,pointquit,pointquit1,"quit")
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

        maca = Maça(win2,macacentro)
        while  not quitbutton.clicked(macacentro):
            while counter == 0:
                update(30)
                body.moveobjetive(maca.centro)
                body.countbatery(bateria.centro)
                objective = maca.centro
                if body.bateryactive == 1:
                    objective = bateria.centro
                body.movearvore(arvore.centre,objective)    
                body.movearvore(arvore2.centre,objective)   
                body.movearvore(arvore3.centre,objective)  
                body.movimentoobst(pedra1.obscentro,objective) 
                body.movimentoobst(pedra2.obscentro,objective)
                if body.centre.getY() == maca.centro.getY() and body.centre.getX() == maca.centro.getX():
                    counter = 1
                    maca.existnt()
                
                body.mover(body.x,body.y)
            while counter == 1:
                update(30)
                distrecolha1 = (pontoderecolha.box1centro.getX()-body.centre.getX())**2 + (pontoderecolha.box1centro.getY()-body.centre.getY())**2
                distrecolha2 = (pontoderecolha.box2centro.getX()-body.centre.getX())**2 + (pontoderecolha.box2centro.getY()-body.centre.getY())**2
                if distrecolha1 <= distrecolha2:
                    body.moveobjetive(pontoderecolha.box1centro)
                    body.countbatery(bateria.centro)
                    objective = pontoderecolha.box1centro
                    if body.bateryactive == 1:
                        objective = bateria.centro
                    body.movearvore(arvore.centre,objective) 
                    body.movearvore(arvore2.centre,objective)   
                    body.movearvore(arvore3.centre,objective)  
                    body.movimentoobst(pedra1.obscentro,objective) 
                    body.movimentoobst(pedra2.obscentro,objective) 
                    if body.centre.getY() == pontoderecolha.box1centro.getY() and body.centre.getX() == pontoderecolha.box1centro.getX():
                        macacentro = win2.getMouse()
                        maca = Maça(win2,macacentro)
                        counter = 0
                if distrecolha1 > distrecolha2:
                    body.moveobjetive(pontoderecolha.box2centro)
                    body.countbatery(bateria.centro)
                    objective = pontoderecolha.box2centro
                    if body.bateryactive == 1:
                        objective = bateria.centro
                    body.movearvore(arvore.centre,objective) 
                    body.movearvore(arvore2.centre,objective)   
                    body.movearvore(arvore3.centre,objective) 
                    body.movimentoobst(pedra1.obscentro,objective) 
                    body.movimentoobst(pedra2.obscentro,objective)  
                    if body.centre.getY() == pontoderecolha.box2centro.getY() and body.centre.getX() == pontoderecolha.box2centro.getX():
                        macacentro = win2.getMouse()
                        maca = Maça(win2,macacentro)
                        counter = 0
                body.mover(body.x,body.y)
        win2.close()
def implementação3():
        win2 = GraphWin("Projeto Ai implementação3", 600, 600)
        win2.setCoords(0, 0, 600, 600)
        win2.setBackground("chartreuse3")
        bateriaponto1 = Point(570,570)
        bateriaponto2 = Point(600,600)
        bateria = baterystation(bateriaponto1,bateriaponto2,win2)
        pontoderecolha1 = Point(0,570)
        pontoderecolha2 = Point(30,600)
        pontoderecolha3 = Point(570,300)
        pontoderecolha4 = Point(600,330)
        pontoderecolha = Recolha(pontoderecolha1,pontoderecolha2,pontoderecolha3,pontoderecolha4,win2)
        counter = 0
        body = Robot(win2,10,10)
        body.random(4)
        for i in body.obstgrouppedras:
            thex = i.getX() -30
            they = i.getY() -30
            the1x = i.getX() +30
            the1y = i.getY() +30
            i = Obstaculo(Point(thex,they),Point(the1x,the1y),win2)
        for a in body.obstgrouparvores:
            a = Arvore(win2,a,30)
        pointquit = Point(570,0)
        pointquit1 = Point(600,30)
        quitbutton = butão(win2,pointquit,pointquit1,"quit")
        checkcounter = 0
        macacentro = win2.getMouse()
        text1 = Text(Point(300,450),"coloque noutro lugar")
        for i in body.obstgrouparvores:
            if (macacentro.getX() - i.getX())**2 + (macacentro.getY() - i.getY())**2 <= 40**2:
                checkcounter = checkcounter + 1
        for i in body.obstgrouppedras:
            if i.getX() - 40 < macacentro.getX() <  i.getX() + 40 and  i.getY() - 40 < macacentro.getY() <  i.getY() + 40:
                checkcounter = checkcounter + 1
        text1.draw(win2)
        while checkcounter > 0:
            macacentro = win2.getMouse()
            text1.undraw()
            text1 = Text(Point(300,450),"coloque noutro lugar")
            checkcounter = 0
            for i in body.obstgrouparvores:
                if (macacentro.getX() - i.getX())**2 + (macacentro.getY() - i.getY())**2 <= 40**2:
                    checkcounter = checkcounter + 1
            for i in body.obstgrouppedras:
                if i.getX() - 40 < macacentro.getX() <  i.getX() + 40 and  i.getY() - 40 < macacentro.getY() <  i.getY() + 40:
                    checkcounter = checkcounter + 1
            text1.draw(win2)
        text1.undraw()
        maca = Maça(win2,macacentro)
        while  not quitbutton.clicked(macacentro):
            while counter == 0:
                update(30)
                body.moveobjetive(maca.centro)
                body.countbatery(bateria.centro) 
                objective = maca.centro
                if body.bateryactive == 1:
                    objective = bateria.centro
                for e in body.obstgrouppedras:
                    body.movimentoobst(e,objective)
                for d in body.obstgrouparvores:
                    body.movearvore(d,objective)
                if body.centre.getY() == maca.centro.getY() and body.centre.getX() == maca.centro.getX():
                    counter = 1
                    maca.existnt()
                
                body.mover(body.x,body.y)
            while counter == 1:
                update(30)
                distrecolha1 = (pontoderecolha.box1centro.getX()-body.centre.getX())**2 + (pontoderecolha.box1centro.getY()-body.centre.getY())**2
                distrecolha2 = (pontoderecolha.box2centro.getX()-body.centre.getX())**2 + (pontoderecolha.box2centro.getY()-body.centre.getY())**2
                if distrecolha1 <= distrecolha2:
                    body.moveobjetive(pontoderecolha.box1centro)
                    body.countbatery(bateria.centro) 
                    objective = pontoderecolha.box1centro
                    if body.bateryactive == 1:
                        objective = bateria.centro
                    for g in body.obstgrouppedras:
                        body.movimentoobst(g,objective)
                    for h in body.obstgrouparvores:
                        body.movearvore(h,objective)
                    if body.centre.getY() == pontoderecolha.box1centro.getY() and body.centre.getX() == pontoderecolha.box1centro.getX():
                        macacentro = win2.getMouse()
                        maca = Maça(win2,macacentro)
                        counter = 0
                if distrecolha1 > distrecolha2:
                    body.moveobjetive(pontoderecolha.box2centro)
                    body.countbatery(bateria.centro)
                    objective = pontoderecolha.box2centro
                    if body.bateryactive == 1:
                        objective = bateria.centro
                    for j in body.obstgrouppedras:
                        body.movimentoobst(j,objective)
                    for k in body.obstgrouparvores:
                        body.movearvore(k,objective)
                    if body.centre.getY() == pontoderecolha.box2centro.getY() and body.centre.getX() == pontoderecolha.box2centro.getX():
                        macacentro = win2.getMouse()
                        maca = Maça(win2,macacentro)
                        counter = 0
                body.mover(body.x,body.y) 
        win2.close()
def implementação4():
        win2 = GraphWin("Projeto Ai implementação4", 600, 600)
        win2.setCoords(0, 0, 600, 600)
        win2.setBackground("chartreuse3")
        bateriaponto1 = Point(570,570)
        bateriaponto2 = Point(600,600)
        bateria = baterystation(bateriaponto1,bateriaponto2,win2)
        pontoderecolha1 = Point(0,570)
        pontoderecolha2 = Point(30,600)
        pontoderecolha3 = Point(570,300)
        pontoderecolha4 = Point(600,330)
        pontoderecolha = Recolha(pontoderecolha1,pontoderecolha2,pontoderecolha3,pontoderecolha4,win2)
        counter = 0
        body = Robot(win2,10,10)
        file = open("fileprojeto.txt","r")
        body.file(file)
        for i in body.obstgrouppedras:
            thex = i.getX() -30
            they = i.getY() -30
            the1x = i.getX() +30
            the1y = i.getY() +30
            i = Obstaculo(Point(thex,they),Point(the1x,the1y),win2)
        for a in body.obstgrouparvores:
            a = Arvore(win2,a,30)
        pointquit = Point(570,0)
        pointquit1 = Point(600,30)
        quitbutton = butão(win2,pointquit,pointquit1,"quit")
        checkcounter = 0
        macacentro = win2.getMouse()
        text1 = Text(Point(300,450),"coloque noutro lugar")
        for i in body.obstgrouparvores:
            if (macacentro.getX() - i.getX())**2 + (macacentro.getY() - i.getY())**2 <= 40**2:
                checkcounter = checkcounter + 1
        for i in body.obstgrouppedras:
            if i.getX() - 40 < macacentro.getX() <  i.getX() + 40 and  i.getY() - 40 < macacentro.getY() <  i.getY() + 40:
                checkcounter = checkcounter + 1
        text1.draw(win2)
        while checkcounter > 0:
            macacentro = win2.getMouse()
            text1.undraw()
            text1 = Text(Point(300,450),"coloque noutro lugar")
            checkcounter = 0
            for i in body.obstgrouparvores:
                if (macacentro.getX() - i.getX())**2 + (macacentro.getY() - i.getY())**2 <= 40**2:
                    checkcounter = checkcounter + 1
            for i in body.obstgrouppedras:
                if i.getX() - 40 < macacentro.getX() <  i.getX() + 40 and  i.getY() - 40 < macacentro.getY() <  i.getY() + 40:
                    checkcounter = checkcounter + 1
            text1.draw(win2)
        text1.undraw()
        maca = Maça(win2,macacentro)
        while  not quitbutton.clicked(macacentro):
            while counter == 0:
                update(30)
                body.moveobjetive(maca.centro)
                body.countbatery(bateria.centro) 
                objective = maca.centro
                if body.bateryactive == 1:
                    objective = bateria.centro
                for e in body.obstgrouppedras:
                    body.movimentoobst(e,objective)
                for d in body.obstgrouparvores:
                    body.movearvore(d,objective)
                if body.centre.getY() == maca.centro.getY() and body.centre.getX() == maca.centro.getX():
                    counter = 1
                    maca.existnt()
                
                body.mover(body.x,body.y)
            while counter == 1:
                update(30)
                distrecolha1 = (pontoderecolha.box1centro.getX()-body.centre.getX())**2 + (pontoderecolha.box1centro.getY()-body.centre.getY())**2
                distrecolha2 = (pontoderecolha.box2centro.getX()-body.centre.getX())**2 + (pontoderecolha.box2centro.getY()-body.centre.getY())**2
                if distrecolha1 <= distrecolha2:
                    body.moveobjetive(pontoderecolha.box1centro)
                    body.countbatery(bateria.centro) 
                    objective = pontoderecolha.box1centro
                    if body.bateryactive == 1:
                        objective = bateria.centro
                    for g in body.obstgrouppedras:
                        body.movimentoobst(g,objective)
                    for h in body.obstgrouparvores:
                        body.movearvore(h,objective)
                    if body.centre.getY() == pontoderecolha.box1centro.getY() and body.centre.getX() == pontoderecolha.box1centro.getX():
                        macacentro = win2.getMouse()
                        maca = Maça(win2,macacentro)
                        counter = 0
                if distrecolha1 > distrecolha2:
                    body.moveobjetive(pontoderecolha.box2centro)
                    body.countbatery(bateria.centro)
                    objective = pontoderecolha.box2centro
                    if body.bateryactive == 1:
                        objective = bateria.centro
                    for j in body.obstgrouppedras:
                        body.movimentoobst(j,objective)
                    for k in body.obstgrouparvores:
                        body.movearvore(k,objective)
                    if body.centre.getY() == pontoderecolha.box2centro.getY() and body.centre.getX() == pontoderecolha.box2centro.getX():
                        macacentro = win2.getMouse()
                        maca = Maça(win2,macacentro)
                        counter = 0
                body.mover(body.x,body.y) 
        win2.close()
def menu():
    win1 = GraphWin("Projeto Ai Menu", 600, 600)
    win1.setCoords(0, 0, 600, 600)
    point1 = Point(30,30)
    point2 = Point(170,70)
    point3 = Point( 200,30)
    point4 = Point(350,70)
    point5 = Point( 380,30)
    point6 = Point(520,70)
    point7 = Point( 230,130)
    point8 = Point(370,170)
    implementacao1 = butão(win1,point1,point2,"implementação 1")
    implementacao2 = butão(win1,point3,point4,"implementação 2")
    implementacao3 = butão(win1,point5,point6,"implementação 3")
    implementacao4 = butão(win1,point7,point8,"implementação 4")
    while True:
        click = win1.getMouse()
        if implementacao1.clicked(click):
            implementação1()
        if implementacao2.clicked(click):
            implementação2()
        if implementacao3.clicked(click):
            implementação3()
        if implementacao4.clicked(click):
            implementação4()
menu()
#somrthing