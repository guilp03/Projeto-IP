import pygame
from sys import exit
import os

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Zumbi')
clock = pygame.time.Clock()

<<<<<<< Updated upstream
test_surface = pygame.Surface((10, 10))
test_surface.fill('White')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
=======
largura_tela = 1920
altura_tela = 1080

colidiu = False
#imagem do zumbi
z = pygame.image.load(os.path.join("imagem zumbi", "zumbi-maior.png"))

x_prota = largura_tela / 2
y_prota = altura_tela / 2
tela = pygame.display.set_mode((largura_tela, altura_tela)) #tamanho da tela do jogo
nome_tela = pygame.display.set_caption('jogo teste') #nome da tela

relogio = pygame.time.Clock()
#criando classe de zumbi
class Zumbi:
    def __init__(self, x_zumbi, y_zumbi):
        self.x_zumbi = x_zumbi
        self.y_zumbi = y_zumbi
    
    def tela(self, tela):
        tela.blit(z,(self.x_zumbi,self.y_zumbi))
inimigos_vivos = []
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
        
    if len(inimigos_vivos) == 0:
        inimigo = Zumbi(50, 40)
        inimigos_vivos.append(inimigo)
    for inimigo in inimigos_vivos:
        inimigo.tela(tela)
        
        
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
    





    
       
        

        





>>>>>>> Stashed changes

    screen.blit(test_surface, (400, 200))

    pygame.display.update()
    clock.tick(60)