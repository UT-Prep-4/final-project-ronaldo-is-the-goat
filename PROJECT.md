# Conway's Game of Life

## What it is
Conway's Game of Life is a simulation that demonstrates how simple rules can create complex and unpredictable patterns. The program displays a grid of cells that can be either alive or dead, and each generation evolves based on the states of neighboring cells. It's interesting because the simulation can produce stable structures, repeating patterns, and moving formations called "gliders" from very simple starting configurations.

## How to run it
1. Make sure Python 3 is installed.
2. Install pygame with `pip install pygame`
3. Run the program with `python final_project.py`
4. The simulation window will open. Use the controls shown in the program (if any) to start, pause, or reset the simulation.

## How it works
The main update function calculates the number of living neighbors for every cell in the grid and applies Conway's four rules simultaneously to create the next generation. The program repeatedly redraws the grid after each update, creating an animated simulation. One of the most challenging parts was ensuring that every cell updates based on the previous generation rather than changing immediately, which would produce incorrect results.

## Built by
Chirag Pant, Suchir Shah, Jayan Patel, Alex Xu
Inspired by John Conway's original Game of Life.
