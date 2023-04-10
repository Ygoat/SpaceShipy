import pygame
import csv

class SpaceShip():
    # パラメーターのインポート
    with open(file='./ships.csv',mode='r',encoding='utf-8') as params_file:
        params = [row for row in csv.DictReader(params_file)]    
    
    def __init__(self,id:int=0) -> None:
        # パラメーターのセット
        param = self.params[id]
        print(param)
        self.shape = (float(param['sx']),float(param['sy']))
        self.weapon_pos = [(float(param['wx1']),float(param['wy1'])),(float(param['wx2']),float(param['wy2']))]
        self.speed = float(param['speed'])
        self.attack = float(param['attack'])
        self.defence = float(param['defence'])
        self.special_id = int(param['special_id'])
        self.level_max = int(param['level_max'])
        self.level_now = 0
        
    def create(self,color:int=(0,255,0)) -> None:
        self.sur = pygame.Surface(self.shape)
        self.sur.set_colorkey((0, 0, 0))
        pygame.draw.rect(self.sur,color,(0, 0, self.shape[0], self.shape[1]))

        
        