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
import json

		
class Facedetect:
	# Constructor 
	def __init__(self):
		# ======================================
		# HaarCascade Face Detection 
		# ======================================
		self.face_cascade  = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
		self.eye_cascade   = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
		# images in our dataset are classified in 7 categories
		self.label_to_text = { 0:'anger', 1:'disgust', 2:'fear', 3:'happiness', 4:'sadness', 5:'surprise', 6:'neutral' }
		# ======================================
		# parameters Intialized
		# ======================================
		self.img_size    = 48   # img resize as per the input size of model
		self.num_classes = 7 # categories of classes
		# setting font 
		self.font = cv2.FONT_HERSHEY_SIMPLEX
		# fontScale
		self.fontScale = 1
		# Blue color in BGR
		self.color = (255, 0, 0)
		# Line thickness of 2 px
		self.thickness = 2

		# Intialized Camera for Capturing video from webcam
		self.video_capture = cv2.VideoCapture(0)
		self.tflite_model = tf.lite.Interpreter(model_path = "model.tflite")
		self.input_details  = self.tflite_model.get_input_details()
		self.output_details = self.tflite_model.get_output_details()
		self.tflite_model.allocate_tensors()
		
		# Global Variable Initialization
		self.facesCount = 0
		self.NoOfFaces = 0
		self.EmotionsCount = {'anger': 0, 'disgust': 0, 'fear': 0, 'happiness': 0, 'sadness': 0, 'surprise': 0, 'neutral': 0}	
		pass
		#return self
		
	def faceDetect(self):
		try:
			global NoOfFaces
			global EmotionsCount
			while True:
				# Capture frame-by-frame
				ret, frame = self.video_capture.read()
				# The Model is trained on grayscale dataset so we need to convert the frame in grayscale image
				gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

				# detecting mutliscale images
				faces = self.face_cascade.detectMultiScale(
												gray,
												scaleFactor=1.3, # fo scaling of image 
												minNeighbors=3,  # minimum gap in images
												minSize=(30, 30) # minimum size of image to be detected
											)

				NoOfFaces = 0
				EmotionsCount = {'anger': 0, 'disgust': 0, 'fear': 0, 'happiness': 0, 'sadness': 0, 'surprise': 0, 'neutral': 0}	
				# Draw a rectangle around the faces
				try:
					for (x, y, w, h) in faces:
						NoOfFaces += 1
						# rectangle dimensions
						cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
						# Get Region of Interest Frame (Means get the face area of image)
						roi_color = frame[y:y + h, x:x + w]
						# Convert RGB image to Grayscale
						roi_color_gray = cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)
						# Resize Image to required img_size i.e. 48x48 as model expect input of this size
						roi_color_gray = cv2.resize(roi_color_gray, (self.img_size,self.img_size), interpolation = cv2.INTER_AREA)
						roi_color_gray = roi_color_gray.astype(np.float32)
						roi_color_gray  = np.expand_dims(roi_color_gray, axis=2)
						# Pass the image to model for prediction and get the key number of highest probability using argmax function at end
						self.tflite_model.set_tensor(self.input_details[0]['index'], [roi_color_gray])
						self.tflite_model.invoke()
						output_data =self.tflite_model.get_tensor(self.output_details[0]['index'])
						# print(output_data.argmax())
						# Add emotion label as text on image if face is detected with some emotion
						cv2.putText(frame, str(self.label_to_text[output_data.argmax()]), (x,y) , self.font, self.fontScale, self.color, self.thickness, cv2.LINE_AA)
						EmotionsCount[str(self.label_to_text[output_data.argmax()])] =  EmotionsCount[str(self.label_to_text[output_data.argmax()])] + 1
						# print(f'Emotions Count {self.EmotionsCount}')
						# print(f'No Of faces: {self.NoOfFaces}')
						# Display the resulting frame

				except:
					print(exception)
				jsonDataForFile = {'NoOfFaces': NoOfFaces, 'emotionsData': EmotionsCount}
				with open('data.json', 'w', encoding='utf-8') as f:
					json.dump(jsonDataForFile, f, ensure_ascii=False, indent=4)
				cv2.imshow('Video', frame)
				# break the streaming on pressing 'q'
				if cv2.waitKey(1) & 0xFF == ord('q'):
					break
		except:
			print(exception)