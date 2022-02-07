from gpiozero import MCP3208
from time import sleep

adc0 = MCP3208(channel = 0)
adc1 = MCP3208(channel = 1)
adc2 = MCP3208(channel = 2)
adc3 = MCP3208(channel = 3)
adc4 = MCP3208(channel = 4)
adc5 = MCP3208(channel = 5)
adc6 = MCP3208(channel = 6)
adc7 = MCP3208(channel = 7)

while True:
        print(adc0.value, adc1.value, adc2.value, adc3.value, adc4.value, adc5.value, adc6.value, adc7.value)
        sleep(1)
