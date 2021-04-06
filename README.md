# **Ultra-Instinct Prototype Rover Project**

This is a personal project with the goal to create a fully autonomous Mars Rover. Various different sensors and techniques will be utilized to achieve autonomous travel.


## Objectives and Motivation

I had worked on a large scale Mars Rover at UW Tacoma that could not be finished due to COVID restrctions. I took it upon myself to construct a rover of my own to practice Python programming, Embedded Systems design, PCB design and many other technical skills that I hope to learn and improve on.

# Table of Contents

- [Parts List](#parts-list)
- [Current Build](#current-build)
- [Mobilizing the Rover](#mobilizing-the-rover)
     * [Remote Control via PS4 Controller](#remote-control-rover-via-PS4-controller)
     * [Remote Control via Webservers](#remote-control-via-webservers)
       + [HTML Based Server](#html-based-server)
       + [Node-RED Server](#node-red-server)
 - [Autonomous Rover Programs](#autonomous-rover)
   * [Obstacle Avoiding Rover](#obstacle-avoiding-rover)
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

# Current Build

The images below show version 2.0 of the current rover design. From version 1, there were a lot of design changes made to make the rover more streamlined. Removed sensors that may not serve a function for autonomous travel as well as new battery supply for the Pi, rearranging the components to help with the center of mass and added 2 more ultra sonic sensors on the left and right side.

## PCB Addition

To save space on the rover, I had converted the breadboard circuit that connects the Ultrasonic sensors and the motors to a PCB design that I developed in Autodesk Eagle. Updated images are found below. I learned how to build the board through a free Udemy Course which covers the basics and I was able to print, solder and implement the board within 2 weeks. This will allow me to use the breadboard to prototype other ciruits for different sensors.

Check out the Youtube video where I discuss my design and the process --> https://www.youtube.com/watch?v=KzVD4Ft9z3k&t=2s

Udemy Course --> https://www.udemy.com/course/pcb-design-eagle/

![Caption](https://user-images.githubusercontent.com/55263663/113646131-0b331280-963d-11eb-8094-8f6ab8cfa5e2.jpg)
<div align="center">The derogatory term “scrub” means several different things. One definition is someone (especially a game player) who is not good at something (especially a game). By this definition, we all start out as scrubs, and there is certainly no shame in that. I mean the term differently, though. A scrub is a player who is handicapped by self-imposed rules that the game knows nothing about. A scrub does not play to win.</div>
![IMG_0808](https://user-images.githubusercontent.com/55263663/109580868-2fd12300-7ab0-11eb-835c-0d006bbe778e.jpg)

# Mobilizing the Rover

At the current build, there are 3 ways to mobilize the rover. One of them uses a PS4 controller, the bluetooth functionality of the Raspberry Pi, pyPS4 library and the libraries that control the Roboclaw Motor Controller. The second method uses the Ultra sonic sensors to help the rover avoid obtructions in its path without physical human interaction. The third method uses a HTML based webserver based on Python libraries to control the rover's movements.

## Remote Control Rover via PS4 Controller

This method requires specific libraries with Python to work properly. One of them is the Roboclaw libraries that will be used for the remainder of the project as this motor controller will be used to control all six motors. The full library with sample code is provided by Basic Micron here: https://www.basicmicro.com/downloads. 

This link will aid in setting up the controller with the raspberry pi --> https://resources.basicmicro.com/packet-serial-with-the-raspberry-pi-3/

NOTE:The sample code imports "roboclaw" at the top. This will only work for Python 2. The file marked as "roboclaw_3" must be imported instead for Python 3

The other library to be used is from this Github page --> https://github.com/ArturSpirin/pyPS4Controller

Using a combination of the sample code from Basic Micron and the pyPS4 functions, I was able to control the movement of the rover with a PS4 controller. Basic movements include Forward, Backward, Left Rotate, and Right Rotate

The code for this part of the project is listed as "test.py" --> https://github.com/karmsingh691/Ultra-Instinct-Rover-Project/blob/main/test.py

## Remote Control via Webservers

### HTML Based Server

This server is constructed with Python's built-in https server library and allows users to create an HTML based server with Python. I found a website that had used the library to control the GPIO pins of a Raspberry Pi and be able to turn off an on an LED through a local webserver. Using the template, I programmed additional HTML code to add features to the server that would allow me to control the rover's movements by clicking hyperlinks. The webserver also keeps track of the CPU temperature of the Pi and can also initiate the obstacle avoidance program with a click of a button. 

<img width="1175" alt="Screen Shot 2021-03-29 at 5 33 50 PM" src="https://user-images.githubusercontent.com/55263663/112916259-0efeec00-90b5-11eb-9e63-109e29d04f2a.png">

The built-in library is a great way to get started with creating webservers. I had only used HTML to customize the server design but we could also use CSS and Javascript to further improve the web server's UI. 

Here is the source code I used to build this webserver: --> https://www.e-tinkers.com/2018/04/how-to-control-raspberry-pi-gpio-via-http-web-server/


### Node-RED Server

Details coming soon

# Autonomous Rover 

The following section discusses the programs and techniques that I have used to get the rover to move autonomously without human interaction. The main program so far is based on using sensors to help the rover avoid obstructions in its path. 

## Obstacle Avoiding Rover 

The next step for this project was to get some autnomous travel going. For the current build, I have three Ultra Sonic Range sensors on the front of the rover to aid in detecting obstrcutions in the rovers path. 

### How the Sensors work (HD-SC04)

In the most basic terms, the sensor has 2 "eyes". One of the eyes sends a sonic pulse towards an object. The pulse will bounce back into the other eye of the sensor. The time it takes for that pulse to be transmitted and received is calculated into a distance based on the speed of sound in air which is collected by the Raspberry Pi.

### How the Code works

The code I have written is listed as "Obstacle Advoidance.py" in the Github --> https://github.com/karmsingh691/Ultra-Instinct-Rover-Project/blob/main/Obstacle_Advoidance.py

The algorithm works as follows: 

The front sensors' responsibility is to detect objects that may be less than 30 cm from the rover. If there is a object, the left and right sensors will also report back if they see an objects less than 15 cm from the rover. If one side has a clearance of more than 15cm, the rover is instrcuted to rotate in the direction of the least amount of the obstructions. This is looped forever so that the rover can continue avoiding obstacles that it can detect.


## Youtube Playlist

I have created a Youtube playlist that discusses the design of the rover for boith Version 1.0 and 2.0 as well as live demonstrations

--> https://youtube.com/playlist?list=PL0pn1a9KXvgb6V_3VPD3S1EDgnbPxO6Ip

## Future Plans

I am currently working on using OpenCV functions for lane tracking algorithms and learing Autodesk Eagle for PCB design.
