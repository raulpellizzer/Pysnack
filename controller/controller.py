#!/usr/bin/env python

import sys

sys.path.append('../view')
from view import View

class Controller:

    def __init__(self):
        self.view = View()

    
    def PrintMenu(self):
        self.view.PrintMenu()


ctrl = Controller()
ctrl.PrintMenu()
