#!/usr/bin/env python

import sys

sys.path.append('../view')
from View import View

class Controller:

    def __init__(self):
        self.view = View()


ctrl = Controller()
