import pygame
from mapa import *

class Celeiro(pygame.sprite.Sprite):
    
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('celeiro..png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (80*1.5, 81*1.5))

        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)

class Casa(pygame.sprite.Sprite):
    
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('casa.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (64*1.5, 36*1.5))

        self.rect = self.image.get_rect(topleft=pos)
        
        self.hitbox = self.rect.inflate(0, -10)
class Trator(pygame.sprite.Sprite):
    
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('trator.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (31*1.2, 27*1.2))

        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)