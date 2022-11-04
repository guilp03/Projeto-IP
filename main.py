import pygame, sys
from mapa import *
from level import Level
class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((1280,720))
		pygame.display.set_caption('Super Mario Borba')
		self.clock = pygame.time.Clock()

		self.level = Level()
	
	def exibe_mensagem (self, msg, tamanho, cor):
		fonte = pygame.font.SysFont('comicsansms', tamanho, cor)
		mensagem = f'{msg}'
		texto_formatado = fonte.render(mensagem, True, cor)
		return texto_formatado

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()    
			
			self.screen.fill('#3f301d')
			game_over = self.exibe_mensagem('GAME OVER',40,'#ff0000')
			self.screen.blit(game_over, (530,50))
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)
			

if __name__ == '__main__':
	game = Game()
	game.run()