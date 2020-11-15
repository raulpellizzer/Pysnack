#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # Example of bcrypt usage
# password = "MinhaSenha123"
# hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
# print(hashed)

import sqlite3
import bcrypt
from sqlite3 import Error
import os

class Model:

    ### Class Constructor
    #
    def __init__(self):
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

        if self.conn is not None:
            self.CreateTable('users')
            self.conn.close()

            # self.CreateTable('products') # implement


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

    ### Creates the specified table in the database
    #
    # @param   string table - type of table to be created
    #
    def CreateTable(self, table):
        sqlUsers = """ CREATE TABLE IF NOT EXISTS Users (
                            name text NOT NULL,
                            password text NOT NULL
                        ); """

        # sqlProducts = (to be implemented)

        if (table == 'users'):
            try:
                c = self.conn.cursor()
                c.execute(sqlUsers)
            except Error as err:
                print(err)
        else:
            nothing = '' # (to be implemented - sqlProducts)