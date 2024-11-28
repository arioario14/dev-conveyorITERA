import os
import glob
import time
import tkinter as tk
from matplotlib import animation
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TemperatureSensor:
    def __init__(self):
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

        base_dir = '/sys/bus/w1/devices/'
        device_folder = glob.glob(base_dir + '28*')[0]
        self.device_file = device_folder + '/w1_slave'

    def read_temp_raw(self):
        with open(self.device_file, 'r') as f:
            lines = f.readlines()
        return lines

    def read_temp(self):
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            temp_c = int(temp_string) / 1000
            return temp_c

class TemperaturePlotter:
    def __init__(self, root, width=470, height=185, x_pos=14.0, y_pos=208.0,dpi=100):
        self.root = root

        self.sensor = TemperatureSensor()
        self.temps = []
        self.max_len = 50
        self.min_temp, self.max_temp = 0, 100

        self.dpi = dpi
        self.fig = plt.Figure(figsize=(width/dpi, height/dpi), dpi=dpi)
        self.ax = self.fig.add_subplot(111)
        
        self.norm = mcolors.Normalize(vmin=self.min_temp, vmax=self.max_temp)
        self.cmap = cm.get_cmap('viridis')

        self.sm = plt.cm.ScalarMappable(cmap=plt.cm.coolwarm, norm=self.norm)
        self.sm.set_array([])
        self.cbar = self.fig.colorbar(self.sm, ax=self.ax, orientation='vertical')
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().place(x=x_pos, y=y_pos)

        self.ani = animation.FuncAnimation(self.fig, self.update_plot, interval=500, blit=False)

    def update_plot(self, frame):
        temp = self.sensor.read_temp()
        self.temps.append(temp)
        if len(self.temps) > self.max_len:
            self.temps.pop(0)
        self.ax.clear()
        scatter = self.ax.scatter(range(len(self.temps)), self.temps, c=self.temps, cmap=self.cmap, norm=self.norm)
        self.ax.set_xlim(max(0, len(self.temps) - self.max_len), len(self.temps) - 1)
        self.ax.set_ylim(self.min_temp - 5, self.max_temp + 5)
    
        self.ax.set_title(f'Temperature ({int(temp)}°C)')
        self.canvas.draw()
