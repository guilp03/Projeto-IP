import pygame
from mapa import *

class Coletaveis(pygame.sprite.Sprite):
    """"'Classe Coletaveis'"""
    def __init__(self, pos, nome, group, coletaveis, obstacle_sprites):
        # Inserindo objeto no grupo camera
        super().__init__(group, coletaveis, obstacle_sprites)
        # Determinando sprite
        self.nome = nome
        self.image = pygame.image.load('medkit.png').convert_alpha()
        # Determinando posição inicial
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,0)
