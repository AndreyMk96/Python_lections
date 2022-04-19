"""Игра Лабиринт часть 3. Добавление персонажа, и реализация его движения с клавиатуры"""
import pygame

WIDTH = 800
HEIGHT = 600

# Обычно цвета тоже выносят в отдельные константы
BROWN = (160,82,45)
DARK_RED = (165,42,42)
DARK_YELLOW = (85,107,47)

# Координаты
X = 65
Y = 65
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

        # События на обработку клавищ
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            X += 5
        if keys[pygame.K_a]:
            X -= 5
        if keys[pygame.K_s]:
            Y += 5
        if keys[pygame.K_w]:
            Y -= 5

    screen.fill("grey")

    # Рисуем верхнюю полосу
    for i in range(20):
        r1 = pygame.Rect((i*40, 0, 40, 40))
        pygame.draw.rect(screen, BROWN, r1, 0)
        r2 = pygame.Rect((5 + i * 40, 5, 30, 30))
        pygame.draw.rect(screen, DARK_RED, r2, 0)

    # Рисуем нижнюю полосу
    for i in range(20):
        r1 = pygame.Rect((i*40, 560, 40, 40))
        pygame.draw.rect(screen, BROWN, r1, 0)
        r2 = pygame.Rect((5 + i * 40, 565, 30, 30))
        pygame.draw.rect(screen, DARK_RED, r2, 0)

    # Рисуем левую боковую полосу
    for i in range(15):
        r1 = pygame.Rect((0, i * 40, 40, 40))
        pygame.draw.rect(screen, BROWN, r1, 0)
        r2 = pygame.Rect((5, 5 + i * 40, 30, 30))
        pygame.draw.rect(screen, DARK_RED, r2, 0)

    # Рисуем правую боковую полосу
    for i in range(15):
        r1 = pygame.Rect((760, i * 40, 40, 40))
        pygame.draw.rect(screen, BROWN, r1, 0)
        r2 = pygame.Rect((765, 5 + i * 40, 30, 30))
        pygame.draw.rect(screen, DARK_RED, r2, 0)

    # Рисуем внутреннюю верхнюю полосу
    for i in range(15):
        r1 = pygame.Rect((100 + i*40, 100, 40, 40))
        pygame.draw.rect(screen, BROWN, r1, 0)
        r2 = pygame.Rect((100 + 5 + i * 40, 105, 30, 30))
        pygame.draw.rect(screen, DARK_RED, r2, 0)

    # Рисуем внутреннюю нижнюю полосу
    for i in range(15):
        r1 = pygame.Rect((100 + i * 40, 460, 40, 40))
        pygame.draw.rect(screen, BROWN, r1, 0)
        r2 = pygame.Rect((105 + i * 40, 465, 30, 30))
        pygame.draw.rect(screen, DARK_RED, r2, 0)

    # Рисуем внутреннюю правую боковую полосу
    for i in range(5):
        r1 = pygame.Rect((660, 200 + i * 40, 40, 40))
        pygame.draw.rect(screen, BROWN, r1, 0)
        r2 = pygame.Rect((665, 5 + 200 + i * 40, 30, 30))
        pygame.draw.rect(screen, DARK_RED, r2, 0)

    # Рисуем внутреннюю левую боковую полосу
    for i in range(5):
        r1 = pygame.Rect((100, 200 + i * 40, 40, 40))
        pygame.draw.rect(screen, BROWN, r1, 0)
        r2 = pygame.Rect((105, 5 + 200 + i * 40, 30, 30))
        pygame.draw.rect(screen, DARK_RED, r2, 0)

    # Создаем объект - круг
    smile = pygame.draw.circle(screen, DARK_YELLOW, (X, Y), 15)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()