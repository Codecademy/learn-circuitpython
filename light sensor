from adafruit_circuitplayground.express import cpx
from time import sleep
import touchio
from board import *

while True:
  if cpx.light <10:
      cpx.pixels[0] = (10,0,0)
      cpx.pixels[9] = (10,0,0)
      for i in range(1,9,1):
        cpx.pixels[i] = (0,0,0)
  elif cpx.light <35:
      for i in range(2,8,1):
        cpx.pixels[i] = (0,0,0)
      cpx.pixels[1] = (10,5,0)
      cpx.pixels[8] = (10,5,0)
      cpx.pixels[0] = (10,0,0)
      cpx.pixels[9] = (10,0,0)
  elif cpx.light <50:
      for i in range(3,7,1):
        cpx.pixels[i] = (0,0,0)
      cpx.pixels[1] = (10,5,0)
      cpx.pixels[8] = (10,5,0)
      cpx.pixels[0] = (10,0,0)
      cpx.pixels[9] = (10,0,0)
      cpx.pixels[2] = (10,10,0)
      cpx.pixels[7] = (10,10,0)
  elif cpx.light <200:
      for i in range(4,6,1):
        cpx.pixels[i] = (0,0,0)
      cpx.pixels[0] = (10,0,0)
      cpx.pixels[9] = (10,0,0)
      cpx.pixels[1] = (10,5,0)
      cpx.pixels[8] = (10,5,0)
      cpx.pixels[2] = (10,10,0)
      cpx.pixels[7] = (10,10,0)
      cpx.pixels[3] = (0,10,0)
      cpx.pixels[6] = (0,10,0)
  elif cpx.light > 200:
      cpx.pixels[1] = (10,5,0)
      cpx.pixels[8] = (10,5,0)
      cpx.pixels[0] = (10,0,0)
      cpx.pixels[9] = (10,0,0)
      cpx.pixels[2] = (10,10,0)
      cpx.pixels[7] = (10,10,0)
      cpx.pixels[3] = (0,10,0)
      cpx.pixels[6] = (0,10,0)
      cpx.pixels[4] = (10,10,10)
      cpx.pixels[5] = (10,10,10)
  print(cpx.light)
