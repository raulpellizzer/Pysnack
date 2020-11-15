#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
import os

sys.path.append('../view')
sys.path.append('../model')

from view import View
from model import Model

class Controller:

    ### Class Constructor
    #
    def __init__(self):
        self.view = View()
        self.model = Model()


    ### Prints the main menu for the application
    #
    #
    def PrintMenu(self):
        # os.system('cls')
        self.menuOption = self.view.PrintMenu()


    ### Prints information about the app
    #
    #
    def PrintAboutApp(self):
        about = self.model.PrintAboutApp()
        self.view.PrintAboutApp(about)


    ### FINISH DESCRIPTION
    #
    # @param   type var - description
    #
    # @return   type 
    #
    def InitializeSetup(self):
        self.model.InitializeTables()










controller = Controller()
controller.InitializeSetup()

controller.PrintMenu()
# controller.menuOption = 10

while (controller.menuOption != 10):
    if (controller.menuOption == 1):
        print('You choose option 1 . . .')   # Cadastrar Novo Produto
        #something here

    elif (controller.menuOption == 2):
        print('You choose option 2 . . .')   # Alterar Produto
        #something here

    elif (controller.menuOption == 3):
        print('You choose option 3 . . .')   # Remover Produto
        #something here

    elif (controller.menuOption == 4):
        print('You choose option 4 . . .')   # Exibir Menu (comidas e bebidas, mostrar itens disponiveis)
        controller.PrintMenu()

    elif (controller.menuOption == 5):
        print('You choose option 5 . . .')   # Novo Pedido
        #something here

    elif (controller.menuOption == 6):
        print('You choose option 6 . . .')   # Ver Estatísticas
        #something here

    elif (controller.menuOption == 7):
        controller.PrintAboutApp()

    elif (controller.menuOption == 8):
        print('You choose option 8 . . .')   # Contate o Suporte
        #something here

    elif (controller.menuOption == 9):
        print('You choose option 9 . . .')   # Registrar Novo Usuário
        #something here

    elif (controller.menuOption == 10):
        print('You choose option 10 . . .')   # Sair
        break
        #something here

    time.sleep(4)
    controller.PrintMenu()