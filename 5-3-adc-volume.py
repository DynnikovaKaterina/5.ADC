import RPi.GPIO as gp
import time
dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [9, 10, 22, 27, 17, 4, 3, 2]
gp.setmode(gp.BCM) 
gp.setup(dac, gp.OUT) #настраиваем все пины из области dac на выход
gp.setup(leds, gp.OUT) #настраиваем все пины из области leds на выход
comp = 14
troyka = 13

#функция перевода из десятичного числа в двоичное 
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def slow_adc():
    for i in range(256):
        gp.output(dac, decimal2binary(i))
        time.sleep(0.01)
        compVal = gp.input(comp)
        if compVal == 1:
            return i
    return 255

def adc():
    i0 = 0
    for i in range (7, -1, -1):
        gp.output(dac, decimal2binary(i0 + 2**i))
        time.sleep(0.001)
        compVal = gp.input(comp)
        if compVal == 0:
            i0 += 2**i
    return i0

gp.setup(troyka, gp.OUT, initial= gp.HIGH)
gp.setup(comp, gp.IN)

try:
    while True:
        blinding_lights = (adc() + 1) // 32
        for i in range(blinding_lights):
            gp.output(leds[i], 1)
        for i in range(blinding_lights, 8):
            gp.output(leds[i], 0)

finally:
    gp.output(dac, 0)
    gp.output(troyka, 0)
    gp.cleanup()
