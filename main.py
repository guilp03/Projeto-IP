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
	
	def exibe_mensagem (self, texto, tamanho, cor, x, y):
		fonte = pygame.font.SysFont('arialblack', tamanho, cor)
		mensagem = f'{texto}'
		texto_formatado = fonte.render(mensagem, True, cor)
		texto_rect = texto_formatado.get_rect()
		texto_rect.midtop = (x, y)
		self.screen.blit(texto_formatado, texto_rect)
		return texto_formatado

	def mostrar_tela_start(self):
		self.screen.fill('#3f301d')
		self.exibe_mensagem('Pressione qualquer tecla', 40, '#ff0000', 640, 300)
		pygame.display.flip()
		self.espera()

	def espera(self):
		esperando = True
		while esperando:
			self.clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					esperando = False
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYUP:
					esperando = False
					

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()    
			
			if self.level.player.vida<=0:
				self.exibe_mensagem('GAME OVER',60,'#ff0000', 640, 300)
				pygame.display.flip()
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)
			

if __name__ == '__main__':
	game = Game()
	game.mostrar_tela_start()
	game.run()