"""Урок 1. Обработка нажати клавиш и мыши"""

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
screen.fill("grey")
r1 = pygame.Rect((40, 0, 40, 40))
pygame.draw.rect(screen, colors_list[random.randint(0, 4)], r1, 0)
surf2 = pygame.Surface((100, 100))



# Цикл игры
running = True

while running:

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        """if pygame.mouse.get_focused():
            pos = pygame.mouse.get_pos()
            pygame.draw.rect(
                screen, BLUE, (pos[0] - 10,
                           pos[1] - 10,
                           20, 20))"""

        pos = pygame.mouse.get_pos()


        screen.fill("grey")
        r1.x += 1
        screen.blit(surf2, r1)

        pygame.display.update()


    # Рендеринг

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()