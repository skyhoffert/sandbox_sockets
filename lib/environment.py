# File:          environment.py
# Description:   Simulates and environment that sensors can sample
# Last Modified: May 9, 2018
# Modified By:   Sky Hoffert


# CONSTANTS ----------------------------------------------------------------------------------------
TYPE_TEMPERATURE = 0
TYPE_PRESSURE    = 1
TYPE_GRAVITY     = 2
TYPE_MAGNETISM   = 3


class Environment():
    '''Simulates a basic environment that can be sampled'''
    
    def __init__(self):
        self._temperature         = 0.0  # K
        self._pressure            = 0.0  # Pa
        self._magnetic_field      = 0.0  # T (magnitude)
        self._gravitational_field = 0.0  # g (magnitude)
        
    def sample_temperature(self):
        return self._temperature
    
    def sample_pressure(self):
        return self._pressure
    
    def sample_magnetic_field(self):
        return self._magnetic_field
    
    def sample_gravitational_field(self):
        return self._gravitational_field

    def sample(self, sample_type):
        if sample_type == TYPE_GRAVITY:
            return self._gravitational_field
        elif sample_type == TYPE_MAGNETISM:
            return self._magnetic_field
        elif sample_type == TYPE_PRESSURE:
            return self._pressure
        elif sample_type == TYPE_TEMPERATURE:
            return self._temperature
        else:
            raise ValueError('Sample Type was not a valid type')


class InterplanetarySpaceEnvironment(Environment):
    '''An environment that could be seen in interplanetary space'''
    
    def __init__(self, cross_section_area=1, distance_from_sun=149.6*pow(10, 9)):
        self._temperature         = 5780 / ( distance_from_sun * 1.38*pow(10,-10) )
        self._pressure            = 0
        self._magnetic_field      = 0
        self._gravitational_field = 0

