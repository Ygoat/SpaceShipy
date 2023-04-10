import pygame
import csv

class ShipClue():
    # パラメーターのインポート
    with open(file='./clues.csv',mode='r',encoding='utf-8') as params_file:
        params = [row for row in csv.DictReader(params_file)]
    shape = (10,10)
    
    def __init__(self,id:int=0) -> None:
        # パラメーターのセット
        param = self.params[id]
        self.attack = float(param['attack'])
        self.defence = float(param['defence'])
        self.speed = float(param['speed'])
        self.role_id = int(param['role_id'])

    def create(self,color:int=(0,0,255)) -> None:
        # 乗組員の図形作成
        self.sur = pygame.Surface(self.shape)
        self.sur.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.sur,color,(self.shape[0]/2, self.shape[1]/2),radius=self.shape[0]/2)

    def movement(self):
        return 0