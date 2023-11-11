import sys
import cv2
sys.path.append("sensor")
sys.path.append("solver")
from sensor import Sensor

# python3 main.py & python3 sensor/display.py
print("Sensing scramble...")

sensor = Sensor()
moves = ['x', 'y', 'y', 'y', 'yx', 'xx']
scramble = []

for i in range(6):
    scramble += sensor.getSide()
    # send moves[i] to ESP32

sensor.release()

print("Scramble:", scramble)
#print("Solving scramble....")
#solution = solver.solveCube(scramble)
#print("Solution:", solution)
#print("Sending solution to ESP32...")
# send solution to EPS32