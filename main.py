import pygame 
from pygame.locals import * 
import sys

def main():
    
    # 初期設定
    pygame.init()
    screen = pygame.display.set_mode((600,400))
    pygame.display.set_caption('Sapce Shipy!')
    clock = pygame.time.Clock()
    # 背景・物の作成
    while True:
        # 画面をクリア
        screen.fill((0,0,0))
        # 背景・物のアップデート
        # 画面上に登場する背景・物を描画
        # 画面の実表示
        pygame.display.update()
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 描画スピードの調整（FPS）
        clock.tick(60)

class SpaceShip():
    shape:list = [0,0]
    weapon_place:list = [0,0]
    speed:float = 0.0
    attack:float = 0.0
    defence:float = 0.0
    special_id:int = 0
    level_max:int = 0
    level_now:int = 0
    
    def __init__(self,shpae:list,weapon_place:list,speed:float,attack:float,defence:float,special_id:int,level_max:int):
        self.shape = shpae
        self.weapon_place = weapon_place
        self.speed = speed
        self.attack = attack
        self.defence = defence
        self.special_id = special_id
        self.level_max = level_max
        self.level_now = 0
        
    def show_ship(self):
        pygame.draw.rect
        
        
if __name__ == '__main__':
    main()
    
    
    

    
    