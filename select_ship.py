import pygame
import csv
from const import *
from scene_manager import SceneManager
from pygame.locals import *
class SelectShip():
    with open(file=f'./master_data/ships.csv',mode='r',encoding='utf-8') as params_file:
        params = [row for row in csv.DictReader(params_file)]
        
    def __init__(self,screen:pygame.Surface):
        # 位置情報
        self.text = self.__create_text(TEXT.SELECT_SHIP,80)
        self.items = self.__create_item(self.params)
        
    def show_texts(self,screen:pygame.Surface):
        selectship_pos = self.__text_place_position(self.text.get_rect(),(screen.get_rect().centerx,screen.get_rect().top + 100))
        screen.blit(self.text,selectship_pos)
                
    def show_items(self,screen:pygame.Surface):
        screen_rect = screen.get_rect()
        init_pos = (screen_rect.left + 30,screen_rect.centery + 30)
        for item in self.items:
            screen.blit(item,init_pos)
        
        
    def select_item(self,click:pygame.event):
        pass
                
    def __create_text(self,text:str,size:int,font:str = 'hg明朝b') ->pygame.Surface:
        textfont = pygame.font.SysFont(font,size)
        text = textfont.render(text,True,COLOR.WHITE)
        return text
        
    def __create_item(self,items:list[dict]) -> list[pygame.Surface]:
        items_sur = [None] * len(items)
        for i in range(0,len(items)):
            sx,sy = float(items[i]['sx']),float(items[i]['sy'])
            item_sur = pygame.Surface((50,50))
            item_rec = pygame.draw.rect(item_sur,COLOR.GREEN,(0,0,sx/10,sy/10))
            pos_on_itemsur = (item_sur.get_rect().centerx-item_rec.centerx,item_sur.get_rect().centery-item_rec.centery)
            item_rec.clamp_ip(item_sur.get_rect())
            item_rec.topleft = pos_on_itemsur
            items_sur[i] = item_sur
        return items_sur

    def __text_place_position(self,text_rec:pygame.Rect,center_pos:tuple[float,float]) -> tuple[float,float]:
        place_pos = (center_pos[0]-text_rec.centerx,center_pos[1]-text_rec.centery)
        return place_pos