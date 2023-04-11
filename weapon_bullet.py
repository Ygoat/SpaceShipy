import pygame
import csv
from ship_weapon import ShipWeapon
MAX_EXIST_BULLET = 500

class WeaponBullet():
    # パラメーターのインポート
    with open(file='./bullets.csv',mode='r',encoding='utf-8') as params_file:
        params = [row for row in csv.DictReader(params_file)]    
    
    def __init__(self,ship_weapon:ShipWeapon,bullet_id:int) -> None:
        # パラメーターのセット
        param = self.params[bullet_id]
        self.attack = float(param['attack'])
        self.radius = float(param['radius'])
        self.spread = float(param['spread'])
        self.penetration = float(param['penetration'])
        self.is_hitscan = bool(param['is_hitscan'])
        self.ship_weapon = ship_weapon

        # 弾丸格納用配列の作成
        self.bullet_n = MAX_EXIST_BULLET
        self.bullet_x =[0]*MAX_EXIST_BULLET
        self.bullet_y =[0]*MAX_EXIST_BULLET
        self.bullet_flag =[False]*MAX_EXIST_BULLET
        
    def create(self,color:int=(255,255,255)) -> None:
        # 弾丸の図形作成
        self.sur = pygame.Surface((self.radius*2,self.radius*2))
        self.sur.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.sur,color,(self.radius, self.radius),radius=self.radius)

    def set(self):
        self.bullet_flag = True
        # bull_x[bull_n] = px-16
        # bull_y[bull_n] = py-32
        bull_n = (bull_n+1)%BULLET_MAX



    def move(self):
        return 0
    
