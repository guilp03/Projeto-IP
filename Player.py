import pygame
from balistica import DisparoArma
from mapa import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,visible_sprites, colisao_player,obstacle_sprites, coletaveis, zumbi, bala):
		super().__init__(visible_sprites, colisao_player)
		#infos base do player
		self.vida = 100
		self.dano = 40
		self.pente = 30
		self.image = pygame.image.load('prota/prota_idle_down.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0, -10)
		self.cooldown_tiro = 30
		self.visible_sprites, self.colisao_player = visible_sprites, colisao_player
		self.direction = pygame.math.Vector2()
		self.speed = 6
		#status que definem se o player esta armado e pra onde se movimenta
		self.arma = 'nada'
		self.status = 'down'
		#infos que compoem a animacao
		self.frame_index = 0
		self.animation_speed = 0.2
		#grupos de colisao
		self.coletaveis = coletaveis
		self.obstacle_sprites = obstacle_sprites
		self.zumbi = zumbi
		self.bala = bala
		#tempos de spawn dos coletaveis
		self.cooldown_spawn_medkit = 0
		self.cooldown_spawn_ammo = 0
		self.cooldown_pot = 0

	def input(self):
		#discriminamos as teclas nessa funcao
		#o status do player precisa ser atualizado para a animacao
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w] and keys[pygame.K_s]:
			self.direction.y = 0

		elif keys[pygame.K_w]:
			self.direction.y = -1
			self.status = 'up'
		elif keys[pygame.K_s]:
			self.direction.y = 1
			self.status = 'down'
		else:
			self.direction.y = 0
		if keys[pygame.K_a] and keys[pygame.K_d]:
			self.direction.x = 0
		elif keys[pygame.K_a]:
			self.direction.x = -1
			self.status = 'left'
		elif keys[pygame.K_d]:
			self.direction.x = 1
			self.status = 'right'
		else:
			self.direction.x = 0
		#para atirar o jogador precisa tem municao no pente e deve respeitar a cadencia da arma, que colocamos como 1 tiro a cada 0,5seg
		if keys[pygame.K_p] and self.cooldown_tiro == 30 and self.arma == 'pistol' and self.pente>0:
			self.cooldown_tiro = 0
			self.pente-=1
			DisparoArma((self.rect.x,self.rect.y), [self.visible_sprites, self.bala], self.obstacle_sprites, self.status, self.zumbi)
		

	def get_status(self):
     #diferenciar o player parado de quando esta andando
		if self.direction.x == 0 and self.direction.y == 0:
			if not 'idle' in self.status:
				self.status = self.status + '_idle'

	def importar(self):
     #diferenciar sprites do player desarmado e armado
		if self.arma == 'nada':
			self.animations = {'up': ['prota/prota_up_0.png', 'prota/prota_up_1.png', 'prota/prota_up_2.png'],
								'down': ['prota/prota_down_0.png', 'prota/prota_down_1.png', 'prota/prota_down_2.png'],
								'left': ['prota/prota_left_0.png', 'prota/prota_left_1.png', 'prota/prota_left_2.png'],
								'right': ['prota/prota_right_0.png', 'prota/prota_right_1.png', 'prota/prota_right_2.png'],
								'up_idle': ['prota/prota_idle_up.png'], 'down_idle': ['prota/prota_idle_down.png'],
								'left_idle': ['prota/prota_idle_left.png'], 'right_idle': ['prota/prota_idle_right.png']}
		elif self.arma == 'pistol':
			self.animations = {'up': ['prota_pistol/prota_pistol_up_1.png', 'prota_pistol/prota_pistol_up_2.png', 'prota_pistol/prota_pistol_up_3.png'],
								'down': ['prota_pistol/prota_pistol_down_1.png', 'prota_pistol/prota_pistol_down_2.png', 'prota_pistol/prota_pistol_down_3.png'],
								'left': ['prota_pistol/prota_pistol_left_1.png', 'prota_pistol/prota_pistol_left_2.png', 'prota_pistol/prota_pistol_left_3.png'],
								'right': ['prota_pistol/prota_pistol_right_1.png', 'prota_pistol/prota_pistol_right_2.png', 'prota_pistol/prota_pistol_right_3.png'],
								'up_idle': ['prota_pistol/prota_pistol_up_1.png'], 'down_idle': ['prota_pistol/prota_pistol_down_1.png'],
								'left_idle': ['prota_pistol/prota_pistol_left_1.png'], 'right_idle': ['prota_pistol/prota_pistol_right_1.png']} 
	
	def animar(self):
     #a funcao seleciona a lista de sprites a ser usada de acordo com o status do player
		animation = self.animations[self.status]
	#roda as listas para animar o jogador
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0

		self.image = pygame.image.load(animation[int(self.frame_index)]).convert_alpha()

	def move(self,speed):
     #atualiza a posicao da hitbox
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
				if sprite in self.coletaveis and sprite.hitbox.colliderect(self.hitbox):
        #caso o jogador colida com os coletaveis, eles serao apagados e acontecera o efeito conforme o coletavel
					if sprite.nome == 'medkit':
						sprite.kill()
						self.cooldown_spawn_medkit = 0
						#medkit recupera vida
						if self.vida <= 75:
							self.vida += 25
						elif self.vida >= 75 and self.vida <= 100:
							self.vida += (100 - self.vida)
					#municao recarrega o pente
					if sprite.nome == 'ammo':
						sprite.kill()
						self.pente = 30
					#A pocao da dano bonus
					if sprite.nome == 'pocao':
						sprite.kill()
						self.dano == self.dano + 10
					#a pistola arma o jogador
					if sprite.nome == 'pistol':
						sprite.kill()
						self.arma = 'pistol'
				
				elif sprite.hitbox.colliderect(self.hitbox) and sprite not in self.coletaveis :
				#o jogador para ao encostar em paredes
					if self.direction.x > 0: # moving right
						self.hitbox.right = sprite.hitbox.left
					if self.direction.x < 0: # moving left
						self.hitbox.left = sprite.hitbox.right
			
			for sprite in self.zumbi:
				if sprite.hitbox.colliderect(self.hitbox):
				#o jogador tambem pode ser bloqueado por zumbis
					if self.direction.x > 0: # moving right
							self.hitbox.right = sprite.hitbox.left
					if self.direction.x < 0: # moving left
						self.hitbox.left = sprite.hitbox.right
		#os mesmos comandos para a vertical
		if direction == 'vertical':
			for sprite in self.obstacle_sprites:
				if sprite in self.coletaveis and sprite.hitbox.colliderect(self.hitbox):
					if sprite.nome == 'medkit':
						sprite.kill()
						self.cooldown_spawn_medkit = 0
						if self.vida <= 75:
							self.vida += 25
						elif self.vida >= 75 and self.vida <= 100:
							self.vida += (100 - self.vida)

					if sprite.nome == 'ammo':
						sprite.kill()
						self.pente = 30

					if sprite.nome == 'pocao':
						sprite.kill()
						self.dano == self.dano + 10
					if sprite.nome == 'pistol':
						sprite.kill()
						self.arma = 'pistol'
						
				elif sprite.hitbox.colliderect(self.hitbox) and sprite not in self.coletaveis:
					if self.direction.y > 0: # moving down
						self.hitbox.bottom = sprite.hitbox.top
					if self.direction.y < 0: # moving up
						self.hitbox.top = sprite.hitbox.bottom
			
			for sprite in self.zumbi:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.y > 0: # moving down
						self.hitbox.bottom = sprite.hitbox.top
					if self.direction.y < 0: # moving up
						self.hitbox.top = sprite.hitbox.bottom


	def update(self):
     #atualiza os dados
		from level import Level
		self.input()
		self.importar()
		self.move(self.speed)
		self.get_status()
		self.animar()
		if self.cooldown_tiro < 30:
			self.cooldown_tiro += 1
		if self.cooldown_spawn_medkit < 1800:
			self.cooldown_spawn_medkit += 1
		if self.cooldown_spawn_ammo < 1200:
			self.cooldown_spawn_ammo += 1
		if self.cooldown_pot < 3600:
			self.cooldown_pot += 1
		#aqui chamamos as funcoes que estao em level para fazer os coletaveis reaparecerem
		if self.cooldown_spawn_medkit == 1800:
			Level.spawn_coletaveis(self.visible_sprites, self.obstacle_sprites, self.coletaveis, self.cooldown_spawn_medkit,self.cooldown_spawn_ammo,self.cooldown_pot)
			self.cooldown_spawn_medkit = 0
		elif self.cooldown_spawn_ammo == 1200:
			Level.spawn_coletaveis(self.visible_sprites, self.obstacle_sprites, self.coletaveis, self.cooldown_spawn_medkit,self.cooldown_spawn_ammo,self.cooldown_pot)
			self.cooldown_spawn_ammo = 0
		elif self.cooldown_pot == 3600:
			Level.spawn_coletaveis(self.visible_sprites, self.obstacle_sprites, self.coletaveis, self.cooldown_spawn_medkit,self.cooldown_spawn_ammo,self.cooldown_pot)
			self.cooldown_pot = 0
		