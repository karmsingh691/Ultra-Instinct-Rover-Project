import RPi.GPIO as GPIO
import os
import Obstacle_Advoidance 
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer
from roboclaw_3 import Roboclaw
host_name = ''  # Change this to your Raspberry Pi IP address
host_port = 

GPIO.setmode(GPIO.BOARD)

# Motor Controller Configuration
address = 0x80
roboclaw = Roboclaw("/dev/ttyS0", 38400)
roboclaw.Open()

class MyServer(BaseHTTPRequestHandler):
    """ A special implementation of BaseHTTPRequestHander for reading data from
        and control GPIO of a Raspberry Pi
    """
    
    def do_HEAD(self):
        """ do_HEAD() can be tested use curl command
            'curl -I http://server-ip-address:port'
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        """ do_GET() can be tested using curl command
            'curl http://server-ip-address:port'
        """
        html = '''
           <html>
           <body style="width:960px; margin: 50px auto;">
           <center><h1>Welcome to the Ultra Instinct Prototype Rover Web Server</h1> </center>
           <center><h2>Activity Monitor</h2> </center>
           <center><p>Current CPU temperature: {}</p>
           <center> <h2>Rover Controls</h2> </center>
           <center><p>The hyperlinks below are used to control the rover</p></center>
           <center><p><a href="/forward"> Forward</a></center>
           <center><p><a href="/backward"> Backward</a></center>
           <center><p><a href="/left"> Left Rotate</a></center>
           <center><p><a href="/right"> Right Rotate</a></center>
           <center><p><a href="/stop"> Stop</a></center>
           <center> <h2>Obstacle Avoidance Program</h2> </center>
           <center><p>The hyperlink below starts the Obstacle Avoidance program on the rover</p></center>
           <center><p><a href="/start"> Start Program</a></center>
           </body>
           </html>
        '''
        temp = os.popen("vcgencmd measure_temp").read()
        self.do_HEAD()
        status = ''
        
        if self.path=='/':
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(37, GPIO.OUT)
        elif self.path=='/forward':

            roboclaw.ForwardM1(address,80)
            roboclaw.ForwardM2(address, 80)

        elif self.path=='/backward':
            
            roboclaw.BackwardM1(address,80)
            roboclaw.BackwardM2(address,80)
            
        elif self.path=='/left':
            
            roboclaw.ForwardM1(address,80)
            roboclaw.BackwardM2(address,80)
            
        elif self.path=='/right':
            
            roboclaw.BackwardM1(address,80)
            roboclaw.ForwardM2(address,80)
            
        elif self.path=='/stop':
            
            roboclaw.ForwardM1(address,0)
            roboclaw.ForwardM2(address, 0)
       
        elif self.path=='/start':
            Obstacle_Advoidance.obstacle_avoidance()

            
        self.wfile.write(html.format(temp[5:], status).encode("utf-8"))


if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
        pass