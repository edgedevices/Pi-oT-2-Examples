import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

while True:
    GPIO.output(26, True)
    
    
    GPIO.output(19, True)
   
    GPIO.output(13, True)
    
    
    GPIO.output(21, True)
    
    GPIO.output(20, True)
    
    GPIO.output(16, True)
    
    


