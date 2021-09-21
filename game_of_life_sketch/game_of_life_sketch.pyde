'''
Game of life

This sketch implement the game of life by John Conway with a random seed and setting option
from mouse interaction

Fausto M. Lagos S. - 2021
piratax007@protonmail.ch - @piratax007
GNU GPL V3.0+
'''


width_ = 960
height_ = 540
resolution = 10
old_generation = [[0 for col in range(width_ / resolution)] for row in range(height_ / resolution)]
frame_rate = 60
run_simulation = False
random_seed = False


def draw_grid():
    noFill()
    stroke(70)
    
    for i in range(0, height_, resolution):
         for j in range(0, width_, resolution):
            rect(j, i, resolution, resolution)
            
            
def draw_cells():
    stroke(70)
    
    for row in range(height_ / resolution):
        for col in range(width_ / resolution):
            if old_generation[row][col] == 1:
                fill(200)
            else:
                fill(75)
                
            rect(col *  resolution, row * resolution, resolution, resolution)
                


def count_neighbours_alive_torus(grid, r, c):
    sum = 0
    for i in range(-1, 2):
        row = (r + i  + (height_ / resolution)) % (height_ / resolution)
        for j in range(-1, 2):
            col = (c + j + (width_ / resolution)) % (width_ / resolution)
            sum += grid[row][col]
            
    sum -= grid[r][c]
    return sum


def count_neighbours_alive_plane(grid, r, c):
    sum = 0
    
    if r == 0:
        range_r = range(2)
    elif r == (height_ / resolution) - 1:
        range_r = range(-1, 1)
    else:
        range_r = range(-1, 2)
        
    if c == 0:
        range_c = range(2)
    elif c == (width_ / resolution) - 1:
        range_c = range(-1, 1)
    else:
        range_c = range(-1, 2)
    
    for i in range_r:
        row = r + i
        
        for j in range_c:
            col = c + j
            
            sum += grid[row][col]
            
    sum -= grid[r][c]
    return sum
                


def new_generation(previous_generation):
    new_gen = [[0 for col in range(width_ / resolution)] for row in range(height_ / resolution)]
                    
    for i in range(height_ / resolution):
        for j in range(width_ / resolution):
            state = previous_generation[i][j]
            neighbours_alive = count_neighbours_alive_torus(previous_generation, i, j)
                
            # rules
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


def mousePressed():
    global old_generation
    
    click_x = floor(mouseX / resolution)
    click_y = floor(mouseY / resolution)
    if old_generation[click_y][click_x] == 0:
        old_generation[click_y][click_x] = 1
    else:
        old_generation[click_y][click_x] = 0
        
    draw_cells()


def instructions():
    fill(200)
    text("Press r (random seed) follow by Enter", 25, height_ + 25)
    text("Mouse click on a cell to change their state", 25, height_ + 50)
    text("ENTER to start / pause the simulation", width_ / 2, height_ + 25)
    text("UP or DOWN to increase or decrease the speed of simulation", width_ / 2, height_ + 50)
    fill(90)
    text("by @piratax007", width_ - 110, height_ + 75)


def setup():
    frameRate(frame_rate)
    size(width_, height_ + 100)
    background(75)
    draw_grid()
    instructions()
    
    
def draw():
    global old_generation
    
    frameRate(frame_rate)
    
    if random_seed is True:
        old_generation = [[int(random(2)) for col in range(width_ / resolution)] for row in range(height_ / resolution)]
        
    if run_simulation is True:
        background(75)
        draw_grid()
        instructions()
        draw_cells()
        old_generation = new_generation(old_generation)
    
