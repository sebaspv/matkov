from gridworld.grid import Grid
import pygame

GRID_SIZE = (90, 90)
MAXCOORDS = (5, 5)
X = MAXCOORDS[0] // 2
Y = MAXCOORDS[1] // 2

grid = Grid(MAXCOORDS[0], MAXCOORDS[1], GRID_SIZE[0], GRID_SIZE[1], title = "Gridworld", margin = 1)

car = pygame.image.load("sedan.png")
car = pygame.transform.scale(car, GRID_SIZE)


def draw_car(grid, cell_dimensions):
    grid.screen.blit(car, cell_dimensions)

def key_action(key):
    global X, Y
    oldx, oldy = X, Y
    if key == pygame.K_LEFT and X > 0:
        X -= 1
    elif key == pygame.K_UP and Y > 0:
        Y -= 1
    elif key == pygame.K_DOWN and Y < MAXCOORDS[1] - 1:
        Y += 1
    elif key == pygame.K_RIGHT and X < MAXCOORDS[0] - 1:
        X += 1
    grid[oldx, oldy] = ""
    grid[X, Y] = "O"

grid.set_drawaction('O', draw_car)
grid[X, Y] = "O"
grid.set_key_action(key_action) 
grid.run()