#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
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


    ### Deletes a product
    #
    # @param   integer productId - product id
    #
    # @return   boolean
    #
    def DeleteProduct(self, productId):
        result = self.model.DeleteProduct(productId)
        return result


    ### Retrieve data about a given product
    #
    # @param   integer productId - product id
    #
    # @return   object
    #
    def GetProductDataById(self, productId):
        productData = self.model.GetProductDataById(productId)
        return productData


    ### Format orders data into a table format
    #
    # @param   array fullOrder - orders data
    #
    # @return   string
    #
    def FormatOrderToTable(self, fullOrder):
        formattedOrder = self.model.FormatOrderToTable(fullOrder)
        return formattedOrder


    ### Calculates the total order amount
    #
    # @param   array fullOrder - orders data
    #
    # @return   float
    #
    def CalculateOrderValue(self, fullOrder):
        totalValue = self.model.CalculateOrderValue(fullOrder)
        return totalValue


    ### Formats the order itens into a string for the database
    #
    # @param   array fullOrder - orders data
    #
    # @return   string
    #
    def StringfyOrderItens(self, fullOrder):
        orderString = self.model.StringfyOrderItens(fullOrder)
        return orderString


    ### Register the sale (order) in the database
    #
    # @param   string clientName - client name
    # @param   string orderItens - order itens
    # @param   float total - total amount of the order
    # @param   string payment - payment method
    # @param   float exchange - order exchange
    # @param   string orderDate - date of the order
    #
    # @return   boolean
    #
    def RegisterSale(self, clientName, orderItens, total, payment, exchange, orderDate):
        result = self.model.RegisterSale(clientName, orderItens, total, payment, exchange, orderDate)
        return result


    ### Show orders done
    #
    #
    def ShowOrderItens(self):
        orders = self.model.GetOrderItens()
        self.view.PrintOrderItens(orders)


    ### Generates the ticket for the user
    #
    # @param   string clientName - client name
    # @param   string orderItens - order itens
    # @param   float total - total amount of the order
    # @param   object payment - data about payment method
    # @param   float exchange - order exchange
    # @param   string orderDate - date of the order
    #
    # @return   string
    #
    def GenerateTicket(self, clientName, orderItens, total, paymentData, exchange, orderDate):
        ticket = self.model.GenerateTicket(clientName, orderItens, total, paymentData, exchange, orderDate)
        return ticket







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

    # Register New Product
    if controller.menuOption == 1:
        productData = controller.view.RequestProductData()
        result      = controller.RegisterNewProduct(productData)

        if result:
            message = 'Produto cadastrado com sucesso!'
        else:
            message = 'Ocorreu um erro ao cadastrar o produto. Tente novamente.'

        controller.view.PrintMessage(message)

    # Update Product
    elif controller.menuOption == 2:
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

    # Remove Product
    elif controller.menuOption == 3:
        controller.ShowMenuItens()
        productId = controller.view.RequestProductID()
        status    = controller.CheckProductInDB(productId) 

        if status:
            result = controller.DeleteProduct(productId)

            if result:
                message = 'Produto deletado com sucesso!'
            else: 
                message = 'Ocorreu um erro ao deletar o produto. Tente novamente.'

            controller.view.PrintMessage(message)

        else:
            message = 'Produto não localizado!'
            controller.view.PrintMessage(message)

    # Show Menu Itens
    elif controller.menuOption == 4:
        controller.ShowMenuItens()

    # New Order
    elif controller.menuOption == 5:
        fullOrder = []

        controller.ShowMenuItens()
        action = controller.view.PrintOrderScreen()

        while action != 3:

            # Add new item to the order
            if action == 1:
                productId = controller.view.RequestProductID()
                status    = controller.CheckProductInDB(productId)

                if status:
                    productData = controller.GetProductDataById(productId)
                    productName = productData['productName']

                    if productName != '':
                        quantity = controller.view.RequestProductQuantity(productName)

                        item = {
                            "productId": productId,
                            "productName": productName,
                            "quantity": quantity,
                            "unitPrice": productData['unitPrice']
                        }
                        
                        fullOrder.append(item)
                        print('Item adicionado a sacola!\n')
                        item = {}

                    else:
                        print('Ocorreu um erro inesperado. Tente novamente.')

                else:
                    print('Produto não localizado')

            # Check current order so far
            elif action == 2:

                if len(fullOrder) > 0:
                    formattedOrder = controller.FormatOrderToTable(fullOrder)
                    print('Sacola:\n')
                    print(formattedOrder)
                else:
                    print('Nenhum item foi adicionado até o momento.\n')

            action = controller.view.PrintOrderScreen()

        # Place order
        if len(fullOrder) > 0:
            clientName  = controller.view.GetClientName()
            total       = controller.CalculateOrderValue(fullOrder)
            paymentData = controller.view.GetPaymentData(total)
            exchange    = float(paymentData['amount']) - float(total)
            exchange    = round(exchange, 2)
            orderDate   = datetime.datetime.now()
            orderItens  = controller.StringfyOrderItens(fullOrder)
            result      = controller.RegisterSale(clientName, orderItens, total, paymentData['payment'], exchange, orderDate)

            if result:
                message = 'Pedido efetuado com sucesso! Cupom fiscal abaixo:\n'
                controller.view.PrintMessage(message)
                ticket = controller.GenerateTicket(clientName, orderItens, total, paymentData, exchange, orderDate)
                controller.view.PrintMessage(ticket)

            else:
                message = 'Ocorreu um erro nesta venda. Tente novamente.\n'
                controller.view.PrintMessage(message)

        else:
            print('Voltando ao menu principal ...\n')

    # See Orders
    elif controller.menuOption == 6:
        controller.ShowOrderItens()

    # About Pysnack
    elif controller.menuOption == 7:
        controller.PrintAboutApp()

    elif controller.menuOption == 8:       # Contate o Suporte

        print('You choose option 8 . . .')
        #something here

    elif controller.menuOption == 9:
        break

    time.sleep(5)
    controller.PrintMainMenu()