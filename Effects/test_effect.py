#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.abspath('../Network'))
import LedBurnProtocol as network
import time

from RainbowEffect import RainbowEffect
animations = [RainbowEffect(range(600))]

flower 	= [0, 0, 0] * 550
sheep 	= [0, 0 ,0] * 302
grass 	= [0, 0, 0] * 600
sign 	= [0, 0, 0] * 150


speed = 200 # in 50 hrz
current_time = 0
frame_id = 0;
    
while True:
        
	time_precent = float(current_time) / speed

	for animation in animations:
		animation.apply(time_precent, grass)

	network.send(frame_id, flower, sheep, grass, sign)

	time.sleep(0.02)
	current_time = (current_time + 1) % speed
 	frame_id += 500

