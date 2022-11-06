import pygame
from mapa import *
#define as classes para as cercas do jogo, que tambem atuam como barreiras
class Cerca(pygame.sprite.Sprite):
    
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('cercas/cerca_cima.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (3*5, 16*5))
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)

class Cerca1(pygame.sprite.Sprite):
    
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('cercas/cerca_topleft.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (16*5, 16*5))

        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
class Cerca2(pygame.sprite.Sprite):
    
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('cercas/cerca_lado.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (16*5, 7*5))
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, 0)


class Cerca3(pygame.sprite.Sprite):
    
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('cercas/cerca_topright.png').convert_alpha()
        
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)


class Cerca4(pygame.sprite.Sprite):
    
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('cercas/cerca_botright.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
  
        
class Cerca5(pygame.sprite.Sprite):
    
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('cercas/cerca_botleft.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)