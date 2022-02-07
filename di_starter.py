
import RPi.GPIO as GPIO
from time import sleep

##GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN,pull_up_down=GPIO.PUD_DOWN )
GPIO.setup(27, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

    

while True:
    di1 = GPIO.input(12)
    di2 = GPIO.input(22)
    di3 = GPIO.input(27)
    di4 = GPIO.input(17)
    sleep(.5)
    print(di1,di2,di3,di4)
