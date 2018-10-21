import numpy as np
import datetime as dt

'''
Objects in array are of the following form. Note everything is in SI
except for the Date of last opposition

Object = [Orbital_radius, Orbital_period, Dates_of_last_opposition]

the date of opposition is in the form of a list of lists [day,month,year]
for earth, there is no time of opposition
'''

Earth = [1.496e11, 3.16e7]
Mars = [2.28e11, 5.94e7, [ [27,7,2018],[13,10,2020],[8,12,2022],[16,1,2025] ], 'Mars']
Jupiter = [7.78e11, 3.7e8, [ [9,5,2018],[10,6,2019],[14,7,2020] ], 'Jupiter' ]
Ceres = [4.1402e11,1.4529e8, [ [31,1,2018] ], 'Ceres']
Pallas2 = [4.14805e11,1.4567e8, [ [23,10,2017] ], 'Pallas2' ]


Month = [31,28,31,30,31,30,31,31,30,31,30,31]

def get_launch_dates(End_location, launch_time_days):
    
    opposition_list = End_location[2]
    launch_dates = []
    for i in range(len(opposition_list)):
        day = opposition_list[i][0]
        month = opposition_list[i][1]
        year = opposition_list[i][2]
        
        date = dt.date(year,month,day)
        launch_dates.append(date + dt.timedelta(days=launch_time_days))
        
    return launch_dates