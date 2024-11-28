import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpu6050 import mpu6050

class MPU6050Plotter:
    def __init__(self, root, w=451, h=185, x_pos=14.0, y_pos=403.0, max_points=100):
        self.root = root
        self.sensor = mpu6050(0x68)
        self.max_points = max_points
        self.x_data = [0] * self.max_points
        self.y_data = [0] * self.max_points
        self.z_data = [0] * self.max_points

        dpi = 100
        self.fig = Figure(figsize=(w/dpi, h/dpi), dpi=dpi)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_ylim([-20, 20])
        
        self.ax.set_title("Vibration 1")

        self.line_x, = self.ax.plot(self.x_data, label='X Axis')
        self.line_y, = self.ax.plot(self.y_data, label='Y Axis')
        self.line_z, = self.ax.plot(self.z_data, label='Z Axis')

        self.ax.legend()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.draw()

        self.canvas.get_tk_widget().place(x=x_pos, y=y_pos)

        self.update_plot()

    def read_accel_data(self):
        accel_data = self.sensor.get_accel_data()
        return accel_data['x'], accel_data['y'], accel_data['z']

    def update_plot(self):
        x_acc, y_acc, z_acc = self.read_accel_data()

        self.x_data.append(x_acc)
        self.y_data.append(y_acc)
        self.z_data.append(z_acc)

        if len(self.x_data) > self.max_points:
            self.x_data.pop(0)
            self.y_data.pop(0)
            self.z_data.pop(0)

        self.line_x.set_ydata(self.x_data)
        self.line_y.set_ydata(self.y_data)
        self.line_z.set_ydata(self.z_data)

        self.canvas.draw()

        self.root.after(100, self.update_plot)