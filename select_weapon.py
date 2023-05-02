import pygame
import csv
from const import *
from pygame.locals import *
SPACE = 15

class SelectWeapon():

        
    def __init__(self,screen:pygame.Surface,params:dict):
        # 位置情報
        self.text_sur = self.__create_text(TEXT.SELECT_WEAPON,80)
        self.items_sur = self.__create_item(params)[0]
        self.items_rect = self.__create_item(params)[1]
        # 初期位置にセット
        self.__set_rect(screen)

    def show_texts(self,screen:pygame.Surface):
        select_pos = self.__text_place_position(self.text_sur.get_rect(),(screen.get_rect().centerx,screen.get_rect().top + 100))
        screen.blit(self.text_sur,select_pos)
                
    def show_items(self,screen:pygame.Surface):
        for i in range(0,len(self.items_sur)):
            screen.blit(self.items_sur[i],self.items_rect[i].topleft)
                
    def select_item(self,click_pos:tuple[float,float]):
        # print(click_pos)
        selected_idx = [i for i in  range(0,len(self.items_rect)) if self.items_rect[i].collidepoint(click_pos)==True]            
        if selected_idx:
            return selected_idx[0]
        else:
            return None
            
    def __create_text(self,text:str,size:int,font:str = 'hg明朝b') ->pygame.Surface:
        textfont = pygame.font.SysFont(font,size)
        text = textfont.render(text,True,COLOR.WHITE)
        return text
        
    def __create_item(self,items:list[dict]) -> tuple[list[pygame.Surface],list[pygame.Rect]]:
        items_sur = [None] * len(items)
        items_rect = [None] * len(items)
        for i in range(0,len(items)):
            # sx,sy = float(items[i]['sx']),float(items[i]['sy'])
            item_sur = pygame.Surface((100,100))
            item_sur.fill(COLOR.BLUE)
            radius = 20
            pygame.draw.rect(item_sur,COLOR.BLACK,(3,3,94,94))
            pygame.draw.circle(item_sur,COLOR.GREEN,item_sur.get_rect().center,radius)
            items_sur[i] = item_sur
            items_rect[i] = item_sur.get_rect()
        return items_sur,items_rect
    
    def __set_rect(self,screen:pygame.Surface):
        screen_rec = screen.get_rect()
        init_pos = [screen_rec.left + SPACE,screen_rec.centery + 30]
        for item_rect in self.items_rect:
            item_rect.clamp_ip(screen.get_rect())
            item_rect.move_ip(init_pos)
            init_pos[0] = item_rect.right + SPACE


    def __text_place_position(self,text_rec:pygame.Rect,center_pos:tuple[float,float]) -> tuple[float,float]:
        place_pos = (center_pos[0]-text_rec.centerx,center_pos[1]-text_rec.centery)
        return place_pos