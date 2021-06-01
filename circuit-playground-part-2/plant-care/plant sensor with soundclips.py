from adafruit_circuitplayground.express import cpx
import time
import board
import touchio
import simpleio
from time import sleep

"""
A fun plant sensor that lights up all of the CircuitPlayground Express's Neopixels accordingly and plays apt tones and UFC soundclips.
"""

# Alligator clip is connected to A1
touch = touchio.TouchIn(board.A1)

DRY_VALUE = 2750 # Sets default dry threshold, value depends on plant/soil

# Counters to prevent unwanted repetitions of certain features
DRY_COUNTER, HYDRATED_COUNTER, TONE_NEG_COUNTER, TONE_POS_COUNTER = 0, 0, 0, 0

print(f"Default DRY_VALUE is set to {DRY_VALUE}")

while True:
  if cpx.switch:
      # Use A&B buttons to decrease and increase DRY_VALUE, respectively
      if cpx.button_b:
          print(f"Old dry value is {DRY_VALUE}")
          print("Increasing by 500...")
          time.sleep(1)
          DRY_VALUE += 500
          cpx.play_tone(500, 0.8)
          print(f"New dry value is {DRY_VALUE}")
      elif cpx.button_a:
          print(f"Old dry value is {DRY_VALUE}")
          print("Decreasing by 500...")
          time.sleep(1)
          DRY_VALUE -= 500
          cpx.play_tone(125, 0.8)
          print(f"New dry value is {DRY_VALUE}")
      # True if the Moisture Value is greater than or equal to the Dry Value (aka plant is DEHYDRATED) and the cpx.switch is on the left side (viewing CPX from front)
      elif touch.raw_value >= DRY_VALUE and cpx.switch:
          HYDRATED_COUNTER, TONE_POS_COUNTER = 0, 0
          print("Moisture value:", touch.raw_value)
          if DRY_COUNTER < 1:
              cpx.pixels.brightness = 0.1
              for i in range(10):
                  cpx.pixels[i] = (255, 0, 0)
                  time.sleep(0.1)
              time.sleep(0.5)
              # Bruce Buffer It's Time audio
              cpx.play_file("buffer.wav")
              cpx.pixels.fill((255, 255, 255))
              cpx.pixels.brightness = 0.05
              for i in range(0, 10, 2):
                  cpx.pixels[i] = (255, 0, 0)
              time.sleep(0.1)
              for i in range(1, 11):
                  cpx.pixels[-i] = (0, 0, 0)
                  time.sleep(0.075)
              time.sleep(0.1)
              DRY_COUNTER += 1
          else:
              cpx.pixels.brightness = 0.2
              for i in range(10):
                  cpx.pixels[i] = (255, 0, 0)
                  time.sleep(0.05)
              if TONE_NEG_COUNTER < 1:
                  cpx.play_tone(100, 1.5)
                  TONE_NEG_COUNTER += 1
      # True if the Moisture Value is less than or equal to the Dry Value (aka plant is HYDRATED) and the cpx.switch is on the left side (viewing CPX from front)
      elif touch.raw_value < DRY_VALUE and cpx.switch:
          DRY_COUNTER, TONE_NEG_COUNTER = 0, 0
          print("Moisture value:", touch.raw_value)
          cpx.pixels.brightness = 0.1
          if HYDRATED_COUNTER < 1:
              for i in range(10):
                  cpx.pixels[i] = (0, 255, 0)
                  time.sleep(0.125)
              time.sleep(0.7)
              # Connor McGregor The King is back audio
              cpx.play_file("connor.wav")
              cpx.pixels.fill((255, 255, 255))
              cpx.pixels.brightness = 0.1
              for i in range(0, 10, 2):
                  cpx.pixels[i] = (0, 255, 0)
              time.sleep(0.1)
              for i in range(1, 11):
                  cpx.pixels[-i] = (0, 0, 0)
                  time.sleep(0.05)
              time.sleep(0.1)
              HYDRATED_COUNTER += 1
          else:
              cpx.pixels.brightness = 0.2
              for i in range(10):
                  cpx.pixels[i] = (0, 255, 0)
                  time.sleep(0.05)
              if TONE_POS_COUNTER < 1:
                  # Success musical notes
                  cpx.play_tone(500, 0.02)
                  cpx.play_tone(600, 0.025)
                  cpx.play_tone(700, 0.05)
                  cpx.play_tone(800, 0.06)
                  cpx.play_tone(900, 0.075)
                  cpx.play_tone(1000, 1)
                  TONE_POS_COUNTER += 1
  else:
      DRY_COUNTER, HYDRATED_COUNTER, TONE_NEG_COUNTER, TONE_POS_COUNTER = 0, 0, 0, 0
      cpx.pixels.fill((0, 0, 0))
