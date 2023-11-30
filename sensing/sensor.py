import cv2
import numpy as np
from crosshairs import points
from time import sleep  

# Maps HLS tuple to color code
def getColor(HLS):
    h, l, s = HLS
    color = 1
    if l > 200 or s < 50: 
        color = 0 # White
    elif h < 3:
        color = 1 # Red
    elif h < 20:
        color = 4 # Orange   
    elif h < 45:
        color = 3 # Yellow     
    elif h < 80:
        color = 2 # Green  
    elif h < 130:
        color = 5 # Blue
    return color

class Sensor:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)  
        sleep(1)   

    def getSide(self):
        side = []
        # Sensing each side
        check, image = self.cam.read()
        imageHLS = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
        # Top to bottom, left to right
        colors = []
        for x, y in points:
            side.append(getColor(imageHLS[y][x]))
        return side
    
    def release(self):
        self.cam.release()
