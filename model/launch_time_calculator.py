import numpy as np
import object_data as obj

'''
Please note for now all values are in SI units
'''

# Defining Constants
G = 6.67e-11
M_sun = 1.989e30
Earth_radius = 1.496e11
Earth_period = 3.16e7
Earth_freq = (2*np.pi)/Earth_period

class Launch_time_calculator:
    '''
    This assumes Earth Start
    '''
    
    def __init__(self, End_location):
        
        # Defining the Radius, Period and Freq
        self.End_radius = End_location[0]
        self.End_period = End_location[1]
        self.End_freq = (2*np.pi)/self.End_period
        
        # Finding the Semimajor axis, and Time of Transit for Hohmann orbits
        self.at = (Earth_radius + self.End_radius)/2
        self.Tt = np.pi * np.sqrt(1/(G*M_sun))*self.at**(3/2)
        
        # We set the initial angle conditions for theta to be zero by starting
        # from the last opposition. The relative angle is
        self.Relative_angle = np.pi + self.End_freq*self.Tt
        
        # Which makes the time of launch
        self.Launch_wait = self.Relative_angle / (Earth_freq-self.End_freq)
        
        # In days
        self.Time_to_launch = self.Launch_wait
        
        # angle of both during launch time
        self.Earth_angle_at_launch = self.Time_to_launch * Earth_freq
        self.End_angle_at_launch = self.Time_to_launch * self.End_freq

        
        
    


