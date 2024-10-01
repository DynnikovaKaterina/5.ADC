import RPi.GPIO as gp
import time
dac = [8, 11, 7, 1, 0, 5, 12, 6]
gp.setmode(gp.BCM) 
gp.setup(dac, gp.OUT) #настраиваем все пины из списка dac на выход
comp = 14
troyka = 13


#функция перевода из десятичного числа в двоичное 
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def adc(v):
    signal = decimal2binary(v)
    gp.output(dac, signal)
    return signal


gp.setup(troyka, gp.OUT, initial= gp.HIGH)
gp.setup(comp, gp.IN)

try:
    while True:
        for i in range (256):
            signal = adc(i)
            time.sleep(0.001)
            U = 3.3 * i / 256
            compVal = gp.input(comp)
            if compVal == 1:
                print("цифровое значение:", i, ", напряжение: ", U)
                break

finally:
    gp.output(dac, 0)
    gp.output(troyka, 0)
    gp.cleanup()
