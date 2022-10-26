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
    """'CLASSE PARA DISPARAR AS BALAS'"""
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 15 # VELOCIDADE DA BALA
        #CALCULO PRA ISOLAR O X E O Y PRA UTILIZAR NA BALA
        self.angulo = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angulo) * self.speed
        self.y_vel = math.sin(self.angulo) * self.speed

    def main(self,display):
        #FUNÇÃO PARA DESENHAR A BALA E FAZER A MOVIMENTAÇÃO
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        pygame.draw.circle(display, '#f3d300', (self.x, self.y), 5)

#define Posição e tamanho do jogador
player = Player(int(lar/2), int(alt/2),64,64)

#centro da tela (pra movimentar)
display_scrool = [0,0]

player_bullets = []

while True:
    #background collor
    display.fill('#95b634')
    mouse_x, mouse_y = pygame.mouse.get_pos()

    #Eventos que acontecem
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
        
        # QUANDO APERTA O BOTÃO 1 DO MOUSE DISPARA A BALA
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player_bullets.append(PlayerBullet(player.x, player.y, mouse_x, mouse_y))

    #Movimentação do Personagem
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        display_scrool[0] -= 5
        #PRA BALA TRILHAR A PRÓPRIA TRAJETÓRIA
        for bullet in player_bullets:
            bullet.x += 5
    if keys[pygame.K_d]:
        display_scrool[0] += 5
        #PRA BALA TRILHAR A PRÓPRIA TRAJETÓRIA
        for bullet in player_bullets:
            bullet.x -= 5
    if keys[pygame.K_w]:
        display_scrool[1] -= 5
        #PRA BALA TRILHAR A PRÓPRIA TRAJETÓRIA
        for bullet in player_bullets:
            bullet.y += 5
    if keys[pygame.K_s]:
        display_scrool[1] += 5
        #PRA BALA TRILHAR A PRÓPRIA TRAJETÓRIA
        for bullet in player_bullets:
            bullet.y -= 5
    #ZUMBI ALEATORIO
    pygame.draw.rect(display,'#ffffff',(x_zumbi-display_scrool[0],y_zumbi-display_scrool[1],32,32))

    #SE TIVER BALA, MOSTRA ELA
    for bullet in player_bullets:
        bullet.main(display)

    player.main(display)
    clock.tick(60)
    pygame.display.update()