#!/usr/bin/python

import datetime
import RPi.GPIO as GPIO
import time

#from textme import *

#initialize variables
debug = True;
diff = datetime.timedelta(hours=2); # set for two hours
interval = 60; 
if (debug):
  diff = datetime.timedelta(minutes=2);
  interval = 1;

trigger = False;  


#Rasperry Pi GPIO Setup
inputPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(inputPin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
  input = GPIO.input(inputPin)
  print("Get Input")
  print(input)
  
  if (input and not(trigger)):  # set initial values. Our state has changed and we want to start counting time
    print("Input High First Time, Set Time")
    trigger = True;
    triggerTime = datetime.datetime.now()
  
  if (input and trigger):
    print("Trigger Still High, Check Time")
    now = datetime.datetime.now();
    if (now - triggerTime > diff):
      print("Send Email")
      #SendEmail()
      trigger = False
      
  if (not(input)):
    print("Trigger Low, Reset")
    trigger = False;
    
  print("Sleep")
  time.sleep(interval)
