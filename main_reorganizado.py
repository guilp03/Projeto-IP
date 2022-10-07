import pygame
import os

pygame.init()
tela = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Super Mário Borba")
rodando = True
x_prota = 640
y_prota = 360
raio = 15
v = 10
while rodando:
    pygame.draw.circle(tela, (155,255,55), (int(x_prota),int(y_prota)), raio)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
            
            
    input = pygame.key.get_pressed()
    if input[pygame.K_LEFT]:
        x_prota -= vel_prota
    if input[pygame.K_RIGHT]:
        x_prota += vel_prota
    if input[pygame.K_UP]:
        y_prota += vel_prota
    if input[pygame.K_DOWN]:
        y_prota -= vel_prota
        
    pygame.display.update()