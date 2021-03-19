import pygame
from settings import *

class Button:
    def __init__(self, x, y, width, height, text=None, colour=(135,206,135), highLightedColour=(255,165,0), function= None, params= None ):
        self.image = pygame.Surface((width, height))
        self.pos = (x,y)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.text = text
        self.colour = colour
        self.highLightedColour = highLightedColour
        self.function = function
        self.params = params
        self.font = pygame.font.SysFont("arial", 16)
        self.highlighted = False

    def update(self, mouse):
        if self.rect.collidepoint(mouse):
            self.highlighted = True
        else:
            self.highlighted = False

    def draw(self, window):
        pos = []
        self.image.fill(self.highLightedColour if self .highlighted else self.colour)
        window.blit(self.image, self.pos)
        text = self.font.render(self.text, False, BLACK)
        fontWidth = text.get_width()
        fontHeight = text.get_height()
        pos =((self.pos[0]+((s1-fontWidth)//2)),(self.pos[1]+((s2-fontHeight)//2)))
        window.blit(text, pos)
