import numpy as np
import matplotlib.pyplot as plt
import launch_time_calculator as ltc
import object_data as obj
import orbit_plotter_v2 as op
import fuel_usage_calculator as fuc
import fuel_production_calculator as fpc
from flask import Flask, render_template
import datetime as dt
import tkinter as tk
#'''
#app = Flask(__name__)
#app.debug = True
#
#@app.route('/')
#def home():
#    return render_template('home.html')
#
#
#if __name__=="__main__":
#    app.run()
# 
#'''
##----------------------------------------------
## Part 1
#
## User input
#end_location = obj.Mars
#
#'''
#ltc.Launch_time_calculator is an object that has
#a variable called Time_to_launch which gives the 
#time from opposition to launch
#
#*** Time given in seconds must be converted to days
#'''
#launch_time = ltc.Launch_time_calculator(end_location)
#print ('The time in seconds after opposition that you must launch is: ')
#print (launch_time.Time_to_launch)
#print ('In days, this is:')
#print (launch_time.Time_to_launch/(24*60**2))
#print ('from opposition. There is a method within object_data called get_launch_dates')
#launch_dates = obj.get_launch_dates(end_location, launch_time.Time_to_launch/(24*60**2))
#print ('So therefore the possible launch dates are the following:')
#for i in range(len(launch_dates)):
#    print (launch_dates[i])
#
#
#print ('')
#
##----------------------------------------------
## Part 2
#
## User input
#payload = 1000
#fuel_speed = 4440  #This is the avg value for today's rockets (m/s)
#
#'''
#fuc.Fuel_usage_calculator is an object that has a variable
#called Fuel_mass that gives the mass of fuel needed
#given the payload
#
#*** all quantities are in SI units 
#'''
#fuel_needed = fuc.Fuel_usage_calculator(end_location,payload,fuel_speed)
#print ('The amount of fuel needed for this journey in kg is:')
#print (fuel_needed.Fuel_mass)
#print ('')
#
##----------------------------------------------
## Part 3
#
## User Input
#fuel_ratio = 0.5
#panel_area = 1
#panel_efficiency = 0.2
#
#'''
#fpc.Fuel_production_calculator is an object that has a variable
#called time_needed that gives the time needed to make the fuel 
#required for a return trip
#
#*** all quantities are in SI units 
#'''
#
#time_needed = fpc.Fuel_production_calculator(
#        end_location,fuel_ratio,panel_area,panel_efficiency,payload,fuel_speed
#        )
#print ('The time it will take to make fuel at your destination in seconds is:')
#print (time_needed.time_needed)
#print ('')
#
#
#----------------------------------------------
# Part 4

# This is just for plotting the path the orbit takes

#'''
#op.Orbit_plotter is a class that takes the end location and 
#a method called plot_orbit plots it using matplotlib
#'''
#
#print ('The inner circle is the orbit of Earth, the outer circle is the orbit of your destination')
#print ('The ellipse is the Hohmann transit orbit')
#orbit_plot = op.Orbit_plotter(end_location)
#orbit_plot.plot_orbit()

#----------------------------------------------
end_location = 0

