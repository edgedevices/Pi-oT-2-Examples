import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT) #DO 1
GPIO.setup(19, GPIO.OUT) #DO 2
GPIO.setup(26, GPIO.OUT) #DO 3
GPIO.setup(21, GPIO.OUT) #DO 4
GPIO.setup(20, GPIO.OUT) #DO 5
GPIO.setup(16, GPIO.OUT) #DO 6


while True:
    GPIO.output(13, True)
    sleep(1)
    GPIO.output(13, False)
    
    GPIO.output(19, True)
    sleep(1)
    GPIO.output(19, False)
    
    GPIO.output(26, True)
    sleep(1)
    GPIO.output(26, False)
        
    GPIO.output(21, True)
    sleep(1)
    GPIO.output(21, False)
    
    GPIO.output(20, True)
    sleep(1)
    GPIO.output(20, False)
    
    GPIO.output(16, True)
    sleep(1)
    GPIO.output(16, False)
    
    


