import pygame
from mapa import *

class Coletaveis(pygame.sprite.Sprite):
    """"'Classe Coletaveis'"""
    def __init__(self, pos, group, obstacle_sprites, lista_coletaveis):
        # Inserindo objeto no grupo camera
        super().__init__(group, obstacle_sprites, lista_coletaveis)
        # Determinando sprite
        self.image = pygame.image.load('medkit.png').convert_alpha()
        # Determinando posição inicial
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,0)
    
    