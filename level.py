from typing_extensions import Self
import pygame 
from mapa import *
from tile import Tile
from Player import Player
import zumbi
from coletaveis import Coletaveis
from random import randint
from ui import UI

class Level:
	def __init__(self):
		self.cooldown = 0
		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = CameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()
		self.coletaveis = pygame.sprite.Group()
	

		# sprite setup
		self.create_map()
		self.ui = UI(self.player)

	def create_map(self):
		for row_index,row in enumerate(WORLD_MAP):
			for col_index, col in enumerate(row):
				x = col_index * TILESIZE
				y = row_index * TILESIZE
				if col == 'x':
					Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
				if col == 'p':
					self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites, self.coletaveis)
				if col == 'z':
					self.zumbi = zumbi.Zumbi('boomer',(x,y),[self.visible_sprites],self.player,self.obstacle_sprites)
				if col == 'c':
					Coletaveis((x,y),self.visible_sprites, self.coletaveis, self.obstacle_sprites )

	def spawn_coletaveis(visible_sprites, obstacle_sprites, coletaveis, cooldown):
		lista_aux = ['medkit', 'nada', 'nada', 'nada']
		if cooldown == 1800:
			for row_index,row in enumerate(WORLD_MAP):
				for col_index, col in enumerate(row):
					x = col_index * TILESIZE
					y = row_index * TILESIZE
					if col == 'j':
						index = randint(0, len(lista_aux) - 1)
						criado = lista_aux[index]
						if criado == 'medkit':
							Coletaveis((x,y),visible_sprites, coletaveis, obstacle_sprites )
							lista_aux.remove('medkit')
						else:
							lista_aux.remove('nada')

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

    def custom_draw(self,player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)