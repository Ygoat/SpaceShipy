import pygame
import csv
from space_ship import SpaceShip

class ShipWeapon():
    # パラメーターのインポート
    with open(file='./weapons.csv',mode='r',encoding='utf-8') as params_file:
        params = [row for row in csv.DictReader(params_file)]    
    
    def __init__(self,space_ship:SpaceShip,weapon_id:int=0,pos_id:int=0) -> None:
        # パラメーターのセット
        param = self.params[weapon_id]
        self.attack = float(param['attack'])
        self.rate = float(param['rate'])
        self.bullet_speed = float(param['bullet_speed'])
        self.bullet_type = int(param['bullet_type'])
        self.space_ship = space_ship
        
    def create(self,color:int=(255,0,0)) -> None:
        self.sur = pygame.Surface((20,20))
        self.sur.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.sur,color,(10, 10),radius=10)

    def weapon_sight(self,color:int=(255,0,0))  -> None:
        ship = self.space_ship
        center = tuple(map(float,(ship.sur.get_rect().center)))
        self.sight_sur = pygame.Surface((200, 200))
        self.sight_sur.set_colorkey((0, 0, 0))
        print(ship.weapon_pos[0][1],center[1])

        sight_vector = (-(ship.weapon_pos[0][0] - center[0]), -(ship.weapon_pos[0][1] - center[1]))
        pygame.draw.line(self.sight_sur, color, (0, 0), sight_vector)
        
def sight_vector_line(weapon_pos:tuple,ship_center:tuple,sight_sur:pygame.Surface) -> tuple:
    x_judge = weapon_pos[0] - ship_center[0] >= 0
    y_judge = weapon_pos[1] - ship_center[1] >= 0
    sight_sur_rec = sight_sur.get_rect()
        
    sight_vector_start = sight_sur_rec.center
    sight_vector_end = (-(weapon_pos[0] - sight_sur_rec.center[0]), -(weapon_pos[1] - sight_sur_rec.center[1]))
        
    vector1=pygame.math.Vector2(0,1)
    vector2=pygame.math.Vector2(1,0).dot(vector1)
    print(vector2)        
    return sight_vector_start,sight_vector_end
