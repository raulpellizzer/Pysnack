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
        self.view.PrintMessage(about)


    ### Initializes the database setup
    #
    #
    def InitializeSetup(self):
        self.model.InitializeTables()


    ### Register User in the database
    #
    # @param   object newCredentials - user credentials
    #
    # @return   boolean
    #
    def RegisterNewUser(self, newCredentials):
        validation = self.model.RegisterNewUser(newCredentials)
        return validation


    ### Authenticates the user when logging in
    #
    # @param   object credentials - user credentials
    #
    # @return   boolean
    #
    def AuthenticateUser(self, credentials):
        auth = self.model.AuthenticateUser(credentials)
        return auth


    ### Creates new product in the database
    #
    # @param   object productData - data about the new product
    #
    # @return   boolean
    #
    def RegisterNewProduct(self, productData):
        result = self.model.RegisterNewProduct(productData)
        return result

    ### Show whats in the menu
    #
    #
    def ShowMenuItens(self):
        menu = self.model.GetMenuItens()
        self.view.PrintMenuItens(menu)


    ### Check if a product exists in the database
    #
    # @param   integer productId - product id
    #
    # @return   boolean
    #
    def CheckProductInDB(self, productId):
        status = self.model.CheckProductInDB(productId)
        return status


    ### Update data about a product
    #
    # @param   integer productId - product id
    # @param   object productData - new data to be updated
    #
    # @return   boolean
    #
    def UpdateProductData(self, productId, productData):
        result = self.model.UpdateProductData(productId, productData)
        return result







controller = Controller()
controller.userLoggedIn = False
controller.InitializeSetup()
controller.PrintLoginScreen()

while not(controller.userLoggedIn):
    if controller.loginOption == 1:

        credentials = controller.view.GetUserCredentials()
        auth = controller.AuthenticateUser(credentials)

        if auth:
            controller.view.PrintMessage('Usuário Autenticado com sucesso!\n')
            controller.userLoggedIn = True
            break
        else:
            controller.view.PrintMessage('Usuário ou senha incorretos.\n')
        
        time.sleep(3)
        controller.PrintLoginScreen()

    elif controller.loginOption == 2:
        newCredentials = controller.view.GetNewUserCredentials()
        validation = controller.RegisterNewUser(newCredentials)

        if validation:
            message = 'Usuário cadastrado com sucesso!'
        else:
            message = 'Não foi possível cadastrar o usuário. Tente um novo nome de usuário.'
        
        controller.view.PrintMessage(message)

        time.sleep(3)
        controller.PrintLoginScreen()




controller.PrintMainMenu()

while controller.menuOption != 9:
    if controller.menuOption == 1:         # Cadastrar Novo Produto

        productData = controller.view.RequestProductData()
        result      = controller.RegisterNewProduct(productData)

        if result:
            message = 'Produto cadastrado com sucesso!'
        else:
            message = 'Ocorreu um erro ao cadastrar o produto. Tente novamente.'

        controller.view.PrintMessage(message)

    elif controller.menuOption == 2:       # Alterar Produto

        controller.ShowMenuItens()
        productId = controller.view.RequestProductID()
        status    = controller.CheckProductInDB(productId) 

        if status:
            productData = controller.view.RequestProductData()
            result      = controller.UpdateProductData(productId, productData)

            if result:
                message = 'Produto alterado com sucesso!'
            else: 
                message = 'Ocorreu um erro ao atualizar o produto. Tente novamente.'

            controller.view.PrintMessage(message)

        else:
            message = 'Produto não localizado!'
            controller.view.PrintMessage(message)

    elif controller.menuOption == 3:       # Remover Produto

        print('You choose option 3 . . .')
        #something here

    elif controller.menuOption == 4:       # Exibir Menu (comidas e bebidas, mostrar itens disponiveis)
        controller.ShowMenuItens()

    elif controller.menuOption == 5:       # Novo Pedido

        print('You choose option 5 . . .')
        #something here

    elif controller.menuOption == 6:       # Ver Estatísticas (?)

        print('You choose option 6 . . .')
        #something here

    elif controller.menuOption == 7:       # Sobre
        controller.PrintAboutApp()

    elif controller.menuOption == 8:       # Contate o Suporte

        print('You choose option 8 . . .')
        #something here

    elif controller.menuOption == 9:       # Sair
        break

    time.sleep(5)
    controller.PrintMainMenu()