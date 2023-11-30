# Window dimensions
HEIGHT = 720
WIDTH = 1280

# x > width / 2
x = 580

# Compute crosshairs determined by x
y = int((HEIGHT - WIDTH) / 2) + x
points = [(x, y), (WIDTH - x, y), (x, HEIGHT - y), (WIDTH - x, HEIGHT - y)]