
import pygame 
from mapa import *
from tile import Tile
from Player import Player
import zumbi
from coletaveis import Coletaveis
from coletaveis import Ammo
from coletaveis import Pocao
from coletaveis import Pistol
from random import randint
from ui import UI
import constru
import cerca

class Level:
	def __init__(self):
		self.cooldown = 0
		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = CameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()
		self.coletaveis = pygame.sprite.Group()
		self.colisao_zumbi = pygame.sprite.Group()
		self.colisao_player = pygame.sprite.Group()
		self.bala = pygame.sprite.Group()

		# sprite setup
		self.create_map()
		self.ui = UI(self.player)

	def create_map(self):
		for row_index,row in enumerate(WORLD_MAP):
			for col_index, col in enumerate(row):
				x = col_index * TILESIZE
				y = row_index * TILESIZE
				if col == 'x':
					cerca.Cerca((x,y),[self.visible_sprites,self.obstacle_sprites])
				if col == 'x1':
					cerca.Cerca1((x,y),[self.visible_sprites,self.obstacle_sprites])
				if col == 'x2':
					cerca.Cerca2((x,y),[self.visible_sprites,self.obstacle_sprites])
				if col == 'p':
					self.player = Player((x,y),self.visible_sprites, self.colisao_player,self.obstacle_sprites, self.coletaveis, self.colisao_zumbi, self.bala)
				if col == 'z':
					self.zumbi = zumbi.Zumbi('boomer',(x,y),[self.visible_sprites, self.colisao_zumbi],self.player,self.obstacle_sprites, self.colisao_player)
				if col == 'me':
					Coletaveis((x,y),'medkit',self.visible_sprites, self.coletaveis, self.obstacle_sprites )
				if col == 'mu':
					Ammo((x,y),'ammo',self.visible_sprites, self.coletaveis, self.obstacle_sprites )
				if col == 'ce':
					constru.Celeiro((x,y),[self.visible_sprites,self.obstacle_sprites])
				if col == 't':
					constru.Trator((x,y),[self.visible_sprites,self.obstacle_sprites])
				if col == 'ca':
					constru.Casa((x,y),[self.visible_sprites,self.obstacle_sprites])
				if col == 'pi':
					Pistol((x,y),'pistol',self.visible_sprites, self.coletaveis, self.obstacle_sprites)
				
	def spawn_coletaveis(visible_sprites, obstacle_sprites, coletaveis, cooldown_medkit, cooldown_ammo, cooldown_pot):
		lista_aux = ['medkit', 'nada', 'nada']
		lista_aux_2 = ['ammo', 'nada', 'nada']
		if cooldown_medkit == 1800:
			for row_index,row in enumerate(WORLD_MAP):
				for col_index, col in enumerate(row):
					x = col_index * TILESIZE
					y = row_index * TILESIZE
					if col == 'm':
						index = randint(0, len(lista_aux) - 1)
						criado = lista_aux[index]
						if criado == 'medkit':
							Coletaveis((x,y), 'medkit', visible_sprites, coletaveis, obstacle_sprites )
							lista_aux.remove('medkit')
						else:
							lista_aux.remove('nada')
		if cooldown_ammo == 1200:
			for row_index,row in enumerate(WORLD_MAP):
				for col_index, col in enumerate(row):
					x = col_index * TILESIZE
					y = row_index * TILESIZE
					if col == 'mun':
						index = randint(0, len(lista_aux_2) - 1)
						criado = lista_aux_2[index]
						if criado == 'ammo':
							Ammo((x,y), 'ammo', visible_sprites, coletaveis, obstacle_sprites )
							lista_aux_2.remove('ammo')
						else:
							lista_aux_2.remove('nada')
		if cooldown_pot == 3600:
			for row_index,row in enumerate(WORLD_MAP):
				for col_index, col in enumerate(row):
					x = col_index * TILESIZE
					y = row_index * TILESIZE
					if col == 'pot':
						Pocao((x,y), 'pocao', visible_sprites, coletaveis, obstacle_sprites )

	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()
		self.ui.display(self.player)


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
		#parte do chao esta funcionando agr so falta a imagem certa
		#criando o chao
        self.floor_surf = pygame.image.load('map_IP_cop.png')
        self.floor_rect = self.floor_surf.get_rect(topleft=(-850,-550))
		


    def custom_draw(self,player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
		#desenhando o chao
        self.floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, self.floor_offset_pos)
		
		

		

	

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
