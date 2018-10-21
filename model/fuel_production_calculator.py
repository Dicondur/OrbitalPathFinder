import numpy as np
import object_data as obj
import fuel_usage_calculator as fuc

'''
237 kJ of energy for each mole of water, thus creating 2g of hydrogen and
16g of oxygen.

required Fuel Ratio is inputted, and the time needed, given a power source
to create enough fuel for the return trip is calculated. 
'''

class Fuel_production_calculator:
    
    def __init__(self,End_location, fuel_ratio, panel_area, panel_efficiency, payload, fuel_speed):
        self.fuel_ratio = fuel_ratio
        self.panel_area = panel_area
        self.panel_efficiency = panel_efficiency
        self.End_location = End_location
        self.End_radius = End_location[0]
        self.payload = payload
        self.fuel_speed = fuel_speed
        
        self.get_power()
        self.get_time()
        
    def get_power(self):
        Sun_power = 4e26
        solar_power_per_area = Sun_power / (4*np.pi*self.End_radius**2)
        
        self.power_output = 0.5*self.panel_area*(solar_power_per_area*self.panel_efficiency)
        
    def get_time(self):
        a = fuc.Fuel_usage_calculator(self.End_location, self.payload, self.fuel_speed)
        self.fuel_needed = a.Fuel_mass
        self.hydrogen_fuel_needed = self.fuel_needed * self.fuel_ratio
        
        self.energy_needed = self.hydrogen_fuel_needed * 2.37e6
        
        self.time_needed = self.energy_needed/self.power_output
        

a = Fuel_production_calculator(obj.Mars, 0.5, 1, 0.2, 1000, 2440)
print (a.time_needed/(24*60**2))