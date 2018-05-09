# File:          channel.py
# Description:   A channel that antennas connect to for data transfer.
#                Basically determines loss for given channel.
# Last Modified: May 9, 2018
# Modified By:   Sky Hoffert


import math


class Channel():
    '''Channel that packets are sent across'''

    def __init__(self, frequency, distance, port=8200):
        val = 4 * 3.1415926 * distance * frequency / 299792458
        raw = pow(val, 2)
        self._loss = 10 * math.log10(raw)