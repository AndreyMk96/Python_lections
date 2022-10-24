"""Урок 3. Поворот объекта"""
import math
import random
import time

import pygame as py


# initialize pygame and create screen
py.init()
screen = py.display.set_mode((800 , 600))
clock = py.time.Clock()

# Определяем интерфейс (прямоугольник)
image_orig = py.Surface((100, 100))
# Делаем черный фон для вращения изображения
image_orig.set_colorkey("black")
# Заполняем прямоугольник зеленым цветом
image_orig.fill("green")
X,Y =400, 300
running = True
angle = 225

while running:
    screen.fill("black")
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    # Поворачиваем изображение
    new_image = py.transform.rotate(image_orig ,angle)
    rect = new_image.get_rect()
    # Устанавливаем центр прямоугольника
    rect.center = (X, Y)
    r = angle * 3.14 / 180
    X += 1 * math.cos(r)
    Y += 1 * math.sin(r)
    # Рисуем повернутый прямоугольник
    screen.blit(new_image , rect)
    # Пролистываем дисплей после рисования
    py.display.flip()
    time.sleep(0.01)

py.quit()