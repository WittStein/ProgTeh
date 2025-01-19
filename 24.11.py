import pygame as p
import random
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

p.init()

root = p.display.set_mode((1000, 500))
p.display.set_caption('Game of Life')

cells = [[random.choice([0, 1]) for j in range(root.get_width() // 20)] for i in range(root.get_height() // 20)]

def near(pos: list, system=[[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]):
    count = 0
    for i in system:
        if cells[(pos[0] + i[0]) % len(cells)][(pos[1] + i[1]) % len(cells[0])]:
            count += 1
    return count

running = True
while running:
    root.fill(WHITE)

    for i in range(0, root.get_height() // 20):
        p.draw.line(root, BLACK, (0, i * 20), (root.get_width(), i * 20))
    for j in range(0, root.get_width() // 20):
        p.draw.line(root, BLACK, (j * 20, 0), (j * 20, root.get_height()))

    for event in p.event.get():
        if event.type == QUIT:
            running = False

    for i in range(len(cells)):
        for j in range(len(cells[i])):
            p.draw.rect(root, (255 * cells[i][j] % 256, 0, 0), [j * 20, i * 20, 20, 20])

    p.display.update()

    cells2 = [[0 for j in range(len(cells[0]))] for i in range(len(cells))]
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            neighbors = near([i, j])
            if cells[i][j]:
                if neighbors in (2, 3):
                    cells2[i][j] = 1
            else:
                if neighbors == 3:
                    cells2[i][j] = 1

    cells = cells2

    p.time.delay(100)

p.quit()
