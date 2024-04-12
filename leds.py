import RPi.GPIO as GPIO
import time

from enum import IntEnum

class Led(IntEnum):
    Green = 17
    Red = 27

def leds_init():
    GPIO.setup(Led.Green, GPIO.OUT)
    GPIO.setup(Led.Red, GPIO.OUT)
    GPIO.output(Led.Green, False)
    GPIO.output(Led.Red, False)

def led_on(led: int):
    GPIO.output(led, True)
    
def led_off(led: int):
    GPIO.output(led, False)

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    leds_init()
    
    led_off(Led.Red)
    led_on(Led.Green)
    time.sleep(0.2)
    led_off(Led.Green)
    time.sleep(0.2)
    led_on(Led.Green)
    time.sleep(0.2)
    led_off(Led.Green)
    time.sleep(0.2)
    led_on(Led.Green)
    time.sleep(0.2)
    led_off(Led.Green)
    time.sleep(0.2)
