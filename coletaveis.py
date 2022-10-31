import pygame
from mapa import *

class Coletaveis(pygame.sprite.Sprite):
    """"'Classe Coletaveis'"""
    def __init__(self, pos, group, coletaveis):
        # Inserindo objeto no grupo camera
        super().__init__(group, coletaveis)
        # Determinando sprite
        self.image = pygame.image.load('medkit.png').convert_alpha()
        # Determinando posição inicial
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-10)