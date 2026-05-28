import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 300, 350
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8 Puzzle Game")

FONT = pygame.font.Font(None, 40)

# initial solved state
goal = [1,2,3,4,5,6,7,8,0]

# shuffle puzzle
state = goal[:]
random.shuffle(state)

def draw():
    WIN.fill((0,0,0))

    for i in range(9):
        x = (i % 3) * 100
        y = (i // 3) * 100

        if state[i] != 0:
            pygame.draw.rect(WIN, (255,255,255), (x, y, 100, 100))
            text = FONT.render(str(state[i]), True, (0,0,0))
            WIN.blit(text, (x+40, y+30))

    # win text
    if state == goal:
        text = FONT.render("YOU WIN!", True, (0,255,0))
        WIN.blit(text, (80, 310))

    pygame.display.update()

def move(pos):
    i = pos[1]*3 + pos[0]
    zero = state.index(0)

    zx, zy = zero % 3, zero // 3

    if abs(zx - pos[0]) + abs(zy - pos[1]) == 1:
        state[zero], state[i] = state[i], state[zero]

while True:
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            move((mx//100, my//100))