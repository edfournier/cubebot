# Window dimensions
height = 720
width = 1280

# x > width / 2
x = 560 

# Compute crosshairs determined by x
y = int((height - width) / 2) + x
points = [(x, y), (width - x, y), (x, height - y), (width - x, height - y)]