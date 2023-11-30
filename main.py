# python3 sensing/display.py & python3 main.py
import sys
import cv2
import serial
sys.path.append("sensing")
sys.path.append("solving")
from sensor import Sensor
from solver import solveCube

PORT = ""
BAUD_RATE = 0

print("Sensing scramble...")

sensor = Sensor()
rotations = ['x', 'y', 'y', 'y', 'yx', 'xx']    # x is up move, y is right
offsets = [0, 8, 4, 20, 16, 12]                 # read top, then front
scramble = [0] * 24
 
for i in range(6):
    input()
    side = sensor.getSide()
    print(side)
    for j in range(4):
        scramble[offsets[i] + j] = side[j]
    # send rotations[i] to ESP32 and wait to proceed

sensor.release()

print("Scramble:", scramble)
print("Solving scramble....")

solution = solveCube(scramble)[0]

print("Solution:", solution)
print("Sending solution to ESP32...")

# send solution to EPS32