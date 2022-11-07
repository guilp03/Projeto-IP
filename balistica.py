import pygame


#cria a classe do projetil
class DisparoArma(pygame.sprite.Sprite):
    """'CLASSE PRARA IMPLEMENTAR O PROJETIL QUE VAI SER DISPARADO PELA ARMA'"""
    def __init__(self, pos, groups, obstacle_sprites, status, colisao_zumbi):
        super().__init__(groups)
        #infos basicas do projetil
        self.image = pygame.image.load('tiro/tiro_right.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,0)
        self.direction = pygame.math.Vector2()
        self.sentido = status
        self.speed = 15
        self.obstacle_sprites = obstacle_sprites
        self.zumbi = colisao_zumbi
        self.index = 0
        self.animation_speed = 0.2
        self.animations = {'up': ['tiro/tiro3_up.png', 'tiro/tiro4_up.png'],
							'down': ['tiro/tiro3_down.png', 'tiro/tiro4_down.png'],
							'left': ['tiro/tiro3_left.png', 'tiro/tiro4_left.png'],
							'right': ['tiro/tiro3_right.png', 'tiro/tiro4_right.png'],
							'up_idle': ['tiro/tiro3_up.png', 'tiro/tiro4_up.png'], 'down_idle': ['tiro/tiro3_down.png', 'tiro/tiro4_down.png'],
							'left_idle': ['tiro/tiro3_left.png', 'tiro/tiro4_left.png'], 'right_idle': ['tiro/tiro3_right.png', 'tiro/tiro4_right.png']}
        self.count = False


    def direcao(self):
        #define a direcao do projetil
        if self.sentido == 'up' or self.sentido == 'up_idle':
            self.direction.y = -1
            self.image = pygame.image.load('tiro/tiro2_up.png').convert_alpha()
        elif self.sentido == 'down' or self.sentido == 'down_idle':
            self.direction.y = 1
            self.image = pygame.image.load('tiro/tiro2_down.png').convert_alpha()
        elif self.sentido == 'left' or self.sentido == 'left_idle':
            self.direction.x = -1
            self.image = pygame.image.load('tiro/tiro2_left.png').convert_alpha()
        elif self.sentido == 'right' or self.sentido == 'right_idle':
            self.direction.x = 1
            self.image = pygame.image.load('tiro/tiro2_right.png').convert_alpha()


    def move(self,speed):
        #atualiza a hitbox de acordo com o movimento
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
		

    def collision(self,direction):
        #implementa a animacao do projetil
        animation = self.animations[self.sentido]
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    #define a colisao do projetil com o terreno
                    self.direction.x = 0
                    self.direction.y = 0
                    self.image = pygame.image.load(animation[int(self.index)]).convert_alpha()
                    self.count= True

            for sprite in self.zumbi:
                if sprite.hitbox.colliderect(self.hitbox):
                    #define a colisao do projetil com o terreno
                    self.direction.y = 0
                    self.direction.x = 0
                    self.image = pygame.image.load(animation[int(self.index)]).convert_alpha()
                    self.count = True

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    #define a colisao do projetil com o terreno
                    self.direction.y = 0
                    self.direction.x = 0
                    self.image = pygame.image.load(animation[int(self.index)]).convert_alpha()
                    self.count = True
            
            for sprite in self.zumbi:
                if sprite.hitbox.colliderect(self.hitbox):
                    #define a colisao do projetil com o terreno
                    self.direction.y = 0
                    self.direction.x = 0
                    self.image = pygame.image.load(animation[int(self.index)]).convert_alpha()
                    self.count = True


    def update(self):
        #atualiza os dados e exclui a bala do mundo apos uma animacao
        if self.count == False:
            self.direcao()
        self.move(self.speed)
        if self.count == True:
            self.index += self.animation_speed
        if self.index >= 1.8:
                self.index = 0
                self.kill()