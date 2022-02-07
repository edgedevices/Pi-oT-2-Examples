import RPi.GPIO as GPIO
from time import sleep
from subprocess import call

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT, initial=1)
GPIO.setup(25, GPIO.IN, pull_up_down= GPIO.PUD_UP)


def power_detect():
        if GPIO.input(25) == 0:
                print("Power Fault! Shutting down in 5 seconds..")
                sleep(5)
                if GPIO.input(25) == 0:
                        print("Goodbye!")
                        #call("sudo shutdown now", shell = True)
                else:
                        print("Power Resumed")
        
        GPIO.remove_event_detect(25)
        sleep(0.5)
        GPIO.add_event_detect(25,GPIO.BOTH,callback= power_detect, bouncetime=200)

while True:
        power_detect():
        sleep(1)
