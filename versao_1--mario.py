import pygame
from pygame import *
from sys import exit
import persoangem
pygame.init()  # inicar o pygame

largura_tela = 800
altura_tela = 600


x_prota = largura_tela / 2
y_prota = altura_tela / 2
tela = pygame.display.set_mode((largura_tela, altura_tela))  # tamanho da tela do jogo
nome_tela = pygame.display.set_caption('jogo teste')  # nome da tela

relogio = pygame.time.Clock()

itens = pygame.image.load('Zombie Apocalypse Tileset.png')
#prota = persoangem.Personagem(#botar o wx, wy, x, y, altu, larg igual ao do m_blit)

def m_blit(tela, img, wx, wy, x, y, altu, larg):
    surf = pygame.Surface((altu, larg)).convert()
    surf.blit(img, (0, 0), (wx, wy, altu, larg))
    surf = pygame.transform.scale(surf, (altu * 10, larg * 10))
    alpha = surf.get_at((0, 0))
    surf.set_colorkey(alpha)
    tela.blit(surf, (x, y))

while True:  # looping principal
    pos = [[], []] #vai receber o wx do primeiro frame e o segund, usar pra ver as diferenças

    relogio.tick(30)  # frames
    tela.fill((0, 0, 200))  # quando o quadrado se move ele deixa um quadradro preto pra tras e isso da a ideia de MOV, ajeitar isso mais tarde para ele deixar um quadradro transparente

    #achar wx e wy, obs por imagem no paint para achar
    m_blit(tela, itens, 479, 125, 200, 200, 16, 16)


    for event in pygame.event.get():  # o looping de eventos
        if event.type == QUIT:  # fechar a tela do jogo
            pygame.quit()
            exit()

    # movimento persongem_principal
    if pygame.key.get_pressed()[K_a]:
        x_prota -= 7
    if pygame.key.get_pressed()[K_d]:
        x_prota += 7
    if pygame.key.get_pressed()[K_w]:
        y_prota -= 7
    if pygame.key.get_pressed()[K_s]:
        y_prota += 7

    # quadrado que representa o personagem principal
    largura_personagem = 50
    altura_personagem = 50

    #quadrado_principal = pygame.draw.rect(tela, (255, 255, 255),(x_prota, y_prota, largura_personagem, altura_personagem))  # personagem
    #box = pygame.draw.rect(tela, (0, 255, 255), (200, 100, 40, 50,))  # personagem


    # codigo para q o personagem n saia da tela do jogo
    if y_prota > altura_tela - altura_personagem:
        y_prota -= 7
    elif y_prota < 0:
        y_prota += 7

    if x_prota > largura_tela - largura_personagem:
        x_prota -= 7
    elif x_prota < 0:
        x_prota += 7

    pygame.display.update()  # comando para atualizar a cada evento que acontece
