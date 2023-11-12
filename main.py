import sys
import cv2
sys.path.append("sensing")
sys.path.append("solving")
from sensing import Sensor
from solving import solveCube

# python3 main.py & python3 sensor/display.py
print("Sensing scramble...")

sensor = Sensor()
moves = ['x', 'y', 'y', 'y', 'yx', 'xx']
offsets = [0, 8, 4, 20, 16, 12]
scramble = [0] * 24
 
for i in range(6):
    input()
    side = sensor.getSide()
    for j in range(4):
        scramble[offsets[i] + j] = side[j]
    # send moves[i] to ESP32 and wait

sensor.release()

print("Scramble:", scramble)
print("Solving scramble....")

solution = solveCube(scramble)[0]

print("Solution:", solution)
#print("Sending solution to ESP32...")
# send solution to EPS32