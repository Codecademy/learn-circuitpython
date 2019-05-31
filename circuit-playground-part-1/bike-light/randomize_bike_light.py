from adafruit_circuitplayground.express import cpx
import random
import time

while True:
  if cpx.switch:
    color_tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cpx.pixels[random.randint(0, 9)] = color_tup
    time.sleep(.5)
    cpx.pixels.fill((0, 0, 0))
    time.sleep(.5)
  else:
    cpx.pixels.fill((0, 0, 0))