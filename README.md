# Implementation
1. Python script running on laptop captures a face via webcam, analyzes it with OpenCV, then repeats on remaining faces, turning as necessary via serial.
2. Complete permutation is sent to ESP32 as a 24-index array via serial.
3. ESP32 solves permutation. 
4. ESP32 executes solution by controlling arms. 

# Features
- 4-button interface to manually input permutation
- Scramble button
- Switch to change input methods

# Materials
- ESP32
- 5 tactile buttons
- Slide switch
- 2-8 servo motors 
- Jumper wires