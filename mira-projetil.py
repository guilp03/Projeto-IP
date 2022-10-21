import pygame
import sys
from random import randint
import math

pygame.init()

lar = 1080
alt = 720
x_zumbi = randint(60,1020)
y_zumbi = randint(60,660)
#FORMATAÇÃO GERAL
display = pygame.display.set_mode((lar,alt))
clock = pygame.time.Clock()

class Player:
    """'CLASSE QUE DEFINE O JOGADOR'"""
    #Formatação geral do jogador
    def __init__(self,x,y,largura,altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
    #desenha um retangulo para representá-lo
    def main(self, display):
        pygame.draw.rect(display,'#964b00',(self.x, self.y, self.largura, self.altura))

class PlayerBullet:
    """'METE BALA TIAMU CHEIROSA TIAMO METEBALA TIAMO'"""
    def __init__(self, x,y,mouse_x,mouse_y,largura,altura,speed):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.speed = speed
        self.ange = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * speed
        self.y_vel = math.sin(self.angle) * speed

    def main(self,display):
        self.x -=


#define Posição e tamanho do jogador
player = Player(int(lar/2), int(alt/2),64,64)

#centro da tela (pra movimentar)
display_scrool = [0,0]

while True:
    #background collor
    display.fill('#7ed957')

    #Eventos que acontecem
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT

    #Movimentação do Personagem
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        display_scrool[0] -= 5
    if keys[pygame.K_d]:
        display_scrool[0] += 5
    if keys[pygame.K_w]:
        display_scrool[1] -= 5
    if keys[pygame.K_s]:
        display_scrool[1] += 5
    #ZUMBI ALEATORIO
    pygame.draw.rect(display,'#ffffff',(x_zumbi-display_scrool[0],y_zumbi-display_scrool[1],32,32))

    player.main(display)
    clock.tick(60)
    pygame.display.update()