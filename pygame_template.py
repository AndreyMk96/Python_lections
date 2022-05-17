import random

import pygame

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

colors_list = [WHITE, BLACK, RED, GREEN, BLUE]

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labyrinth")



# Цикл игры
running = True
screen.fill("grey")
while running:

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                r1 = pygame.Rect((40, 0, 40, 40))
                pygame.draw.rect(screen, colors_list[random.randint(0,4)], r1, 0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                r1 = pygame.Rect((40, 0, 40, 40))
                pygame.draw.rect(screen, colors_list[random.randint(0, 4)], r1, 0)

    # Рендеринг

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()