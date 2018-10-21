import numpy as np
import matplotlib.pyplot as plt
import launch_time_calculator as ltc
import object_data as obj

# Defining Constants
G = 6.67e-11
M_sun = 1.989e30
Earth_radius = 1.496e11
Earth_period = 3.16e7
Earth_freq = (2*np.pi)/Earth_period

class Orbit_plotter:
    
    def __init__(self, End_location):
        self.Launch_time_calc = ltc.Launch_time_calculator(End_location)
        self.Earth_angle = self.Launch_time_calc.Earth_angle_at_launch
        
        # end measurements
        self.End_radius = End_location[0]
        self.End_period = End_location[1]
        self.End_freq = (2*np.pi)/self.End_period
        
        # transit measurements
        self.e = (self.End_radius - Earth_radius) / (
                self.End_radius + Earth_radius)
        self.a = (self.End_radius + Earth_radius) / 2
        
        # defining t
        t = np.linspace(0,2*self.End_period,1000)
        
        # defining the orbits
        self.x_earth = Earth_radius*np.cos(Earth_freq*t)
        self.y_earth = Earth_radius*np.sin(Earth_freq*t)
        
        self.x_end = self.End_radius*np.cos(self.End_freq*t)
        self.y_end = self.End_radius*np.sin(self.End_freq*t)
        
        self.r = self.a*(1-self.e**2)/(1+self.e*np.cos(
                t*np.sqrt(G*M_sun*self.a**3)))
        
        self.x_transit = self.r*np.cos(t*np.sqrt(G*M_sun*self.a**3))
        self.y_transit = self.r*np.sin(t*np.sqrt(G*M_sun*self.a**3))
        
    def plot_orbit(self):
        plt.plot(self.x_earth,self.y_earth,'.')
        plt.plot(self.x_end,self.y_end,'.')
        plt.plot(self.x_transit,self.y_transit,'.')
        plt.show()
        
#a1= Orbit_plotter(obj.Jupiter)
#a1.plot_orbit()

