"""Урок 1. Обработка нажати клавиш и мыши"""

import random
import datetime
import time

import pygame

WIDTH = 800
HEIGHT = 600


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))



# Цикл игры
running = True

while running:
    now = datetime.datetime.now()

    if now.second % 2 == 0:
        r1 = pygame.Rect((random.randint(100,700), random.randint(100,600), 40, 40))
        pygame.draw.rect(screen, "red", r1, 0)
        #time.sleep(0.3)
        r1 = pygame.Rect((r1.x + 1, 0, 40, 40))  # Объект r1 движется по горизонтали

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False


    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()