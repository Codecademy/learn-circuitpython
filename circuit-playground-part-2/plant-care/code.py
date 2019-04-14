from adafruit_circuitplayground.express import cpx
import touchio
from board import *

touch = touchio.TouchIn(A1)

while True:
  if cpx.switch:
    if cpx.button_a:
      print("Temperature:", cpx.temperature)
    if cpx.button_b:
      print("Light value:", cpx.light)
  else:
    if cpx.button_a:
      print("Moisture:", touch.raw_value)
    if cpx.button_b:
      if touch.raw_value > 1500:
        print("Water me!")
      else:
        print("I'm good, thanks!")
