#file_ename = movement.py
# Author    =

# Importing Required Libraries
import RPi.GPIO as gpio
import time
import lcdhelper as lcd

# Declare module name 
class Movement:
    # Constructor 
    def __init__(self):
        self.motor1_pin1 = 12
        self.motor1_pin2 = 16
        self.motor2_pin1 = 20
        self.motor2_pin2 = 21
        self.lcdHelper = lcd.LcdHelper()
        # Setting up GPIO's PI
        pass
        #return self
    
    #True is for passing  1
    #false is for passing 0
    
    # forward movement
    # limiting driving time upto 2 seconds
    def initializeBot(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(self.motor1_pin1, gpio.OUT)
        gpio.setup(self.motor1_pin2, gpio.OUT)
        gpio.setup(self.motor2_pin1, gpio.OUT)
        gpio.setup(self.motor2_pin2, gpio.OUT)
    
    def forward(self,seconds = 2):
        self.initializeBot()
        gpio.output(self.motor1_pin1, False)
        gpio.output(self.motor1_pin2, True)
        gpio.output(self.motor2_pin1, True)
        gpio.output(self.motor2_pin2, False)
        time.sleep(seconds)
        self.lcdHelper.clearLcd()
        gpio.cleanup() 

    # backward movement
    # limiting driving time upto 2 seconds
    def backward(self,seconds = 2):
        self.initializeBot()
        
        gpio.output(self.motor1_pin1, True)
        gpio.output(self.motor1_pin2, False)
        gpio.output(self.motor2_pin1, False)
        gpio.output(self.motor2_pin2, True)
        time.sleep(seconds)
        self.lcdHelper.clearLcd()
        gpio.cleanup()

    # right turn 
    # limiting driving time upto 2 seconds
    def right_turn(self,seconds = 2):
        self.initializeBot()
        
        gpio.output(self.motor1_pin1, True)
        gpio.output(self.motor1_pin2, False)
        gpio.output(self.motor2_pin1, True)
        gpio.output(self.motor2_pin2, False)
        time.sleep(seconds)
        self.lcdHelper.clearLcd()
        gpio.cleanup()

    # left turn
    # limiting driving time upto 2 seconds
    def left_turn(self,seconds = 2):
        self.initializeBot()
        
        gpio.output(self.motor1_pin1, False)
        gpio.output(self.motor1_pin2, True)
        gpio.output(self.motor2_pin1, False)
        gpio.output(self.motor2_pin2, True)
        time.sleep(seconds)
        self.lcdHelper.clearLcd()
        gpio.cleanup()
        
    def stop(self):
        self.initializeBot()
        gpio.output(self.motor1_pin1, False)
        gpio.output(self.motor1_pin2, False)
        gpio.output(self.motor2_pin1, False)
        gpio.output(self.motor2_pin2, False)
        gpio.cleanup()
        
