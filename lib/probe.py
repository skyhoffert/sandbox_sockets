# File:          probe.py
# Description:   Space probe that can be placed into an environment
# Last Modified: May 9, 2018
# Modified By:   Sky Hoffert


class Probe():
    '''Probe that can be placed in an environment'''

    def __init__(self, environment=None):
        self._environment = environment
