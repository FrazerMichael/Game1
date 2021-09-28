import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game1")

FPS = 60

a = 30
b = 30
c = 30
d = 30

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

            draw_window()
            draw_rectangle()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN:
                    global b, d
                    b += d
                    draw_rectangle()
                    pygame.display.update

                elif event.key == pygame.K_UP:
                    b -= d
                    draw_rectangle()
                    pygame.display.update

                elif event.key == pygame.K_LEFT:
                    global a, c
                    a -= c
                    draw_rectangle()
                    pygame.display.update

                elif event.key == pygame.K_RIGHT:
                    a += c
                    draw_rectangle()
                    pygame.display.update


    pygame.quit()

def draw_rectangle():
    pygame.draw.rect(WIN, (250, 0, 0), pygame.Rect(a, b, c, d))
    pygame.display.flip()
    pygame.display.update()

if __name__ == "__main__":
    main()