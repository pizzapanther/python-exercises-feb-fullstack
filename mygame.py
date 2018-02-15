import pygame
import sys

def move_square(dx=1, dy=1):
    global x
    global y

    x += dx
    y += dy

    screen.fill((0, 0, 0))
    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (x, y, 100, 100),
        0
    )
    pygame.display.update()

pygame.init()

screen = pygame.display.set_mode((500, 500))

x = 200
y = 200
pygame.draw.rect(
  screen,
  (255, 0, 0),
  (x, y, 100, 100),
  0
)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_square(0, -1)
            elif event.key == pygame.K_DOWN:
                move_square(0, 1)

            print(event)
        else:
            print(event.type)
            
