import time, signal, sys
import RPi.GPIO as gpio

sys.path.append('./SDL_Adafruit_ADS1x15')
import SDL_Adafruit_ADS1x15

gpio.setmode(gpio.BOARD)
signal.signal(signal.SIGINT, signal_handler)

#  Function Definitions
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

def turnPin_ON_OFF(pin, desiredState):
    currentState = gpio.input(pin)
    if desiredState:
        if currentState == 0:
            gpio.output(pin, gpio.HIGH)
    elif not desiredState:
        if currentState == 1:
            gpio.output(pin, gpio.LOW)

def invertPin(pin):
    currentState = gpio.input(pin)
    if currentState:
        turnPin_ON_OFF(pin, 0)
    elif not currentState:
        turnPin_ON_OFF(pin, 1)

#  Variables
control = {'outPumps': '0',         #  Placeholder Pin Values
           'airFlow': '1',
           'sunLight': '2'}

[gpio.setup(pin, gpio.OUT, initial=gpio.HIGH) for pin in control.values()]

lightTiming = {'on': {'hour': 6,
                      'min': 0},
               'off': {'hour': 18,
                       'min': 0}}

ADS1115 = 0x01	# 16-bit ADC

# Select the gain
gain = 4096  # +/- 4.096V

# Select the sample rate
sps = 250  # 250 samples per second

# Initialise the ADC using the default mode (use default I2C address)
adc = SDL_Adafruit_ADS1x15.ADS1x15(ic=ADS1115)

#  Begin Script Workload
while 1:
    currentTime = {}
    timeData = time.localtime()

    currentTime['hour'] = timeData.tm_hour
    currentTime['min'] = timeData.tm_min

    if currentTime['hour'] == lightTiming['on']['hour'] and currentTime['min'] == lightTiming['on']['min']:
        turnPin_ON_OFF(control['sunLight'], 1)
    elif currentTime['hour'] == lightTiming['off']['hour'] and currentTime['min'] == lightTiming['off']['min']:
        turnPin_ON_OFF(control['sunLight'], 0)

    # Read channels  in single-ended mode using the settings above
    voltsCh0 = adc.readADCSingleEnded(0, gain, sps) / 1000
    rawCh0 = adc.readRaw(0, gain, sps) / 10000

    if (rawCh0 >= 1.5):     # Placeholder Waterlevel Value
        while adc.readRaw(0, gain, sps) / 10000 >= 1.5:
            turnPin_ON_OFF(control['outPumps'], 1)
        turnPin_ON_OFF(control['outPumps'], 0)
    else:
        turnPin_ON_OFF(control['outPumps'], 0)

    time.sleep(60)
