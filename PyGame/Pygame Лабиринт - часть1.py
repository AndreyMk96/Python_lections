"""Игра Лабиринт, часть 1. Создание сцены и фона"""
import pygame

WIDTH = 800
HEIGHT = 600

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labyrinth")

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