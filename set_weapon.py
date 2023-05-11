import pygame
import csv
from const import *
from pygame.locals import *
from space_ship import SpaceShip
SPACE = 15
MAX_NUM_OF_WEAPON:int = 5
class SetWeapon():

    def __init__(self,screen:pygame.Surface,space_ship:SpaceShip):
        # 位置情報
        self.text_sur = self.__create_text(TEXT.SET_WEAPON,80)
        self.item_sur = self.__create_item(space_ship.shape,space_ship.weapon_pos)[0]
        self.item_rect = self.__create_item(space_ship.shape,space_ship.weapon_pos)[1]
        self.weapon_rec = self.__create_item(space_ship.shape,space_ship.weapon_pos)[2]
        # 初期位置にセット
        self.__set_rect(screen)

    def show_texts(self,screen:pygame.Surface):
        select_pos = self.__text_place_position(self.text_sur.get_rect(),(screen.get_rect().centerx,screen.get_rect().top + 100))
        screen.blit(self.text_sur,select_pos)

    def show_items(self,screen:pygame.Surface):       
        screen.blit(self.item_sur,(screen.get_rect().centerx - self.item_sur.get_rect().centerx, screen.get_rect().centery - self.item_sur.get_rect().centery))
        # screen.blit(self.item_sur,(0,0))

    def select_item(self,click_pos:tuple[float,float]):
        print(self.weapon_rec[0].topleft)
        print(click_pos)
        print(self.item_rect.topleft)
        if self.weapon_rec[0].collidepoint((click_pos[0]-self.item_rect.topleft[0],click_pos[1]-self.item_rect.topleft[1])):
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

    def __create_item(self,ship_shape:tuple[float,float],weapon_pos:list[tuple[float,float]]) -> tuple[pygame.Surface,pygame.Rect,list[pygame.Rect]]:
        size=(400,400)
        item_sur = pygame.Surface(size)
        item_sur.fill(COLOR.BLUE)
        pygame.draw.rect(item_sur,COLOR.BLACK,(10,10,380,380))
        ship_rec = pygame.draw.rect(item_sur,COLOR.GREEN,(size[0]/2-ship_shape[0]/2,size[1]/2-ship_shape[1]/2,ship_shape[0],ship_shape[1]))
        ship_rec.topleft = (size[0]/2-ship_shape[0]/2,size[1]/2-ship_shape[1]/2)
        radius = 15
        weapon_rec = [None]*MAX_NUM_OF_WEAPON
        for i in range(0,MAX_NUM_OF_WEAPON):
            wc = pygame.draw.circle(item_sur,COLOR.BLUE,(ship_rec.topleft[0]+weapon_pos[i][0],ship_rec.topleft[1]+weapon_pos[i][1]),radius)
            wc = pygame.draw.circle(pygame.Surface((30,30)),COLOR.GREEN,weapon_pos[i],15)
            wc.center = (ship_rec.topleft[0] + weapon_pos[i][0],ship_rec.topleft[1] + weapon_pos[i][1])
            weapon_rec[i] = wc
        item_rec = item_sur.get_rect()
        return item_sur,item_rec,weapon_rec
    
    def __set_rect(self,screen:pygame.Surface):
        screen_rec = screen.get_rect()
        self.item_rect.center = screen_rec.center
        [self.weapon_rec[i].move_ip(self.item_rect.topleft) for i in range(0,MAX_NUM_OF_WEAPON)]

    def __text_place_position(self,text_rec:pygame.Rect,center_pos:tuple[float,float]) -> tuple[float,float]:
        place_pos = (center_pos[0]-text_rec.centerx,center_pos[1]-text_rec.centery)
        return place_pos
    
    def hover(self,) -> None:
        self.weapon_rec