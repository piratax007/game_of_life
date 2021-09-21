# Game of life

This implementation of [John Conway's game of life][1] developed with processing language 
with python-mode use a random seed and mouse interaction to set seed. At any 
instant, the user can pause the simulation to change the state of any cell. 
Can too interact in the execution time.


## How to execute the simulation

To run the simulation is needed an installation of [Processing 3.5.4 IDE][2] and 
add the python-mode from the top-right menu. Once you have the Processing IDE 
go to the File menu, select the Open option and search for the game_of_life_sketch.pyde 
file. In the IDE use the run button (top-left corner) to execute the simulation.

If you need to compile this such an application from any operating system 
(GNU Linux, Mac OS or Windows), go to the File menu and search for the 
Export Application option.


## Modes Torus and Plane

The simulation can be run over a torus (whitout edges) i.e. in a ciclic mode using the
function 'count_neighbours_alive_torus(grid, r, c)' or over a plane (with edges) using
the funcition 'count_neighbours_alive_plane(grid, r, c)'.

In the first one (_torus_) the neighbours alive search look for the state of the last
cell or the first one if the current cell is on the edge. In the last one mode (_plane_)
the search does not take into account any other cell beyond the edge.

[1]: https://en.wikipedia.org/wiki/Conway's_Game_of_Life
[2]: https://processing.org/download
