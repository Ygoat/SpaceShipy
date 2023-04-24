import pygame
import csv
from weapon_bullet import WeaponBullet
from const import *

class HostileShip():
    # パラメーターのインポート
    with open(file='./master_data/hostiles.csv',mode='r',encoding='utf-8') as params_file:
        params = [row for row in csv.DictReader(params_file)]    
    
    def __init__(self,screen:pygame.Surface,weapon_bullet:WeaponBullet,hostile_id:int=0) -> None:
        # パラメーターのセット
        param:dict = self.params[hostile_id]
        self.attack:float = float(param['attack'])
        self.attack:float = float(param['speed'])
        self.attack:float = float(param['defence'])
        self.rate:int = int(param['rate'])
        self.bullet_speed:float = float(param['bullet_speed'])
        self.bullet_type:int = int(param['bullet_type'])
        self.shape:float = float(param['shape']) 
        self.hp:float = float(param['hp'])
        self.weapon_bullet:pygame.Surface = weapon_bullet
        self.pos_id:int = hostile_id
        self.screen = screen
        self.status = HOSTILE_STAT.MOVE
        # 図形作成
        self.sur:pygame.Surface = pygame.Surface((self.shape,self.shape))
        self.rect = self.__create() 
        # 位置情報
        self.grobal_position_x:float = 400
        self.grobal_position_y:float = 50
        self.grobal_position_x_center:float = 0
        self.grobal_position_y_center:float = 0
        self.dx = 3 #テスト用
        # スクリーン上初期位置にセット
        self.rect.clamp_ip(screen.get_rect())
        self.rect.topleft = (self.grobal_position_x,self.grobal_position_y)

        
    def __create(self,color:int=(255,255,255)) -> pygame.Rect:
        """create hostile ship shape"""
        # 敵機の図形作成
        self.sur.set_colorkey((0, 0, 0))
        rect = pygame.draw.rect(self.sur,color,(0,0,self.shape,self.shape))
        return rect

    def move(self):
        """show hostile ship shape"""
        if (self.rect.right >= self.screen.get_rect().right) and (self.dx > 0):
            self.dx = -self.dx
        if (self.rect.left <= self.screen.get_rect().left) and (self.dx < 0):
            self.dx = -self.dx
        self.rect.move_ip(self.dx,0)
        self.grobal_position_x = self.rect.topleft[0]
        self.grobal_position_y = self.rect.topleft[1]
        self.grobal_position_x_center = self.rect.centerx
        self.grobal_position_y_center = self.rect.centery   
        # 敵機の表示
        self.screen.blit(self.sur,self.rect.topleft)
        
    def destroyed(self):
        """destroyed hostile ship"""
        self.status = HOSTILE_STAT.DESTROYED
            
    