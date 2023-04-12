import pygame
import sys
from space_ship import SpaceShip
from ship_clue import ShipClue
from ship_weapon import ShipWeapon
from weapon_bullet import WeaponBullet
from pygame.locals import *
MAX_NUM_OF_WEAPON = 5

def main():

    # 初期設定
    pygame.init()
    pygame.display.set_caption('Space Shipy')
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((750, 1000))
    SCREEN = screen.get_rect()
    SCREEN_CENTER = SCREEN.center


    

    # 登場する人/物/背景の作成
    circ_sur = pygame.Surface((20, 20))
    circ_sur.set_colorkey((0, 0, 0))
    circ_rect = circ_sur.get_rect()
    circ_rect.topleft = (300, 100)
    dx, dy = 5, 4
    pygame.draw.circle(circ_sur, (255, 255, 255), (10, 10), 10)
    rect_sur = pygame.Surface((100, 60))
    pygame.draw.rect(rect_sur, (255, 0, 0), (0, 0, 100, 60))
    
    # 船作成
    space_ship = SpaceShip()
    space_ship.create()    
    
    # 船員作成
    ship_clue = ShipClue()
    ship_clue.create()

    # 武器作成
    ship_weapon = [ShipWeapon(space_ship,pos_id=i) for i in range(0,MAX_NUM_OF_WEAPON)]
    [ship_weapon[i].create() for i in range(0,MAX_NUM_OF_WEAPON)]
    [ship_weapon[i].weapon_sight() for i in range(0,MAX_NUM_OF_WEAPON)]

    # 弾丸作成
    weapon_bullet = [WeaponBullet(ship_weapon=ship_weapon[i]) for i in range(0,MAX_NUM_OF_WEAPON)]
    [weapon_bullet[i].create() for i in range(0,MAX_NUM_OF_WEAPON)]
 
    SHIP_RECT = space_ship.sur.get_rect()  
    fpscounter = 0
    while True:
        fpscounter = (fpscounter + 1) % 60  
        print(fpscounter)
        # 画面(screen)をクリア
        screen.fill((0, 0, 0))

        # ゲームに登場する人/物/背景の位置Update
        circ_rect.move_ip(dx, dy)
        if circ_rect.left < SCREEN.left or circ_rect.right > SCREEN.right:
            dx = -dx
        if circ_rect.top < SCREEN.top or circ_rect.bottom > SCREEN.bottom:
            dy = -dy
        if (circ_rect.left < SCREEN.centerx + SHIP_RECT.centerx and circ_rect.right > SCREEN.centerx - SHIP_RECT.centerx) and (circ_rect.top < SCREEN.centery + SHIP_RECT.centery and circ_rect.bottom > SCREEN.centery - SHIP_RECT.centery): 
            dx = -dx            
        if (circ_rect.left < SCREEN.centerx + SHIP_RECT.centerx and circ_rect.right > SCREEN.centerx - SHIP_RECT.centerx) and (circ_rect.top < SCREEN.centery + SHIP_RECT.centery and circ_rect.bottom > SCREEN.centery - SHIP_RECT.centery): 
            dy = -dy            
        circ_rect.clamp_ip(SCREEN)

        # 画面(screen)上に登場する人/物/背景を描画
        screen.blit(circ_sur,circ_rect.topleft)
        space_center_pos = space_ship.sur.get_rect().center        
        space_ship.show(screen)
        screen.blit(ship_clue.sur,(100,200))
        [ship_weapon[i].show(screen,space_ship.sur.get_rect().center,space_ship.weapon_pos[i]) for i in range(0,MAX_NUM_OF_WEAPON)]
        [screen.blit(ship_weapon[i].sight_sur,(SCREEN_CENTER[0] + space_ship.weapon_pos[i][0] - space_center_pos[0] - ship_weapon[i].sight_sur.get_rect().center[0],SCREEN_CENTER[1] + space_ship.weapon_pos[i][1] - space_center_pos[1] - ship_weapon[i].sight_sur.get_rect().center[1])) for i in range(0,MAX_NUM_OF_WEAPON)]

    # ---------------bullet--------------------------------------------------     
        [weapon_bullet[i].set(time=fpscounter) for i in range(0,MAX_NUM_OF_WEAPON)]
        [weapon_bullet[i].move(screen) for i in range(0,MAX_NUM_OF_WEAPON)]      
    # ---------------bullet--------------------------------------------------        
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