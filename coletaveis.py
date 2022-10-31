import pygame
from mapa import *

class Coletaveis(pygame.sprite.Sprite):
    """"'Classe Coletaveis'"""



    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('medkit.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, 0)