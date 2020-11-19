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


    ### Register User in the database
    #
    # @param   object newCredentials - user credentials
    #
    # @return   boolean
    #
    def RegisterNewUser(self, newCredentials):
        registerValidation = False
        validation         = self.ValidateCredentials(newCredentials)
        
        if (validation):
            userValidation = self.CheckUserInDB(newCredentials['userName'])

            if (userValidation == False):
                registerValidation = self.RegisterUser(newCredentials)

        return registerValidation


    ### Check if the credentials are valid
    #
    # @param   object newCredentials - user credentials
    #
    # @return   boolean
    #
    def ValidateCredentials(self, newCredentials):
        validation = False

        if (
            newCredentials['userName'] != '' and newCredentials['password'] != '' and newCredentials['confirmPassword'] != ''
            and len(newCredentials['userName']) >= 5 and len(newCredentials['password']) >= 5
            and newCredentials['password'] == newCredentials['confirmPassword']
        ):
            validation = True

        return validation


    ### Check if the user already exists in the database
    #
    # @param   string userName - username
    #
    # @return   boolean
    #
    def CheckUserInDB(self, userName):
        conn = self.CreateDBConnection(self.dbFile)

        if conn is not None:
            cur = conn.cursor()
            cur.execute("SELECT name FROM Users")
            rows = cur.fetchall()
            conn.close()

            for row in rows:
                if (row[0] == userName):
                    return True

            return False


    ### Inserts new user to the database
    #
    # @param   object newCredentials - user credentials
    #
    # @return   boolean
    #
    def RegisterUser(self, newCredentials):

        userName          = newCredentials['userName']
        password          = newCredentials['password']
        encryptedPassword = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        sql = ''' INSERT INTO Users (name, password) VALUES ('%s', "%s") ''' % (userName, encryptedPassword) 

        conn = self.CreateDBConnection(self.dbFile)
        if conn is not None:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            conn.close()

            return True
        return False

 
    ### Authenticates the user when logging in
    #
    # @param   object credentials - user credentials
    #
    # @return   boolean
    #
    def AuthenticateUser(self, credentials):
        login    = credentials['userName']
        password = credentials['password']
        auth     = False

        conn = self.CreateDBConnection(self.dbFile)

        if conn is not None:
            cur = conn.cursor()
            cur.execute("SELECT name, password FROM Users")
            rows = cur.fetchall()
            conn.close()

            for row in rows:
                dbUserName = row[0]
                dbPassword = row[1]

                dbPassword = dbPassword[2:len(dbPassword)-1]
                dbPassword = bytes(dbPassword, 'utf8')

                if (login == dbUserName and bcrypt.checkpw(password.encode('utf8'), dbPassword  )):
                    auth = True

        return auth