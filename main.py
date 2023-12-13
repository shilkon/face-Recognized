from identity import *
from train import name_person
from buzzer import *
from leds import *
from oled_display import Display
from time import sleep

def main(display: Display):
    result = face_recognation("trainer", name_person)

    print(result.condition, ' ', result.name)

    if result.condition == Condition.RECOGNIZED:
        led_on(Led.Green)
        display.success()
        buzzer_success()
        sleep(2)
        display.welcome(result.name)
        sleep(5)
        led_off(Led.Green)
    else:
        led_on(Led.Red)
        display.fail()
        buzzer_fail()
        sleep(5)
        led_off(Led.Red)
    display.wait()

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    
    leds_init()
    display = Display()
    buzzer_init()

    try:
        while True:
            main(display)
    except KeyboardInterrupt:
        print('\nExit pressed Ctrl+C')
    finally:
        led_off(Led.Green)
        led_off(Led.Red)
        display.clear()
        buzzer_off()
        GPIO.cleanup()
