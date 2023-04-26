import pygame
import csv
MAX_NUM_OF_WEAPON = 5

class SpaceShip():
    # パラメーターのインポート
    with open(file='./master_data/ships.csv',mode='r',encoding='utf-8') as params_file:
        params = [row for row in csv.DictReader(params_file)]    
    
    def __init__(self,screen:pygame.Surface,id:int=0) -> None:
        # パラメーターのセット
        param = self.params[id]
        self.shape = (float(param['sx']),float(param['sy']))
        self.weapon_pos = [(float(param[f'wx{i}']),float(param[f'wy{i}'])) for i in range(1,MAX_NUM_OF_WEAPON+1)]
        self.speed = float(param['speed'])
        self.attack = float(param['attack'])
        self.defence = float(param['defence'])
        self.special_id = int(param['special_id'])
        self.level_max = int(param['level_max'])
        self.hp = float(param['hp'])
        self.level_now = 0
        # 図形作成
        self.sur = pygame.Surface(self.shape)        
        self.rect = self.__create()
        # 位置情報
        self.grobal_pos_x = screen.get_rect().centerx - self.sur.get_rect().centerx
        self.grobal_pos_y = screen.get_rect().centery - self.sur.get_rect().centery
        self.grobal_pos_x_center = screen.get_rect().centerx
        self.grobal_pos_y_center = screen.get_rect().centery
        # スクリーン上初期位置にセット
        self.rect.clamp_ip(screen.get_rect())
        self.rect.move_ip(self.grobal_pos_x,self.grobal_pos_y)

        
    def __create(self,color:int=(0,255,0)) -> pygame.Rect:
        """create space ship shape"""
        # 宇宙船の図形作成
        self.sur.set_colorkey((0, 0, 0))
        drawrect = pygame.draw.rect(self.sur,color,(0, 0, self.shape[0], self.shape[1]))
        return drawrect 
        
    def show(self,screen:pygame.Surface) -> None:
        """show space ship shape"""
        # 宇宙船の表示
        
        screen.blit(self.sur,self.rect.topleft)
        
        