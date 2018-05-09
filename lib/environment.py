# File:          environment.py
# Description:   Simulates and environment that sensors can sample
# Last Modified: May 9, 2018
# Modified By:   Sky Hoffert


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


class InterplanetarySpaceEnvironment(Environment):
    '''An environment that could be seen in interplanetary space'''
    
    def __init__(self, cross_section_area=1, distance_from_Sun=149.6*10^9):
        self._temperature         = 5780 / ( distance_from_Sun * 1.38*10^-10 )
        self._pressure            = 0
        self._magnetic_field      = 0
        self._gravitational_field = 0

