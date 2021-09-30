import pygame
import random

WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game1")

FPS = 7

a = 450
b = 300
c = 30
d = 30

delta_a = 0

delta_b = 0



def draw_window():
        WIN.fill((220, 255, 255))
        pygame.display.update()

def draw_rectangle():
    pygame.draw.rect(WIN, (250, 0, 0), pygame.Rect(a, b, c, d))
    pygame.display.update()

def random_x():
    ranWidth = random.choice(range(0, WIDTH, 30))
    return ranWidth

def random_y():
    ranHeight = random.choice(range(0, HEIGHT, 30))
    return ranHeight

def draw_food():
    global c, d, x, y
    pygame.draw.rect(WIN, (250, 0, 0), pygame.Rect(x, y, c, d))

x = random_y()
y = random_x()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        global a, b, c, d, delta_a, delta_b

        draw_window()
        draw_rectangle()
        draw_food()

        pygame.display.update()

        a += delta_a
        b += delta_b

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN:
                delta_a = 0
                delta_b = c
                draw_rectangle()
                pygame.display.update()

            elif event.key == pygame.K_UP:
                delta_a = 0
                delta_b = - c
                draw_rectangle()
                pygame.display.update

            elif event.key == pygame.K_LEFT:
                delta_a = - d
                delta_b = 0
                draw_rectangle()
                pygame.display.update

            elif event.key == pygame.K_RIGHT:
                delta_a = d
                delta_b = 0
                draw_rectangle()
                pygame.display.update

    pygame.quit()

if __name__ == "__main__":
    main()