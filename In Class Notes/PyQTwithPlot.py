#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 13:34:29 2024
@author: mwelz
"""
import sys
from PyQt5.QtWidgets import (QDialog, QLabel, QGridLayout, QDoubleSpinBox, QApplication, QVBoxLayout, QWidget)
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

#define a PlotCanvas object

class PlotCanvas(FigureCanvas):
 #the initializer/constructor function
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        
        super(PlotCanvas, self).__init__(self.fig)

#define a method to draw the plot
        
    def plot_trajectory(self, v0, angle, h0):
        self.axes.clear()
        gravity = 9.81
        angle_rad = angle * np.pi / 180
        v_x = v0 * np.cos(angle_rad)
        v_y = v0 * np.sin(angle_rad)
        
        # Calculate time of impact
        impact_time = (-v_y - np.sqrt(v_y**2 + 2 * gravity * h0)) / (-gravity)
        
        # Create time points
        t = np.linspace(0, impact_time, 100)
        
        # Calculate trajectory
        x = v_x * t
        y = h0 + v_y * t - 0.5 * gravity * t**2
        
        # Plot the trajectory
        self.axes.plot(x, y, 'b-')
        self.axes.set_xlabel('Distance (m)')
        self.axes.set_ylabel('Height (m)')
        self.axes.set_title('Projectile Trajectory')
        self.axes.grid(True)
        
        # Set reasonable axis limits
        max_distance = v_x * impact_time
        max_height = max(y)
        self.axes.set_xlim(0, max_distance * 1.1)
        self.axes.set_ylim(0, max(max_height * 1.1, h0 * 1.1, 1.0))  # Ensure at least some height is shown
        
        self.fig.tight_layout()
        self.draw()

class Form(QDialog):
    
    def __init__(self):
        super().__init__()
        
        # Create main layout
        main_layout = QVBoxLayout()
        
        # Create inputs and outputs widget
        input_widget = QWidget()
        grid = QGridLayout(input_widget)
        
        # Plot widget
        self.canvas = PlotCanvas(self, width=8, height=4)
        
        # inputs
        
        # launch angle
        self.angleBox = QDoubleSpinBox()
        self.angleBox.setRange(0, 90)
        self.angleBox.setValue(45)
        self.angleBox.setSuffix(" degrees")
        self.angleBox.setDecimals(2)
        angleLabel = QLabel("Initial Launch Angle")
        
        # initial height 
        self.heightBox = QDoubleSpinBox()
        self.heightBox.setRange(0, 100)
        self.heightBox.setValue(0)
        self.heightBox.setSuffix(" m")
        self.heightBox.setDecimals(2)
        heightLabel = QLabel("Initial Height")
        
        # initial velocity
        self.veloBox = QDoubleSpinBox()
        self.veloBox.setRange(0, 100)
        self.veloBox.setValue(10)  # Start with a non-zero value
        self.veloBox.setSuffix(" m/s")
        self.veloBox.setDecimals(2)
        veloLabel = QLabel("Initial Velocity")
        
        # outputs
        self.time = QLabel()
        timeLabel = QLabel("Time of Impact")
        self.maxHeight = QLabel()
        maxHeightLabel = QLabel("Max Height Attained")
        self.distance = QLabel()
        distanceLabel = QLabel("Horizontal Distance Travelled")
        
        # Add widgets to grid
        grid.addWidget(self.angleBox, 0, 1)
        grid.addWidget(angleLabel, 0, 0)
        grid.addWidget(self.veloBox, 1, 1)
        grid.addWidget(veloLabel, 1, 0)
        grid.addWidget(self.heightBox, 2, 1)
        grid.addWidget(heightLabel, 2, 0)
        grid.addWidget(timeLabel, 0, 2)
        grid.addWidget(maxHeightLabel, 1, 2)
        grid.addWidget(distanceLabel, 2, 2)        
        grid.addWidget(self.time, 0, 3)
        grid.addWidget(self.maxHeight, 1, 3)
        grid.addWidget(self.distance, 2, 3) 
        
        # Add widgets to main layout
        main_layout.addWidget(input_widget)
        main_layout.addWidget(self.canvas)
        
        # Connect signals
        self.heightBox.valueChanged.connect(self.updateUi)
        self.angleBox.valueChanged.connect(self.updateUi)
        self.veloBox.valueChanged.connect(self.updateUi)
        
        self.setLayout(main_layout)
        self.setWindowTitle("Projectile Motion Visualizer")
        self.resize(800, 600)  # Set a reasonable initial size
        
        # Initialize with default values
        self.updateUi()
        
    def updateUi(self):
        velocity = self.veloBox.value()
        angle = self.angleBox.value()
        height = self.heightBox.value()
        
        v_y = velocity * np.sin(angle * np.pi / 180)
        v_x = velocity * np.cos(angle * np.pi / 180)
        gravity = 9.81  # gravity 
        
        # Calculate time of impact
        impact = (-v_y - np.sqrt(v_y**2 + 2 * gravity * height)) / (-gravity)
        
        # Other calculations
        hDistance = v_x * impact
        high_time = v_y / gravity
        maxH = height + v_y**2 / (2 * gravity)  # Simplified formula for max height
        
        # Update labels
        self.time.setText("{:.3f} s".format(impact))
        self.distance.setText("{:.3f} m".format(hDistance))
        self.maxHeight.setText("{:.3f} m".format(maxH))
        
        # Update plot
        self.canvas.plot_trajectory(velocity, angle, height)
        
app = QApplication(sys.argv)
form = Form()
form.show()
sys.exit(app.exec_())