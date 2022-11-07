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
from zumbi import UI
import constru
import cerca

class Level:
	def __init__(self):
		self.hordas = 1
		self.cooldown = 0
		self.time = 0
		self.first_spawn = True
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
		self.ui = zumbi.UI(self.player)


	def create_map(self):
     #criando o mapa
		for row_index,row in enumerate(WORLD_MAP):
      #traduz as linhas do mapa em numeros
			for col_index, col in enumerate(row):
       #traduz as colunas do mapa em numeros
				x = col_index * TILESIZE
				y = row_index * TILESIZE
		#verifica cada coluna e linha para colocar cada objeto em seu devido lugar
				if col == 'x':
					cerca.Cerca((x,y),[self.visible_sprites,self.obstacle_sprites])
				if col == 'x1':
					cerca.Cerca1((x,y),[self.visible_sprites,self.obstacle_sprites])
				if col == 'x2':
					cerca.Cerca2((x,y),[self.visible_sprites,self.obstacle_sprites])
				if col == 'p':
					self.player = Player((x,y),self.visible_sprites, self.colisao_player,self.obstacle_sprites, self.coletaveis, self.colisao_zumbi, self.bala)
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
     #funcao para spawn de coletaveis em locais aleatorios do mapa periodicamente
     #utiliza-se essas listas para auxiliar na aleatoriedade da ocorrencia dos spawns
     #os cooldowns de cada coletavel dizem respeito a quanto tempo eles demoram para aparecer no jogo
		lista_aux = ['medkit', 'nada', 'nada']
		lista_aux_2 = ['ammo', 'nada', 'nada']
		if cooldown_medkit == 1800:
			for row_index,row in enumerate(WORLD_MAP):
				for col_index, col in enumerate(row):
					x = col_index * TILESIZE
					y = row_index * TILESIZE
					#usa-se os 3 spawns disponiveis do mapa para criar nada ou o item, utiliza-se a a funcao randint para isso
					if col == 'm':
						index = randint(0, len(lista_aux) - 1)
						criado = lista_aux[index]
						if criado == 'medkit':
							Coletaveis((x,y), 'medkit', visible_sprites, coletaveis, obstacle_sprites )
							lista_aux.remove('medkit')
						else:
							lista_aux.remove('nada')
       #fazemos a mesma coisa para as municoes
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
       #a pocao aparece sempre no mesmo local
		if cooldown_pot == 3600:
			for row_index,row in enumerate(WORLD_MAP):
				for col_index, col in enumerate(row):
					x = col_index * TILESIZE
					y = row_index * TILESIZE
					if col == 'pot':
						Pocao((x,y), 'pocao', visible_sprites, coletaveis, obstacle_sprites )
      
      
	def spawn_zombies(self):
     #funcao para spawnar os zumbis
		lista_aux= []
	#lista com os tipos de zumbis
		lista_zumbi = ['normal', 'zumbinho', 'boomer']
	#os primeros zumbis nascem com 10 segundos de jogo iniciado
		if self.time >= 600 and self.first_spawn == True:
			for row_index,row in enumerate(WORLD_MAP):
					for col_index, col in enumerate(row):
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if col == 'z':
							lista_aux.append((x,y))
	#a variavel hordas define quantos zumbis serao adicionados,uma lista de spawns e feita a partir do mapa e sao sorteados alguns para os zumbis nascerem
			for i in range(0, self.hordas * 3):
				numero = randint(0, len(lista_aux) -1 )
				pos = lista_aux[numero]
				aux = randint(0, 2)
				tipo_zumbi = lista_zumbi[aux]
				self.zumbi = zumbi.Zumbi(f'{tipo_zumbi}',pos,[self.visible_sprites, self.colisao_zumbi],self.player,self.obstacle_sprites, self.colisao_player)
			self.time = 0
			self.hordas += 1
			self.first_spawn = False
   #os nascimentos subsequentes sao feitos a cada 30 segundos, sempre adicionando mais 5 segundos de intervalo para o jogador ter mais tempo de matar os zumbis
		elif self.time >= 1800:
			for row_index,row in enumerate(WORLD_MAP):
					for col_index, col in enumerate(row):
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if col == 'z':
							lista_aux.append((x,y))

			for i in range(0, self.hordas * 3):
				numero = randint(0, len(lista_aux) -1 )
				pos = lista_aux[numero]
				aux = randint(0, 2)
				tipo_zumbi = lista_zumbi[aux]
				self.zumbi = zumbi.Zumbi(f'{tipo_zumbi}',pos,[self.visible_sprites, self.colisao_zumbi],self.player,self.obstacle_sprites, self.colisao_player)
	#time diz respeito ao tempo passado desde o ultimo nascimento, hordas ao numero de nascimentos ja feitos(isso define quantos zumbis vao spawnar) e cooldown serve para aumentar o intervaloe entre nascimentos			
			self.time = 0
			self.hordas += 1
					

	def run(self):
		# update and draw the game
		self.time += 1
		self.spawn_zombies()
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

		self.zoom_scale = 1
		self.internal_surface_size = (1280, 1280)
		self.internal_surf = pygame.Surface(self.internal_surface_size, pygame.SRCALPHA)
		self.internal_rect = self.internal_surf.get_rect(center = (self.half_width, self.half_height))
		self.internal_surf_size_vector = pygame.math.Vector2(self.internal_surface_size)
		self.internal_offset = pygame.math.Vector2()
		self.internal_offset.x = self.internal_surface_size[1] // 2 - self.half_width
		self.internal_offset.y = self.internal_surface_size[1] // 2 - self.half_height

	
	def zoom_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_q] and self.zoom_scale < 1.8:
			self.zoom_scale += 0.1
		if keys[pygame.K_e] and self.zoom_scale > 1:
			self.zoom_scale -= 0.1


	def custom_draw(self, player):
		self.zoom_input()
		self.internal_surf.fill('black')
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height
		#desenhando o chao
		self.floor_offset_pos = self.floor_rect.topleft - self.offset
		self.internal_surf.blit(self.floor_surf, self.floor_offset_pos)
		
        # for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
			self.internal_surf.blit(sprite.image,offset_pos)
		
		scaled_surf = pygame.transform.scale(self.internal_surf, self.internal_surf_size_vector * self.zoom_scale)
		scaled_rect = scaled_surf.get_rect(center = (self.half_width, self.half_height))
		self.display_surface.blit(scaled_surf, scaled_rect)
