import numpy as np
import object_data as obj

# Defining Constants
G = 6.67e-11
M_sun = 1.989e30
Earth_radius = 1.496e11
Earth_period = 3.16e7
Earth_freq = (2*np.pi)/Earth_period

class Fuel_usage_calculator:
    
    def __init__(self, End_location, payload, fuel_speed):
        
        # End radius
        self.End_radius = End_location[0]
        
        # Intermediary Calculations
        term_1 = np.sqrt((2*G*M_sun*self.End_radius)/(Earth_radius*(Earth_radius+self.End_radius)))
        term_2 = np.sqrt((2*G*M_sun*Earth_radius)/(self.End_radius*(Earth_radius+self.End_radius)))
        term_3 = np.sqrt(G*M_sun/Earth_radius)
        term_4 = np.sqrt(G*M_sun/self.End_radius)
        
        # Total speed change for Hohmann orbit
        self.speed_change = (term_1 - term_2) - (term_3 - term_4)
        
        # Initial mass required
        self.mass_initial = payload * np.exp( self.speed_change/fuel_speed )
        
        # Fuel Mass Needed
        self.Fuel_mass = self.mass_initial - payload
        
