import pygame
import csv
import random
import math
from ship_weapon import ShipWeapon
from space_ship import SpaceShip
from const import WEAPON_STAT

class ShipClue():
    # パラメーターのインポート
    with open(file='./master_data/clues.csv',mode='r',encoding='utf-8') as params_file:
        params = [row for row in csv.DictReader(params_file)]
    shape = (10,10)
    
    def __init__(self,space_ship:SpaceShip,ship_weapon:tuple[ShipWeapon,...],color:tuple[int,int,int],clue_id:int=0) -> None:
        # パラメーターのセット
        param = self.params[clue_id]
        self.attack = float(param['attack'])
        self.defence = float(param['defence'])
        self.speed = float(param['speed'])
        self.role_id = int(param['role_id'])
        self.ship_weapon = ship_weapon[:]
        self.space_ship = space_ship
        self.walk_speed = 5
        self.use_weapon_id = None
        self.status = []
        # 図形の作成
        self.sur = pygame.Surface(self.shape)
        self.rect = self.__create(color)
        # 船員の位置情報
        self.grobal_pos_x = space_ship.grobal_pos_x + space_ship.sur.get_rect().centerx - self.shape[0]/2
        self.grobal_pos_y = space_ship.grobal_pos_y + space_ship.sur.get_rect().centery - self.shape[1]/2
        # スクリーン上初期位置にセット
        # self.rect.move_ip(self.grobal_pos_x,self.grobal_pos_y)
        # self.rect.clamp_ip(space_ship.sur.get_rect())
        

    def __create(self,color:int=(0,0,255)) -> pygame.Rect:
        """create clue shape"""
        # 乗組員の図形作成
        self.sur.set_colorkey((0, 0, 0))
        rect = pygame.draw.circle(self.sur,color,(self.shape[0]/2, self.shape[1]/2),radius=self.shape[0]/2)
        return rect
        
    def show(self,screen:pygame.Surface) -> None:
        """show clue shape"""
        # 乗組員の表示
        screen.blit(self.space_ship.sur,(100,350))

    def move(self,screen:pygame.Surface,time:int = 0,timer:int = 0,target_grobal_pos=(0,0)):
        """move ship clue and show ship clue"""
        # !!!!blitをmove_ipに変更予定!!!!
        if self.__decision_next_action(factor1=997,factor2=timer) == 1:
            i = self.__choice_next_weapon()
            self.__left_weapon(self.use_weapon_id)
            self.use_weapon_id = i
            target_pos = (self.ship_weapon[self.use_weapon_id].grobal_position_x,self.ship_weapon[self.use_weapon_id].grobal_position_y)
            self.grobal_pos_x = target_pos[0] + self.ship_weapon[0].sur.get_rect().centerx - self.shape[0]/2
            self.grobal_pos_y = target_pos[1] + self.ship_weapon[0].sur.get_rect().centerx - self.shape[1]/2
            self.__use_weapon(self.use_weapon_id)
        self.__move_weapon_sight(self.use_weapon_id,target_grobal_pos)
        screen.blit(self.sur,(self.grobal_pos_x,self.grobal_pos_y))
            # circ_rect.move_ip(dx, dy)     
            # circ_rect.clamp_ip(SCREEN)
        
    def __choice_next_weapon(self) -> int:
        indexes = [0,1,2,3,4]
        validindexes =[]
        for i in indexes:
            if self.ship_weapon[i].status['use'] == WEAPON_STAT.UNUSED:
                validindexes.append(i)
        weapon_id = random.choice(validindexes)
        return weapon_id
        
    def __use_weapon(self,weapon_id:int) -> None:
        self.ship_weapon[weapon_id].status['use'] = WEAPON_STAT.USING
    
    def __left_weapon(self,weapon_id:int) -> None:
        if weapon_id == None:
            return
        self.ship_weapon[weapon_id].status['use'] = WEAPON_STAT.UNUSED
    
    def __decision_next_action(self,factor1,factor2) -> int:
        factor1_score = 1*factor1 
        factor2_score = (1000- 10 * (factor2 % 600))
        max_score = max(factor1_score,factor2_score)
        if max_score == factor1_score:
            # 現在の行動を継続
            return 0
        if max_score == factor2_score:
            # 次の武器へ移動
            return 1
        
    def __move_weapon_sight(self,weapon_id:int = 0,target_grobal_pos = (0, 0)):
        if weapon_id == None:
            return
        weapon_to_target_vec = pygame.math.Vector2(target_grobal_pos[0] - self.ship_weapon[weapon_id].grobal_position_x_center, target_grobal_pos[1] - self.ship_weapon[weapon_id].grobal_position_y_center)
        sight_vector = pygame.math.Vector2(self.ship_weapon[weapon_id].sight_vector[1][0] - self.ship_weapon[weapon_id].sight_vector[0][0],self.ship_weapon[weapon_id].sight_vector[1][1] - self.ship_weapon[weapon_id].sight_vector[0][1])
        angle = acute_angle(sight_vector,weapon_to_target_vec)
        rotate_rad = 10 * sigmoid_function(angle,0.1) * sign(sight_vector,weapon_to_target_vec)
        sight_vector = sight_vector.rotate(rotate_rad)
        self.ship_weapon[weapon_id].sight_vector[1] = (sight_vector[0] + self.ship_weapon[weapon_id].sight_vector[0][0],sight_vector[1] + self.ship_weapon[weapon_id].sight_vector[0][1])


def sigmoid_function(x,b=1):
    # シグモイド関数
    # ターゲットまでの距離に応じて、bの値を変化させる。
    if abs(x) < 0.0001:
        y = 0
    else:   
        y = 2*(1 / (1 + math.e**-abs(b*x)) - 0.5)
    return y

def acute_angle(base_vector:pygame.math.Vector2,target_vector:pygame.math.Vector2):
    if base_vector.cross(target_vector) >= 0:
        return base_vector.angle_to(target_vector)
    if base_vector.cross(target_vector) < 0:
        return -base_vector.angle_to(target_vector)
    
def sign(base_vector:pygame.math.Vector2,target_vector:pygame.math.Vector2):
    if base_vector.cross(target_vector) >= 0:
        return 1
    else:
        return -1