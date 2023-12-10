import RPi.GPIO as GPIO
import time

from data_return import Condition

GREEN_LED = 17
RED_LED = 27

def leds_init():
    #GPIO.setmode(GPIO.BCM)
    GPIO.setup(GREEN_LED, GPIO.OUT)
    GPIO.setup(RED_LED, GPIO.OUT)
    GPIO.output(GREEN_LED, False)
    GPIO.output(RED_LED, False)

#cringe
def led_reaction(pitch, duraction, led): 
    period = 1.0 / pitch
    delay = period / 2
    cycles = int(duraction * pitch)
    
    for i in range(cycles):
        GPIO.output(led, True)
        time.sleep(delay)
        GPIO.output(led, False)
        time.sleep(delay)
        GPIO.output(led, True)
        time.sleep(delay)
        GPIO.output(led, False)
        time.sleep(delay)

def led_recognized(condition: Condition):
    if condition == Condition.UNKNOWN:
        led_reaction(500, 2, GREEN_LED)
    else:
        led_reaction(200, 2, RED_LED)

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    leds_init()
    
    GPIO.output(GREEN_LED, True)
    time.sleep(0.2)
    GPIO.output(GREEN_LED, False)
    time.sleep(0.2)
    GPIO.output(GREEN_LED, True)
    time.sleep(0.2)
    GPIO.output(GREEN_LED, False)
    time.sleep(0.2)
    GPIO.output(GREEN_LED, True)
    time.sleep(0.2)
    GPIO.output(GREEN_LED, False)
    time.sleep(0.2)
