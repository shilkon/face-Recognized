from buzzer import *
from identity import *
from leds import *
from train import name_person

def main():
    while True:
        myClass = face_recognation("trainer", name_person)

        print(myClass.condition, ' ', myClass.name)

        if myClass.condition == Condition.RECOGNIZED:
            buzzer_reaction(400, 2)
            #display here
            led_reaction(500, 2, GREEN_LED)

        else:
            buzzer_reaction(400, 2)
            led_reaction(200, 2, RED_LED)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    
    buzzer_init()
    leds_init()
    
    buzzer_reaction(400, 2)
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

    #main()
