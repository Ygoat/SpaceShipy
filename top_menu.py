import pygame
from const import *
from pygame.locals import *
class Topmenu():
    def __init__(self,screen:pygame.Surface):
        # 位置情報
        self.title_text = self.create_text(TEXT.TITLE,80)
        self.startbutton_text = self.create_text(TEXT.START_BUTTON,40) 
        
    def create_text(self,text:str,size:int,font:str = 'hg明朝b') ->pygame.Surface:
        textfont = pygame.font.SysFont(font,size)
        text = textfont.render(text,True,COLOR.WHITE)
        return text
        
    def show(self,screen:pygame.Surface):
        title_pos = self.place_position(self.title_text.get_rect(),(screen.get_rect().centerx,screen.get_rect().top + 100))
        startbutton_pos = self.place_position(self.startbutton_text.get_rect(),(screen.get_rect().centerx,screen.get_rect().bottom - 100))
        screen.blit(self.title_text,title_pos)
        screen.blit(self.startbutton_text,startbutton_pos)

    def place_position(self,text_rec:pygame.Rect,center_pos:tuple[float,float]) -> tuple[float,float]:
        place_pos = (center_pos[0]-text_rec.centerx,center_pos[1]-text_rec.centery)
        return place_pos