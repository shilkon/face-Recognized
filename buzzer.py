import RPi.GPIO as GPIO
import time

Buzzer = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(Buzzer, GPIO.OUT)
GPIO.output(Buzzer, GPIO.LOW)

def Buzz(pitch, duraction):
	period = 1.0 / pitch
	delay = period / 2

	cycles = int(duraction * pitch)
	for i in range(cycles):
		GPIO.output(Buzzer, True)
		time.sleep(delay)
		GPIO.output(Buzzer, False)
		time.sleep(delay)
try:
	while True:
		print('Enter Pitch 200...2000')
		Pitch = int(input())
		print('Enter Duraction, seconds: ')
		Duraction = int(input())
		Buzz(Pitch, Duraction)
except KeyboardInterrupt:
	print('Exit pressed Ctrl+C')
	GPIO.cleanup()
finally:
	GPIO.cleanup()
	print('End')