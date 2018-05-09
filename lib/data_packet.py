# File:          data_packet.py
# Description:   Packet that can be sent from antenna to antenna
# Last Modified: May 9, 2018
# Modified By:   Sky Hoffert


class DataPacket():
    '''Data packet that can be sent somewhere'''

    def __init__(self, packet=b''):
        self._packet = packet  # byte array