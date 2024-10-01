import RPi.GPIO as gp
dac = [8, 11, 7, 1, 0, 5, 12, 6]
gp.setmode(gp.BCM) 
gp.setup(dac, gp.OUT) #настраиваем все пины из списка dac на выход
comp = 
troyka = 

#функция перевода из десятичного числа в двоичное 
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

#функция возвращает десятичное число, пропорциональное напряжению клемме S тройка-модуля
def adc():
    return( gp.input(troyka) )


gp.setup(troyka, gp.OUT, initial= )
gp.setup(comp, gp.IN)

try:
    adc()

finally:
    gp.output(dac, 0)
    gp.cleanup()