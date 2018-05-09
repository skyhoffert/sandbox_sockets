# File:          antenna.py
# Description:   An antenna that sends and receives packets from a channel
# Last Modified: May 9, 2018
# Modified By:   Sky Hoffert


class Antenna():
    '''Antenna used for sending data'''

    def __init__(self):
        self._type = ''
        self._gain = 0.0
        self._pattern = ( [], [], [] )  # gain (relative) in x, y, z directions by 10 degree increments

    def send_packet(self, packet, channel):
        channel.enter(packet)