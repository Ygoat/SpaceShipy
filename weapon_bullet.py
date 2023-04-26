import pygame
import csv
import random
from ship_weapon import ShipWeapon
from pygame.locals import *
from const import *
# メモ
# 画面範囲外に判定が残り続けるため、どうにかする。

MAX_EXIST_BULLET = 500
BULLET_SPEED_COF = 0.01

class WeaponBullet():
    # パラメーターのインポート
    with open(file='./master_data/bullets.csv',mode='r',encoding='utf-8') as params_file:
        params = [row for row in csv.DictReader(params_file)]    
    
    def __init__(self,screen:pygame.Surface,ship_weapon:ShipWeapon,bullet_id:int=0) -> None:
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
        self.hitbox_surs = [pygame.Surface((self.radius*2*0.8,self.radius*2*0.8))] * MAX_EXIST_BULLET        
        self.rect = self.__create_bullet()
        self.hitbox_rects = self.__create_hitbox()
        # 弾丸格納用配列の作成&弾丸情報格納
        self.bullet_n = 0
        self.grobal_bullet_x = [self.__init_grobal_pos()[0]] * MAX_EXIST_BULLET
        self.grobal_bullet_y = [self.__init_grobal_pos()[1]] * MAX_EXIST_BULLET
        self.grobal_hitbox_x = [self.__init_hitbox_grobal_pos()[0]] * MAX_EXIST_BULLET
        self.grobal_hitbox_y = [self.__init_hitbox_grobal_pos()[1]] * MAX_EXIST_BULLET
        self.bullet_flag = [False] * MAX_EXIST_BULLET
        self.spread_cof = 0
        self.spread_bullet_vector = [(0,0) for i in range(MAX_EXIST_BULLET)]
        # 位置情報
        self.grobal_position_x:float = self.ship_weapon.grobal_position_x_center - self.view_sur.get_rect().centerx
        self.grobal_position_y:float = self.ship_weapon.grobal_position_y_center - self.view_sur.get_rect().centery
        self.hitbox_grobal_position_x:float = self.ship_weapon.grobal_position_x_center - self.hitbox_surs[0].get_rect().centerx
        self.hitbox_grobal_position_y:float = self.ship_weapon.grobal_position_y_center - self.hitbox_surs[0].get_rect().centery
        # スクリーン上初期位置にセット
        self.rect.clamp_ip(screen.get_rect())        
        self.rect.move_ip(self.grobal_position_x,self.grobal_position_y)
        [self.hitbox_rects[i].clamp_ip(screen.get_rect()) for i in range(0,MAX_EXIST_BULLET)]
        [self.hitbox_rects[i].move_ip(self.hitbox_grobal_position_x,self.hitbox_grobal_position_y) for i in range(0,MAX_EXIST_BULLET)]

        
    def __create_bullet(self,color:int=(100,200,100)) -> pygame.Rect:
        """create bullet shape"""
        # 弾丸の図形作成
        self.view_sur.set_colorkey((0, 0, 0))
        rect = pygame.draw.circle(self.view_sur,color,(self.radius, self.radius),radius=self.radius)
        return rect
    
    def __create_hitbox(self,color=(0,0,255)) -> list[pygame.Rect]:
        # 弾丸のヒットボックス作成
        [self.hitbox_surs[i].set_colorkey((0,0,0)) for i in range(0,MAX_EXIST_BULLET)]
        hitbox_rects = list([pygame.draw.rect(self.hitbox_surs[i],color,(0,0,self.radius*2*0.8,self.radius*2*0.8)) for i in range(0,MAX_EXIST_BULLET)])
        return hitbox_rects

    def __init_grobal_pos(self) -> tuple[float,float]:
        # グローバル座標での弾丸初期位置
        grobal_x = self.ship_weapon.grobal_position_x_center - self.view_sur.get_rect().centerx
        grobal_y = self.ship_weapon.grobal_position_y_center - self.view_sur.get_rect().centery
        return grobal_x,grobal_y

    def __init_hitbox_grobal_pos(self) -> tuple[float,float]:
        # グローバル座標での弾丸ヒットボックス初期位置
        hitbox_grobal_x = self.ship_weapon.grobal_position_x_center - self.hitbox_surs[0].get_rect().centerx
        hitbox_grobal_y = self.ship_weapon.grobal_position_y_center - self.hitbox_surs[0].get_rect().centery
        return hitbox_grobal_x,hitbox_grobal_y
        
    def __set(self,time:int = 0):
        """set bullet array"""
        # 弾丸のセット
        if time % self.ship_weapon.rate == 0: #設定されたレートで弾丸を発射
            self.__update_bullet_vector()
            if self.bullet_flag[self.bullet_n] == False:
                self.bullet_flag[self.bullet_n] = True
                grobal_bullet_pos = self.__init_grobal_pos()
                grobal_hitbox_pos = self.__init_hitbox_grobal_pos()
                self.grobal_bullet_x[self.bullet_n] = grobal_bullet_pos[0]
                self.grobal_bullet_y[self.bullet_n] = grobal_bullet_pos[1]
                self.grobal_hitbox_x[self.bullet_n] = grobal_hitbox_pos[0]
                self.grobal_hitbox_y[self.bullet_n] = grobal_hitbox_pos[1]
                self.hitbox_rects[self.bullet_n].topleft = grobal_hitbox_pos
                self.spread_cof = spread_bullet(self.spread)
                self.spread_bullet_vector[self.bullet_n] = self.sight_vector.rotate(self.spread_cof)
            self.bullet_n = (self.bullet_n+1)%MAX_EXIST_BULLET

    def __move(self,screen:pygame.Surface) -> None:
        """update bullet position and show bullet shape"""
        # 弾丸の移動
        for i in range(MAX_EXIST_BULLET):
            if self.bullet_flag[i] == True:
                self.grobal_bullet_x[i] = self.grobal_bullet_x[i] + self.ship_weapon.bullet_speed * self.spread_bullet_vector[i][0]*BULLET_SPEED_COF
                self.grobal_bullet_y[i] = self.grobal_bullet_y[i] + self.ship_weapon.bullet_speed * self.spread_bullet_vector[i][1]*BULLET_SPEED_COF
                self.grobal_hitbox_x[i] = self.grobal_bullet_x[i] + self.view_sur.get_rect().centerx - self.hitbox_surs[i].get_rect().centerx
                self.grobal_hitbox_y[i] = self.grobal_bullet_y[i] + self.view_sur.get_rect().centery - self.hitbox_surs[i].get_rect().centery
                self.rect.topleft = (self.grobal_bullet_x[i],self.grobal_bullet_y[i]) #hitboxと異なり、rect自体は１つ
                self.hitbox_rects[i].topleft = (self.grobal_hitbox_x[i],self.grobal_hitbox_y[i]) 
                screen.blit(self.view_sur,(self.grobal_bullet_x[i],self.grobal_bullet_y[i]))
                # screen.blit(self.hitbox_surs[i],(self.hitbox_rects[i].topleft))
                if self.grobal_bullet_x[i]+self.view_sur.get_rect().right <-10 or self.grobal_bullet_y[i] + self.view_sur.get_rect().bottom <-10 or self.grobal_bullet_x[i] > screen.get_rect().right +10 or self.grobal_bullet_y[i] > screen.get_rect().bottom +10:
                    self.bullet_flag[i] = False
                    
    def __update_bullet_vector(self) -> None:
        self.sight_vector = pygame.math.Vector2(self.ship_weapon.sight_vector[1][0]-self.ship_weapon.sight_vector[0][0],self.ship_weapon.sight_vector[1][1]-self.ship_weapon.sight_vector[0][1])
    
    def shot(self,screen,time):
        if self.ship_weapon.status['use'] == WEAPON_STAT.UNUSED:
            self.__move(screen)
            return
        self.__set(time)
        self.__move(screen)
        
    def reset_bullet(self,id):
        self.grobal_bullet_x[id],self.grobal_bullet_y[id] = self.__init_grobal_pos()
        self.grobal_hitbox_x[id],self.grobal_hitbox_y[id] = self.__init_hitbox_grobal_pos()
        self.hitbox_rects[id].topleft = (self.grobal_bullet_x[id],self.grobal_bullet_y[id])      
        
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