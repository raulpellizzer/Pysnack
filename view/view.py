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
        while(not(optionValid)):
            try:
                option = int(input('Opção: '))
                if (option > 0 and option < 11):
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
        while(not(optionValid)):
            try:
                option = int(input('Opção: '))
                if (option > 0 and option < 4):
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
        os.system('cls')
        userName        = str(input('Cadastre seu usuário: '))
        password        = str(input('Cadastre sua senha: '))
        confirmPassword = str(input('Confirme sua senha: '))

        data = {
            "userName": userName,
            "password": password,
            "confirmPassword": confirmPassword
        }

        return data


    ### Prints information about the app
    #
    # @param   string about - the text about the application
    #
    def PrintAboutApp(self, about):
        print(about)
        print('\n\n')