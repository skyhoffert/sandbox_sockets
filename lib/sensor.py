# File:          sensor.py
# Description:   Senses a given environment
# Last Modified: May 9, 2018
# Modified By:   Sky Hoffert


from lib.environment import *
import random


class Sensor():
    '''Senses an environment'''

    def __init__(self, environment=None, sample_type=0, accuracy=1):
        self._environment = environment
        self._sample_type = sample_type
        self._accuracy = accuracy

    def sample(self):
        sample = self._environment.sample( self._sample_type )
        error = (1 - self._accuracy) * (random.random() - 0.5) * sample
        return sample + error


class TemperatureSensor(Sensor):
    '''Senses temperature of an environment'''

    def __init__(self, environment, accuracy):
        super(TemperatureSensor, self).__init__(environment=environment, sample_type=TYPE_TEMPERATURE, accuracy=accuracy)