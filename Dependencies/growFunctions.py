import RPi.GPIO as gpio


def turnPin_ON_OFF(pin, desiredState):
    currentState = gpio.input(pin)
    if desiredState:
        if currentState == 0:
            gpio.output(pin, gpio.HIGH)
    elif not desiredState:
        if currentState == 1:
            gpio.output(pin, gpio.LOW)
