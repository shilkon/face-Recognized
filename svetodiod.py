import RPi.GPIO as IO
import time

from data_return import Condition

LED = 40
IO.cleanup()
IO.setmode (IO.BOARD)
IO.setup(LED,IO.OUT)
IO.output(LED, IO.LOW)

def Led(pitch, duraction):
  period = 1.0 / pitch
  delay = period / 2
  cycles = int(duraction * pitch)
  for i in range(cycles):
    IO.output(LED, IO.HIGHT)
    time.sleep(delay)
    IO.output(LED, IO.LOW)
    time.sleep(delay)
    IO.output(LED, IO.HIGHT)
    time.sleep(delay)
    IO.output(LED, IO.LOW)
    time.sleep(delay)

def led_recognized(condition: Condition):
  if condition == Condition.UNKNOWN:
    Led(500, 2)
  else:
    Led(200, 2)

