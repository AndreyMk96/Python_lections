"""Fruit Ninja 3. удаление объектов"""
import random
import time
import math

import pygame

WIDTH = 800
HEIGHT = 600

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit ninja")

# Добавляем яблоко

apple_x = 50
apple_y = 50

group = pygame.sprite.Group()


apple = pygame.image.load('apple.png')
dog_rect = apple.get_rect(
    bottomright=(apple_x, apple_y))
screen.blit(apple, dog_rect)

pygame.display.update()

# Цикл игры
running = True
r = 0
while running:
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Рендеринг
    screen.fill("grey")

    if int(time.time()) % 5 == 0:
        apple_x = random.randint(0, 800)
        apple_y = random.randint(0, 600)
        r = random.randint(0, 360)
    else:
        dog_rect = apple.get_rect(
            bottomright=(apple_x, apple_y))
        apple_x += 0.1 * math.cos(r)
        apple_y += 0.1 * math.sin(r)
        if abs(dog_rect.x - pygame.mouse.get_pos()[0]) < 10 and abs(dog_rect.y - pygame.mouse.get_pos()[1]) < 10:
            dog_rect = apple.get_rect(
                bottomright=(apple_x, apple_y))
            apple_x = 1000
            apple_y = 1000
    screen.blit(apple, dog_rect)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()


pygame.quit()