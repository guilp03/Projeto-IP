import pygame
from typing_extensions import Self

class DisparoArma(pygame.sprite.Sprite):
    """'CLASSE PRARA IMPLEMENTAR O PROJETIL QUE VAI SER DISPARADO PELA ARMA'"""
    def __init__(self, pos, groups, obstacle_sprites, status):
        super().__init__(groups)
        self.image = pygame.image.load('../Projeto-IP/prota/prota_idle_down.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,0)
        self.direction = pygame.math.Vector2()
        self.speed = 15
        self.obstacle_sprites = obstacle_sprites
        print(status)

    def direcao(self):
        if self.sentido == 'up' or self.sentido == 'up_idle':
            self.direction.y = -1
        elif self.sentido == 'down' or self.sentido == 'down_idle':
            self.direction.y = 1
        elif self.sentido == 'left' or self.sentido == 'left_idle':
            self.direction.x = -1
        elif self.sentido == 'right' or self.sentido == 'right_idle':
            self.direction.x = 1


    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
		

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                        if self.direction.x > 0: # moving right
                            self.hitbox.right = sprite.hitbox.left
                        if self.direction.x < 0: # moving left
                            self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.move(self.speed)