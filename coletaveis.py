import pygame
from mapa import *
#define as classes de coletaveis
class Coletaveis(pygame.sprite.Sprite):
    """"'Classe Coletaveis'"""
    def __init__(self, pos, nome, group, coletaveis, obstacle_sprites):
        # Inserindo objeto no grupo camera
        super().__init__(group, coletaveis, obstacle_sprites)
        # Determinando sprite
        self.nome = nome
        self.image = pygame.image.load('coletaveis/medkit.png').convert_alpha()
        # Determinando posição inicial
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,0)
        
        
class Ammo(pygame.sprite.Sprite):
    """"'Classe Coletaveis'"""
    def __init__(self, pos, nome, group, coletaveis, obstacle_sprites):
        # Inserindo objeto no grupo camera
        super().__init__(group, coletaveis, obstacle_sprites)
        # Determinando sprite
        self.nome = nome
        self.image = pygame.image.load('coletaveis/municao.png').convert_alpha()
        # Determinando posição inicial
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,0)
        
        
class Pocao(pygame.sprite.Sprite):
    """"'Classe Coletaveis'"""
    def __init__(self, pos, nome, group, coletaveis, obstacle_sprites):
        # Inserindo objeto no grupo camera
        super().__init__(group, coletaveis, obstacle_sprites)
        # Determinando sprite
        self.nome = nome
        self.image = pygame.image.load('coletaveis/poção.png').convert_alpha()
        # Determinando posição inicial
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,0)
        
        
class Pistol(pygame.sprite.Sprite):
    """"'Classe Coletaveis'"""
    def __init__(self, pos, nome, group, coletaveis, obstacle_sprites):
        # Inserindo objeto no grupo camera
        super().__init__(group, coletaveis, obstacle_sprites)
        # Determinando sprite
        self.nome = nome
        self.image = pygame.image.load('coletaveis/pistol.png').convert_alpha()
        # Determinando posição inicial
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,0)