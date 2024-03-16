from gridworld.grid import Grid
import pygame
import random

GRID_SIZE = (90, 90)
MAXCOORDS = (4, 3)
X = MAXCOORDS[0] // 2
Y = MAXCOORDS[1] // 2

grid = Grid(
    MAXCOORDS[0],
    MAXCOORDS[1],
    GRID_SIZE[0],
    GRID_SIZE[1],
    title="Markov Chain 1",
    margin=1,
    framerate=1,
)

car = pygame.image.load("sedan.png")
car = pygame.transform.scale(car, GRID_SIZE)


def draw_car(grid, cell_dimensions):
    grid.screen.blit(car, cell_dimensions)


def tick():
    global X, Y
    oldx, oldy = X, Y
    tupcoords = (X, Y)
    if tupcoords in targets:
        return
    value = random.random()
    if value < 0.25 and Y > 0:
        Y -= 1
    elif value >= 0.25 and value < 0.5 and Y < MAXCOORDS[1] - 1:
        Y += 1
    elif value >= 0.5 and value < 0.75 and X < MAXCOORDS[0] - 1:
        X += 1
    elif X > 0:
        X -= 1
    grid[oldx, oldy] = ""
    grid[X, Y] = "O"


targets = [(0, 0), (3, 1)]

for i in targets:
    grid[i[0], i[1]] = "*"

grid.set_drawaction("O", draw_car)
grid[X, Y] = "O"
grid.set_timer_action(tick)
grid.run()
