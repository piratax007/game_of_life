from random import randrange

width_ = 500
height_ = 500
resolution = 10
grid_states = [[randrange(2) for col in range(width_ / resolution)] for row in range(height_ / resolution)]

def setup():
    size(width_, height_)
    
    
def draw():
    background(200)
    
    for col in range(width_ / resolution):
        for row in range(height_ / resolution):
            if grid_states[col][row] == 1:
                fill(255)
                rect(col *  resolution, row * resolution, resolution, resolution)
