# ==================================
# Importing libraries
# ==================================
import time

import movement as move
import lcdhelper as lcd
import facedetect as faces

import threading
import queue
import cv2
import numpy as np
# import tensorflow as tf 


import logging
import os

import json
from flask import Flask
from flask_ask import Ask, request, session, question, statement
import RPi.GPIO as GPIO

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

STATUSON = ['on','high']
STATUSOFF = ['off','low']

# Face Detection Class
#file_ename = movement.py
# Author    =

## Importing Required Libraries

# ==================================
# Importing libraries
# ==================================

# For video streaming and face detection  
from logging import exception
import cv2
# operating system code library for file open and creation
import os
# using to make arrays anfd apply mathematical expressions
import numpy as np

# using for convolution technique 
import tensorflow as tf 
from tensorflow import keras


@ask.launch
def launch():
	speech_text = 'Welcome to Raspberry Pi Automation.'
	return question(speech_text).reprompt(speech_text).simple_card(speech_text)

# Forward Movement Intent
@ask.intent('forward')
def forward():
	print("Moving bot forward")
	lcdHelper.clearLcd()
	lcdHelper.writeToLcd("Moving Forward")
	global botMovementThread
	
	botMovementThread = threading.Thread(target=botMovementHelper.forward)
	botMovementThread.daemon = True 
	botMovementThread.start()
	speech_text = 'ok bot Moved Forward'
	return question(speech_text).reprompt(speech_text).simple_card('Bot Moving Forward', speech_text)

# backward Movement Intent
@ask.intent('backward')
def backward():
	print("Moving bot backward")
	lcdHelper.clearLcd()
	lcdHelper.writeToLcd("Moving backward")
	global botMovementThread
	
	botMovementThread = threading.Thread(target=botMovementHelper.backward)
	botMovementThread.daemon = True 
	botMovementThread.start()
	speech_text = 'ok bot Moved backward'
	return question(speech_text).reprompt(speech_text).simple_card('Bot Moving backward', speech_text)

# right_turn Movement Intent
@ask.intent('rightturn')
def right_turn():
	print("Moving bot right_turn")
	lcdHelper.clearLcd()
	lcdHelper.writeToLcd("Moving Bot right")
	global botMovementThread
	
	botMovementThread = threading.Thread(target=botMovementHelper.right_turn)
	botMovementThread.daemon = True 
	botMovementThread.start()
	speech_text = 'ok bot Moved right turn'
	return question(speech_text).reprompt(speech_text).simple_card('Bot Moving right turn', speech_text)


# left_turn Movement Intent
@ask.intent('leftturn')
def left_turn():
	print("Moving bot left_turn")
	lcdHelper.clearLcd()
	lcdHelper.writeToLcd("Moving Bot left")
	global botMovementThread
	
	botMovementThread = threading.Thread(target=botMovementHelper.left_turn)
	botMovementThread.daemon = True 
	botMovementThread.start()
	speech_text = 'ok bot Moved left turn'
	return question(speech_text).reprompt(speech_text).simple_card('Bot Moving left turn', speech_text)

# stop Movement Intent
@ask.intent('stopbot')
def stop():
	print("Stopping bot")
	lcdHelper.clearLcd()
	lcdHelper.writeToLcd("stopping bot")
	global botMovementThread
	
	botMovementThread = threading.Thread(target=botMovementHelper.stop)
	botMovementThread.daemon = True 
	botMovementThread.start()
	speech_text = 'ok bot Stopped'
	return question(speech_text).reprompt(speech_text).simple_card('Bot Stopped', speech_text)

@ask.intent('emotiondetection')
def face_detect():
	print("Detecting Face")
	lcdHelper.clearLcd()
	lcdHelper.writeToLcd("Detecting face")
	speech_text = 'detecting emotions'

	with open('data.json') as f:
  		data = json.load(f)
	print(data)
	emotionsCount = data['emotionsData']
	noOfFaces = data['NoOfFaces']

	speech_text = "\r\nNumber of Faces Detected: " + str(noOfFaces) + '\r\n'
	speech_text = speech_text + '\r\nEmotions Detected: \r\n\r\n'

	if(emotionsCount):
		for key,value in emotionsCount.items():
			if value>0:
				speech_text.replace('0', '')
				speech_text = speech_text + str(key) + ' ' + str(value) + '\r\n'
				 
	print(emotionsCount)
	print(noOfFaces)
	print(speech_text)
	return question(speech_text).reprompt(speech_text).simple_card()

@ask.intent('AMAZON.HelpIntent')
def help():
	speech_text = 'You can say hello to me!'
	return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)


@ask.session_ended
def session_ended():
	return "{}", 200


if __name__ == '__main__':
	if 'ASK_VERIFY_REQUESTS' in os.environ:
		verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
		if verify == 'false':
			app.config['ASK_VERIFY_REQUESTS'] = False
	
	# Initializing Global Variables Here
	global botMovementThread
	global emotionDetectionThread
	global botMovementQueue
	global emotionDetectionQueue
	global lcdHelper 
	global botMovementHelper
	global queues1
	global queues2
	global emotionDetectionHelper
			

	# Initializing LCD
	lcdHelper = lcd.LcdHelper()
	lcdHelper.clearLcd()

	# Initializing botMovementHelper 
	botMovementHelper = move.Movement()
	botMovementHelper.stop()

	# Thread Creation for Bot Movement
	botMovementThread = threading.Thread(target=botMovementHelper.initializeBot)
	botMovementThread.start()

	global emotionsCount
	global noOfFaces

	noOfFaces = 0
	emotionsCount = {'anger': 0, 'disgust': 0, 'fear': 0, 'happiness': 0, 'sadness': 0, 'surprise': 0, 'neutral': 0}
	# Initializing Emotion Detection Helper
	emotionDetectionHelper = faces.Facedetect()
	emotionDetectionThread = threading.Thread(target = emotionDetectionHelper.faceDetect)
	emotionDetectionThread.start()
	time.sleep(2)
	
	# Thread Creation for 
	app.run(debug=True)