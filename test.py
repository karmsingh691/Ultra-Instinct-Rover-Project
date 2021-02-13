# Karmdeep Singh
# 11/03/2020
# Bogie Runt Rover Control Module

# This file contains the algorithm to control the
# Bogie Runt Rover with a 2x7A Roboclaw Motor Controller
# with a Bluetooth Connection to a PS4 Controller 

# Controller Library Source: https://github.com/ArturSpirin/pyPS4Controller

############################### Parts List ####################################

# 1. 2 LiPo Batteries rated at 3.7V connected in Series
# 2. 2x7A RoboClaw Motor Controller
# 3. Raspberry Pi 4B 
# 4. 6 140RPM Motors (3 In Parallel for M1 and M2)
# 5. Mini Breadboard for Motor Connections
# 6. USB Camera (Optional with VLC - Launched Seperately)

 
################################# Wiring ######################################
# 3 wires from the Pi go to the Roboclaw
# - UART TXD (GPIO 14 - Pin 8) goes to S1 pin close to the edge of the board
# - UART RXD (GPIO 14 - Pin 10) goes to S2  pinclose to the edge of the board
# - Pin 6 - Common Ground

################################ Imports ######################################

# pyPS4Controller is imported to use a PS4 controller with the raspberry Pi 
# via Bluetooth

# roboclaw_3 import for motor controller

from pyPS4Controller.controller import Controller
#from serial import Serial
#from time import sleep
from roboclaw_3 import Roboclaw
import sys


if __name__ == "__main__":
    
    address = 0x80 # Hexidecimal Address for specific Roboclaw
    roboclaw = Roboclaw("/dev/ttyS0", 38400) # Source File and Baudrate
    roboclaw.Open() 

class MyController(Controller):
    
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_up_arrow_press(self):
        roboclaw.ForwardM1(address, 100)
        roboclaw.ForwardM2(address, 100)
        print("Forward")
        
    def on_down_arrow_press(self):
        roboclaw.BackwardM1(address,100)
        roboclaw.BackwardM2(address,100)
        print("Backward")
        
    def on_left_arrow_press(self):
        roboclaw.ForwardM1(address,100)
        roboclaw.BackwardM2(address,70)
        print("Left Turn")
        
    def on_right_arrow_press(self):
        roboclaw.BackwardM1(address,70)
        roboclaw.ForwardM2(address,100)
        print("Right Turn")
        
    def on_left_right_arrow_release(self):
        roboclaw.BackwardM1(address,0)
        roboclaw.BackwardM2(address,0)
        print("STOP")
        
    def on_up_down_arrow_release(self):
        roboclaw.BackwardM1(address,0)
        roboclaw.BackwardM2(address,0)
        print("STOP")
    def on_square_press(self):
        sys.exit()

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)
