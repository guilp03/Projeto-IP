import pygame, sys
from mapa import *
from level import Level

class Game:
	def __init__(self):
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((1280,720))
		icone = pygame.image.load('boomer/boomer_right_0.png')
		pygame.display.set_icon(icone)
		pygame.display.set_caption('Regular Zombie Game')
		self.clock = pygame.time.Clock()

		self.level = Level()


	def exibe_mensagem (self, texto, tamanho, cor, x, y):
		fonte = pygame.font.Font('HUD/font/UpheavalPro.ttf', tamanho)
		mensagem = f'{texto}'
		texto_formatado = fonte.render(mensagem, True, cor)
		#retângulo para a "caixa de texto"
		texto_rect = texto_formatado.get_rect()
		#posição da mensagem (referenciais x e y no meio da caixa de texto)
		texto_rect.midtop = (x, y)
		#printando a mensagem na tela
		self.screen.blit(texto_formatado, texto_rect)
		return texto_formatado


	def mostrar_tela_start(self):
		#preenche a tela na cor preta
		self.screen.fill('#000000')
		#printa as mensagens
		self.exibe_mensagem('Press any key to start', 40, '#ff0000', 640, 400)
		self.exibe_mensagem('Regular Zombie Game', 72, '#ff0000',640,200)
		#mantém sempre printando
		pygame.display.flip()
		#chama a função "sala de espera"
		self.espera()


	def espera(self):
		esperando = True
		while esperando:
			#define o 60 ticks por segundo
			self.clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					#se clicar em fechar, termina a função 'espera' e fecha o jogo
					esperando = False
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYUP:
					#se apertar qualquer tecla, termina a função espera e abre o jogo, pois também finaliza a função 'mostrar_tela_start'
					esperando = False


	#função que roda o jogo
	def run(self):
		while True:
			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					#se clicar em fechar, fecha o jogo
					pygame.quit()
					sys.exit()    

			if self.level.player.vida<=0:
				#se o player ficar com vida 0 ou menos, chama a função de exibir a mensagem, e exibe 'game over'
				self.exibe_mensagem('GAME OVER',60,'#ff0000', 640, 300)
				#mantém exibindo 'game over'
				pygame.display.flip()
				
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						#se clicar em fechar, fecha o jogo
						pygame.quit()
						sys.exit()
			
			else:
				#roda a função que executa o jogo
				self.level.run()
				#atualiza a tela
				pygame.display.update()
				#frequência de atualização em 60 ticks por segundo
				self.clock.tick(FPS)


if __name__ == '__main__':
	#coloca a classe Game como uma variável
	game = Game()
	#abre o menu inicial
	game.mostrar_tela_start()
	#abre o jogo em si
	game.run()