# File:          voyager.py
# Description:   Attempts to place the Voyager spacecraft in an environment and talk to Earth
# Last Modified: May 9, 2018
# Modified By:   Sky Hoffert

import environment
import probe
import sys

class Voyager(Probe):
    '''Voyager probe'''

    def set_environment(self, env):
        self._environment = env

def main():
    voyager = Voyager()
    voyager.set_environment( InterplanetarySpaceEnvironment() )

if __name__ == '__main__':
    main()
    sys.exit()