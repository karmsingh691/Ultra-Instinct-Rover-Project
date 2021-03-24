# **Ultra-Instinct Prototype Rover Project**

This is a personal project with the goal to create a fully autonomous Mars Rover. Various different sensors and techniques will be utilized to achieve autonomous travel.


## Objectives and Motivation

I had worked on a large scale Mars Rover at UW Tacoma that could not be finished due to COVID restrctions. I took it upon myself to construct a rover of my own to practice Python programming, Embedded Systems design, PCB design and many other technical skills that I hope to learn and improve on.

# Table of Contents

- [Parts List](#parts-list)
- [Current Build](#current-build)
- [Mobilizing the Rover](#mobilizing-the-rover)
      * [Remote Control via PS4 Controller](#remote-control-rover-via-PS4-controller)
- [Remote Control via PS4 Controller](#remote-control-rover-via-PS4-controller)
- [Obstacle Avoiding Rover](#obstacle-avoiding-rover)
- [Youtube Playlist](#youtube-playlist)
- [Future Plans](#future-plans)

## Parts List

The following is the up-to-date parts list for the project. Links are provided when applicable.

1. Bogie Runt Rover Kit from ServoCity (Includes 6 140RPM Motors) -->  https://www.servocity.com/bogie-runt-rover/
2. 2 Lithium Polymer batteries rated at 3.7V 2000 mAh --> https://www.sparkfun.com/products/13855
3. 2x7A Roboclaw Motor Controller --> https://www.servocity.com/roboclaw-2x7a-motor-controller/
4. Raspberry Pi 4 (8GB RAM)
5. Half-Size Breadboard
6. 3 HD-SR04 Ultra Sonic Range Sensors
7. Anker 20100 mAh Battery Pack
8. PS4 Controller
9. Jumper Wires

## Current Build

The images below show version 2.0 of the current rover design. From version 1, there were a lot of design changes made to make the rover more streamlined. Removed sensors that may not serve a function for autonomous travel as well as new battery supply for the Pi, rearranging the components to help with the center of mass and added 2 more ultra sonic sensors on the left and right side.

![IMG_0805](https://user-images.githubusercontent.com/55263663/109580813-192acc00-7ab0-11eb-8c98-af28e35127a8.jpg)
![IMG_0808](https://user-images.githubusercontent.com/55263663/109580868-2fd12300-7ab0-11eb-835c-0d006bbe778e.jpg)

## Mobilizing the Rover

At the current build, there are 3 ways to mobilize the rover. One of them uses a PS4 controller, the bluetooth functionality of the Raspberry Pi, pyPS4 library and the libraries that control the Roboclaw Motor Controller. The second method uses the Ultra sonic sensors to help the rover avoid obtructions in its path without physical human interaction. The third method uses a HTML based webserver based on Python libraries to control the rover's movements.

## Remote Control Rover via PS4 Controller

This method requires specific libraries with Python to work properly. One of them is the Roboclaw libraries that will be used for the remainder of the project as this motor controller will be used to control all six motors. The full library with sample code is provided by Basic Micron here: https://www.basicmicro.com/downloads. 

This link will aid in setting up the controller with the raspberry pi --> https://resources.basicmicro.com/packet-serial-with-the-raspberry-pi-3/

NOTE:The sample code imports "roboclaw" at the top. This will only work for Python 2. The file marked as "roboclaw_3" must be imported instead for Python 3

The other library to be used is from this Github page --> https://github.com/ArturSpirin/pyPS4Controller

Using a combination of the sample code from Basic Micron and the pyPS4 functions, I was able to control the movement of the rover with a PS4 controller. Basic movements include Forward, Backward, Left Rotate, and Right Rotate

The code for this part of the project is listed as "test.py" --> https://github.com/karmsingh691/Ultra-Instinct-Rover-Project/blob/main/test.py

## Obstacle Avoiding Rover 

The next step for this project was to get some autnomous travel going. For the current build, I have three Ultra Sonic Range sensors on the front of the rover to aid in detecting obstrcutions in the rovers path. 

### How the Sensors work (HD-SC04)

In the most basic terms, the sensor has 2 "eyes". One of the eyes sends a sonic pulse towards an object. The pulse will bounce back into the other eye of the sensor. The time it takes for that pulse to be transmitted and received is calculated into a distance based on the speed of sound in air which is collected by the Raspberry Pi.

### How the Code works

The code I have written is listed as "Obstacle Advoidance.py" in the Github --> https://github.com/karmsingh691/Ultra-Instinct-Rover-Project/blob/main/Obstacle_Advoidance.py

The algorithm works as follows: 

The front sensors' responsibility is to detect objects that may be less than 30 cm from the rover. If there is a object, the left and right sensors will also report back if they see an objects less than 15 cm from the rover. If one side has a clearance of more than 15cm, the rover is instrcuted to rotate in the direction of the least amount of the obstructions. This is looped forever so that the rover can continue avoiding obstacles that it can detect.

## Using a Webserver to control the Rover

### HTML Based Server

### Server using Node-RED

## Youtube Playlist

I have created a Youtube playlist that discusses the design of the rover for boith Version 1.0 and 2.0 as well as live demonstrations

--> https://youtube.com/playlist?list=PL0pn1a9KXvgb6V_3VPD3S1EDgnbPxO6Ip

## Future Plans

I am currently working on using OpenCV functions for lane tracking algorithms and learing Autodesk Eagle for PCB design.
