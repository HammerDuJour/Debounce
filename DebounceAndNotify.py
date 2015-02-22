import datetime
import RPi.GPIO as GPIO
import time

from textme import *

#initialize variables
debug = true;
diff = 2*60*60; # set for two hours
interval = 60; 
if (debug):
  diff = 2*60;
  interval = 1;

trigger = false;  


#Rasperry Pi GPIO Setup
inputPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(inputPin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
  input = GPIO.input(inputPin)
  print("Get Input")
  print(input)
  
  if (input && !trigger):  # set initial values. Our state has changed and we want to start counting time
    print("Input High First Time, Set Time")
    trigger = true;
    triggerTime = datetime.now()
  
  if (input && trigger):
    print("Trigger Still High, Check Time")
    now = datetime.now();
    if (now - triggerTime > diff):
      print("Send Email")
      #SendEmail()
      
  if (!input):
    print("Trigger Low, Reset")
    trigger = false;
    
sleep(interval);
print("Sleep")
  
