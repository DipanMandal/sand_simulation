import pygame
import random
import sys

# Configuration
WIDTH, HEIGHT = 400, 400
CELL_SIZE = 4
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
BLACK = (0, 0, 0)

grid = [[None for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("COLOURED SAND SIMULATION : PYGAME")
clock = pygame.time.Clock()

def draw_grid():
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if grid[x][y] is not None:
                pygame.draw.rect(screen, grid[x][y], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def update_simulation():
    for y in range(GRID_HEIGHT - 2, -1, -1):  
        for x in range(1, GRID_WIDTH - 1):   
                if grid[x][y + 1] is None:
                    grid[x][y + 1] = grid[x][y]
                    grid[x][y] = None
                elif grid[x - 1][y + 1] is None:
                    grid[x - 1][y + 1] = grid[x][y]
                    grid[x][y] = None
                elif grid[x + 1][y + 1] is None:
                    grid[x + 1][y + 1] = grid[x][y]
                    grid[x][y] = None

def add_sand(mouse_pos, color):
    mx, my = mouse_pos
    x, y = mx // CELL_SIZE, my // CELL_SIZE
    if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
        grid[x][y] = color


current_sand_color = (255,255,255)
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Press a key to change sand color randomly
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                current_sand_color = (
                    random.randint(50, 150),
                    random.randint(50, 150),
                    random.randint(50, 150),
                )

    # Add sand with mouse
    if pygame.mouse.get_pressed()[0]:
        add_sand(pygame.mouse.get_pos(), current_sand_color)

    update_simulation()
    draw_grid()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
