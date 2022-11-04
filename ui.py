import Player as player
import pygame as pg

#variaveis
BAR_ALTURA = 20
HEALTH_BAR_LARGURA = 200
AMMO_BAR_LARGURA = 200
ITEM_BOX_SIDE = 80
UI_FONT = '../PROJETO-IP/HUD/font/Upheaval.fon'
UI_FONT_SIZE = 18

#cores gerais
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLLOR = '#111111'
TEXT_COLLOR = '#EEEEEE'

# cores da interface
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

class UI:
    def __init__(self):
        
        # general
        self.display_surface = pg.display.get_surface()
        self.font =pg.font.Font(UI_FONT,UI_FONT_SIZE)

        #bar setup
        self.health_bar_rect = pg.Rect(10,10,HEALTH_BAR_LARGURA,BAR_ALTURA)
        self.ammo_bar_rect = pg.Rect(10,10,AMMO_BAR_LARGURA,BAR_ALTURA)

    def display(self,player):
        pg.draw.rect(self.display_surface, 'black', self.health_bar_rect)