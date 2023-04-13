import pygame
import csv
from ship_weapon import ShipWeapon
from pygame.locals import *
MAX_EXIST_BULLET = 500
BULLET_SPEED_COF = 0.01

class WeaponBullet():
    # パラメーターのインポート
    with open(file='./bullets.csv',mode='r',encoding='utf-8') as params_file:
        params = [row for row in csv.DictReader(params_file)]    
    
    def __init__(self,ship_weapon:ShipWeapon,bullet_id:int=0) -> None:
        # パラメーターのセット
        param = self.params[bullet_id]
        self.attack = float(param['attack'])
        self.radius = float(param['radius'])
        self.spread = float(param['spread'])
        self.penetration = float(param['penetration'])
        self.is_hitscan = bool(param['is_hitscan'])
        self.ship_weapon = ship_weapon
        self.sight_vector = pygame.math.Vector2(self.ship_weapon.sight_vector[1][0]-self.ship_weapon.sight_vector[0][0],self.ship_weapon.sight_vector[1][1]-self.ship_weapon.sight_vector[0][1])
        
        # 弾丸格納用配列の作成
        self.bullet_n = 0
        self.global_bullet_x =[0]*MAX_EXIST_BULLET
        self.global_bullet_y =[0]*MAX_EXIST_BULLET
        self.bullet_flag =[False]*MAX_EXIST_BULLET
        
        # 図形とヒットボックス作成
        self.__create()
        
    def __create(self,color:int=(100,200,100)) -> None:
        # 弾丸の図形作成
        self.view_sur = pygame.Surface((self.radius*2,self.radius*2))
        self.view_sur.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.view_sur,color,(self.radius, self.radius),radius=self.radius)
        
        # 弾丸のヒットボックス作成
        self.hitbox_sur = pygame.Surface((self.radius*2*0.8,self.radius*2*0.8))
        self.hitbox_sur.set_colorkey((0,0,0))
        pygame.draw.rect(self.hitbox_sur,color,(0,0,self.radius*2*0.8,self.radius*2*0.8))

    def set(self,time:int = 0):
        # 弾丸のセット
        if time % self.ship_weapon.rate == 0:
            if self.bullet_flag[self.bullet_n] == False:
                self.bullet_flag[self.bullet_n] = True
                self.global_bullet_x[self.bullet_n] = self.ship_weapon.grobal_position_x + self.ship_weapon.sur.get_rect().centerx - self.view_sur.get_rect().centerx
                self.global_bullet_y[self.bullet_n] = self.ship_weapon.grobal_position_y + self.ship_weapon.sur.get_rect().centery - self.view_sur.get_rect().centery
            self.bullet_n = (self.bullet_n+1)%MAX_EXIST_BULLET


    def move(self,screen:pygame.Surface) -> None:
        # 弾丸の移動
        for i in range(MAX_EXIST_BULLET):
            if self.bullet_flag[i] == True:
                self.global_bullet_x[i] = self.global_bullet_x[i] + self.ship_weapon.bullet_speed * self.sight_vector[0]*BULLET_SPEED_COF
                self.global_bullet_y[i] = self.global_bullet_y[i] + self.ship_weapon.bullet_speed * self.sight_vector[1]*BULLET_SPEED_COF
                screen.blit(self.view_sur,(self.global_bullet_x[i],self.global_bullet_y[i]))
                if self.global_bullet_x[i]<0 or self.global_bullet_y[i]<0 or self.global_bullet_x[i] > screen.get_rect().right or self.global_bullet_y[i] > screen.get_rect().bottom:
                    self.bullet_flag[i] = False
        