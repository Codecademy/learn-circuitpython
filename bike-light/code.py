from adafruit_circuitplayground.express import cpx
import time

while True:

  if cpx.switch:
    cpx.pixels.fill((30, 0, 0))
    time.sleep(0.5)
    cpx.pixels.fill((0, 0, 0))
    time.sleep(0.5)
  else:
    cpx.pixels.fill((0, 0, 0))