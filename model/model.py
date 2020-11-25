#!/usr/bin/env python
# -*- coding: utf-8 -*-

from texttable import Texttable
from zipfile import ZipFile
from sqlite3 import Error
import sqlite3
import bcrypt
import time
import json
import os

class Model:

    ### Class Constructor
    #
    #
    def __init__(self):
        self.dbFile = os.getcwd() + '\database\pysnackdb.db'


    ### Prints information about the app
    #
    # @return   string
    #
    def PrintAboutApp(self):
        about = 'Este aplicativo foi desenvolvido para a disciplina de Tópicos Especiais em Informática '
        about = about + 'pelos alunos Carlos Matheus (RA: 2840481711003)\ne Raul Pellizzer (RA: 2840481723043) no ano de 2020. Este aplicativo tem como '
        about = about + 'objetivo auxiliar uma lanchonete a gerenciar seus pedidos.'
        return about


    ### Initializes tables for the app
    #
    #
    def InitializeTables(self):
        self.conn = self.CreateDBConnection(self.dbFile)

        if self.conn is not None:
            self.CreateTable('users')
            self.CreateTable('products')
            self.CreateTable('orders')
            self.conn.close()


    ### Created database connection
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

        if table == 'users':
            sql = """ CREATE TABLE IF NOT EXISTS Users (
                            name text NOT NULL,
                            password text NOT NULL
                        ); """

        elif table == 'products':
            sql = """ CREATE TABLE IF NOT EXISTS Products (
                            id integer PRIMARY KEY AUTOINCREMENT,
                            name text NOT NULL,
                            description text NOT NULL,
                            unitPrice real
                        ); """

        elif table == 'orders':
            sql = """ CREATE TABLE IF NOT EXISTS Orders (
                            id integer PRIMARY KEY AUTOINCREMENT,
                            clientName text NOT NULL,
                            itens text NOT NULL,
                            total real,
                            payment text NOT NULL,
                            exchange real,
                            date text NOT NULL
                        ); """

        try:
            c = self.conn.cursor()
            c.execute(sql)

        except Error as err:
            print(err)


    ### Register User in the database
    #
    # @param   object newCredentials - user credentials
    #
    # @return   boolean
    #
    def RegisterNewUser(self, newCredentials):
        registerValidation = False
        validation         = self.ValidateCredentials(newCredentials)
        
        if validation:
            userValidation = self.CheckUserInDB(newCredentials['userName'])

            if userValidation == False:
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
                if row[0] == userName:
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

                if login == dbUserName and bcrypt.checkpw(password.encode('utf8'), dbPassword):
                    auth = True

        return auth


    ### Inserts a new product into the database
    #
    # @param   object productData - ata about the new product
    #
    # @return   boolean
    #
    def RegisterNewProduct(self, productData):
        productName       = productData['productName']
        producDescription = productData['producDescription']
        pricePerUnit      = productData['pricePerUnit']

        sql = ''' INSERT INTO Products (name, description, unitPrice)
                    VALUES ('%s', '%s', '%s') ''' % (productName, producDescription, pricePerUnit)

        conn = self.CreateDBConnection(self.dbFile)
        if conn is not None:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            conn.close()

            return True
        return False


    ### Retrieves all products from the database
    #
    # @return   string
    #
    def GetMenuItens(self):
        conn      = self.CreateDBConnection(self.dbFile)
        menuItens = []

        if conn is not None:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Products")
            rows = cur.fetchall()
            conn.close()

            for row in rows:
                tempRow = {
                    "productId": row[0],
                    "productName": row[1],
                    "productDescription": row[2],
                    "unitPrice": row[3]
                }

                menuItens.append(tempRow)
                tempRow = {}

            menuTable = self.FormatMenuItens(menuItens)
            return menuTable


    ### Format data into a table format
    #
    # @param   array menuItens - product data
    #
    # @return   string
    #
    def FormatMenuItens(self, menuItens):
        menu = Texttable()

        header = ['Codigo', 'Nome Produto', 'Descrição', 'Preço']
        menu.header(header)

        for item in menuItens:
            productId          = item['productId']
            productName        = item['productName']
            productDescription = item['productDescription']
            unitPrice          = item['unitPrice']

            row = [productId, productName, productDescription, unitPrice]
            menu.add_row(row)

        menu.set_cols_width([6, 25, 50, 10])
        menu.set_cols_align(['l','l','l', 'l'])
        menu.set_cols_valign(['m','m', 'm', 'm'])
        menu.set_deco(menu.HEADER | menu.VLINES)
        menu.set_chars(['-','|','+','#'])
        menuTable = menu.draw()

        return menuTable


    ### Check if a product exists in the database
    #
    # @param   integer productId - product id
    #
    # @return   boolean
    #
    def CheckProductInDB(self, productId):
        conn = self.CreateDBConnection(self.dbFile)

        if conn is not None:
            cur = conn.cursor()
            cur.execute("SELECT id FROM Products")
            rows = cur.fetchall()
            conn.close()

            for row in rows:
               if productId == row[0]:
                   return True
            
            return False


    ### Update data about a product
    #
    # @param   integer productId - product id
    # @param   object productData - new data to be updated
    #
    # @return   boolean
    #
    def UpdateProductData(self, productId, productData):
        productName       = productData['productName']
        producDescription = productData['producDescription']
        pricePerUnit      = productData['pricePerUnit']

        sql = ''' UPDATE Products
              SET name = '%s', 
                  description = '%s', 
                  unitPrice = %s
              WHERE id = %s''' % (productName, producDescription, pricePerUnit, productId)

        conn = self.CreateDBConnection(self.dbFile)
        if conn is not None:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            conn.close()

            return True
        return False


    ### Deletes a product
    #
    # @param   integer productId - product id
    #
    # @return   boolean
    #
    def DeleteProduct(self, productId):
        sql = ''' DELETE FROM Products WHERE id = %s''' % (productId)

        conn = self.CreateDBConnection(self.dbFile)
        if conn is not None:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            conn.close()

            return True
        return False


    ### Retrieve data about a given product
    #
    # @param   integer productId - product id
    #
    # @return   object
    #
    def GetProductDataById(self, productId):
        productName = ''
        conn = self.CreateDBConnection(self.dbFile)
        sql = ''' SELECT name, unitPrice FROM Products WHERE id = %s''' % (productId)

        if conn is not None:
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            conn.close()

            for row in rows:
                productName = row[0]
                unitPrice   = row[1]

            data = {
                "productName": productName,
                "unitPrice": unitPrice
            }

            return data


    ### Format orders data into a table format
    #
    # @param   array fullOrder - orders data
    #
    # @return   string
    #
    def FormatOrderToTable(self, fullOrder):
        bag = Texttable()

        header = ['Codigo', 'Nome Produto', 'Quantidade', 'Preço Unidade', 'Sub Total']
        bag.header(header)

        for order in fullOrder:
            productId   = order['productId']
            productName = order['productName']
            quantity    = order['quantity']
            unitPrice   = order['unitPrice']
            subTotal    = quantity*unitPrice

            row = [productId, productName, quantity, unitPrice, subTotal]
            bag.add_row(row)

        bag.set_cols_width([6, 25, 10, 10, 10])
        bag.set_cols_align(['l','l','l', 'l', 'l'])
        bag.set_cols_valign(['m','m', 'm', 'm', 'm'])
        bag.set_deco(bag.HEADER | bag.VLINES)
        bag.set_chars(['-','|','+','#'])
        bagTable = bag.draw()

        return bagTable


    ### Calculates the total order amount
    #
    # @param   array fullOrder - orders data
    #
    # @return   float
    #
    def CalculateOrderValue(self, fullOrder):
        totalValue = 0

        for item in fullOrder:
            totalValue = totalValue + (item['quantity']*item['unitPrice'])

        totalValue = ('%.2f' % totalValue)
        return totalValue


    ### Formats the order itens into a string for the database
    #
    # @param   array fullOrder - orders data
    #
    # @return   string
    #
    def StringfyOrderItens(self, fullOrder):
        orderString = ''

        for order in fullOrder:
            orderString = orderString + '%s x %s\n' % (str(order['quantity']), str(order['productName']))

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
        sql = ''' INSERT INTO Orders (clientName, itens, total, payment, exchange, date) 
                VALUES ('%s', '%s', %s, '%s', %s, '%s') ''' % (clientName, orderItens, total, payment, exchange, orderDate)

        conn = self.CreateDBConnection(self.dbFile)
        if conn is not None:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            conn.close()

            return True
        return False


    ### Retrieves all orders from the database
    #
    # @return   string
    #
    def GetOrderItens(self):
        conn       = self.CreateDBConnection(self.dbFile)
        orderItens = []

        if conn is not None:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Orders")
            rows = cur.fetchall()
            conn.close()

            for row in rows:
                tempRow = {
                    "orderId": row[0],
                    "clientName": row[1],
                    "orderItens": row[2],
                    "totalValue": row[3],
                    "paymentMethod": row[4],
                    "exchange": row[5],
                    "date": row[6]
                }

                orderItens.append(tempRow)
                tempRow = {}

            orderTable = self.FormatOrderItens(orderItens)
            return orderTable


    ### Retrieves all orders from the database, raw mode
    #
    # @return   array
    #
    def GetRawOrderItens(self):
        conn       = self.CreateDBConnection(self.dbFile)
        orderItens = []

        if conn is not None:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Orders")
            rows = cur.fetchall()
            conn.close()

            for row in rows:
                tempRow = {
                    "orderId": row[0],
                    "clientName": row[1],
                    "orderItens": row[2],
                    "totalValue": row[3],
                    "paymentMethod": row[4],
                    "exchange": row[5],
                    "date": row[6]
                }

                orderItens.append(tempRow)
                tempRow = {}

            return orderItens


    ### Format data into a table format
    #
    # @param   array orderItens - order data
    #
    # @return   string
    #
    def FormatOrderItens(self, orderItens):
        order = Texttable()

        header = ['Codigo', 'Nome Cliente', 'Itens', 'Valor Total', 'Pagamento', 'Troco', 'Data']
        order.header(header)

        for item in orderItens:
            orderId       = item['orderId']
            clientName    = item['clientName']
            orderItens    = item['orderItens']
            totalValue    = item['totalValue']
            paymentMethod = item['paymentMethod']
            exchange      = item['exchange']
            date          = item['date']

            row = [orderId, clientName, orderItens, totalValue, paymentMethod, exchange, date]
            order.add_row(row)

        order.set_cols_width([6, 25, 50, 12, 12, 12, 18])
        order.set_cols_align(['l','l','l', 'l', 'l', 'l', 'l'])
        order.set_cols_valign(['m','m', 'm', 'm', 'm', 'm', 'm'])
        order.set_deco(order.HEADER | order.VLINES)
        order.set_chars(['-','|','+','#'])
        orderTable = order.draw()

        return orderTable


    ### Generates the ticket for the user
    #
    # @param   string clientName - client name
    # @param   string orderItens - order itens
    # @param   float total - total amount of the order
    # @param   object paymentData - data about payment method
    # @param   float exchange - order exchange
    # @param   string orderDate - date of the order
    #
    # @return   string
    #
    def GenerateTicket(self, clientName, orderItens, total, paymentData, exchange, orderDate):
        ticket = Texttable()

        header = ['Cupom Fiscal - Lanchonete PySnack']
        ticket.header(header)

        clientName = 'Nome Cliente: %s\n' % (clientName)
        row = [clientName]
        ticket.add_row(row)

        orderItens = 'Produtos:\n%s' % (orderItens)
        row = [orderItens]
        ticket.add_row(row)

        total = 'Valor Total Pedido: %.2f' % (float(total))
        row = [total]
        ticket.add_row(row)

        paymentMethod = paymentData['payment']
        paymentMethod = 'Forma de pagamento: %s' % (paymentMethod)
        row = [paymentMethod]
        ticket.add_row(row)

        paymentAmount = paymentData['amount']
        paymentAmount = 'Valor do pagamento: %s' % (paymentAmount)
        row = [paymentAmount]
        ticket.add_row(row)

        exchange = 'Troco: %s' % (exchange)
        row = [exchange]
        ticket.add_row(row)

        orderDate = 'Data do Pedido: %s' % (orderDate)
        row = [orderDate]
        ticket.add_row(row)

        ticket.set_cols_width([75])
        ticket.set_cols_align(['c'])
        ticket.set_cols_valign(['m'])
        ticket.set_deco(ticket.HEADER | ticket.VLINES)
        ticket.set_chars(['-','|','+','#'])
        ticketTable = ticket.draw()

        return ticketTable


    ### Export orders data to json file
    #
    # @param   array ordersData - all orders data
    #
    def ExportToJson(self, ordersData):

        jsonData = json.dumps(ordersData, indent = 4)
        with open("../orders.json", "w") as outputFile:
            outputFile.write(jsonData)


    ### Compress a file to .zip format
    #
    # @param   string fileName - name of the file to be zipped
    #
    def CompressToZipFile(self, fileName):
        canProceed = False
        while not(canProceed):
            time.sleep(1)
            canProceed = os.path.isfile(fileName)

        ZipFile('../orders.zip', 'w').write(fileName)