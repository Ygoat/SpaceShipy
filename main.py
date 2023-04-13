import pygame
import sys
from space_ship import SpaceShip
from ship_clue import ShipClue
from ship_weapon import ShipWeapon
from weapon_bullet import WeaponBullet
from hostile_ship import HostileShip
from pygame.locals import *
MAX_NUM_OF_WEAPON:int = 5

def main() -> None:

    # 初期設定
    pygame.init()
    pygame.display.set_caption('Space Shipy')
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((750, 1000))
    SCREEN = screen.get_rect()

    # 登場する人/物/背景の作成
    # 船作成
    space_ship = SpaceShip(screen)
    # 武器作成 !!!!weapon_idは画面から選択させる予定!!!!
    ship_weapon = [ShipWeapon(space_ship,pos_id=i,weapon_id=i) for i in range(0,MAX_NUM_OF_WEAPON)]
    # 弾丸作成　!!!!bullet_idは画面から選択させる予定!!!!
    weapon_bullet = [WeaponBullet(ship_weapon=ship_weapon[i],bullet_id=i) for i in range(0,MAX_NUM_OF_WEAPON)]
    # 船員作成
    ship_clue = ShipClue(space_ship,ship_weapon)
    # 敵船作成
    hostile_ship = HostileShip(weapon_bullet)
    
    # FPSカウンター（経過時間取得用）
    fpscounter:int = 0
    set_timer:int = 0
    while True:
        fpscounter = (fpscounter + 1) % 60
        set_timer = (set_timer + 1) % 600 #キャラ移動用のテストタイマー
        
        # 画面(screen)をクリア
        screen.fill((0, 0, 0))

        # ゲームに登場する人/物/背景の位置Update
        # 画面(screen)上に登場する人/物/背景を描画
        space_ship.show(screen)
        hostile_ship.move(screen)
        [ship_weapon[i].show(screen,space_ship.sur.get_rect().center,space_ship.weapon_pos[i]) for i in range(0,MAX_NUM_OF_WEAPON)]
        [ship_weapon[i].show_weapon_sight(screen,space_ship.sur.get_rect().center,space_ship.weapon_pos[i]) for i in range(0,MAX_NUM_OF_WEAPON)]
        # !!!!弾丸発射は乗組員が兵器を操作している時だけ発射するように変更予定!!!!
        [weapon_bullet[i].set(time=fpscounter) for i in range(0,MAX_NUM_OF_WEAPON)]
        [weapon_bullet[i].move(screen) for i in range(0,MAX_NUM_OF_WEAPON)]
        # !!!!乗組員は武装に向かって移動するように変更予定!!!!
        ship_clue.move(screen,fpscounter,set_timer)

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