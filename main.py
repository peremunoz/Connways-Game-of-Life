# Pere Muñoz Figuerol - Connway's Game of Life
import sys
import random
from time import sleep

import pygame

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (128, 128, 128)

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Cell size
CELL_SIZE = 10

# Game control
global CELLS_ALIVE
CELLS_ALIVE = 0


def main():
    # Control entry parameters
    if len(sys.argv) < 2:
        print('Usage: python main.py <execution mode> [random]')
        sys.exit(1)

    EXECUTION_MODE = sys.argv[1]

    # Init
    pygame.init()

    # Screen
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Conway's Game of Life by Pere Muñoz")

    if len(sys.argv) > 2 and sys.argv[2] == 'random':
        print('Random mode')
        state = [[random.randint(0, 1) for i in range(0, SCREEN_WIDTH, CELL_SIZE)] for j in
                 range(0, SCREEN_HEIGHT, CELL_SIZE)]
    else:
        state = readInitialState()

    printStartingGame(SCREEN)
    drawGrid(SCREEN, state)
    countAliveCells(state)

    pygame.display.set_caption(
        "Conway's Game of Life by Pere Muñoz - Iteration 0 - Cells alive: {}".format(CELLS_ALIVE))

    iterations = 0

    while CELLS_ALIVE > 0:
        if EXECUTION_MODE == 'manual':
            while True:
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN:
                    break
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        else:
            sleep(0.22)
        iterations += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        drawGrid(SCREEN, state)
        processState(state)
        pygame.display.update()
        pygame.display.set_caption(
            "Conway's Game of Life by Pere Muñoz - Iteration " + str(iterations) + " - Cells alive: " + str(
                CELLS_ALIVE))

    printGameOver(SCREEN)


def printGameOver(screen):
    screen.fill(WHITE)
    sysFont = pygame.font.SysFont(pygame.font.get_default_font(), 50)
    img = sysFont.render('Game over !!', True, RED)
    screen.blit(img, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 50))
    pygame.display.update()
    sleep(2)


def printStartingGame(screen):
    screen.fill(WHITE)
    sysFont = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    img = sysFont.render('Starting game', True, RED)
    screen.blit(img, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 50))
    pygame.display.update()
    sleep(0.5)
    for i in range(0, 4):
        img = sysFont.render('.' * i, True, RED)
        screen.blit(img, (SCREEN_WIDTH / 2 + 40, SCREEN_HEIGHT / 2 - 50))
        pygame.display.update()
        sleep(0.5)

    screen.fill(WHITE)
    pygame.display.update()


def processState(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            state[i][j] = processCell(state, i, j)


def processCell(state, i, j):
    global CELLS_ALIVE
    neighbours = getNeighbours(state, i, j)
    if state[i][j] == 1:
        if neighbours < 2 or neighbours > 3:
            CELLS_ALIVE -= 1
            return 0
        else:
            return 1
    else:
        if neighbours == 3:
            CELLS_ALIVE += 1
            return 1
        else:
            return 0


def getNeighbours(state, i, j):
    neighbours = 0
    for k in range(i - 1, i + 2):
        for l in range(j - 1, j + 2):
            if 0 <= k < len(state) and 0 <= l < len(state[i]) and (k != i or l != j):
                neighbours += 1 if state[k][l] == 1 else 0
    return neighbours


def readInitialState():
    with open('initialState.txt', 'r') as initialFile:
        matrix = [[int(num) for num in line.split(',')] for line in initialFile]
        return matrix


def countAliveCells(state):
    global CELLS_ALIVE
    CELLS_ALIVE = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            CELLS_ALIVE += 1 if state[i][j] == 1 else 0


def drawGrid(screen, state):
    global CELLS_ALIVE
    for i in range(0, SCREEN_WIDTH, CELL_SIZE):
        for j in range(0, SCREEN_HEIGHT, CELL_SIZE):
            cellLine = pygame.Rect(i, j, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREY, cellLine, 1)
            cell = pygame.Rect(i + 2, j + 2, CELL_SIZE - 4, CELL_SIZE - 4)
            normalizedState = state[int(j / CELL_SIZE)][int(i / CELL_SIZE)]
            pygame.draw.rect(screen, BLACK if normalizedState == 1 else WHITE, cell,
                             0)


if __name__ == "__main__":
    main()
