import time, signal, sys
import RPi.GPIO as gpio

sys.path.append('./SDL_Adafruit_ADS1x15')

import SDL_Adafruit_ADS1x15 

def signal_handler(signal, frame):
        print( 'You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

led1 = 11

gpio.setmode(gpio.BOARD)
gpio.setup(led1, gpio.OUT, initial=gpio.HIGH)
time.sleep(1)

ADS1115 = 0x01	# 16-bit ADC

# Select the gain
gain = 4096  # +/- 4.096V

# Select the sample rate
sps = 250  # 250 samples per second


# Initialise the ADC using the default mode (use default I2C address)
adc = SDL_Adafruit_ADS1x15.ADS1x15(ic=ADS1115)
gpio.output(led1, gpio.LOW)

while (1):
    # Read channels  in single-ended mode using the settings above
    voltsCh0 = adc.readADCSingleEnded(0, gain, sps) / 1000
    rawCh0 = adc.readRaw(0, gain, sps) / 10000
    print(rawCh0)
    if (rawCh0 <= 1.5):
        gpio.output(led1, gpio.HIGH)
    else:
        gpio.output(led1, gpio.LOW)