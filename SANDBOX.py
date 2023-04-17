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
    
    screen = pygame.display.set_mode((400, 400))
    SCREEN = screen.get_rect()
    
    # rec = pygame.Rect(0,0,100,100)
    rec1 = pygame.Surface((100,100))
    rec2 = pygame.Surface((50,50))
    rec3 = pygame.Surface((100,100))
    # pygame.Surface.blit(re)
    drawrec1 = pygame.draw.rect(rec1,(255,0,0),(0,0,100,100))
    drawrec2 = pygame.draw.rect(rec2,(0,255,0),(0,0,50,50))
    drawrec3 = pygame.draw.rect(rec3,(0,0,255),(0,0,100,100))

    fpscounter:int = 0
    set_timer:int = 0
    while True:
        fpscounter = (fpscounter + 1) % 60
        set_timer = (set_timer + 1) % 600 #キャラ移動用のテストタイマー
        
        # 画面(screen)をクリア
        screen.fill((0, 0, 0))

        drawrec1.move_ip(1,1)
        drawrec1.clamp_ip(screen.get_rect())
        drawrec2.move_ip(5,5)
        drawrec2.clamp_ip(screen.get_rect())
        drawrec3.move_ip(3,3)
        drawrec3.clamp_ip(screen.get_rect())
        screen.blit(rec1,drawrec1.topleft)
        screen.blit(rec2,drawrec2.topleft)
        screen.blit(rec3,drawrec3.topleft)
        # screen.blit(rec2,(300,300))
        print(drawrec1.collidelistall([drawrec2,drawrec3]))
        # ゲームに登場する人/物/背景の位置Update

        
        
        # 画面(screen)の実表示
        pygame.display.update()

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 描画スピードの調整（FPS)
        clock.tick(30)
        # print(clock.get_fps())
        
if __name__ == "__main__":
    main()