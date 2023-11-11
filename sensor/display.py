import cv2
import numpy as np
from crosshairs import points
from time import sleep
from sensor import getColor

cam = cv2.VideoCapture(0)   # 0 for front camera
sleep(1)                    # Give camera time to initialize

# Map color codes to BGR and name
colorMap = [
    ((255, 255, 255), "WHITE"),
    ((0, 20, 229), "RED"),
    ((0, 204, 153), "GREEN"),
    ((0, 204, 255), "YELLOW"),
    ((0, 102, 255), "ORANGE"),
    ((255, 204, 153), "BLUE")
]

while True:
    # Capture and make HLS copy
    result, image = cam.read()
    imageHLS = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    # Draw and label crosshairs
    for x, y in points:
        bgr, name = colorMap[getColor(imageHLS[y][x])]
        cv2.circle(image, (x, y), 3, (0, 0, 0), -1)
        cv2.rectangle(image, (x - 50, y - 10), (x + int(len(name) / 6.0 * 75), y - 50), (30, 30, 30), -1)
        cv2.putText(image, name, (x - 50, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, bgr, 1)
    # Display image and wait 1ms or end when key is pressed
    cv2.imshow('image', image)
    key = cv2.waitKey(1) 
    if key == 27:
        break

cam.release()