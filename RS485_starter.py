import minimalmodbus
from time import sleep

ins = minimalmodbus.Instrument('/dev/ttyS0', 1, debug = True)
ins.serial.timeout = 2
ins.serial.baudrate = 9600

while True:
    try:
        temp = ins.read_register(0,1)
        RH = ins.read_register(1,1)
        print(temp,RH)
        sleep(1)
    except IOError:
        print("Failed to read from instrument")
