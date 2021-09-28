import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game1")

FPS = 10

a = 450
b = 240
c = 30
d = 30

delta_a = 0

delta_b = 0

def draw_window():
        WIN.fill((220, 255, 255))
        pygame.display.update()


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

        a += delta_a
        b += delta_b

        pygame.display.update

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

def draw_rectangle():
    pygame.draw.rect(WIN, (250, 0, 0), pygame.Rect(a, b, c, d))
    pygame.display.flip()
    pygame.display.update()

if __name__ == "__main__":
    main()