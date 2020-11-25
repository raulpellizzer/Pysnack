#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class View:

    ### Class Constructor
    #
    #
    def __init__(self):
        self.start = 'OK'


    ### Prints the main menu for the application
    #
    # @return   integer
    #
    def PrintMainMenu(self):
        print('\n############## Lanchonete PySnack ##############')
        print('Escolha a opção desejada . . .\n')
        print('1 - Cadastrar Novo Produto')
        print('2 - Alterar Produto')
        print('3 - Remover Produto')
        print('4 - Exibir Menu')
        print('5 - Novo Pedido')
        print('6 - Ver Pedidos')
        print('7 - Sobre o PySnack')
        print('8 - Exportar Pedidos')
        print('9 - Sair\n')

        optionValid = False
        while not(optionValid):
            try:
                option = int(input('Opção: '))
                if option > 0 and option < 11:
                    optionValid = True
                    return option
                else:
                    print('Opção Inválida, digite novamente')

            except:
                print('Opção Inválida, digite novamente')


    ### Prints the login screen
    #
    # @return   integer
    #
    def PrintLoginScreen(self):
        print('\n############## Lanchonete PySnack ##############')
        print('Escolha a opção desejada . . .\n')
        print('1 - Entrar')
        print('2 - Registrar Novo Usuário')

        optionValid = False
        while not(optionValid):
            try:
                option = int(input('Opção: '))
                if option > 0 and option < 3:
                    optionValid = True
                    return option
                else:
                    print('Opção Inválida, digite novamente')

            except:
                print('Opção Inválida, digite novamente')

    ### Request new user credentials
    #
    # @return   object
    #
    def GetNewUserCredentials(self):
        userName        = str(input('Cadastre seu usuário: '))
        password        = str(input('Cadastre sua senha: '))
        confirmPassword = str(input('Confirme sua senha: '))

        data = {
            "userName": userName,
            "password": password,
            "confirmPassword": confirmPassword
        }

        return data

    ### Request user credentials
    #
    # @return   object
    #
    def GetUserCredentials(self):
        userName        = str(input('Entre com seu usuário: '))
        password        = str(input('Entre com sua senha: '))

        data = {
            "userName": userName,
            "password": password
        }

        return data


    ### Prints a message for the user
    #
    # @param   string message - message to be printed
    #
    def PrintMessage(self, message):
        print(message)
        print('\n')


    ### Requests data about the new product from the user
    #
    # @return   object
    #
    def RequestProductData(self):
        productName       = str(input('Entre com o nome do produto: '))
        producDescription = str(input('Breve descrição do produto: '))
        
        optionValid = False
        while not(optionValid):
            try:
                pricePerUnit = float(input('Preço de venda por unidade: '))

                while pricePerUnit <= 0:
                    print('Preço inválido. Digite novamente')
                    pricePerUnit = float(input('Preço de venda por unidade: '))

                optionValid = True
            except:
                optionValid = False
                print('Opção inválida. Entre com um número real.')

        productData = {
            "productName": productName,
            "producDescription": producDescription,
            "pricePerUnit": pricePerUnit
        }

        return productData

    
    ### Print menu itens
    #
    # @param   string menu - menu itens table
    #
    def PrintMenuItens(self, menu):
        print('Cardápio:\n')
        print(menu)


    ### Print order itens
    #
    # @param   string orders - orders itens table
    #
    def PrintOrderItens(self, orders):
        print('Pedidos:\n')
        print(orders)


    ### Requests an ID from the user
    #
    # @return   integer
    #
    def RequestProductID(self):
        optionValid = False
        productId   = -1

        while not(optionValid):
            try:
                print('\n')
                productId = int(input('Entre com o codigo do produto: '))

                if productId > 0:
                    optionValid = True
                else:
                    print('Opção inválida. Entre com um número inteiro positivo.')
            except:
                optionValid = False
                print('Opção inválida. Entre com um número inteiro positivo.')

        return productId


    ### Prints the orders screen
    #
    # @return   integer
    #
    def PrintOrderScreen(self):
        print('\n1 - Adicionar item a sacola')
        print('2 - Ver sacola')
        print('3 - Finalizar pedido')

        optionValid = False
        while not(optionValid):
            try:
                option = int(input('Opção: '))
                if option > 0 and option < 4:
                    optionValid = True
                    return option
                else:
                    print('Opção Inválida, digite novamente')

            except:
                print('Opção Inválida, digite novamente')


    ### Request a quantity for a given product from the user
    #
    # @param   string productName - name of the product
    #
    # @return   integer
    #
    def RequestProductQuantity(self, productName):
        print('Produto selecionado: ' + productName)

        optionValid = False
        while not(optionValid):
            try:
                option = int(input('Quantidade desejada: '))

                if option > 0:
                    optionValid = True
                    return option
                
                else:
                    print('Valor não permitido. Digite novamente')

            except:
                print('Opção Inválida, digite novamente')


    ### Asks for the client name
    #
    # @return   string
    #
    def GetClientName(self):
        clientName = ''

        while clientName == '':
            clientName = str(input('Seu nome? '))
            clientName = clientName.strip()

        return clientName


    ### Asks the client for payment data
    #
    # @param   float total - total value from the order
    #
    # @return   object
    #
    def GetPaymentData(self, total):
        print('\nForma de pagamento:')
        print('1 - Dinheiro')
        print('2 - Cartão')

        optionValid = False
        while not(optionValid):
            try:
                option = int(input('Opção: '))
                if option > 0 and option < 3:
                    optionValid = True

                    if option == 1:
                        amount  = self.GetPaymentAmount()
                        payment = 'Dinheiro'

                    elif option == 2:
                        amount  = total
                        payment = 'Cartão'

                    paymentData = {
                        "amount": amount,
                        "payment": payment
                    }
                    return paymentData

                else:
                    print('Opção Inválida, digite novamente')

            except:
                print('Opção Inválida, digite novamente')


    ### Asks for the amount payed in cash
    #
    # @return   float
    #
    def GetPaymentAmount(self):
        optionValid = False
        while not(optionValid):
            try:
                payment = float(input('Quantia em dinheiro: '))
                optionValid = True

            except:
                print('Opção Inválida, digite novamente')

        return payment