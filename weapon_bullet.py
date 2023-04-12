import pygame
import csv
from ship_weapon import ShipWeapon
from pygame.locals import *
MAX_EXIST_BULLET = 3

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
        self.sight_vector = pygame.math.Vector2(self.ship_weapon.sight_vector[1][0]-self.ship_weapon.sight_vector[0][0],self.ship_weapon.sight_vector[1][1]-self.ship_weapon.sight_vector[0][1]).scale_to_length(100)

        
        # 弾丸格納用配列の作成
        self.bullet_n = 0
        self.bullet_x =[0]*MAX_EXIST_BULLET
        self.bullet_y =[0]*MAX_EXIST_BULLET
        self.bullet_flag =[False]*MAX_EXIST_BULLET
        
    def create(self,color:int=(100,200,100)) -> None:
        # 弾丸の図形作成
        self.view_sur = pygame.Surface((self.radius*2,self.radius*2))
        self.view_sur.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.view_sur,color,(self.radius, self.radius),radius=self.radius)
        
        # 弾丸のヒットボックス作成
        self.hitbox_sur = pygame.Surface((self.radius*2*0.8,self.radius*2*0.8))
        self.hitbox_sur.set_colorkey((0,0,0))
        pygame.draw.rect(self.hitbox_sur,color,(0,0,self.radius*2*0.8,self.radius*2*0.8))

    def set(self,time = 0):
        if time % self.ship_weapon.rate == 0:
            if self.bullet_flag[self.bullet_n] == False:
                self.bullet_flag[self.bullet_n] = True
                self.bullet_x[self.bullet_n] = 120 #* self.sight_vector[1]
                self.bullet_y[self.bullet_n] = 100 #* self.sight_vector[1]
            self.bullet_n = (self.bullet_n+1)%MAX_EXIST_BULLET


    def move(self,screen:pygame.Surface):
        for i in range(MAX_EXIST_BULLET):
            if self.bullet_flag[i] == True:
                self.bullet_x[i] = self.bullet_x[i] - self.ship_weapon.bullet_speed * 0.1#* self.sight_vector[0] 適当に０．１をかけただけ
                self.bullet_y[i] = self.bullet_y[i] - self.ship_weapon.bullet_speed * 0.1#* self.sight_vector[1] 適当に０．１をかけただけ
                screen.blit(self.view_sur,(100+self.bullet_x[i],100+self.bullet_y[i])) #適当に100をぷらすしただけ
                if self.bullet_x[i]<0 or self.bullet_y[i]<0:
                    self.bullet_flag[i] = False
                

