import pygame
from mapa import *
class Zumbi(pygame.sprite.Sprite):
    #definindo os dados base de um zumbi
    def __init__(self,tipo_zumbi, pos, group, player, obstacle_sprites):
        super().__init__(group)
        #Player
        self.player = player
        # Tipo do zumbi
        self.zumbis = ['normal', 'zumbinho', 'boomer']
        self.zombies= {'normal': {'hp': 40, 'speed': 3, 'animation_speed': 0.15}, 'zumbinho': {'hp': 40, 'speed': 5, 'animation_speed': 0.2}, 'boomer': {'hp': 40, 'speed': 2, 'animation_speed': 0.1 }  }
        self.tipo_zumbi = tipo_zumbi
        infos = self.zombies[self.tipo_zumbi]
        # HP e VEl
        self.hp = infos['hp']
        self.speed = infos['speed']
        #Animação e Movimento
        self.animation_speed = infos['animation_speed']
        self.image = pygame.image.load(f'../Projeto-IP/{self.tipo_zumbi}/{self.tipo_zumbi}_down_0.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.direction = pygame.math.Vector2()
        self.status = 'down'
        self.frame_index = 0
        self.importar()

        self.obstacle_sprites = obstacle_sprites

        #movimentacao ainda em experimentacao
    def zombie_move(self): 

        if self.rect.y > self.player.rect.y:
            self.direction.y = -1
            self.status = 'up'
        elif self.rect.y < self.player.rect.y:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if self.rect.x > self.player.rect.x:
            self.direction.x = -1
            self.status = 'left'
        elif self.rect.x < self.player.rect.x:
            self.direction.x = 1
            self.status = 'right'
        else:
            self.direction.x = 0

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status:
                self.status = self.status + '_idle'
                
        
    def importar(self):
        if self.tipo_zumbi == 'boomer':
            self.animations = {'up': ['../Projeto-IP/boomer/boomer_up_0.png', '../Projeto-IP/boomer/boomer_up_1.png', '../Projeto-IP/boomer/boomer_up_2.png'], 'down': ['../Projeto-IP/boomer/boomer_down_0.png', '../Projeto-IP/boomer/boomer_down_1.png', '../Projeto-IP/boomer/boomer_down_2.png'], 
                            'left': ['../Projeto-IP/boomer/boomer_left_0.png', '../Projeto-IP/boomer/boomer_left_1.png', '../Projeto-IP/boomer/boomer_left_2.png'], 'right': ['../Projeto-IP/boomer/boomer_right_0.png', '../Projeto-IP/boomer/boomer_right_1.png', '../Projeto-IP/boomer/boomer_right_2.png'], 
                            'up_idle': ['../Projeto-IP/boomer/boomer_idle_up.png'], 'down_idle': ['../Projeto-IP/boomer/boomer_idle_down.png'], 
                            'left_idle': ['../Projeto-IP/boomer/boomer_idle_left.png'], 'right_idle': ['../Projeto-IP/boomer/boomer_idle_right.png']}
        elif self.tipo_zumbi == 'normal':
            self.animations = {'up': ['../Projeto-IP/normal/up_0.png', '../Projeto-IP/normal/up_1.png', '../Projeto-IP/normal/up_2.png'], 'down': ['../Projeto-IP/normal/down_0.png', '../Projeto-IP/normal/down_1.png', '../Projeto-IP/normal/down_2.png'], 
                            'left': ['../Projeto-IP/normal/left_0.png', '../Projeto-IP/normal/left_1.png', '../Projeto-IP/normal/left_2.png'], 'right': ['../Projeto-IP/normal/right_0.png', '../Projeto-IP/normal/right_1.png', '../Projeto-IP/normal/right_2.png'], 
                            'up_idle': ['../Projeto-IP/normal/idle_up.png'], 'down_idle': ['../Projeto-IP/normal/idle_down.png'], 
                            'left_idle': ['../Projeto-IP/normal/idle_left.png'], 'right_idle': ['../Projeto-IP/normal/idle_right.png']}
        elif self.tipo_zumbi == 'zumbinho':
            self.animations = {'up': ['../Projeto-IP/zumbinho/zumbinho_up_0.png', '../Projeto-IP/zumbinho/zumbinho_up_1.png', '../Projeto-IP/zumbinho/zumbinho_up_2.png'], 'down': ['../Projeto-IP/zumbinho/zumbinho_down_0.png', '../Projeto-IP/zumbinho/zumbinho_down_1.png', '../Projeto-IP/zumbinho/zumbinho_down_2.png'], 
                            'left': ['../Projeto-IP/zumbinho/zumbinho_left_0.png', '../Projeto-IP/zumbinho/zumbinho_left_1.png', '../Projeto-IP/zumbinho/zumbinho_left_2.png'], 'right': ['../Projeto-IP/zumbinho/zumbinho_right_0.png', '../Projeto-IP/zumbinho/zumbinho_right_1.png', '../Projeto-IP/zumbinho/zumbinho_right_2.png'], 
                            'up_idle': ['../Projeto-IP/zumbinho/zumbinho_idle_up.png'], 'down_idle': ['../Projeto-IP/zumbinho/zumbinho_idle_down.png'], 
                            'left_idle': ['../Projeto-IP/zumbinho/zumbinho_idle_left.png'], 'right_idle': ['../Projeto-IP/zumbinho/zumbinho_idle_right.png']}
            
    def animar(self):
        animation = self.animations[self.status]
        
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        self.image = pygame.image.load(animation[int(self.frame_index)]).convert_alpha()
    
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
        self.zombie_move()
        self.move(self.speed)
        self.get_status()
        self.animar()