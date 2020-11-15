#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error
import os

class Model:

    ### Class Constructor
    #
    def __init__(self):
        self.start = 'OK'
        self.dbFile = os.getcwd() + '\database\pysnackdb.db'


    ### Prints information about the app
    #
    # @return   string
    #
    def PrintAboutApp(self):
        about = 'Este aplicativo foi desenvolvido para a disciplina de Tópicos Especiais em Informática '
        about = about + 'pelos alunos Carlos Matheus e Raul Pellizzer no ano de 2020.\nEste aplicativo tem como '
        about = about + 'objetivo auxiliar uma lanchonete a gerenciar seus pedidos.'
        return about


    ### Initializes tables for the app
    #
    #
    def InitializeTables(self):
        self.conn = self.CreateDBConnection(self.dbFile)
        # Create tables here
        self.conn.close()


    ### Initializes tables for the app
    #
    # @param   string dbFile - the path for the database file
    #
    # @return   DB connection object 
    #
    def CreateDBConnection(self, dbFile):
        conn = None

        try:
            conn = sqlite3.connect(dbFile)
            return conn

        except Error as err:
            print(err)

        return conn


