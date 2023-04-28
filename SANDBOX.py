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
import math
from enum import Enum
MAX_NUM_OF_WEAPON:int = 5
MAX_NUM_OF_CLUE:int = 3

class cons():
    class con(Enum):
        RED = 1
class a():
    def __init__(self) -> None:
        self.name = "aa"
        self.a = self.getA
        
    def getA(self):
        return self.name[0] 
        

def main() -> None:
    
    b={'a':1,'b':2}
    print(len(b))
    
    print(cons.con.RED)
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
    rec4 = pygame.Surface((100,100))
    minirec = pygame.Surface((30,30))
    
    # pygame.Surface.blit(re)
    drawrec1 = pygame.draw.rect(rec1,(255,0,0),(0,0,100,100))
    drawrec1.clamp_ip(screen.get_rect())
    drawrec1.move_ip(100,100)
    drawrec2 = pygame.draw.rect(rec2,(0,255,0),(0,0,50,50))
    drawrec3 = pygame.draw.rect(rec3,(0,0,255),(0,0,100,100))
    drawrec4 = pygame.draw.line(rec4,(0,0,255),(0,0),(100,100))
    drawminirec1 = pygame.draw.rect(minirec,(0,0,255),(0,0,30,30))
    drawminirec1.clamp_ip(rec1.get_rect())
    drawminirec2 = pygame.draw.rect(minirec,(0,0,255),(0,0,30,30))
    drawminirec2.clamp_ip(rec1.get_rect())

    for i in range(-180,180):
        print(f'{i}:',sigmoid_function(i,1,0.1))
    
    fpscounter:int = 0
    set_timer:int = 0
    while True:
        fpscounter = (fpscounter + 1) % 60
        set_timer = (set_timer + 1) % 600 #キャラ移動用のテストタイマー
        
        # 画面(screen)をクリア
        screen.fill((0, 0, 0))



        drawrec1.move_ip(1,1)
        # print(drawrec1.topleft) #topleftがグローバル座標となる。

        drawrec2.move_ip(5,5)
        # drawrec2.clamp_ip(screen.get_rect())
        drawrec3.move_ip(3,3)
        # drawrec3.clamp_ip(screen.get_rect())
        drawrec4.move_ip(4,4)
        # drawrec4.clamp_ip(screen.get_rect())
        drawminirec1.move_ip(1,1)
        drawminirec1.clamp_ip(rec1.get_rect())
        drawminirec2.move_ip(1,1)


        screen.blit(rec1,drawrec1.topleft)
        screen.blit(rec2,drawrec2.topleft)
        screen.blit(rec3,drawrec3.topleft)
        # screen.blit(rec4,drawrec4.topleft)
        # screen.blit(rec2,(300,300))
        rec1.fill((255,0,0))        
        rec1.blit(minirec,drawminirec2.topleft)
        # print("before clamp:",drawminirec1.centerx)
        # print("after clamp:",drawminirec2.centerx)
        # print(drawrec1.collidelistall([drawrec2,drawrec3]))

        # ゲームに登場する人/物/背景の位置Update

        
        
        # 画面(screen)の実表示
        pygame.display.update()

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # マウスクリック時の動作
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                print("mouse clicked -> (" + str(x) + ", " + str(y) + ")")
                
            # マウスポインタが移動したときの動作
            if event.type == MOUSEMOTION:
                x, y = event.pos
                print("mouse moved   -> (" + str(x) + ", " + str(y) + ")")
                
                
        # 描画スピードの調整（FPS)
        clock.tick(30)
        # print(clock.get_fps())
        
def sigmoid_function(x,a=1,b=1000):
    # シグモイド関数
    if abs(x) < 0.000001:
        y = 0
    else:
        # y = (math.e**abs(x) - math.e**-abs(x))/(math.e**abs(x) + math.e**-abs(x))
        # y = abs(b*x)/(1+abs(b*x))
        y = 2*(1 / (1 + math.e**-abs(b*x)) - 0.5)
        # y =  (1 + math.e**-(1/b*abs(x-100)))-1/2
        # y = 1
    return y
        
if __name__ == "__main__":
    main()
    
    
    