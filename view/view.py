#!/usr/bin/env python
# -*- coding: utf-8 -*-

class View:

    def __init__(self):
        self.start = 'OK'        


    def PrintMenu(self):
        print('############## Lanchonete PySnack ##############')
        print('Escolha a opção desejada . . .\n')
        print('1 - Cadastrar Novo Produto')
        print('2 - Alterar Produto')
        print('3 - Remover Produto')
        print('4 - Voltar ao Menu Principal')
        print('5 - Novo Pedido')
        print('6 - Ver Estatísticas')
        print('7 - Sobre o PySnack')
        print('8 - Contate o Suporte')
        print('9 - Registrar Novo Usuário')
        print('10 - Sair\n')

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