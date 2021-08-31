from random import randrange

width_ = 700
height_ = 500
resolution = 10
frame_rate = 60
run_simulation = False
random_seed = False


def draw_grid():
    for i in range(height_ / resolution):
        for j in range(width_ / resolution):
            noFill()
            stroke(70)
            rect(j *  resolution, i * resolution, resolution, resolution)
            
            
def draw_cells(generation):
    for row in range(height_ / resolution):
        for col in range(width_ / resolution):
            if old_generation[row][col] == 1:
                fill(255)
                stroke(70)
                rect(col *  resolution, row * resolution, resolution, resolution)


def count_neighbours_alive(grid, x, y):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            col = (y + j + (width_ / resolution)) % (width_ / resolution)
            row = (x + i  + (height_ / resolution)) % (height_ / resolution)
            sum += grid[row][col]
            
    sum -= grid[x][y]
    return sum


def new_generation(previous_generation):
    new_gen = [[0 for col in range(width_ / resolution)] for row in range(height_ / resolution)]
                    
    for i in range(height_ / resolution):
        for j in range(width_ / resolution):
            state = previous_generation[i][j]
            neighbours_alive = count_neighbours_alive(previous_generation, i, j)
                
            if state == 0 and neighbours_alive == 3:
                new_gen[i][j] = 1
            elif state == 1 and (neighbours_alive < 2 or neighbours_alive > 3):
                new_gen[i][j] = 0
            else:
                new_gen[i][j] = state
                
    return new_gen


def keyPressed():
    global frame_rate
    global random_seed
    global run_simulation
    
    if key == 'r':
        random_seed = True
    elif key == ENTER:
        random_seed = False
        run_simulation = not run_simulation
    elif keyCode == UP:
        if frame_rate > 55:
            frame_rate = 60
        else:
            frame_rate += 5
    elif keyCode == DOWN:
        if frame_rate < 10:
            frame_rate = 5
        else:
            frame_rate -= 5


def setup():
    frameRate(frame_rate)
    size(width_, height_)
    
    
def draw():
    global old_generation
    
    frameRate(frame_rate)    
    background(75)
    draw_grid()
    
    if random_seed is True:
        old_generation = [[randrange(2) for col in range(width_ / resolution)] for row in range(height_ / resolution)]
        
    if run_simulation is True:
        draw_cells(old_generation)
        old_generation = new_generation(old_generation)
    
