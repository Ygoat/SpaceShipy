import pygame
import csv
import random
from ship_weapon import ShipWeapon
class ShipClue():
    # パラメーターのインポート
    with open(file='./clues.csv',mode='r',encoding='utf-8') as params_file:
        params = [row for row in csv.DictReader(params_file)]
    shape = (10,10)
    
    def __init__(self,ship_weapon:tuple[ShipWeapon,...],clue_id:int=0) -> None:
        # パラメーターのセット
        param = self.params[clue_id]
        self.attack = float(param['attack'])
        self.defence = float(param['defence'])
        self.speed = float(param['speed'])
        self.role_id = int(param['role_id'])
        self.ship_weapon = ship_weapon[:]
        # 船員の位置情報
        self.grobal_pos_x = ship_weapon[0].grobal_position_x + ship_weapon[0].sur.get_rect().centerx - self.shape[0]/2
        self.grobal_pos_y = ship_weapon[0].grobal_position_y + ship_weapon[0].sur.get_rect().centery - self.shape[1]/2
        # 図形の作成
        self.sur = pygame.Surface(self.shape)
        self.__create()

    def __create(self,color:int=(0,0,255)) -> None:
        """create clue shape"""
        # 乗組員の図形作成
        self.sur.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.sur,color,(self.shape[0]/2, self.shape[1]/2),radius=self.shape[0]/2)
        
    def show(self,screen:pygame.Surface) -> None:
        """show clue shape"""
        # 乗組員の表示
        screen.blit(self.sur,(100,200))

    def move(self,screen:pygame.Surface,time:int = 0):
        if time % 60 == 0:
            i = random.randrange(0,5)
            target_pos = (self.ship_weapon[i].grobal_position_x,self.ship_weapon[i].grobal_position_y)
            self.grobal_pos_x = target_pos[0] + self.ship_weapon[0].sur.get_rect().centerx - self.shape[0]/2
            self.grobal_pos_y = target_pos[1] + self.ship_weapon[0].sur.get_rect().centerx - self.shape[1]/2
        screen.blit(self.sur,(self.grobal_pos_x,self.grobal_pos_y))