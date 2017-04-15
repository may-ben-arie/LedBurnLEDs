from SignAnimation import SignAnimation

import sys, os
sys.path.append(os.path.abspath('../UIElements'))
from Sign import Sign

sys.path.append(os.path.abspath('../Effects'))
from FireEffect import FireEffect
from AlwaysOnEffect import AlwaysOnEffect

class FireSignAnimation(SignAnimation):

    def __init__(self, sign):
        SignAnimation.__init__(self, sign)

        self.effects = []
        self.effects.append(FireEffect(self.sign.a_bottom_to_top, add_red_bootom=False))
        self.effects.append(FireEffect(self.sign.s_bottom_to_top, add_red_bootom=False))
        # self.effects.append(FireEffect(self.sign.l))
        # self.effects.append(FireEffect(self.sign.i))
        # self.effects.append(FireEffect(self.sign.o))
        # self.effects.append(FireEffect(self.sign.t))


    def apply(self, time_percent):
        
        for effect in self.effects:
            effect.apply(time_percent, self.sign.get_array())



