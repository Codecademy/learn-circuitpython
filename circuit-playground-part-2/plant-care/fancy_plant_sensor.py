from adafruit_circuitplayground.express import cpx
from time import sleep
import touchio
from board import *

# temperature and light sensors, plus light output and sound. thresholds to be adjusted as needed.

while True:
  if cpx.switch:
    if cpx.button_a:
      print('Temperature: ', cpx.temperature)
      if cpx.temperature <= 21.0:
        temp1_count = 0
        while temp1_count < 3:
          cpx.play_tone(262, 1.0)
          temp1_count += 1
        cpx.pixels.fill((0, 102, 255))
      elif cpx.temperature >= 35.0:
        temp2_count = 0
        while temp2_count < 3:
          cpx.play_tone(294, 1.0)
          temp2_count += 1
        cpx.pixels.fill((255, 51, 0))
      else:
          cpx.pixels.fill((0, 255, 0))
          sleep(0.5)
          cpx.pixels.fill((0, 0, 0))

    if cpx.button_b:
      print('Light Value: ', cpx.light)
      cpx.pixels.fill((255, 255, 0))
      sleep(0.5)
      cpx.pixels.fill((0, 0, 0))

  else:
    #moisture sensor. fancy light output included. same thing on thresholds here.
    touch = touchio.TouchIn(A1)
    if cpx.button_a:
      print('Moisture Level: ', touch.raw_value)
      sleep(2.0)
      if touch.raw_value < 1500:
        cpx.play_tone(262, 1.0)
        cpx.pixels.fill((51, 204,51))
        sleep(0.5)
        cpx.pixels[0] = (0, 0, 0)
        sleep(0.2)
        cpx.pixels[1] = (0, 0, 0)
        sleep(0.2)
        cpx.pixels[2] = (0, 0, 0)
        sleep(0.2)
        cpx.pixels[3] = (0, 0, 0)
        sleep(0.2)
        cpx.pixels[4] = (0, 0, 0)
        sleep(0.2)
        cpx.pixels[5] = (0, 0, 0)
        sleep(0.2)
        cpx.pixels[6] = (0, 0, 0)
        sleep(0.2)
        cpx.pixels[7] = (0, 0, 0)
        sleep(0.2)
        cpx.pixels[8] = (0, 0, 0)
        sleep(0.2)
        cpx.pixels[9] = (0, 0, 0)
        cpx.pixels.fill((0, 0, 0))
      else: 
        cpx.pixels.fill((51, 204, 51))
        sleep(0.5)
        cpx.pixels.fill((0, 0, 0))
        cpx.pixels[0] = (51, 204, 51)
        sleep(0.2)
        cpx.pixels[1] = (51, 204, 51)
        sleep(0.2)
        cpx.pixels[2] = (51, 204, 51)
        sleep(0.2)
        cpx.pixels[3] = (51, 204, 51)
        sleep(0.2)
        cpx.pixels[4] = (51, 204, 51)
        sleep(0.2)
        cpx.pixels[5] = (51, 204, 51)
        sleep(0.2)
        cpx.pixels[6] = (51, 204, 51)
        sleep(0.2)
        cpx.pixels[7] = (51, 204, 51)
        sleep(0.2)
        cpx.pixels[8] = (51, 204, 51)
        sleep(0.2)
        cpx.pixels[9] = (51, 204, 51)
        cpx.pixels.fill((51, 204, 51))
        sleep(0.2)
        cpx.pixels.fill((0, 0, 0))
