from adafruit_circuitplayground.express import cpx
import time

while True:
  if cpx.switch:
    #red blinkz stuff:
    count = 0
    while count <= 3:
      cpx.pixels.fill((255, 0, 0)) 
      time.sleep(0.5)
      cpx.pixels.fill((0, 0, 0))
      time.sleep(0.5)
      count += 1

    #bedazzle function:
    time.sleep(0.5)
    cpx.pixels[0] = (255, 0, 0)
    time.sleep(0.2)
    cpx.pixels[1] = (255, 85, 0)
    time.sleep(0.2)
    cpx.pixels[2] = (255, 255, 0)
    time.sleep(0.2)
    cpx.pixels[3] = (0, 255, 0)
    time.sleep(0.2)
    cpx.pixels[4] = (34, 139, 34)
    time.sleep(0.2)
    cpx.pixels[5] = (0, 255, 255)
    time.sleep(0.2)
    cpx.pixels[6] = (0, 0, 255)
    time.sleep(0.2)
    cpx.pixels[7] = (0, 0, 139)
    time.sleep(0.2)
    cpx.pixels[8] = (255, 0, 255)
    time.sleep(0.2)
    cpx.pixels[9] = (75, 0, 130)
    time.sleep(0.5)
    cpx.pixels.fill((0, 0, 0))
    time.sleep(0.5)
  else:
    #shut it up:
    cpx.pixels.fill((0, 0, 0))
