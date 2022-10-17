import pygame
from pygame import *

class Player(pygame.sprite.Sprite):
    def init(self, pos, groups):
        super().init(groups)
        self.image = pygame.image.load('graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5


    def input(self):
        key = pygame.key.get_pressed()


        if key[K_w]:
            self.direction.y = -1
        elif key[K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if key[K_a]:
            self.direction.x = -1
        elif key[K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        
    
    def mov(self, speed):
        self.rect.center += self.direction * speed


    def update(self):
        self.input()
        self.mov(self.speed)
