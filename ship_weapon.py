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
        self.pos_id = pos_id
        
    def create(self,color:int=(255,0,0)) -> None:
        # 武器の図形作成
        self.sur = pygame.Surface((20,20))
        self.sur.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.sur,color,(10, 10),radius=10)

    def show(self,screen:pygame.Surface,ship_center:tuple[float,float],ship_weapon_pos:tuple[float,float]):
        screen.blit(self.sur,(screen.get_rect().center[0] + ship_weapon_pos[0] - self.sur.get_rect().center[0] - ship_center[0],screen.get_rect().center[1] + ship_weapon_pos[1] - self.sur.get_rect().center[1] - ship_center[1]))

    def weapon_sight(self,color:int=(255,0,0))  -> None:
        # 武器の照準
        self.sight_sur = pygame.Surface((200, 200))
        self.sight_sur.set_colorkey((0, 0, 0))
        
        self.sight_vector = standard_sight_vector_line(self.space_ship.weapon_pos[self.pos_id],self.space_ship.sur.get_rect().center,self.sight_sur)
        
        pygame.draw.line(self.sight_sur, color, self.sight_vector[0], self.sight_vector[1])
    
    

def standard_sight_vector_line(weapon_pos:tuple,ship_center:tuple,sight_sur:pygame.Surface) -> tuple[(float,float),(float,float)]:
    # 基準となる武器の照準線のベクトル作成
    sight_sur_rec = sight_sur.get_rect()
    sight_vector_start = sight_sur_rec.center
    
    ship_center2weapon_pos = pygame.math.Vector2(weapon_pos[0] - ship_center[0], weapon_pos[1] - ship_center[1])
    ship_center2weapon_pos.scale_to_length(100)

    sight_vector_end = ( sight_sur_rec.center[0] + ship_center2weapon_pos.x ,sight_sur_rec.center[1] + ship_center2weapon_pos.y  ) 
       
    return sight_vector_start,sight_vector_end

