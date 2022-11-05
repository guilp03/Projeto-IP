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
UI_BG_COLOR = '#222222' # bg = background
UI_BORDER_COLLOR = '#111111'
TEXT_COLLOR = '#EEEEEE'

# cores da interface
HEALTH_COLOR = 'red'
AMMO_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

class UI():
    def __init__(self, player):
        self.player = player
        # general
        self.display_surface = pg.display.get_surface()
        self.font =pg.font.Font(UI_FONT,UI_FONT_SIZE)

        #bar setup
        self.health_bar_rect = pg.Rect(20,10,HEALTH_BAR_LARGURA,BAR_ALTURA)
        self.ammo_bar_rect = pg.Rect(10,10,AMMO_BAR_LARGURA,BAR_ALTURA)


    def show_bar(self,current,max_amount, bg_rect, color):
        #draw bg
        pg.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        # convert stat to pixel
        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        #drawing the bar
        pg.draw.rect(self.display_surface,color, current_rect)
        pg.draw.rect(self.display_surface, UI_BORDER_COLLOR, current_rect, 3)

    #def show_exp

    def display(self,player):
        self.show_bar(self.player.vida, 100, self.health_bar_rect, HEALTH_COLOR)
        #self.show_bar(self.player.pente, 100, self.ammo_bar_rect, AMMO_COLOR)
        #pg.draw.rect(self.display_surface, 'black', self.health_bar_rect)

        #self.show_exp()