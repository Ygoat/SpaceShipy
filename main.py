import pygame
import sys
from space_ship import SpaceShip
from ship_clue import ShipClue
from ship_weapon import ShipWeapon
from pygame.locals import *

def main():

    # 初期設定
    pygame.init()
    screen = pygame.display.set_mode((700, 1000))
    SCREEN = screen.get_rect()
    pygame.display.set_caption('Space Shipy')
    clock = pygame.time.Clock()

    space_ship = SpaceShip()
    ship_clue = ShipClue()
    ship_weapon = ShipWeapon(space_ship)

    # 登場する人/物/背景の作成
    circ_sur = pygame.Surface((20, 20))
    circ_sur.set_colorkey((0, 0, 0))
    circ_rect = circ_sur.get_rect()
    circ_rect.topleft = (300, 150)
    dx, dy = 5, 4
    pygame.draw.circle(circ_sur, (255, 255, 255), (10, 10), 10)
    rect_sur = pygame.Surface((100, 60))
    pygame.draw.rect(rect_sur, (255, 0, 0), (0, 0, 100, 60))

    ship_clue.create()
    space_ship.create()
    ship_weapon.create()
    ship_weapon.weapon_sight()

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
        screen.blit(circ_sur,circ_rect.topleft)
        space_center_pos = space_ship.sur.get_rect().center        
        screen.blit(space_ship.sur,(350 - space_center_pos[0],500 - space_center_pos[1]))
        screen.blit(ship_clue.sur,(100,200))
        screen.blit(ship_weapon.sur,(350 - space_center_pos[0],500 - space_center_pos[1]))
        screen.blit(ship_weapon.sight_sur,(350 - space_center_pos[0],500 - space_center_pos[1]))
        
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