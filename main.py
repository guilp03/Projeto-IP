import pygame
from support import import_folder
from random import randint

class Player(pygame.sprite.Sprite):
    """'Classe Player: Determina o sprite do jogador, sua velocidade, direção e atualiza sua posição'"""
    def __init__(self, pos, group):
        super().__init__(group)
        # Sprite do jogador
        self.image = pygame.image.load('Protagonista.png').convert_alpha()
        # Determina onde está o centro do sprite (posição inicial)
        self.rect = self.image.get_rect(center=pos)
        # Cria um vetor (x,y)
        self.direction = pygame.math.Vector2()
        # Velocidade inicial do jogador
        self.speed = 3

    # Função input: Muda a direção do jogador baseado no input
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    # Função update: Movimenta o personagem baseado na direção e velocidade
    def update(self):
        self.player_input()
        self.rect.center += self.direction * self.speed
        
class Zumbi(pygame.sprite.Sprite):
    #definindo os dados base de um zumbi
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('down_0.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 3.3
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.importar()
        #movimentacao ainda em experimentacao
    def zombie_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        else:
            self.direction.x = 0
    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status:
                self.status = self.status + '_idle'
              
    def importar(self):
        zombie_path = '../graphics/player/'
        self.animations = {'up': ['up_0.png', 'up_1.png', 'up_2.png', 'up_3.png'], 'down': ['down_0.png', 'down_1.png', 'down_2.png', 'down_3.png'], 
                           'left': ['left_0.png', 'left_1.png', 'left_2.png', 'left_3.png'], 'right': ['right_0.png', 'right_1.png', 'right_2.png', 'right_3.png'], 
                           'up_idle': ['idle_up.png'], 'down_idle': ['idle_down.png'], 
                           'left_idle': ['idle_left.png'], 'right_idle': ['idle_right.png']}
        #for animation in self.animations.keys():
            #full_path = zombie_path + animation
            #self.animations[animation] = import_folder(full_path)
            
    def animar(self):
        animation = self.animations[self.status]
        
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        self.image = animation[int(self.frame_index)]
    def update(self):
        self.zombie_input()
        self.rect.center += self.direction * self.speed 
        self.get_status()
        self.animar()
        


class Car(pygame.sprite.Sprite):
    """"'Classe Carro: Determina sprite e posição do carro'"""
    def __init__(self, pos, group):
        # Inserindo objeto no grupo camera
        super().__init__(group)
        # Determinando sprite
        self.image = pygame.image.load('car.png').convert_alpha()
        # Determinando posição inicial
        self.rect = self.image.get_rect(topleft=pos)


class CameraGroup(pygame.sprite.Group):
    """"'Classe Camera: Especifica o funcionamento da camera (Centraliza a camera no personagem, estabelece o zoom e determina que objeto está na frente)'"""
    def __init__(self):
        super().__init__()
        # Cria superficie da camera
        self.display_surface = pygame.display.get_surface()

        # Offset (vetor de ajuste para centralizar a camera)
        # Cria vetor (x,y)
        self.offset = pygame.math.Vector2()
        # Decobre a meia largura e meia altura da superficie da camera
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2
        # Determina o Sprite do chão
        self.ground_surf = pygame.image.load('car.png').convert_alpha()
        # Determina a posição do sprite do chão (0,0)
        self.ground_rect = self.ground_surf.get_rect(topleft=(0, 0))

        # Zoom
        # Determina a escala inicial como 1x1
        self.zoom_scale = 1
        # Criar uma superficie com os objetos separada da camera para poder ser redimensionada de acordo com o zoom
        self.internal_surface_size = (2000, 2000)
        self.internal_surface = pygame.Surface(self.internal_surface_size, pygame.SRCALPHA)
        self.internal_rect = self.internal_surface.get_rect(center=(self.half_w, self.half_h))
        # Cria um vetor (x,y) com as dimensões da superficie dos objetos
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surface_size)
        # Cria um vetor (x,y) que calcula o vetor offset (vetor que ajusta a camera)
        self.internal_offset = pygame.math.Vector2()
        self.internal_offset.x = self.internal_surface_size[0] // 2 - self.half_w
        self.internal_offset.y = self.internal_surface_size[1] // 2 - self.half_h

    # Função que centraliza a camera

    def center_camera(self, target):
        # Descobre o centro do alvo(personagem) e subtrai metade e altura e da largura da superficie da camera
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    # Função que printa os objetos manualmente
    def custom_draw(self, player):
        # Centraliza a camera no jogador
        self.center_camera(player)
        self.internal_surface.fill('#71ddee')

        # Reposiciona o chão levando em conta o zoom e o personagem
        ground_offset = self.ground_rect.topleft - self.offset + self.internal_offset
        self.internal_surface.blit(self.ground_surf, ground_offset)

        # Loop que printa cada sprite levando em conta o zoom e o personagem
        # A função sorted com esses parametros determina que objeto esta na frente
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
            self.internal_surface.blit(sprite.image, offset_pos)

        # Muda a escala da superficie das imagens
        scaled_surface = pygame.transform.scale(self.internal_surface, self.internal_surface_size_vector * self.zoom_scale)
        scaled_rect = scaled_surface.get_rect(center=(self.half_w, self.half_h))
        # printa a superficie das imagens
        self.display_surface.blit(scaled_surface, scaled_rect)


pygame.init()
pygame.display.set_caption('Zombie')
# Criar tela de 800x400
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

camera_group = CameraGroup()
# determina posição inicial do jogador e a que grupo pertence
player = Player((640, 360), camera_group)

#cria o zumbi
spawn_zumbi_x = randint(0,700)
spawn_zumbi_y = randint(0,600)
zumbi = Zumbi((spawn_zumbi_x, spawn_zumbi_y), camera_group)
# Criar 5 carror em posições aletorias (Feito para teste)
for i in range(5):
    random_x = randint(0, 500)
    random_y = randint(0, 500)
    Car((random_x, random_y), camera_group)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Muda o zoom baseado no scroll do mouse
        if event.type == pygame.MOUSEWHEEL:
            camera_group.zoom_scale += event.y * 0.03

    screen.fill('#71ddee')
    camera_group.update()
    camera_group.custom_draw(player)

    pygame.display.update()
    clock.tick(60)
