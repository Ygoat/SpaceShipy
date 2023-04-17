import pygame
import sys
from space_ship import SpaceShip
from ship_clue import ShipClue
from ship_weapon import ShipWeapon
from weapon_bullet import WeaponBullet
from hostile_ship import HostileShip
from battle_controller import BattleController
from pygame.locals import *
from const import *
MAX_NUM_OF_WEAPON:int = 5
MAX_NUM_OF_CLUE:int = 3

def main() -> None:

    # 初期設定
    pygame.init()
    pygame.display.set_caption('Space Shipy')
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((500, 500))
    SCREEN = screen.get_rect()
    
    rec = pygame.Rect(0,0,100,100)
    # pygame.Surface.blit(re)
    drawrec = pygame.draw.rect(screen,(255,0,0),rec)

    fpscounter:int = 0
    set_timer:int = 0
    while True:
        fpscounter = (fpscounter + 1) % 60
        set_timer = (set_timer + 1) % 600 #キャラ移動用のテストタイマー
        
        # 画面(screen)をクリア
        screen.fill((0, 0, 0))
        # screen.blit(screen,(0,0))
        rec.move_ip(100,100)
        # ゲームに登場する人/物/背景の位置Update
 
        # 画面(screen)の実表示
        pygame.display.update()

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 描画スピードの調整（FPS)
        clock.tick(60)
        # print(clock.get_fps())
        
if __name__ == "__main__":
    main()