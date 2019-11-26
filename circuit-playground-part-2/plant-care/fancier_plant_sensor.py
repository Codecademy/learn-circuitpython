'''
A somewhat fancier plantsensor based on cephir909's fancy plant sensor.
This sensor takes the value it gets when booting up and uses it as a baseline to measure moisture against.
You can change the step size of the capacity leds below, some trial and error is needed to find best values 
for different vessels/moisture levels/use cases.
'''
from adafruit_circuitplayground.express import cpx
import time
import touchio
from board import *

touch = touchio.TouchIn(A1)
touch_init = touch.raw_value #calibrates capacity base value
step_size_capacitance = 10 #how much capacity lies between each capacity step, some trial and error needed
while True:
    if cpx.button_a:
        print(cpx.temperature)
    if cpx.button_b:
        print(cpx.light)

    else:
        if cpx.switch:
            #print(touch.raw_value) #used for debugging to see capacity readings

            if touch.raw_value <= touch_init:
                cpx.pixels.fill((50,0,0))
            if touch.raw_value > touch_init and touch.raw_value < (touch_init+step_size_capacitance):
                cpx.pixels[0] = (0,50,0)
                cpx.pixels[1] = (50,0,0)
                cpx.pixels[2] = (50,0,0)
                cpx.pixels[3] = (50,0,0)
                cpx.pixels[4] = (50,0,0)
                cpx.pixels[5] = (50,0,0)
                cpx.pixels[6] = (50,0,0)
                cpx.pixels[7] = (50,0,0)
                cpx.pixels[8] = (50,0,0)
                cpx.pixels[9] = (50,0,0)
            if touch.raw_value > (touch_init+step_size_capacitance) and touch.raw_value < (touch_init+step_size_capacitance*2):
                cpx.pixels[0] = (0,50,0)
                cpx.pixels[1] = (0,50,0)
                cpx.pixels[2] = (50,0,0)
                cpx.pixels[3] = (50,0,0)
                cpx.pixels[4] = (50,0,0)
                cpx.pixels[5] = (50,0,0)
                cpx.pixels[6] = (50,0,0)
                cpx.pixels[7] = (50,0,0)
                cpx.pixels[8] = (50,0,0)
                cpx.pixels[9] = (50,0,0)
            if touch.raw_value > (touch_init+step_size_capacitance*2) and touch.raw_value < (touch_init+step_size_capacitance*3):
                cpx.pixels[0] = (0,50,0)
                cpx.pixels[1] = (0,50,0)
                cpx.pixels[2] = (0,50,0)
                cpx.pixels[3] = (50,0,0)
                cpx.pixels[4] = (50,0,0)
                cpx.pixels[5] = (50,0,0)
                cpx.pixels[6] = (50,0,0)
                cpx.pixels[7] = (50,0,0)
                cpx.pixels[8] = (50,0,0)
                cpx.pixels[9] = (50,0,0)
            if touch.raw_value > (touch_init+step_size_capacitance*3) and touch.raw_value < (touch_init+step_size_capacitance*4):
                cpx.pixels[0] = (0,50,0)
                cpx.pixels[1] = (0,50,0)
                cpx.pixels[2] = (0,50,0)
                cpx.pixels[3] = (0,50,0)
                cpx.pixels[4] = (50,0,0)
                cpx.pixels[5] = (50,0,0)
                cpx.pixels[6] = (50,0,0)
                cpx.pixels[7] = (50,0,0)
                cpx.pixels[8] = (50,0,0)
                cpx.pixels[9] = (50,0,0)
            if touch.raw_value > (touch_init+step_size_capacitance*4) and touch.raw_value < (touch_init+step_size_capacitance*5):
                cpx.pixels[0] = (0,50,0)
                cpx.pixels[1] = (0,50,0)
                cpx.pixels[2] = (0,50,0)
                cpx.pixels[3] = (0,50,0)
                cpx.pixels[4] = (0,50,0)
                cpx.pixels[5] = (50,0,0)
                cpx.pixels[6] = (50,0,0)
                cpx.pixels[7] = (50,0,0)
                cpx.pixels[8] = (50,0,0)
                cpx.pixels[9] = (50,0,0)
            if touch.raw_value > (touch_init+step_size_capacitance*5) and touch.raw_value < (touch_init+step_size_capacitance*6):
                cpx.pixels[0] = (0,50,0)
                cpx.pixels[1] = (0,50,0)
                cpx.pixels[2] = (0,50,0)
                cpx.pixels[3] = (0,50,0)
                cpx.pixels[4] = (0,50,0)
                cpx.pixels[5] = (0,50,0)
                cpx.pixels[6] = (50,0,0)
                cpx.pixels[7] = (50,0,0)
                cpx.pixels[8] = (50,0,0)
                cpx.pixels[9] = (50,0,0)
            if touch.raw_value > (touch_init+step_size_capacitance*6) and touch.raw_value < (touch_init+step_size_capacitance*7):
                cpx.pixels[0] = (0,50,0)
                cpx.pixels[1] = (0,50,0)
                cpx.pixels[2] = (0,50,0)
                cpx.pixels[3] = (0,50,0)
                cpx.pixels[4] = (0,50,0)
                cpx.pixels[5] = (0,50,0)
                cpx.pixels[6] = (0,50,0)
                cpx.pixels[7] = (50,0,0)
                cpx.pixels[8] = (50,0,0)
                cpx.pixels[9] = (50,0,0)
            if touch.raw_value > (touch_init+step_size_capacitance*7) and touch.raw_value < (touch_init+step_size_capacitance*8):
                cpx.pixels[0] = (0,50,0)
                cpx.pixels[1] = (0,50,0)
                cpx.pixels[2] = (0,50,0)
                cpx.pixels[3] = (0,50,0)
                cpx.pixels[4] = (0,50,0)
                cpx.pixels[5] = (0,50,0)
                cpx.pixels[6] = (0,50,0)
                cpx.pixels[7] = (0,50,0)
                cpx.pixels[8] = (50,0,0)
                cpx.pixels[9] = (50,0,0)
            if touch.raw_value > (touch_init+step_size_capacitance*8) and touch.raw_value < (touch_init+step_size_capacitance*9):
                cpx.pixels[0] = (0,50,0)
                cpx.pixels[1] = (0,50,0)
                cpx.pixels[2] = (0,50,0)
                cpx.pixels[3] = (0,50,0)
                cpx.pixels[4] = (0,50,0)
                cpx.pixels[5] = (0,50,0)
                cpx.pixels[6] = (0,50,0)
                cpx.pixels[7] = (0,50,0)
                cpx.pixels[8] = (0,50,0)
                cpx.pixels[9] = (50,0,0)
            if touch.raw_value > (touch_init+step_size_capacitance*9):
                cpx.pixels.fill((0,50,0))
            #time.sleep(0.5)
        else:
            cpx.pixels.fill((0,0,0))
