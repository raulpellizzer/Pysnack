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
        self.view  = View()
        self.model = Model()


    ### Prints the main menu for the application
    #
    #
    def PrintMainMenu(self):
        # os.system('cls')
        self.menuOption = self.view.PrintMainMenu()


    ### Prints the main menu for the application
    #
    #
    def PrintLoginScreen(self):
        # os.system('cls')
        self.loginOption = self.view.PrintLoginScreen()


    ### Prints information about the app
    #
    #
    def PrintAboutApp(self):
        about = self.model.PrintAboutApp()
        self.view.PrintAboutApp(about)


    ### Initializes the database setup
    #
    #
    def InitializeSetup(self):
        self.model.InitializeTables()

    ### Register a new user into the application
    #
    #
    def RegisterNewUser(self, newCredentials):
        validation = self.model.RegisterNewUser(newCredentials)

        if (validation):
            message = 'Usuário cadastrado com sucesso!'
        else:
            message = 'Não foi possível cadastrar o usuário. Tente um novo nome de usuário.'
        
        self.view.PrintMessage(message)







controller = Controller()
controller.userLoggedIn = False
controller.InitializeSetup()

# Login/Register screen here
controller.PrintLoginScreen()
while (not(controller.userLoggedIn)):
    if (controller.loginOption == 1):
        print('You choose option 1 . . .')   # Entrar


        controller.userLoggedIn = True
        #something here

    elif (controller.loginOption == 2):      # Registrar Novo Usuário
        newCredentials = controller.view.GetNewUserCredentials()
        controller.RegisterNewUser(newCredentials)
        time.sleep(5)
        controller.PrintLoginScreen()




controller.PrintMainMenu()
# controller.menuOption = 9

while (controller.menuOption != 9):
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
        controller.PrintMainMenu()

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
        print('You choose option 9 . . .')   # Sair
        break

    time.sleep(4)
    controller.PrintMainMenu()