# Alexa-Controlled-Differential-Drive-Bot
AVS (Alexa - Voice - Service Controlled Differential Drive Bot)

### Alexa Contolled Bot Features
* **BOT Movement (Forward/Reverse/Left/Right)**
* **Face and Emotions Detection**

### Overview
The Alexa controlled bot uses the combination of hardward and software. Below are the list of main components

* **Alexa Custom Skill: One can create custom skill using Amazon developer console**
To understand Alexa Custom skill and how to set them up [Alexa Custom Skill kit](https://developer.amazon.com/en-US/docs/alexa/custom-skills/steps-to-build-a-custom-skill.html).
  
  Created the following intents on AVS custom skill
    * Forward
    * Backward
    * Right
    * Left
    * Face_detect
  
* **Raspberry Pi** 
* **H-Bridge to Control Motor**
* **2 wheel Differential Drive kit**
* **USB Webcam for Face and Emotion Detection**
* **Flask_ASK (Flask Amazon alexa skill kit library for setting up flask server locally on rpi to listen to custom amazon alexa skill intent)**
* **[ngrok](https://ngrok.com/): Service to create a tunnel between RPi Flask local server and the Amazon Alexa custom skill**

### Required Libraries:
* **Tensorflow for Raspberry Pi: [Setting up TensorFlow on Raspberry Pi](https://qengineering.eu/install-tensorflow-2.1.0-on-raspberry-pi-4.html)**
* **OpenCV for Image Processing**
* **Lcd I2C Library** 
* **Ngrok for Ngrok Service: [ngrok](https://ngrok.com/download)**
* *Commands.txt* is also in the repo that contains all the commands to install the dependencies and required libraries

### Basic WorkFlow
![Flow Diagram](https://github.com/eengrhassaan/Alexa-Controlled-Differential-Drive-Bot/blob/main/assets/Alexa%20Bot%20Flow.png?raw=true)

### File Brief Overview:
*  **lcdhelper.py:** Helper or custom module to write to 16x2 Character LCD from main thread.
*  **movement.py:** Helper to control the GPIOs of RPi for bot movement
*  **facedetect.py:** Helper to detect the faces and their emotions using trained model file *model.tflite*, face detection will run as a separate thread continuously on the background and store the data on data.json file and whenever the request for face detection received from alexa, main thread will read this data.json file
*  **flask-main.py:** Flask server file that contains the end points for Alexa custom skill intents.
*  **model.tflite:** Originally the model was trained and tested on personal computer using Google Colab and Jupyter Notebook respectively and then converted to tflite model. 

### Work in-progress and future enhancement:
*  *Once the face and the emotion has been identified, the device needs to cheer the person by telling joke or some inspirational quote based on the emotion*
*  *Need to improve the accuracy of model by improving validation accuracy*
