from typing_extensions import Self
import pygame 
from mapa import *
from tile import Tile
from Player import Player
from coletaveis import Coletaveis
import constru
import cerca

class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = CameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

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
					self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
				if col == 'm':
					Coletaveis((x,y),[self.visible_sprites,self.obstacle_sprites])
				if col == 'ce':
					constru.Celeiro((x,y),[self.visible_sprites,self.obstacle_sprites])
				if col == 't':
					constru.Trator((x,y),[self.visible_sprites,self.obstacle_sprites])
				if col == 'ca':
					constru.Casa((x,y),[self.visible_sprites,self.obstacle_sprites])


				



	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()


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