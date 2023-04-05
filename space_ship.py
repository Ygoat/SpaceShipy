import pygame
import csv

class SpaceShip():
    
    def __init__(self,id:int=0) -> None:
        # パラメーターのインポート
        with open(file='./ships.csv',mode='r',encoding='utf-8') as params_file:
            self.params = [row for row in csv.DictReader(params_file)]
        
        # パラメーターのセット
        param = self.params[id]
        self.shape = tuple(map(float,(param['sx'],param['sy'])))
        self.weapon_place = [(param['wx1'],param['wy1']),(param['wx2'],param['wy2'])]
        self.speed = float(param['speed'])
        self.attack = float(param['attack'])
        self.defence = float(param['defence'])
        self.special_id = int(param['special_id'])
        self.level_max = int(param['level_max'])
        self.level_now = 0
        
    def create(self,color:int=(0,0,0)):
        self.sur = pygame.Surface(self.shape)
        pygame.draw.rect(self.sur,color,(0, 0, self.shape[0], self.shape[1]))
