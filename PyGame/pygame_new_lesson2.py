"""Урок 2. Автоматическое движение объекта"""
import pygame
import time

WIDTH = 800
HEIGHT = 600

# Создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labyrinth")

screen.fill("grey")

r1 = pygame.Rect((40, 0, 40, 40))
pygame.draw.rect(screen, "red", r1, 0)

r2 = pygame.Rect((0,0, 40, 40))
pygame.draw.rect(screen, "green", r2, 0)

r3 = pygame.Rect((80,0, 40, 40))
pygame.draw.rect(screen, "blue", r3, 0)

r4 = pygame.Rect((120,0, 40, 40))
pygame.draw.rect(screen, "black", r4, 0)

# Цикл игры
running = True

r1_color = "red"

while running:
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Движение красного куба по горизонтали
    screen.fill("grey")

    r1 = pygame.Rect((r1.x + 1, 0, 40, 40))  # Объект r1 движется по горизонтали
    r2 = pygame.Rect((0, r2.y + 1, 40, 40))  # Объект r2 движется по вертикали

    x, y = pygame.mouse.get_pos()
    r3 = pygame.Rect((x - 20, y - 20, 40, 40))  # Объект r3 движется за курсором


    r4 = pygame.Rect((r3.x - 50, r3.y - 50, 40, 40))  # Объект движется за объектом r3

    rot = (45 + 45) % 360
    # rotating the orignal image
    new_image = pygame.transform.rotate(pygame.Surface((100 , 100)) , rot)
    rect = new_image.get_rect()
    # set the rotated rectangle to the old center
    rect.center = r4.center
    # drawing the rotated rectangle to the screen
    screen.blit(new_image, rect)
    pygame.draw.rect(screen, r1_color, r1, 0)
    pygame.draw.rect(screen, "green", r2, 0)
    pygame.draw.rect(screen, "blue", r3, 0)
    pygame.draw.rect(screen, "black", r4, 0)


    if r3.colliderect(r1) == True:
        r1_color = "grey"

    pygame.display.flip()

    time.sleep(0.01)

pygame.quit()