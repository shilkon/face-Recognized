import RPi.GPIO as GPIO
import time

BUZZER = 4

def buzzer_init():
	GPIO.setup(BUZZER, GPIO.OUT)
	GPIO.output(BUZZER, False)

def buzzer_sound(pitch, duraction):
	period = 1.0 / pitch
	delay = period / 2

	cycles = int(duraction * pitch)
	for i in range(cycles):
		GPIO.output(BUZZER, True)
		time.sleep(delay)
		GPIO.output(BUZZER, False)
		time.sleep(delay)
  
def buzzer_off():
    GPIO.output(BUZZER, False)
    
def buzzer_success():
    for i in range(10):
        buzzer_sound(800, 0.1)
        time.sleep(0.1)
        
def buzzer_fail():
    for i in range(5):
        buzzer_sound(200, 0.2)
        time.sleep(0.1)
  
if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    buzzer_init()
    
    buzzer_sound(600, 0.1)
    time.sleep(0.1)
    buzzer_sound(600, 0.1)
    time.sleep(0.1)
    buzzer_sound(600, 0.1)
    time.sleep(1)
    buzzer_sound(200, 0.1)
    time.sleep(0.1)
    buzzer_sound(200, 0.1)
    time.sleep(0.1)
    buzzer_sound(200, 0.1)
