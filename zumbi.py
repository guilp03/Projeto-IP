import pygame
from mapa import *

mortes = 0
class Zumbi(pygame.sprite.Sprite):
    #definindo os dados base de um zumbi
    def __init__(self,tipo_zumbi, pos, group, player, obstacle_sprites, colisao_player):
        super().__init__(group)
        #Player
        self.player = player
        
        # Tipo do zumbi
        self.zumbis = ['normal', 'zumbinho', 'boomer']
        self.zombies= {'normal': {'hp': 150, 'speed': 3, 'animation_speed': 0.15}, 'zumbinho': {'hp': 50, 'speed': 5, 'animation_speed': 0.2}, 'boomer': {'hp': 300, 'speed': 2, 'animation_speed': 0.1 }  }
        self.tipo_zumbi = tipo_zumbi
        infos = self.zombies[self.tipo_zumbi]
        # HP e VEl
        self.hp = infos['hp']
        self.speed = infos['speed']
        #Animação e Movimento
        self.animation_speed = infos['animation_speed']
        self.image = pygame.image.load(f'{self.tipo_zumbi}/{self.tipo_zumbi}_down_0.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.inflate(0,0)
        self.direction = pygame.math.Vector2()
        self.status = 'down'
        self.frame_index = 0
        self.importar()

        #informacao para a morte do zumbi
        self.mortes = 0
        self.colisao_player = colisao_player
        self.obstacle_sprites = obstacle_sprites
        self.cooldown_dano = 2


    def zombie_move(self): 
        #movimentacao do zumbi, que se move de acordo com a localizacao do player
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
        #funcao para diferenciar quando o zumbi se movimenta e quando esta parado
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status:
                self.status = self.status + '_idle'
                
        
    def importar(self):
        #funcao que seleciona o banco de sprites para o zumbi de acordo com seu tipo
        if self.tipo_zumbi == 'boomer':
            self.animations = {'up': ['boomer/boomer_up_0.png', 'boomer/boomer_up_1.png', 'boomer/boomer_up_2.png'], 'down': ['boomer/boomer_down_0.png', 'boomer/boomer_down_1.png', 'boomer/boomer_down_2.png'], 
                            'left': ['boomer/boomer_left_0.png', 'boomer/boomer_left_1.png', 'boomer/boomer_left_2.png'], 'right': ['boomer/boomer_right_0.png', 'boomer/boomer_right_1.png', 'boomer/boomer_right_2.png'], 
                            'up_idle': ['boomer/boomer_idle_up.png'], 'down_idle': ['boomer/boomer_idle_down.png'], 
                            'left_idle': ['boomer/boomer_idle_left.png'], 'right_idle': ['boomer/boomer_idle_right.png']}
        elif self.tipo_zumbi == 'normal':
            self.animations = {'up': ['normal/up_0.png', 'normal/up_1.png', 'normal/up_2.png'], 'down': ['normal/down_0.png', 'normal/down_1.png', 'normal/down_2.png'], 
                            'left': ['normal/left_0.png', 'normal/left_1.png', 'normal/left_2.png'], 'right': ['normal/right_0.png', 'normal/right_1.png', 'normal/right_2.png'], 
                            'up_idle': ['normal/idle_up.png'], 'down_idle': ['normal/idle_down.png'], 
                            'left_idle': ['normal/idle_left.png'], 'right_idle': ['normal/idle_right.png']}
        elif self.tipo_zumbi == 'zumbinho':
            self.animations = {'up': ['zumbinho/zumbinho_up_0.png', 'zumbinho/zumbinho_up_1.png', 'zumbinho/zumbinho_up_2.png'], 'down': ['zumbinho/zumbinho_down_0.png', 'zumbinho/zumbinho_down_1.png', 'zumbinho/zumbinho_down_2.png'], 
                            'left': ['zumbinho/zumbinho_left_0.png', 'zumbinho/zumbinho_left_1.png', 'zumbinho/zumbinho_left_2.png'], 'right': ['zumbinho/zumbinho_right_0.png', 'zumbinho/zumbinho_right_1.png', 'zumbinho/zumbinho_right_2.png'], 
                            'up_idle': ['zumbinho/zumbinho_idle_up.png'], 'down_idle': ['zumbinho/zumbinho_idle_down.png'], 
                            'left_idle': ['zumbinho/zumbinho_idle_left.png'], 'right_idle': ['zumbinho/zumbinho_idle_right.png']}
      
            
    def animar(self):
        #funcao utilizada para animacao
        #selecao de qual lista de animacoes vai usar de acordo com o status
        animation = self.animations[self.status]
        #rodando a lista para mostar todas os sprites
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        self.image = pygame.image.load(animation[int(self.frame_index)]).convert_alpha()
    
    
    def move(self,speed):
        #funcao para atualizar a posicao da hitbox junto ao movimento do zumbi
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
        

    def collision(self,direction):
        global mortes
        #colisoes
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                #essa funcao faz com que o zumbi pare ao se chocar com a parede
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # moving left
                        self.hitbox.left = sprite.hitbox.right

            for sprite in self.colisao_player:
                #essa funcao faz com que o zumbi cause dano ao jogador ao encostar nele
                if sprite.hitbox.colliderect(self.hitbox):
                    self.player.vida -= 20
                    self.player.image = pygame.image.load(f'prota/prota_dmg_{self.player.status}.png').convert_alpha()
                    #o zumbi eh jogado pra tras quando bate no player para possibilitar fuga e evitar muitas batidas sucessivas
                    if self.direction.x > 0: # moving right
                      self.hitbox.x -= self.speed * 15
                    if self.direction.x < 0: # moving left
                       self.hitbox.x += self.speed * 15
            
            for sprite in self.player.bala:
                #funcao para que o zumbi receba dano quando a bala se chocar contra ele
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.cooldown_dano >= 2:
                        self.hp -= self.player.dano
                        self.image = pygame.image.load(f'{self.tipo_zumbi}/{self.tipo_zumbi}_dmg_{self.status}.png').convert_alpha()
                        self.cooldown_dano = 0
                    #caso o hp do zumbi chegue a zero, ele morre
                    if self.hp <= 0:
                        self.kill()
                        self.mortes+=1
        #basicamente as mesmas coisas de cima, mas para a vertical
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # moving up
                        self.hitbox.top = sprite.hitbox.bottom
            
            for sprite in self.colisao_player:
                if sprite.hitbox.colliderect(self.hitbox):
                    self.player.vida -= 20
                    self.player.image = pygame.image.load(f'prota/prota_dmg_{self.player.status}.png').convert_alpha()
                    if self.direction.y > 0: # moving down
                        self.hitbox.y -= self.speed * 15
                    if self.direction.y < 0: # moving up
                        self.hitbox.y += self.speed * 15

            for sprite in self.player.bala:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.cooldown_dano >= 2:
                        self.hp -= self.player.dano
                        self.image = pygame.image.load(f'{self.tipo_zumbi}/{self.tipo_zumbi}_dmg_{self.status}.png').convert_alpha()
                        self.cooldown_dano = 0
                    if self.hp <= 0:
                        self.kill()
                        mortes+=1
                        
                        
    def count(self):
        #funcao que retorna o numero de mortes
        return self.mortes
    
    
    def update(self):
        #atualiza os dados do zumbi e os cooldowns
        if self.cooldown_dano < 2:
            self.cooldown_dano += 0.2
        self.zombie_move()
        self.move(self.speed)
        self.get_status()
        self.animar()
        

#variaveis
BAR_ALTURA = 20
HEALTH_BAR_LARGURA = 200
AMMO_BAR_LARGURA = 200
ITEM_BOX_SIDE = 80
UI_FONT = 'HUD/font/UpheavalPro.ttf'
UI_FONT_SIZE = 36


#cores gerais
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222' # bg = background
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# cores da interface
HEALTH_COLOR = 'red'
AMMO_COLOR = 'gold'
UI_BORDER_COLOR_ACTIVE = 'gold'

class UI():
    def __init__(self, player):
        self.player = player
        # general
        self.display_surface = pygame.display.get_surface()
        self.font =pygame.font.Font(UI_FONT,UI_FONT_SIZE)

        #bar setup
        self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_LARGURA,BAR_ALTURA)
        self.ammo_bar_rect = pygame.Rect(10,BAR_ALTURA+20,AMMO_BAR_LARGURA,BAR_ALTURA)
        
        
    def show_bar(self,current,max_amount, bg_rect, color):
        #draw bg
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        # convert stat to pixel
        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        #drawing the bar
        pygame.draw.rect(self.display_surface,color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, current_rect, 3)
        
    
    def show_morte_zumbi(self, qtd_mortes):
        text_surf = self.font.render(str(int(qtd_mortes)),False,TEXT_COLOR)
        x, y = 640, 20
        text_rect = text_surf.get_rect(midtop = (x,y))
        
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(15,5))
        self.display_surface.blit(text_surf,text_rect)
        

    def display(self,player):
        self.show_bar(self.player.vida, 100, self.health_bar_rect, HEALTH_COLOR)
        self.show_bar(self.player.pente, 30, self.ammo_bar_rect, AMMO_COLOR)
        self.show_morte_zumbi(mortes)