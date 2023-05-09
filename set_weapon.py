import pygame
import csv
from const import *
from pygame.locals import *
from space_ship import SpaceShip
SPACE = 15

class SetWeapon():

    def __init__(self,screen:pygame.Surface,space_ship:SpaceShip):
        # 位置情報
        self.text_sur = self.__create_text(TEXT.SET_WEAPON,80)
        self.item_sur = self.__create_item(space_ship.shape,space_ship.weapon_pos[0])[0]
        self.item_rect = self.__create_item(space_ship.shape,space_ship.weapon_pos[0])[1]
        # 初期位置にセット
        self.__set_rect(screen)

    def show_texts(self,screen:pygame.Surface):
        select_pos = self.__text_place_position(self.text_sur.get_rect(),(screen.get_rect().centerx,screen.get_rect().top + 100))
        screen.blit(self.text_sur,select_pos)

    def show_items(self,screen:pygame.Surface):
        # for i in range(0,len(self.items_sur)):
        screen.blit(self.item_sur,(screen.get_rect().centerx - self.item_sur.get_rect().centerx, screen.get_rect().centery - self.item_sur.get_rect().centery))

    def select_item(self,click_pos:tuple[float,float]):
        # selected_idx = [i for i in  range(0,len(self.item_rect)) if self.item_rect.collidepoint(click_pos)==True]            
        # if selected_idx:
        #     return selected_idx[0]
        # else:
        #     return None
        pass

    def __create_text(self,text:str,size:int,font:str = 'hg明朝b') ->pygame.Surface:
        textfont = pygame.font.SysFont(font,size)
        text = textfont.render(text,True,COLOR.WHITE)
        return text

    def __create_item(self,ship_shape:tuple[float,float],weapon_pos:tuple[float,float]) -> tuple[pygame.Surface,pygame.Rect]:
        size=(400,400)
        item_sur = pygame.Surface(size)
        item_sur.fill(COLOR.BLUE)
        pygame.draw.rect(item_sur,COLOR.BLACK,(10,10,380,380))
        ship_rec = pygame.draw.rect(item_sur,COLOR.GREEN,(size[0]/2-ship_shape[0]/2,size[1]/2-ship_shape[1]/2,ship_shape[0],ship_shape[1]))
        radius = 15
        weapon_rec = pygame.draw.circle(item_sur,COLOR.BLUE,(ship_rec.topleft[0],ship_rec.topleft[1]),radius)
        print(ship_rec.topleft)
        weapon_rec.center = (item_sur.get_rect().topleft[0] + weapon_pos[0],item_sur.get_rect().topleft[1] + weapon_pos[1])
        item_rec = item_sur.get_rect()
        return item_sur,item_rec       
        # items_rect = [None] * len(items)
        # for i in range(0,len(items)):
        #     item_sur = pygame.Surface((100,100))
        #     item_sur.fill(COLOR.BLUE)
        #     radius = 20
        #     pygame.draw.rect(item_sur,COLOR.BLACK,(3,3,94,94))
        #     pygame.draw.circle(item_sur,COLOR.GREEN,item_sur.get_rect().center,radius)
        #     items_sur[i] = item_sur
        #     items_rect[i] = item_sur.get_rect()
        # return items_sur,items_rect
        pass
    
    def __set_rect(self,screen:pygame.Surface):
        # screen_rec = screen.get_rect()
        # init_pos = [screen_rec.left + SPACE,screen_rec.centery + 30]
        # for item_rect in self.items_rect:
        #     item_rect.clamp_ip(screen.get_rect())
        #     item_rect.move_ip(init_pos)
        #     init_pos[0] = item_rect.right + SPACE
        pass


    def __text_place_position(self,text_rec:pygame.Rect,center_pos:tuple[float,float]) -> tuple[float,float]:
        place_pos = (center_pos[0]-text_rec.centerx,center_pos[1]-text_rec.centery)
        return place_pos