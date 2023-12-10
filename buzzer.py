import RPi.GPIO as GPIO
import time

BUZZER = 4

def buzzer_init():
	#GPIO.setmode(GPIO.BCM)
	GPIO.setup(BUZZER, GPIO.OUT)
	GPIO.output(BUZZER, GPIO.LOW)

def buzzer_reaction(pitch, duraction):
	period = 1.0 / pitch
	delay = period / 2

	cycles = int(duraction * pitch)
	for i in range(cycles):
		GPIO.output(BUZZER, True)
		time.sleep(delay)
		GPIO.output(BUZZER, False)
		time.sleep(delay)
  
if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    buzzer_init()
    
    buzzer_reaction(600, 0.1)
    time.sleep(0.1)
    buzzer_reaction(600, 0.1)
    time.sleep(0.1)
    buzzer_reaction(600, 0.1)
    time.sleep(1)
    buzzer_reaction(200, 0.1)
    time.sleep(0.1)
    buzzer_reaction(200, 0.1)
    time.sleep(0.1)
    buzzer_reaction(200, 0.1)
