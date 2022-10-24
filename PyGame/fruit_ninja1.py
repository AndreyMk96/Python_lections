"""Игра Fruit Ninja, часть 1. Создание сцены и фона"""
import pygame

# Создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fruit ninja")

# Цикл игры
running = True
while running:
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Рендеринг
    screen.fill("grey")
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()