class Main:
    
    def __init__ (self):
        self.end_location = obj.Mars
        self.launch_dates = []
    
    def select_Mars(self):
        self.end_location = obj.Mars
        
    def select_Jupiter(self):
        self.end_location = obj.Jupiter
        
    def select_dest(self):
        display = tk.Text(master=root, height = 1, width = 20)
        display.grid(row=4,column=0)
        #display.pack()
        display.insert(tk.END, 'You Chose: '+a.end_location[3]+'!')
        
    def select_payload(self):
        self.payload = float(payload.get())
        display_payload = tk.Text(master=root, height = 1, width = 30)
        display_payload.grid(row=8,column=0)
        display_payload.insert(tk.END, 'Your payload is: '+str(self.payload)+'kg!')
        
    def select_fuel_speed(self):
        self.fuel_speed = float(fuel_speed.get())
        display_fuel_speed = tk.Text(master=root, height = 1, width = 30)
        display_fuel_speed.grid(row=12,column=0)
        display_fuel_speed.insert(tk.END, 'Your fuel speed is: '+str(self.fuel_speed)+'m/s!')
        
    def select_fuel_ratio(self):
        self.fuel_ratio = float(fuel_ratio.get())
        display_fuel_ratio = tk.Text(master=root, height = 1, width = 30)
        display_fuel_ratio.grid(row=17,column=0)
        display_fuel_ratio.insert(tk.END, 'Your fuel ratio is: '+str(self.fuel_ratio)+'!')
        
    def select_panel_area(self):
        self.panel_area = float(panel_area.get())
        display_panel_area = tk.Text(master=root, height = 1, width = 30)
        display_panel_area.grid(row=22,column=0)
        display_panel_area.insert(tk.END, 'Your panel area is: '+str(self.panel_area)+'m^2!')
        
    def select_panel_efficiency(self):
        self.panel_efficiency = float(panel_efficiency.get())
        display_panel_efficiency = tk.Text(master=root, height = 1, width = 30)
        display_panel_efficiency.grid(row=26,column=0)
        display_panel_efficiency.insert(tk.END, 'Your panel efficiency is: '+str(self.panel_efficiency)+'!')
        
    def launch_times(self):
        launch_time = ltc.Launch_time_calculator(self.end_location)
        days = launch_time.Time_to_launch/(24*60**2)
        
        self.launch_dates = obj.get_launch_dates(self.end_location, days)
        return self.launch_dates
        
    def fuel(self):
        fuel_needed = fuc.Fuel_usage_calculator(self.end_location,self.payload,self.fuel_speed)
        self.fuel_mass = fuel_needed.Fuel_mass
        return self.fuel_mass
    
    def fuel_prod(self):
        time_needed = fpc.Fuel_production_calculator(
                self.end_location,self.fuel_ratio,self.panel_area,self.panel_efficiency,self.payload,self.fuel_speed
                )
        self.time_for_fuel = time_needed.time_needed
        return self.time_for_fuel/(24*60**2)
    
    def display_launch_dates(self):
        c = ''
        for i in range(len(self.launch_dates)):
             c += str((self.launch_dates[i]))+" "
             
        return c
    
    def display_results(self):
        tk.Label(root, text='The next optimal Lauch date is: '+str(self.launch_times()[0]), font=20).grid(row=30, column=0, sticky='W')
        tk.Label(root, text='The amount of fuel in kg needed is: '+str(self.fuel())+'kg', font=20).grid(row=31, column=0, sticky='W')
        tk.Label(root, text='The time it would take to produce fuel required for a return is: '+str(self.fuel_prod())+' days', font=20).grid(row=32, column=0, sticky='W')

        
        

a = Main()



root = tk.Tk()
root.title("My Program")
root.geometry("500x900")

# End Location
tk.Label(root, text="Please Select your Destination!", font=20).grid(row=0, column=0, sticky='W')
tk.Button(root, text="Mars", width=6, command=a.select_Mars).grid(row=1,column=0,sticky='W')
tk.Button(root, text="Jupiter", width=6, command=a.select_Jupiter).grid(row=2,column=0,sticky='W')
tk.Button(root, text="Confirm", width=6, command=a.select_dest).grid(row=3,column=0,sticky='W')

# Payload Mass
tk.Label(root, text="Please Select your Payload Mass (in kg)!", font=20).grid(row=5, column=0, sticky='W')
payload = tk.Entry()
payload.grid(row=6,column=0, sticky='W')
tk.Button(root, text="Confirm", width=6, command=a.select_payload).grid(row=7,column=0,sticky='W')

# Fuel Speed
tk.Label(root, text="Please Select your Fuel Speed (in m/s)!", font=20).grid(row=9, column=0, sticky='W')
fuel_speed = tk.Entry()
fuel_speed.grid(row=10,column=0, sticky='W')
tk.Button(root, text="Confirm", width=6, command=a.select_fuel_speed).grid(row=11,column=0,sticky='W')

# Fuel Ratio
tk.Label(root, text="Please Select the Ratio of Liquid Hydrogen to", font=20).grid(row=13, column=0, sticky='W')
tk.Label(root, text="Liquid Oxygen you would need (between 0 and 1)!", font=20).grid(row=14, column=0, sticky='W')
fuel_ratio = tk.Entry()
fuel_ratio.grid(row=15,column=0, sticky='W')
tk.Button(root, text="Confirm", width=6, command=a.select_fuel_ratio).grid(row=16,column=0,sticky='W')

# Panel Area
tk.Label(root, text="Please Select the Area of the Solar Panel you have!", font=20).grid(row=18, column=0, sticky='W')
panel_area = tk.Entry()
panel_area.grid(row=20,column=0, sticky='W')
tk.Button(root, text="Confirm", width=6, command=a.select_panel_area).grid(row=21,column=0,sticky='W')

# Panel Efficiency
tk.Label(root, text="Please Select the Efficiency of the Solar Panel you have!", font=20).grid(row=23, column=0, sticky='W')
panel_efficiency = tk.Entry()
panel_efficiency.grid(row=24,column=0, sticky='W')
tk.Button(root, text="Confirm", width=6, command=a.select_panel_efficiency).grid(row=25,column=0,sticky='W')

# Display Results
tk.Button(root, text="Calculate", width=6, command=a.display_results).grid(row=29,column=0,sticky='W')

root.mainloop()


