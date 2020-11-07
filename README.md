# Karmdeep Singh
# 11/03/2020
# Bogie Runt Rover Control Module

# This file contains the algorithm to control the
# Bogie Runt Rover with a 2x7A Roboclaw Motor Controller
# with a Bluetooth Connection to a PS4 Controller 

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
