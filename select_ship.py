import pygame
from const import *
from scene_manager import SceneManager
from pygame.locals import *
class SelectShip():
    def __init__(self,screen:pygame.Surface):
        # 位置情報
        self.selectship_text = self.create_text(TEXT.SELECT_SHIP,80)
                
    def create_text(self,text:str,size:int,font:str = 'hg明朝b') ->pygame.Surface:
        textfont = pygame.font.SysFont(font,size)
        text = textfont.render(text,True,COLOR.WHITE)
        return text
        
    def show(self,screen:pygame.Surface):
        selectship_pos = self.place_position(self.selectship_text.get_rect(),(screen.get_rect().centerx,screen.get_rect().top + 100))
        screen.blit(self.selectship_text,selectship_pos)
        
    def place_position(self,text_rec:pygame.Rect,center_pos:tuple[float,float]) -> tuple[float,float]:
        place_pos = (center_pos[0]-text_rec.centerx,center_pos[1]-text_rec.centery)
        return place_pos