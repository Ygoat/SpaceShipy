import pygame
from const import *

class Topmenu():
    def __init__(self,screen:pygame.Surface):
        # 位置情報
        # self.grobal_pos_x = screen.get_rect().centerx - self.sur.get_rect().centerx
        # self.grobal_pos_y = screen.get_rect().centery - self.sur.get_rect().centery
        self.grobal_pos_x_center = screen.get_rect().centerx
        self.grobal_pos_y_center = screen.get_rect().centery
        # スクリーン上初期位置にセット
        # self.rect.clamp_ip(screen.get_rect())
        # self.rect.move_ip(self.grobal_pos_x,self.grobal_pos_y)
        # pass
    
    def show(self,screen:pygame.Surface):
        font = pygame.font.SysFont("hg明朝b",80)
        text = font.render("---Space Shipy!!---",True,COLOR.WHITE)
        place_pos = self.place_position(text.get_rect(),screen.get_rect().center)
        screen.blit(text,place_pos)

    def place_position(self,text_rec:pygame.Rect,center_pos:tuple[float,float]) -> tuple[float,float]:
        place_pos = (center_pos[0]-text_rec.centerx,center_pos[1]-text_rec.centery)
        return place_pos