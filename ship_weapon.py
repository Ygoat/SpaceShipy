import pygame
import csv
from space_ship import SpaceShip
from const import WEAPON_STAT
        
class ShipWeapon():
    # パラメーターのインポート
    with open(file='./master_data/weapons.csv',mode='r',encoding='utf-8') as params_file:
        params = [row for row in csv.DictReader(params_file)]    
    
    def __init__(self,screen:pygame.Surface,space_ship:SpaceShip,weapon_id:int=0,pos_id:int=0) -> None:
        # パラメーターのセット
        param:dict = self.params[weapon_id]
        self.weapon_id = weapon_id
        self.attack:float = float(param['attack'])
        self.rate:int = int(param['rate'])
        self.bullet_speed:float = float(param['bullet_speed'])
        self.bullet_type:int = int(param['bullet_type'])
        self.space_ship = space_ship
        self.pos_id:int = pos_id
        self.status = {'use':WEAPON_STAT.UNUSED,'reload':WEAPON_STAT.UNUSED}
        # 図形作成
        self.sur:pygame.Surface = pygame.Surface((20,20))
        self.sight_sur = pygame.Surface((200, 200))
        self.sight_vector:list[tuple[float,float],tuple[float,float]] = standard_sight_vector_line(self.space_ship.weapon_pos[self.pos_id],self.space_ship.sur.get_rect().center,self.sight_sur)
        self.rect = self.__create()
        self.sight_rect = self.__create_init_weapon_sight()
        # 位置情報
        self.grobal_position_x:float = space_ship.rect.topleft[0] + space_ship.weapon_pos[weapon_id][0] - self.rect.centerx
        self.grobal_position_y:float = space_ship.rect.topleft[1] + space_ship.weapon_pos[weapon_id][1] - self.rect.centery
        self.grobal_position_x_center:float = space_ship.rect.topleft[0] + space_ship.weapon_pos[weapon_id][0]
        self.grobal_position_y_center:float = space_ship.rect.topleft[1] + space_ship.weapon_pos[weapon_id][1]
        self.grobal_sight_position_x:float = 0
        self.grobal_sight_position_y:float = 0
        self.grobal_sight_position_x_center:float = 0
        self.grobal_sight_position_y_center:float = 0
        # スクリーン上初期値位置にセット
        self.rect.move_ip(self.grobal_position_x,self.grobal_position_y)
        self.rect.clamp_ip(screen.get_rect())
        
    def __create(self,color:int=(255,0,0)) -> pygame.Rect:
        """create weapon shape"""
        # 武器の図形作成
        self.sur.set_colorkey((0, 0, 0))
        rect = pygame.draw.circle(self.sur,color,(10, 10),radius=10)
        return rect
        
    def __create_init_weapon_sight(self,color:int=(255,0,0))  -> pygame.Rect:
        """create weapon sight line"""
        # 武器の照準
        self.sight_sur.set_colorkey((0, 0, 0))
        sight_rect = pygame.draw.line(self.sight_sur, color, self.sight_vector[0], self.sight_vector[1])
        return sight_rect
        
    def show(self,screen:pygame.Surface) -> None:
        """show weapon shape"""
        # 武器の表示
        screen.blit(self.sur,(self.rect.topleft[0], self.rect.topleft[1]))
        
    def show_weapon_sight(self,screen:pygame.Surface,ship_center:tuple[float,float],ship_weapon_pos:tuple[float,float]) -> None:
        """show weapon sight(initial)"""
        # 線の描画を消去
        pygame.draw.rect(self.sight_sur,(0,0,0),(0,0,200,200))
        # 照準の表示
        self.grobal_sight_position_x = screen.get_rect().centerx + ship_weapon_pos[0] - ship_center[0] - self.sight_sur.get_rect().centerx
        self.grobal_sight_position_y = screen.get_rect().centery + ship_weapon_pos[1] - ship_center[1] - self.sight_sur.get_rect().centery
        self.grobal_sight_position_x_center = self.grobal_sight_position_x + self.sight_sur.get_rect().centerx
        self.grobal_sight_position_y_center = self.grobal_sight_position_y + self.sight_sur.get_rect().centery
        pygame.draw.line(self.sight_sur, (0,255,0), self.sight_vector[0], self.sight_vector[1])
        screen.blit(self.sight_sur,(self.grobal_sight_position_x,self.grobal_sight_position_y))

def standard_sight_vector_line(weapon_pos:tuple,ship_center:tuple,sight_sur:pygame.Surface) -> tuple[(float,float),(float,float)]:
    # 基準となる武器の照準線のベクトル作成
    sight_sur_rec = sight_sur.get_rect()
    sight_vector_start = sight_sur_rec.center
    
    ship_center2weapon_pos = pygame.math.Vector2(weapon_pos[0] - ship_center[0], weapon_pos[1] - ship_center[1])
    ship_center2weapon_pos.scale_to_length(100)

    sight_vector_end = ( sight_sur_rec.center[0] + ship_center2weapon_pos.x ,sight_sur_rec.center[1] + ship_center2weapon_pos.y )
       
    return [sight_vector_start,sight_vector_end]

