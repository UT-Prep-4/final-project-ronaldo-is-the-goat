#Name(s): Suchir, Jayan, Chirag, Alex
#Final Project - Build Something Worth Showing Off
'''
This is the big one. At the end of camp you will demo this project at the
SHOWCASE, and it should be good enough to put on a resume or mention in a
college application. That means it is not just "code that works." It is a
project you designed, built, polished, and can explain.

WHAT MAKES IT SHOWCASE-WORTHY (the autograder checks for these):
  1. ORGANIZED: your code is split into clear, purposeful segments (functions optional), not one
     giant blob. (Aim for at least 3-4 functions with real jobs.)
  2. SUBSTANTIAL: this is a multi-day build, bigger than the mini-project.
  3. REAL LOGIC: decisions (if/elif/else) and repetition (loops) working together.
  4. DOCUMENTED: fill out PROJECT.md so a stranger (or a college admissions
     reader!) can understand what you built and how to run it.

Whether it is impressive, creative, and demo-ready is judged by humans at
showcase, not by the autograder.

============================= PICK YOUR TRACK =================================

TRACK A: IMAGE PROCESSING PROGRAM
  Build a program that opens an image and transforms it with a special
  function you write yourself: brightness adjustment, a color filter overlay,
  grayscale, mirror, pixelate, or invent your own effect.
  The Pillow library is preinstalled. The core moves:

      from PIL import Image
      img = Image.open("photo.png")
      width, height = img.size
      pixel = img.getpixel((x, y))          # (red, green, blue), each 0-255
      img.putpixel((x, y), (r, g, b))       # set a pixel
      img.save("output.png")                # then click it in VS Code to view!

  Brightness is a for loop over every pixel that multiplies r, g, b by a
  factor the user chooses (careful: values must stay between 0 and 255).
  A filter overlay nudges every pixel toward a color (add red, drop blue...).
  Level up: ask the user which effect to apply with input(), show a menu,
  process any image file they name, draw the result with turtle or pygame.

TRACK B: ADVENTURE GAME
  Build a text adventure where the player explores, makes choices, and wins
  or loses based on decisions and luck. Use random for surprises: treasure,
  traps, enemy encounters, dice rolls, critical hits.
  The shape of it: one function per location or scene, input() for choices,
  an inventory list, health or gold as numbers, and random.randint() for
  the unexpected. Level up: turn-based combat, a map, multiple endings,
  ASCII art title screens, a save-your-score high score.

TRACK C: YOUR OWN IDEA
  A bigger game (pygame or turtle), a quiz app, a tool that solves a real
  problem you have, a simulation, generative turtle art... Pitch it to your
  instructor FIRST, then build it. The four requirements above still apply.

=============================== PLAN FIRST ====================================
Before you write code, fill this in (it will keep you honest all week):

  MY PROJECT: (one sentence)
  THE PIECES I NEED TO BUILD: (list 3-6 functions or parts)
  WHAT I WILL DEMO AT SHOWCASE: (the 60-second version)

==============================================================================
Build your project below (and split it into more .py files if it gets big;
the grader reads all of them). Delete this line and start!
'''

import pygame
import sys
import copy
import random as r

pygame.init()

WIDTH, HEIGHT = 500, 500

GRID_SIZE: int = 25 # size of each grid pixel

WHITE = (255,255,255)
DARK_GREY = (50, 50, 50)
LIGHT_GREY = (200, 200, 200)
YELLOW = (255,255,0)

COLS: int = WIDTH // GRID_SIZE
ROWS: int = HEIGHT // GRID_SIZE

FPS = 2


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 15)

is_paused = False

def create_grid():
  return [[False for _ in range(COLS)] for _ in range(ROWS)]


def draw_grid(grid):
    # draws the grid pattern
    for row in range(ROWS):
        for col in range(COLS):

            color = YELLOW if grid[row][col] == 1 else LIGHT_GREY
            pygame.draw.rect(
                screen, 
                color, 
                (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1)
            )

def count_neighbors(grid, x, y):
  live_neighbors = 0           
  for dx in [-1, 0 , 1]:
    for dy in [-1, 0 , 1]:

      if dx == 0 and dy == 0:
        continue

      neighbor_x = (x + dx) % ROWS
      neighbor_y = (y + dy) % COLS

      live_neighbors += grid[neighbor_x][neighbor_y]

  return live_neighbors


def draw_txt():
  time_txt = font.render(f"Elapsed time: {(pygame.time.get_ticks()/1000):.1f}", True, WHITE)
  controls_txt = font.render(f"Press SPACEBAR to pause/unpause", True, WHITE)
  screen.blit(time_txt, (10, 5))
  screen.blit(controls_txt, (10, 15))

def update_grid(grid):
    new_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    
    for x in range(ROWS):
        for y in range(COLS):
            neighbors = count_neighbors(grid, x, y)

            # if grid[x][y] == 1: do underpopulation, overpopuylation, survival
            # else do reproduction
            if grid[x][y] == 1:
              if neighbors < 2 or neighbors > 3:
                 new_grid[x][y] = 0
              else:
                 new_grid[x][y] = 1
            elif neighbors == 3 and grid[x][y] == 0:
                new_grid[x][y] = 1

    return new_grid

clicked_column, clicked_row = 0, 0
grid = create_grid()

while True:
  mouse_x, mouse_y = pygame.mouse.get_pos()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        mouse_x, mouse_y = event.pos
          
        clicked_column = mouse_x // GRID_SIZE
        clicked_row = mouse_y // GRID_SIZE
      
      if 0 <= clicked_column < COLS and 0 <= clicked_row < ROWS:
        grid[clicked_row][clicked_column] = not grid[clicked_row][clicked_column]

    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        is_paused = not is_paused
      if event.key = pygame.K_a:
        FPS -= 1
      if event.key = pygame.K_d:
        FPS += 1
        
  if not is_paused:
    grid = update_grid(grid)
    clock.tick(FPS)


  screen.fill(DARK_GREY)
  draw_grid(grid)
  draw_txt()
  pygame.display.flip()