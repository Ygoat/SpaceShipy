import pygame
import csv
from weapon_bullet import WeaponBullet

class HostileShip():
    # パラメーターのインポート
    with open(file='./hostiles.csv',mode='r',encoding='utf-8') as params_file:
        params = [row for row in csv.DictReader(params_file)]    
    
    def __init__(self,weapon_bullet:WeaponBullet,hostile_id:int=0) -> None:
        # パラメーターのセット
        param:dict = self.params[hostile_id]
        self.attack:float = float(param['attack'])
        self.attack:float = float(param['speed'])
        self.attack:float = float(param['defence'])
        self.rate:int = int(param['rate'])
        self.bullet_speed:float = float(param['bullet_speed'])
        self.bullet_type:int = int(param['bullet_type'])
        self.shape:float = float(param['shape']) 
        self.weapon_bullet:pygame.Surface = weapon_bullet
        self.pos_id:int = hostile_id
        # 位置情報
        self.grobal_position_x:float = 200
        self.grobal_position_y:float = 0
        self.dx = 5 #テスト用
        # 図形作成
        self.sur:pygame.Surface = pygame.Surface((20,20))
        self.__create()
        
    def __create(self,color:int=(255,255,255)) -> None:
        """create hostile ship shape"""
        # 敵機の図形作成
        self.sur.set_colorkey((0, 0, 0))
        pygame.draw.rect(self.sur,color,(0,0,self.shape,self.shape))

    def move(self,screen:pygame.Surface):
        """show hostiel ship shape"""
        if (self.sur.get_rect().right + self.grobal_position_x > screen.get_rect().right) and (self.dx > 0):
            self.dx = -self.dx
        if (self.sur.get_rect().left + self.grobal_position_x < screen.get_rect().left) and (self.dx < 0):
            self.dx = -self.dx
        self.grobal_position_x = self.grobal_position_x + self.dx
        self.grobal_position_y = screen.get_rect().centery-250
        # 敵機の表示
        screen.blit(self.sur,(self.grobal_position_x, self.grobal_position_y))