import pygame
from pygame.locals import *
import sys

def main():

    # 初期設定
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    SCREEN = screen.get_rect()
    pygame.display.set_caption('Hello World')

    clock = pygame.time.Clock()

    # 登場する人/物/背景の作成
    circ_sur = pygame.Surface((20, 20))
    circ_sur.set_colorkey((0, 0, 0))
    circ_rect = circ_sur.get_rect()
    circ_rect.topleft = (300, 150)
    dx, dy = 5, 4
    pygame.draw.circle(circ_sur, (255, 255, 255), (10, 10), 10)
    rect_sur = pygame.Surface((100, 60))
    pygame.draw.rect(rect_sur, (255, 0, 0), (0, 0, 100, 60))
    line_sur = pygame.Surface((100, 50))
    line_sur.set_colorkey((0, 0, 0))
    pygame.draw.line(line_sur, (0, 255, 0), (0, 0), (100, 50))
    

    
    while True:
        
        # 画面(screen)をクリア
        screen.fill((0, 0, 0))

        # ゲームに登場する人/物/背景の位置Update
        circ_rect.move_ip(dx, dy)
        if circ_rect.left < SCREEN.left or circ_rect.right > SCREEN.right:
            dx = -dx
        if circ_rect.top < SCREEN.top or circ_rect.bottom > SCREEN.bottom:
            dy = -dy
        circ_rect.clamp_ip(SCREEN)

        # 画面(screen)上に登場する人/物/背景を描画
        screen.blit(rect_sur,(150, 150))
        screen.blit(circ_sur,circ_rect.topleft)
        screen.blit(line_sur,(250, 250))
        
        # 画面(screen)の実表示
        pygame.display.update()

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 描画スピードの調整（FPS)
        clock.tick(60)

if __name__ == "__main__":
    main()



class SpaceShip():
    
    def __init__(self,
                 shpae:list,
                 weapon_place:list,
                 speed:float,
                 attack:float,
                 defence:float,
                 special_id:int,
                 level_max:int):
        # ここにCSVをインポートする
        self.shape = shpae
        self.weapon_place = weapon_place
        self.speed = speed
        self.attack = attack
        self.defence = defence
        self.special_id = special_id
        self.level_max = level_max
        self.level_now = 0
        self.width = 1
        
    def show(self):
        pygame.draw.rect()
        
    def create(self,width:float,height:float,color:int=(0,0,0)):
        ship_sur = pygame.Surface((width, height))
        pygame.draw.rect(ship_sur,color,(0, 0, width, height))
    
class  ShipeClue():
    attack:float = 0.0
    defence:float = 0.0
    speed:float = 0.0
    pattern:int = 0
    special_id:int = 0