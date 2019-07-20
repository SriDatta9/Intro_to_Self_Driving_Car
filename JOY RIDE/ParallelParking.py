#!/usr/bin/env python
# coding: utf-8

# # Joy Ride - Part 3: Parallel Parking
# In this section you will write a function that implements the correct sequence of steps required to parallel park a vehicle.
# 
# NOTE: for this segment the vehicle's maximum speed has been set to just over 4 mph. This should make parking a little easier.
# 
# ![](https://upload.wikimedia.org/wikipedia/commons/2/26/ParallelParkingAnimation.gif)

# If you have never heard of WASD keys, please check out this [link](https://en.wikipedia.org/wiki/Arrow_keys#WASD_keys).

# In[1]:


get_ipython().run_cell_magic('HTML', '', '<link rel="stylesheet" type="text/css" href="buttonStyle.css">\n<button id="launcher">Launch Car Simulator</button>\n<button id="restart">Restart Connection</button>\n<script src="setupLauncher.js"></script>\n<script src="kernelRestart.js"></script>')


# In[ ]:


# Before running any code changes make sure to click the button "Restart Connection" above first.
# Also make sure to click Reset in the simulator to refresh the connection.
# After making any code changes, make sure to click the button "Restart Connection" above first. Then re-run your code cell (Ctrl+Enter).
# You need to wait for the Kernel Ready message.

car_parameters = {"throttle": 0, "steer": 0, "brake": 0}

def control(pos_x, pos_y, time, velocity):
    """ Controls the simulated car"""
    global car_parameters
    
    
    # TODO: Use WASD keys in simulator to gain an intuitive feel of parallel parking.
    # Pay close attention to the time, position, and velocity in the simulator.
    
    # TODO: Use this information to make decisions about how to set your car parameters
    
    # In this example the car will drive forward for three seconds
    # and then backs up until its pos_y is less than 32 then comes to a stop by braking
    if time < 3.2:
        car_parameters['throttle'] = -0.5
        car_parameters['steer'] = 1
        car_parameters['brake'] = 0
    elif time <6.2:
        car_parameters['throttle'] = -0.7
        car_parameters['steer'] = -1
        car_parameters['brake'] = 0
    elif pos_y <32:
        car_parameters['throttle'] =0.05
        car_parameters['steer'] = 0
        car_parameters['brake'] = 0
    else :
        car_parameters['throttle'] = 0
        car_parameters['steer'] = 0
        car_parameters['brake'] = 1  
    return car_parameters
    
import src.simulate as sim
sim.run(control)


# # Submitting this Project!
# Your parallel park function is "correct" when:
# 
# 1. Your car doesn't hit any other cars.
# 2. Your car stops completely inside of the right lane.
# 
# Once you've got it working, it's time to submit. Submit by pressing the `SUBMIT` button at the lower right corner of this page.

# In[ ]:




