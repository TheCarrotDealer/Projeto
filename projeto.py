# Projeto feito pelo grupo 69
# 102680 Luís Alberto Canha Abreu Gomes Gonçalves
# 103545 Rúben Nelson da Silva Vieira Alves
from graphics import * 
from classes import *
from random import *
from outrasclasses import *
from implementacao1 import *
from implementacao2 import *
from implementacao4 import *
from implementacao3 import *
from implementacao41 import *
def menu():

    #cria a janela
    win1 = GraphWin("Projeto Ai Menu", 1000, 550)
    win1.setCoords(0, 0, 1000, 550)

    #dá setup ao backround
    menubackround = Image(Point(500,275),"sprites/menubackround.png")
    menubackround.draw(win1)
    title = Image(Point(200,500),"sprites/title.png")
    title.draw(win1)

    #cria o butão easteregg localizado na maça no canto superior esquerdo
    buttoneasteregg = butão(win1,Point(230,480),Point(250,505)," ")
    red = Rectangle(Point(230,480),Point(250,505))
    red.setOutline("red")
    red.setFill("red")
    red.draw(win1)
    
    #cria o resto dos butões
    quitbutton = butão(win1,Point(830,30),Point(970,70),"Quit")
    implementacao1 = butão(win1,Point(830,475),Point(970,525),"Implementação 1")
    implementacao2 = butão(win1,Point( 830,400),Point(970,450),"Implementação 2")
    implementacao3 = butão(win1,Point( 830,325),Point(970,375),"Implementação 3")
    implementacao4 = butão(win1,Point( 830,250),Point(970,300),"Implementação 4")
    implementacao41 = butão(win1,Point( 830,175),Point(970,225),"Implementação 4.1")

    while True:
        click = win1.getMouse()

        #ativa a função easter egg
        if buttoneasteregg.clicked(click):

            #cria um ponto random (fora dos butões)
            
            funny = 0
            while funny==0:
                funyx = randrange(10,990)
                funyy = randrange(540)
                if 810 < funyx < 985:
                    if 23 < funyy < 77 or 253 < funyy < 307 or 328 < funyy < 382 or 403 < funyy < 457 or 468 < funyy < 532 or 170 < funyy < 230:
                        funny = 0
                    else:
                        funny = 1
                else:
                     funny = 1
                
            #transforma esse ponto em um texto a dizer "apple"
            a= Text(Point(funyx,funyy),"apple")
            a.draw(win1)

        #cada butão ativa a implementação designada 
        if implementacao1.clicked(click):
            win1.close()
            implementação1()
            menu()

        if implementacao2.clicked(click):
            win1.close()
            implementação2()
            menu()

        if implementacao3.clicked(click):
            win1.close()
            implementação3()
            menu()

        if implementacao4.clicked(click):
            win1.close()
            implementação4()
            menu()
        
        if implementacao41.clicked(click):
            win1.close()
            implementação41()
            menu()

        #fecha a janela
        if quitbutton.clicked(click):
            break
    win1.close()

menu()