import datetime
import RPi.GPIO as GPIO
import time


#initialize variables
diff = 0; # set for two hours
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
      #SendEmail()
      
  if (!input):
    trigger = false;
  
