import numpy as np

'''
Objects in array are of the following form. Note everything is in SI
except for the Date of last opposition

Object = [Orbital_radius, Orbital_period, Dates_of_last_opposition]

the date of opposition is in the form of a list of lists [day,month,year]
for earth, there is no time of opposition
'''

Earth = [1.496e11, 3.16e7]
Mars = [2.28e11, 5.94e7, [ [27,7,2018],[13,10,2020],[8,12,2022],[16,1,2025] ]]
Jupiter = [7.78e11, 3.7e8, [ [9,5,2018],[10,6,2019],[14,7,2020] ] ]


Month = [31,28,31,30,31,30,31,31,30,31,30,31]
