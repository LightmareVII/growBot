import time, sys
import RPi.GPIO as gpio
from growFunctions import turnPin_ON_OFF

sys.path.append('./SDL_Adafruit_ADS1x15')
import SDL_Adafruit_ADS1x15

outPumpPin = 6
gpio.setmode(gpio.BCM)
gpio.setup(outPumpPin, gpio.OUT, initial=gpio.LOW)

ADS1115 = 0x01	# 16-bit ADC
gain = 4096  # +/- 4.096V
sps = 250  # 250 samples per second
adc = SDL_Adafruit_ADS1x15.ADS1x15(ic=ADS1115)

while 1:
    voltsCh0 = adc.readADCSingleEnded(0, gain, sps) / 1000
    rawCh0 = adc.readRaw(0, gain, sps) / 10000

    if (rawCh0 >= 1.5):  # Placeholder Waterlevel Value - find real value
        while adc.readRaw(0, gain, sps) / 10000 >= 1.5:
            turnPin_ON_OFF(outPumpPin, 1)
        turnPin_ON_OFF(outPumpPin, 0)
    else:
        turnPin_ON_OFF(outPumpPin, 0)
    time.sleep(3)
