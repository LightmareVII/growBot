import RPi.GPIO as gpio
from time import sleep

m1 = 11
m2 = 13
#s1 = 10

gpio.setmode(gpio.BOARD)

gpio.setup(m1, gpio.OUT, initial=gpio.HIGH)
gpio.setup(m2, gpio.OUT, initial=gpio.HIGH)
#gpio.setup(s1, gpio.IN)

#gpio.output(m1, gpio.HIGH)
#gpio.output(m2, gpio.HIGH)
#sleep(2)
#gpio.output(m1, gpio.LOW)
#gpio.output(m2, gpio.LOW)
