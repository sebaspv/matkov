from gridworld.grid import Grid
import pygame
import random

GRID_SIZE = (90, 90)
MAXCOORDS = (4, 3)
X = MAXCOORDS[0] // 2 - 1
Y = MAXCOORDS[1] // 2 + 1

grid = Grid(
    MAXCOORDS[0],
    MAXCOORDS[1],
    GRID_SIZE[0],
    GRID_SIZE[1],
    title="Markov Chain",
    margin=1,
    framerate=1,
)

car = pygame.image.load("sedan.png")
car = pygame.transform.scale(car, GRID_SIZE)

def get_action(moves):
    otactions = []
    currprob = 0
    for i in moves:
        currprob += i[1]
        otactions.append((currprob-i[1], currprob, i[0]))
    tomove = random.random()
    for i in otactions:
        if i[0] <= tomove and tomove < i[1]:
            finalmove = i[2]
    return finalmove

def draw_car(grid, cell_dimensions):
    grid.screen.blit(car, cell_dimensions)

trans = {
    (0, 0): [("U", 0.25), ("D", 0.25), ("L", 0.25), ("R", 0.25)],
    (1, 0): [("L", 1.0)],
    (2, 0): [("R", 0.33), ("D", 0.33), ("L", 0.33)],
    (3, 0): [("D", 1.0)],
    (0, 1): [("U", 1.0)],
    (1, 1): [("L", 0.33), ("U", 0.33), ("R", 0.33)],
    (2, 1): [("R", 1.0)],
    (0, 2): [("U", 1.0)],
    (1, 2): [("L", 0.33), ("U", 0.33), ("R", 0.33)],
    (2, 2): [("U", 0.5), ("R", 0.5)],
    (3, 2): [("U", 1.0)],
    (3, 1): [("U", 0.25), ("D", 0.25), ("L", 0.25), ("R", 0.25)]
}

def tick():
    global X, Y
    oldx, oldy = X, Y
    tupcoords = (X, Y)
    if tupcoords in targets:
        return
    move = get_action(trans[tupcoords])
    if move == "U" and Y > 0:
        Y -= 1
    elif move == "D" and Y < MAXCOORDS[1] - 1:
        Y += 1
    elif move == "R" and X < MAXCOORDS[0] - 1:
        X += 1
    elif move == "L" and X > 0:
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
