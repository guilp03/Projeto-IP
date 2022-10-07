import pygame
from pygame import *
from sys import exit

pygame.init() #inicar o pygame

largura_tela = 700
altura_tela = 500

colidiu = False


x_prota = largura_tela / 2
y_prota = altura_tela / 2
tela = pygame.display.set_mode((largura_tela, altura_tela)) #tamanho da tela do jogo
nome_tela = pygame.display.set_caption('jogo teste') #nome da tela

relogio = pygame.time.Clock()


#dados colisao do prota com as paredes


while True:#looping principal
    
    
    relogio.tick(30)#frames
    tela.fill((0,0,0))#quando o quadrado se move ele deixa um quadradro preto pra tras e isso da a ideia de MOV, ajeitar isso mais tarde para ele deixar um quadradro transparente
    
    for event in pygame.event.get(): #o looping de eventos 
        if event.type == QUIT: #fechar a tela do jogo
            pygame.quit()
            exit()
   
    #movimento persongem_principal    
    if pygame.key.get_pressed()[K_a]:
                x_prota -= 7
    if pygame.key.get_pressed()[K_d]:
                x_prota += 7
    if pygame.key.get_pressed()[K_w]:
                y_prota -= 7
    if pygame.key.get_pressed()[K_s]:
                y_prota += 7
        

        #quadrado que representa o personagem principal 
    largura_personagem = 50
    altura_personagem = 50

    quadrado_principal = pygame.draw.rect(tela, (255,255,255), (x_prota, y_prota, largura_personagem, altura_personagem))#personagem 
    box = pygame.draw.rect(tela, (0,255,255), (200, 100, 40, 50,))#personagem 

    
    '''#paredes
    quadrado_parede_right = pygame.draw.rect(tela, (255,255,255), (largura - 0.1, 0, 20, altura))
    quadrado_parede_left = pygame.draw.rect(tela, (255,255,255), (0, 0, 1.1, altura))
    quadrado_teto = pygame.draw.rect(tela, (255 ,0 ,0), (0, 0, largura, 1.1))
    quadrado_chao = pygame.draw.rect(tela, (255 ,0 ,0), (0, altura - 0.1 ,  largura, 20))'''
     #codigo para q o personagem n saia da tela do jogo
    if y_prota > altura_tela - altura_personagem :
        y_prota -= 7
    elif y_prota < 0:
        y_prota += 7
    
    if x_prota > largura_tela - largura_personagem:
        x_prota -= 7
    elif x_prota < 0:
        x_prota += 7
    





    
       
        

        







    pygame.display.update() # comando para atualizar a cada evento que acontece