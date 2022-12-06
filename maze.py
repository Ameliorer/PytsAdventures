import pygame
from random import choice, randrange

RES = WIDTH, HEIGHT = 602, 602
TILE = 20
cols, rows = WIDTH // TILE, HEIGHT // TILE

class Cell:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        self.top = True
        self.right = True
        self.left = True
        self.bot = True
        self.visited = False
        self.thickness = 4

    def draw(self, screen):
        x, y = self.x * TILE, self.y * TILE

        if self.top:
            pygame.draw.line(screen, pygame.Color('darkorange'), (x, y), (x + TILE, y), self.thickness)
        if self.right:
            pygame.draw.line(screen, pygame.Color('darkorange'), (x + TILE, y), (x + TILE, y + TILE), self.thickness)
        if self.bot:
            pygame.draw.line(screen, pygame.Color('darkorange'), (x + TILE, y + TILE), (x , y + TILE), self.thickness)
        if self.left:
            pygame.draw.line(screen, pygame.Color('darkorange'), (x, y + TILE), (x, y), self.thickness)

    def get_valid_neighboor(self, grid_cells, row, col):
        neighbors = []
        top = is_valid_neightboor(self.x, self.y - 1, grid_cells, row, col)
        right = is_valid_neightboor(self.x + 1, self.y, grid_cells, row, col)
        bottom = is_valid_neightboor(self.x, self.y + 1, grid_cells, row, col)
        left = is_valid_neightboor(self.x - 1, self.y, grid_cells, row, col)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        if neighbors:
            return choice(neighbors)
        else:
            return None

def is_valid_neightboor(x, y, grid_cells, row, col):
    if x < 0 or x >= col or y < 0 or y >= row:
        return None
    # print(f'x : {x}, y : {y}')
    return grid_cells[x][y]

def draw_current_cell(current_cell, screen):
    x, y = current_cell.x * TILE, current_cell.y * TILE
    pygame.draw.rect(screen, pygame.Color('saddlebrown'), (x + 2, y + 2, TILE - 2, TILE - 2))

def remove_walls(current_cell, next_cell):
    match current_cell.x - next_cell.x:
        case 1:
            current_cell.left = False
            next_cell.right = False
        case -1:
            current_cell.right = False
            next_cell.left = False
    match current_cell.y - next_cell.y:
        case 1:
            current_cell.top = False
            next_cell.bot = False
        case -1:
            current_cell.bot = False
            next_cell.top = False

def main():
    # print(f'row : {rows}, col : {cols}')
    pygame.init()
    screen = pygame.display.set_mode(RES, pygame.SRCALPHA)
    grid_cells = [[Cell(col, row) for row in range(rows)] for col in range(cols)]
    # grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
    current_cell = grid_cells[0][0]
    clock = pygame.time.Clock()
    stack = []
    colors = []
    color = 40

    while True:
        screen.fill(pygame.Color('darkslategray'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        for cells in grid_cells:
            for cell in cells:
                cell.draw(screen)
        current_cell.visited = True
        draw_current_cell(current_cell, screen)
        next_cell = current_cell.get_valid_neighboor(grid_cells, rows, cols)
        for i, cell in enumerate(stack):
            pygame.draw.rect(screen, colors[i], (cell.x * TILE + 5, cell.y * TILE + 5, TILE - 10, TILE - 10), border_radius=12)
        if next_cell:
            next_cell.visited = True
            if current_cell.get_valid_neighboor(grid_cells, rows, cols):
                stack.append(current_cell)
            colors.append((min(color, 255), 10, 100))
            color += 1
            remove_walls(current_cell, next_cell)
            current_cell = next_cell
        elif stack:
            current_cell = stack.pop()
        pygame.display.flip()
        clock.tick(1080)

if __name__ == '__main__':
    main()