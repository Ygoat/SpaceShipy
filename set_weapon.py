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
        self.item_sur = self.__create_item(screen,space_ship.shape,space_ship.weapon_pos[0])[0]
        self.item_rect = self.__create_item(screen,space_ship.shape,space_ship.weapon_pos[0])[1]
        self.weapon_rec = self.__create_item(screen,space_ship.shape,space_ship.weapon_pos[0])[2]
        # 初期位置にセット
        self.__set_rect(screen)

    def show_texts(self,screen:pygame.Surface):
        select_pos = self.__text_place_position(self.text_sur.get_rect(),(screen.get_rect().centerx,screen.get_rect().top + 100))
        screen.blit(self.text_sur,select_pos)

    def show_items(self,screen:pygame.Surface):       
        screen.blit(self.item_sur,(screen.get_rect().centerx - self.item_sur.get_rect().centerx, screen.get_rect().centery - self.item_sur.get_rect().centery))
        self.weapon_rec.clamp(screen.get_rect())

    def select_item(self,click_pos:tuple[float,float]):
        print(self.weapon_rec.topleft)
        print(self.weapon_rec.center)
        print(self.item_rect.topleft)
        
        # print(click_pos[0]-)
        # print(click_pos[0]-self.item_rect.topleft[0],click_pos[1]-self.item_rect.topleft[1])
        if self.weapon_rec.collidepoint((click_pos[0]-self.item_rect.topleft[0],click_pos[1]-self.item_rect.topleft[1])):
            print("clicked")
        # selected_idx = [i for i in  range(0,len(self.item_rect)) if self.item_rect.collidepoint(click_pos)==True]            
        # if selected_idx:
        #     return selected_idx[0]
        # else:
        #     return None

    def __create_text(self,text:str,size:int,font:str = 'hg明朝b') ->pygame.Surface:
        textfont = pygame.font.SysFont(font,size)
        text = textfont.render(text,True,COLOR.WHITE)
        return text

    def __create_item(self,screen:pygame.Surface,ship_shape:tuple[float,float],weapon_pos:tuple[float,float]) -> tuple[pygame.Surface,pygame.Rect,pygame.Rect]:
        size=(400,400)
        item_sur = pygame.Surface(size)
        item_sur.fill(COLOR.BLUE)
        pygame.draw.rect(item_sur,COLOR.BLACK,(10,10,380,380))
        ship_rec = pygame.draw.rect(item_sur,COLOR.GREEN,(size[0]/2-ship_shape[0]/2,size[1]/2-ship_shape[1]/2,ship_shape[0],ship_shape[1]))
        radius = 15
        weapon_rec = pygame.draw.circle(item_sur,COLOR.BLUE,(ship_rec.topleft[0],ship_rec.topleft[1]),radius)
        weapon_rec.center = (ship_rec.center[0] + weapon_pos[0],ship_rec.center[1] + weapon_pos[1])
        item_rec = item_sur.get_rect(center=screen.get_rect().center)
        return item_sur,item_rec,weapon_rec
    
    def __set_rect(self,screen:pygame.Surface):
        screen_rec = screen.get_rect()
        self.item_rect.center = screen_rec.center

    def __text_place_position(self,text_rec:pygame.Rect,center_pos:tuple[float,float]) -> tuple[float,float]:
        place_pos = (center_pos[0]-text_rec.centerx,center_pos[1]-text_rec.centery)
        return place_pos