"""
This module can produce a color that changes over time.
Effects and animations can then be configured with complex color models by suplling a single instance
"""

from abc import ABCMeta, abstractmethod

import Colors


class AbstractTimedColor:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_color(self, time_percent, location_percent): pass
    def get_hue(self, time_percent, location_percent): pass

class ConstTimedColor(AbstractTimedColor):

    def __init__(self, rgb_color):
        AbstractTimedColor.__init__(self)
        self.rgb_color = rgb_color

    def get_color(self, time_percent, location_percent):
        return self.rgb_color

    def get_hue(self, time_percent, location_percent):
        return 0

class HueChangeTimedColor(AbstractTimedColor):

    def __init__(self, hue_start, hue_end):
        AbstractTimedColor.__init__(self)
        self.hue_start = hue_start
        self.hue_end = hue_end
        self.hue_diff = hue_end - hue_start

    def get_color(self, time_percent, location_percent):
        return Colors.hls_to_rgb(self.get_hue(time_percent, location_percent), 1.0, 1.0)

    def get_hue(self, time_percent, location_percent):
        curr_hue = self.hue_start + self.hue_diff * time_percent
        while curr_hue < 0:
            curr_hue += 1
        while curr_hue > 1:
            curr_hue -= 1
        return curr_hue;


class HueChangeTimedColorByLocation(AbstractTimedColor):

    def __init__(self, hue_start, hue_end):
        AbstractTimedColor.__init__(self)
        self.hue_start = hue_start
        self.hue_end = hue_end
        self.hue_diff = hue_end - hue_start

    def get_color(self, time_percent, location_percent):
        return Colors.hls_to_rgb(self.get_hue(time_percent, location_percent), 1.0, 1.0)

    def get_hue(self, time_percent, location_percent):
        curr_hue = self.hue_start + self.hue_diff * location_percent
        while curr_hue < 0:
            curr_hue += 1
        while curr_hue > 1:
            curr_hue -= 1
        return curr_hue;





