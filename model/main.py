import numpy as np
import matplotlib.pyplot as plt
import launch_time_calculator as ltc
import object_data as obj
import orbit_plotter_v2 as op
import fuel_usage_calculator as fuc
import fuel_production_calculator as fpc
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return render_template('home.html')


if __name__=="__main__":
    app.run()