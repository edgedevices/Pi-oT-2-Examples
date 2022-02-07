##This script uses the RS485 port on the Pi-oT 2 to read a modbus temperature and humidity sensor.
##Depending on the slave device being used, the slave address, register

import minimalmodbus
from time import sleep

ins = minimalmodbus.Instrument('/dev/ttyS0', 1)
ins.serial.timeout = 2
ins.serial.baudrate = 9600

while True:
    try:
        temp = ins.read_register(0,1) #register number=0 , number of decimals=1
        RH = ins.read_register(1,1) #register number=1 , number of decimals=1
        print(temp,RH)
        sleep(1)
    except IOError:
        print("Failed to read from instrument")
