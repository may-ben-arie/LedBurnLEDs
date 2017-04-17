from abc import ABCMeta, abstractmethod

import sys, os
sys.path.append(os.path.abspath('../UIElements'))
from Sign import Sign


class SignAnimation:
    __metaclass__ = ABCMeta
    
    def __init__(self, sign):
        self.sign = sign

    @abstractmethod
    def apply(self, time_percent): pass
