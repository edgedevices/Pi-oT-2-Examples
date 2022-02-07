import minimalmodbus

ins = minimalmodbus.Instrument('/dev/ttyS0', 1, debug = True)
ins.serial.timeout = 2
ins.serial.baudrate = 9600

while True:
    temp = ins.read_register(0,1)
    RH = ins.read_register(1,1)
    print(temp,RH)

