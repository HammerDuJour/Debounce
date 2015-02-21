import datetime
import RPi.GPIO as GPIO
import time

from textme import *

#initialize variables
diff = 2*60*60; # set for two hours
trigger = false;  

#Rasperry Pi GPIO Setup
inputPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(inputPin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
  input = GPIO.input(inputPin)
  
  if (input && !trigger):  # set initial values. Our state has changed and we want to start counting time
    trigger = true;
    triggerTime = datetime.now()
  
  if (input && trigger):
    now = datetime.now();
    if (now - triggerTime > diff):
      print("Send Email")
      #SendEmail()
      
  if (!input):
    trigger = false;
  
