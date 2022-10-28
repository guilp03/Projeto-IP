import pygame 
from mapa import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups,obstacle_sprites):
		super().__init__(groups)
		self.image = pygame.image.load('../Projeto-IP/prota/prota_idle_down.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-10)

		self.direction = pygame.math.Vector2()
		self.speed = 6

		self.status = 'down'
		self.frame_index = 0
		self.animation_speed = 0.2
		self.importar()

		self.obstacle_sprites = obstacle_sprites

	def input(self):
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
		

	def get_status(self):
		if self.direction.x == 0 and self.direction.y == 0:
			if not 'idle' in self.status:
				self.status = self.status + '_idle'

	def importar(self):
		self.animations = {'up': ['../Projeto-IP/prota/prota_up_0.png', '../Projeto-IP/prota/prota_up_1.png', '../Projeto-IP/prota/prota_up_2.png'],
							'down': ['../Projeto-IP/prota/prota_down_0.png', '../Projeto-IP/prota/prota_down_1.png', '../Projeto-IP/prota/prota_down_2.png'],
							'left': ['../Projeto-IP/prota/prota_left_0.png', '../Projeto-IP/prota/prota_left_1.png', '../Projeto-IP/prota/prota_left_2.png'],
							'right': ['../Projeto-IP/prota/prota_right_0.png', '../Projeto-IP/prota/prota_right_1.png', '../Projeto-IP/prota/prota_right_2.png'],
							'up_idle': ['../Projeto-IP/prota/prota_idle_up.png'], 'down_idle': ['../Projeto-IP/prota/prota_idle_down.png'],
							'left_idle': ['../Projeto-IP/prota/prota_idle_left.png'], 'right_idle': ['../Projeto-IP/prota/prota_idle_right.png']}
	
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
		self.input()
		self.move(self.speed)
		self.get_status()
		self.animar()