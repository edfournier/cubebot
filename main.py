# python3 sensing/display.py & python3 main.py
import sys
import cv2
import serial
sys.path.append("sensing")

sys.path.append("solving")
from time import sleep
from sensor import Sensor
from solver import solveCube

PORT = "/dev/cu.usbserial-10"
BAUD_RATE = 115200

print("Sensing scramble...")

socket = serial.Serial(PORT, BAUD_RATE)
sensor = Sensor()
rotations = ["x", "y", "y", "y", "yx", "xx"]    # x is up move, y is right
offsets = [0, 8, 4, 20, 16, 12]                 # read top, then front
scramble = [0] * 24
 
for i in range(6):
    input()
    side = sensor.getSide()
    print(side)
    for j in range(4):
        scramble[offsets[i] + j] = side[j]

sensor.release()

print("Scramble:", scramble)
print("Solving scramble....")

solution = solveCube(scramble)[0]   \
            .replace("F2", "F F")   \
            .replace("U2", "U U")   \
            .replace("R2", "R R")   \
            .replace("F'", "f")     \
            .replace("U'", "u")     \
            .replace("R'", "r")     \

print("Solution:", solution)
print("Ready to send solution")
input()

socket.write(solution.encode())
socket.close()