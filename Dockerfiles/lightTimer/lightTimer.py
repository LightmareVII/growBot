import RPi.GPIO as gpio
from growFunctions import turnPin_ON_OFF
import time

lightPin = 5
gpio.setmode(gpio.BCM)
gpio.setup(lightPin, gpio.OUT, initial=gpio.LOW)

lightTiming = {'on': {'hour': 6,
                      'min': 0},
               'off': {'hour': 18,
                       'min': 0}}

while 1:
    currentTime = {}
    timeData = time.localtime()

    currentTime['hour'] = timeData.tm_hour
    currentTime['min'] = timeData.tm_min

    if currentTime['hour'] == lightTiming['on']['hour'] and currentTime['min'] == lightTiming['on']['min']:
        turnPin_ON_OFF(lightPin, 1)
    elif currentTime['hour'] == lightTiming['off']['hour'] and currentTime['min'] == lightTiming['off']['min']:
        turnPin_ON_OFF(lightPin, 0)

    time.sleep(60)
