# File:          probe.py
# Description:   Space probe that can be placed into an environment
# Last Modified: May 9, 2018
# Modified By:   Sky Hoffert


from lib.sensor import TemperatureSensor


class Probe():
    '''Probe that can be placed in an environment'''

    def __init__(self, environment=None):
        self._environment = environment
        self._sensor_temperature = None

    def add_sensor(self, type='', accuracy=0):
        if type == 'temperature':
            self._sensor_temperature = TemperatureSensor( environment=self._environment, accuracy=accuracy )
        else:
            raise Exception('Not implemented')

    def sample(self, type=''):
        if type == 'temperature':
            return self._sensor_temperature.sample()
        else:
            raise Exception('Not implemented')
