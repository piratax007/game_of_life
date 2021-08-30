from random import randrange

width_ = 500
height_ = 500
resolution = 10


def count_neighbours_alive(grid, x, y):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            col = (y + j + (height_ / resolution)) % (height_ / resolution)
            row = (x + i  + (width_ / resolution)) % (width_ / resolution)
            sum += grid[row][col]
            
    sum -= grid[x][y]
    return sum


def setup():
    size(width_, height_)
    global old_gen 
    old_gen = [[randrange(2) for col in range(width_ / resolution)] for row in range(height_ / resolution)]
    
    
def draw():    
    background(75)
    
    global old_gen
    
    for row in range(height_ / resolution):
        for col in range(width_ / resolution):
            if old_gen[row][col] == 1:
                fill(255)
                stroke(70)
                rect(col *  resolution, row * resolution, resolution, resolution)
                
    new_generation = [[0 for col in range(width_ / resolution)] for row in range(height_ / resolution)]
                
    for i in range(height_ / resolution):
        for j in range(width_ / resolution):
            state = old_gen[i][j]
            neighbours_alive = count_neighbours_alive(old_gen, i, j)
            
            if state == 0 and neighbours_alive == 3:
                new_generation[i][j] = 1
            elif state == 1 and (neighbours_alive < 2 or neighbours_alive > 3):
                new_generation[i][j] = 0
            else:
                new_generation[i][j] = state
                
    old_gen = new_generation
    
