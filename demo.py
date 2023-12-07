# python3 sensing/display.py & python3 main.py
import sys
import cv2
import serial
import numpy as np
sys.path.append("sensing")
sys.path.append("solving")
from crosshairs import points
from time import sleep
from sensor import getColor
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

# Map color codes to BGR and name
colorMap = [
    ((255, 255, 255), "WHITE"),
    ((0, 20, 229), "RED"),
    ((0, 204, 153), "GREEN"),
    ((0, 204, 255), "YELLOW"),
    ((0, 102, 255), "ORANGE"),
    ((255, 204, 153), "BLUE")
]

cam = cv2.VideoCapture(0)   # 0 for front camera
sleep(1)                    # Give camera time to initialize

# Capture and make HLS copy
i = 0
while i < 6:
    check, image = cam.read()
    imageHLS = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    # Draw and label crosshairs
    for x, y in points:
        bgr, name = colorMap[getColor(imageHLS[y][x])]
        cv2.circle(image, (x, y), 3, (0, 0, 0), -1)
        cv2.rectangle(image, (x - 32, y - 6), (x + int(len(name) / 6.0 * 35), y - 26), (30, 30, 30), -1)
        cv2.putText(image, name, (x - 30, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, bgr, 1)
    # Display image and wait 1ms or end when key is pressed
    cv2.imshow('image', image)
    key = cv2.waitKey(1) 
    if key == 27:
        break
    if key == ord('q'):
        side = sensor.getSide()
        print(side)
        for j in range(4):
            scramble[offsets[i] + j] = side[j]
        i = i + 1
 

cam.release()
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
