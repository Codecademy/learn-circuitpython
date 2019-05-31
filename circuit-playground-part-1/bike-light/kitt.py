# K.I.T.T. Bike Light
#
# Use Button A to change color
# Use Button B to change style
# Use Slide Switch to power on/off
# Ride safe and don't hassle the Hoff
#
# Created by Eric Gross. Sublime Text on MacBook Pro (5/27/2019)
# Codecademy: Learn Hardware Programming with CircuitPython - Bike Light

from adafruit_circuitplayground.express import cpx
import time

colorIndex = 0
functionIndex = 0
rainbow = ((255, 0, 0), (255, 85, 0), (255, 255, 0), (0, 255, 0), (34, 139, 34), (0, 255, 255), (0, 0, 255), (0, 0, 139), (255, 0, 255), (75, 0, 130), (0,0,0))

###### Function to Change Color ######
def checkPress(colorIndex):
  if cpx.button_a:
    colorIndex += 1
    if colorIndex > 10:
      return 0
  return colorIndex

###### Function to Change Function ######
def functionPress(functionIndex):
  if cpx.button_b:
    functionIndex += 1
    if functionIndex > 2:
      return 0
  return functionIndex

###### Color and Blinking ######
def blinkLed(colorIndex, d = 0.5, ledIndex = 10, turnOff = True):
  if ledIndex == 10:
    cpx.pixels.fill((rainbow[colorIndex][0], rainbow[colorIndex][1], rainbow[colorIndex][2]))
    time.sleep(d)
  else:
    cpx.pixels[ledIndex] = (rainbow[colorIndex][0], rainbow[colorIndex][1], rainbow[colorIndex][2])
    time.sleep(d)
  if turnOff == True:
  	cpx.pixels.fill((0, 0, 0))
  	time.sleep(d)
  return

def kitt(d = 0.1):
  global colorIndex
  colorIndex = checkPress(colorIndex)
  for x in range(0, 10):
    blinkLed(10, d, x, False)
    blinkLed(colorIndex, 0, x, False)
  time.sleep(d)
  colorIndex = checkPress(colorIndex)
  for x in range(9, -1, -1):
    blinkLed(10, d, x, False)
    blinkLed(colorIndex, 0, x, False)
  time.sleep(d)
  return

def rainbowSpin(d = 0.1):
  global colorIndex
  for x in range(0, 10):
    blinkLed(colorIndex, d, x, False)
  colorIndex += 1
  if colorIndex > 10:
    colorIndex = 0
  return

##########################
###### Main Program ######
##########################

while True:
  if cpx.switch:
    functionIndex = functionPress(functionIndex)
    colorIndex = checkPress(colorIndex)
    if functionIndex == 0:
      blinkLed(colorIndex)
    elif functionIndex == 1:
      kitt()
    else:
      rainbowSpin()
  else:
    # shut it
    cpx.pixels.fill((0, 0, 0))