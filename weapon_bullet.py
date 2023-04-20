import pygame
import csv
import random
from ship_weapon import ShipWeapon
from pygame.locals import *
from const import *

MAX_EXIST_BULLET = 500
BULLET_SPEED_COF = 0.01

class WeaponBullet():
    # パラメーターのインポート
    with open(file='./master_data/bullets.csv',mode='r',encoding='utf-8') as params_file:
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
        # 図形とヒットボックス作成
        self.view_sur = pygame.Surface((self.radius*2,self.radius*2))        
        self.hitbox_sur = pygame.Surface((self.radius*2*0.8,self.radius*2*0.8))        
        self.rect = self.__create()[0]
        self.hitbox_rect = self.__create()[1]        
        # 弾丸格納用配列の作成&弾丸情報格納
        self.bullet_n = 0
        self.global_bullet_x =[self.__init_grobal_pos()[0]]*MAX_EXIST_BULLET
        self.global_bullet_y =[self.__init_grobal_pos()[1]]*MAX_EXIST_BULLET
        self.bullet_flag =[False]*MAX_EXIST_BULLET     
        self.spread_cof = 0
        self.spread_bullet_vector = [(0,0) for i in range(MAX_EXIST_BULLET)]

    def __create(self,color:int=(100,200,100)) -> tuple[pygame.Rect,pygame.Rect]:
        """create bullet shape"""
        # 弾丸の図形作成
        self.view_sur.set_colorkey((0, 0, 0))
        rect = pygame.draw.circle(self.view_sur,color,(self.radius, self.radius),radius=self.radius)
        # 弾丸のヒットボックス作成
        self.hitbox_sur.set_colorkey((0,0,0))
        hitbox_rect = pygame.draw.rect(self.hitbox_sur,color,(0,0,self.radius*2*0.8,self.radius*2*0.8))
        return rect,hitbox_rect

    def __init_grobal_pos(self) -> tuple[float,float]:
        # グローバル座標での弾丸初期位置
        grobal_x = self.ship_weapon.rect.centerx - self.view_sur.get_rect().centerx
        grobal_y = self.ship_weapon.rect.centery - self.view_sur.get_rect().centery
        return grobal_x,grobal_y
        
    def __set(self,time:int = 0):
        """set bullet array"""
        # 弾丸のセット
        if time % self.ship_weapon.rate == 0: #設定されたレートで弾丸を発射
            self.__update_bullet_vector()
            if self.bullet_flag[self.bullet_n] == False:
                self.bullet_flag[self.bullet_n] = True
                groblal_bullet_pos = self.__init_grobal_pos()
                self.global_bullet_x[self.bullet_n] = groblal_bullet_pos[0]
                self.global_bullet_y[self.bullet_n] = groblal_bullet_pos[1]
                self.spread_cof = spread_bullet(self.spread)
                self.spread_bullet_vector[self.bullet_n] = self.sight_vector.rotate(self.spread_cof)
            self.bullet_n = (self.bullet_n+1)%MAX_EXIST_BULLET

    def __move(self,screen:pygame.Surface) -> None:
        """update bullet position and show bullet shape"""
        # 弾丸の移動
        for i in range(MAX_EXIST_BULLET):
            if self.bullet_flag[i] == True:
                self.global_bullet_x[i] = self.global_bullet_x[i] + self.ship_weapon.bullet_speed * self.spread_bullet_vector[i][0]*BULLET_SPEED_COF
                self.global_bullet_y[i] = self.global_bullet_y[i] + self.ship_weapon.bullet_speed * self.spread_bullet_vector[i][1]*BULLET_SPEED_COF
                distance_x = self.ship_weapon.bullet_speed * self.spread_bullet_vector[i][0]*BULLET_SPEED_COF
                distance_y = self.ship_weapon.bullet_speed * self.spread_bullet_vector[i][1]*BULLET_SPEED_COF
                self.rect.move_ip(self.view_sur,(distance_x,distance_y))
                screen.blit(self.view_sur,(self.global_bullet_x[i],self.global_bullet_y[i]))
                if self.global_bullet_x[i]<0 or self.global_bullet_y[i]<0 or self.global_bullet_x[i] > screen.get_rect().right or self.global_bullet_y[i] > screen.get_rect().bottom:
                    self.bullet_flag[i] = False
                    
    def __update_bullet_vector(self) -> None:
        self.sight_vector = pygame.math.Vector2(self.ship_weapon.sight_vector[1][0]-self.ship_weapon.sight_vector[0][0],self.ship_weapon.sight_vector[1][1]-self.ship_weapon.sight_vector[0][1])
    
    def shot(self,screen,time):
        if self.ship_weapon.status['use'] == WEAPON_STAT.UNUSED:
            self.__move(screen)
            return
        self.__set(time)
        self.__move(screen)
        
        
def spread_bullet(param_bullet_spread:float) -> float:
    """add bullet attribution:bullet spread"""
    spread_cof = 0.1*random.randrange(-10,10) * param_bullet_spread
    return spread_cof

def shot_multiple(pos) -> None:
    """add bullet attribution:enabling to shot multiple bullet"""
    pass

def explode(pos) -> None:
    """add bullet attribution:bullet explode when bullet hit anything"""
    pass

def homing(pos) -> None:
    """add bullet attribution:bullet chaise the target"""
    pass