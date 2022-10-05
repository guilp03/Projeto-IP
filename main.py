import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Zumbi')
clock = pygame.time.Clock()

test_surface = pygame.Surface((10, 10))
test_surface.fill('White')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface, (400, 200))

    pygame.display.update()
    clock.tick(60)