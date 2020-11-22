#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class View:

    ### Class Constructor
    #
    def __init__(self):
        self.start = 'OK'


    ### Prints the main menu for the application
    #
    # @return   integer
    #
    def PrintMainMenu(self):
        print('############## Lanchonete PySnack ##############')
        print('Escolha a opção desejada . . .\n')
        print('1 - Cadastrar Novo Produto')
        print('2 - Alterar Produto')
        print('3 - Remover Produto')
        print('4 - Exibir Menu')
        print('5 - Novo Pedido')
        print('6 - Ver Estatísticas')
        print('7 - Sobre o PySnack')
        print('8 - Contate o Suporte')
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
        print('############## Lanchonete PySnack ##############')
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
        # os.system('cls')
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
        # os.system('cls')
        userName        = str(input('Entre com seu usuário: '))
        password        = str(input('Entre com sua senha: '))

        data = {
            "userName": userName,
            "password": password
        }

        return data


    ### Prints a message for the user
    #
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
    #
    def PrintMenuItens(self, menu):
        print('Cardápio:\n')
        print(menu)


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