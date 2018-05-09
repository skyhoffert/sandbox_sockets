# File:          voyager.py
# Description:   Attempts to place the Voyager spacecraft in an environment and talk to Earth
# Last Modified: May 9, 2018
# Modified By:   Sky Hoffert


from lib.environment import InterplanetarySpaceEnvironment
from lib.probe import Probe
import sys


class Voyager(Probe):
    '''Voyager probe'''

    def set_environment(self, env):
        self._environment = env
        self.add_sensor(type='temperature', accuracy=0.999)


# UTILITY FUNCTION ----------------------------------------------------------------------------------------
def print_smart(val, debug=False, error=False, end='\n', prefix=True):
    # modify string to fit given args
    val = str(val)
    val = '[ ERROR ] ' + val if error else '[ DEBUG ] ' + val if debug else '[ VYGER ] ' + val if prefix else val
    val = val + end if end else val

    # print and flush
    sys.stdout.write(val)
    sys.stdout.flush()


def main():
    voyager = Voyager()
    voyager.set_environment( InterplanetarySpaceEnvironment() )

    print_smart( voyager.sample(type='temperature') )


if __name__ == '__main__':
    main()
    sys.exit()