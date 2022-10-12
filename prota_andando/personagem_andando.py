import pygame
from pygame import *
from sys import exit
pygame.init()  # inicar o pygame

largura_tela = 800
altura_tela = 600




tela = pygame.display.set_mode((largura_tela, altura_tela))  # tamanho da tela do jogo
nome_tela = pygame.display.set_caption('Animação andando')  # nome da tela

imagem = pygame.image.load('Meu projeto.png').convert_alpha()
imagem = pygame.transform.scale(imagem, (50 * 5, 77 * 5))

relogio = pygame.time.Clock().tick(10)

x_sprites_prota = 0
y_sprites_prota = 0

posicao_x_prota = 200
posicao_y_prota = 200

largura_personagem = 80
altura_personagem = 80
while True:

    tela.blit(imagem, (posicao_x_prota, posicao_y_prota), (x_sprites_prota, y_sprites_prota, largura_personagem, altura_personagem))

    for event in pygame.event.get():  # o looping de eventos
        if event.type == QUIT:  # fechar a tela do jogo
            pygame.quit()
            exit()



    #PROTA ANDANDO
    key = pygame.key.get_pressed()

    # DIGANOAIS
    if key[K_a] and key[K_w]:
        posicao_x_prota -= 17
        posicao_y_prota -= 17
        y_sprites_prota = 0
        x_sprites_prota += 80
        if x_sprites_prota >= 240:
            x_sprites_prota = 6

    elif key[K_w] and key[K_d]:
        posicao_x_prota += 17
        posicao_y_prota -= 17
        y_sprites_prota = 0
        x_sprites_prota += 80
        if x_sprites_prota >= 240:
            x_sprites_prota = 6

    elif key[K_s] and key[K_d]:
        posicao_x_prota += 17
        posicao_y_prota += 17
        y_sprites_prota = 96
        x_sprites_prota += 80
        if x_sprites_prota >= 240:
            x_sprites_prota = 6

    elif key[K_s] and key[K_a]:
        posicao_x_prota -= 17
        posicao_y_prota += 17
        y_sprites_prota = 96
        x_sprites_prota += 80
        if x_sprites_prota >= 240:
            x_sprites_prota = 6


    elif key[K_d]:#direita


        posicao_x_prota += 17
        posicao_y_prota += 0
        x_sprites_prota += 80
        y_sprites_prota = 190
        if x_sprites_prota >= 240:
            x_sprites_prota = 9

    elif key[K_a]:#esquerda



        posicao_x_prota -= 17
        posicao_y_prota += 0
        y_sprites_prota = 290
        x_sprites_prota += 80
        if x_sprites_prota >= 240:
            x_sprites_prota = 9









    elif key[K_w]:#cima


        posicao_x_prota += 0
        posicao_y_prota -= 17
        y_sprites_prota = 0
        x_sprites_prota += 80
        if x_sprites_prota >= 240:
            x_sprites_prota = 6

    elif key[K_s]:#baixo


        posicao_x_prota += 0
        posicao_y_prota += 17
        y_sprites_prota = 96
        x_sprites_prota += 80
        if x_sprites_prota >= 240:
            x_sprites_prota = 6

    #DIAGANOAIS
    elif key[K_a] and key[K_w]:
        posicao_x_prota -= 17
        posicao_y_prota -= 17
        y_sprites_prota = 0
        x_sprites_prota += 80
        if x_sprites_prota >= 240:
            x_sprites_prota = 6

    #CASO O PROTA ESTEJA PARADO
    else:
        #cima
        if y_sprites_prota == 0:
            x_sprites_prota = 0
        #baixo
        elif y_sprites_prota == 96:
            x_sprites_prota = 0

        #direita
        elif y_sprites_prota == 190:
            x_sprites_prota = 0

        #esquerda
        elif y_sprites_prota == 290:
            x_sprites_prota = 164




    # codigo para q o personagem n saia da tela do jogo
    if posicao_y_prota > altura_tela - altura_personagem:
        posicao_y_prota -= 7
    elif posicao_y_prota < 0:
        posicao_y_prota += 7

    # codigo para q o personagem n saia da tela do jogo
    if posicao_x_prota > largura_tela - largura_personagem:
        posicao_x_prota -= 7
    elif posicao_x_prota < 0:
        posicao_x_prota += 7



    pygame.display.flip()
    tela.fill((170, 170, 170))
    pygame.time.Clock().tick(10)