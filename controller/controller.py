#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

sys.path.append('../view')
sys.path.append('../model')

from view import View
from model import Model

class Controller:

    def __init__(self):
        self.view = View()


    def PrintMenu(self):
        os.system('cls')
        self.menuOption = self.view.PrintMenu()


controller = Controller()
controller.PrintMenu()