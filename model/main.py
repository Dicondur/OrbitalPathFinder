import numpy as np
import matplotlib.pyplot as plt
import launch_time_calculator as ltc
import object_data as obj
import orbit_plotter_v2 as op
import fuel_usage_calculator as fuc
import fuel_production_calculator as fpc
from flask import Flask, render_template
'''
app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return render_template('home.html')


if __name__=="__main__":
    app.run()
 
'''
#----------------------------------------------
# Part 1

# User input
end_location = obj.Mars

'''
ltc.Launch_time_calculator is an object that has
a variable called Time_to_launch which gives the 
time from opposition to launch

*** Time given in seconds must be converted to days
'''
launch_time = ltc.Launch_time_calculator(end_location)
print ('The time in seconds after opposition that you must launch is: ')
print (launch_time.Time_to_launch)
print ('')

#----------------------------------------------
# Part 2

# User input
payload = 1000
fuel_speed = 4440  #This is the avg value for today's rockets (m/s)

'''
fuc.Fuel_usage_calculator is an object that has a variable
called Fuel_mass that gives the mass of fuel needed
given the payload

*** all quantities are in SI units 
'''
fuel_needed = fuc.Fuel_usage_calculator(end_location,payload,fuel_speed)
print ('The amount of fuel needed for this journey in kg is:')
print (fuel_needed.Fuel_mass)
print ('')

#----------------------------------------------
# Part 3

# User Input
fuel_ratio = 0.5
panel_area = 1
panel_efficiency = 0.2

'''
fpc.Fuel_production_calculator is an object that has a variable
called time_needed that gives the time needed to make the fuel 
required for a return trip

*** all quantities are in SI units 
'''

time_needed = fpc.Fuel_production_calculator(
        end_location,fuel_ratio,panel_area,panel_efficiency,payload,fuel_speed
        )
print ('The time it will take to make fuel at your destination in seconds is:')
print (time_needed.time_needed)
print ('')


#----------------------------------------------
# Part 4

# This is just for plotting the path the orbit takes

'''
op.Orbit_plotter is a class that takes the end location and 
a method called plot_orbit plots it using matplotlib
'''

print ('The inner circle is the orbit of Earth, the outer circle is the orbit of your destination')
print ('The ellipse is the Hohmann transit orbit')
orbit_plot = op.Orbit_plotter(end_location)
orbit_plot.plot_orbit()







