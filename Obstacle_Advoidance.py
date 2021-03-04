## Karmdeep Singh
## 3/3/2021
## Ultra Instinct Rover Project
## Version 2.0

## Main Function: Uses HRSC04 Ultrasonic Sensors to avoid obstacles

## Components

# 1. Raspberry Pi 4
# 2. 2x3.7 Li-Po Batteries (Series Connection)
# 3. Anker 20100 mAh battery Pack (For Raspberry Pi)
# 4. 2x7A Roboclaw Dual Motor Controller
# 5. 3 HRSC04 Ultrasonic Range Sensors
# 6. Half-size Breadboard
# 7. 7 1k Ohm Resistors
# 8. 2.2k Ohm Resistor


from roboclaw_3 import Roboclaw
from time import sleep
import time
import RPi.GPIO as GPIO
import PCF8591 as ADC
#import math
import LCD1602 as LCD
#import sys

############################## Pin Declaration ############################

# Front Side HRSC04 Sensor (Trigger and Echo Pins)
F_TRIG = 7 
F_ECHO = 12  

# Right Side HRSC04 Sensor (Trigger and Echo Pins)
R_TRIG = 40
R_ECHO = 38

# Left Side HRSC04 Sensor (Trigger and Echo Pins)
L_TRIG = 31
L_ECHO = 33

# Green/Red LED Pins
Gpin = 15
Rpin = 16

# Pins are set according to board pin numbers
GPIO.setmode(GPIO.BOARD)

# Motor Controller Configuration
address = 0x80
roboclaw = Roboclaw("/dev/ttyS0", 38400)
roboclaw.Open()

############################## Setup Function #############################

# Mainly for other sensors which will be added soon
def setup():
    ADC.setup(0x48)
    GPIO.setup(11, GPIO.IN)
    LCD.init(0x27,1)



######################## Rover Direction Functions ########################
 
def forward():
    roboclaw.ForwardM1(address,80)
    roboclaw.ForwardM2(address, 80)
def backward():
    roboclaw.BackwardM1(address,80)
    roboclaw.BackwardM2(address,80)
def left_rotate():
    roboclaw.ForwardM1(address,80)
    roboclaw.BackwardM2(address,80)
def right_rotate():
    roboclaw.BackwardM1(address,80)
    roboclaw.ForwardM2(address,80)
def stop():
    roboclaw.ForwardM1(address,0)
    roboclaw.BackwardM2(address,0)

######################## Left side Distance Function ######################

def left_distance():
    while True:
        GPIO.setup(L_TRIG,GPIO.OUT)
        GPIO.setup(L_ECHO,GPIO.IN)
        GPIO.output(L_TRIG,False)
        time.sleep(0.01)
        GPIO.output(L_TRIG,True)
        
        time.sleep(0.00001)
        
        GPIO.output(L_TRIG,False)
        l_pulse_start = time.time()
        timeout = l_pulse_start + 0.04
        while GPIO.input(L_ECHO) == 0 and l_pulse_start < timeout:
            l_pulse_start = time.time()
            
        l_pulse_end = time.time()
        timeout = l_pulse_end + 0.04
        while GPIO.input(L_ECHO) == 1 and l_pulse_end < timeout:
            l_pulse_end = time.time()
            
        l_pulse_duration = l_pulse_end-l_pulse_start 
        left_distance = l_pulse_duration * 17150
        
        return left_distance
    
######################## Right side Distance Function #####################

def right_distance():
    while True:
        GPIO.setup(R_TRIG,GPIO.OUT)
        GPIO.setup(R_ECHO,GPIO.IN)
        GPIO.output(R_TRIG,False)
        time.sleep(0.01)
        GPIO.output(R_TRIG,True)
        
        time.sleep(0.00001)
        
        GPIO.output(R_TRIG,False)
        r_pulse_start = time.time()
        timeout = r_pulse_start + 0.04
        while GPIO.input(R_ECHO) == 0 and r_pulse_start < timeout:
            r_pulse_start = time.time()
            
        r_pulse_end = time.time()
        timeout = r_pulse_end + 0.04
        while GPIO.input(R_ECHO) == 1 and r_pulse_end < timeout:
            r_pulse_end = time.time()
            
        r_pulse_duration = r_pulse_end-r_pulse_start
        right_distance = r_pulse_duration * 17150
        
        return right_distance

######################## Obstacle Avoidance Function ######################

def obstacle_avoidance():
    
    # Front Sensor 
    
    while True:
        print("distance measurement in progress")
        GPIO.setup(F_TRIG,GPIO.OUT)
        GPIO.setup(F_ECHO,GPIO.IN)
        GPIO.output(F_TRIG,False)
        time.sleep(0.01)
        GPIO.output(F_TRIG,True)

        time.sleep(0.00001)
        
        GPIO.output(F_TRIG,False)
        f_pulse_start = time.time()
        timeout = f_pulse_start + 0.04
        while GPIO.input(F_ECHO) == 0 and f_pulse_start < timeout:
            f_pulse_start = time.time()
            
        f_pulse_end = time.time()
        timeout = f_pulse_end + 0.04
        while GPIO.input(F_ECHO) == 1 and f_pulse_end < timeout:
            f_pulse_end = time.time()

        f_pulse_duration = f_pulse_end-f_pulse_start
        forward_distance = f_pulse_duration * 17150
        left = left_distance()
        right = right_distance()
        print("Forward Distance:",forward_distance,"cm")
        print("\n")
        print("Left Distance:",left,"cm")
        print("Right Distance:",right,"cm")
        print("\n")
        
        # Conditional Statements when rover "sees" an obstacle
        
        if (forward_distance > 20 and left > 10 and right > 10):
            forward()

        elif (forward_distance < 20 or left < 20 or right < 20 ):
            
            left = left_distance()
            right = right_distance()
            print("Left Distance:",left,"cm")
            print("Right Distance:",right,"cm")
        
            if (forward_distance < 20 and left > 20 and right > 20):
                left_rotate()
                sleep(0.3)
            if (left > 20 and right < 20):
                left_rotate()
                sleep(0.3)
            if (left < 20 and right > 20):
                right_rotate()
                sleep(0.3)

            if (left < 15 and right < 15):
                backward()
                right_rotate()
          
            sleep(0.5)

if __name__ == '__main__':
    try:
        setup()
        obstacle_avoidance()
    except KeyboardInterrupt:
        stop()
        pass


