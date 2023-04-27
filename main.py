import pygame
import sys
from space_ship import SpaceShip
from ship_clue import ShipClue
from ship_weapon import ShipWeapon
from weapon_bullet import WeaponBullet
from hostile_ship import HostileShip
from battle_controller import BattleController
from masterdata_import import MasterImport
from scene_manager import SceneManager
from pygame.locals import *
from top_menu import Topmenu
from const import *
MAX_NUM_OF_WEAPON:int = 5
MAX_NUM_OF_CLUE:int = 3

def main() -> None:

    # 初期設定 
    pygame.init()
    pygame.display.set_caption('Space Shipy')
    clock = pygame.time.Clock() #FPS
    screen = pygame.display.set_mode((750, 950)) #描写スクリーン

    # マスターデータインポート
    bullets_params = MasterImport.csv_import("bullets")
    clues_params = MasterImport.csv_import("clues")
    hostiles_params = MasterImport.csv_import("hostiles")
    ships_params = MasterImport.csv_import("ships")
    weapons_params = MasterImport.csv_import("weapons")
    
    # 登場する人/物/背景の作成
    # 船作成
    space_ship = SpaceShip(screen)
    ship_weapon = [ShipWeapon(screen,space_ship,pos_id=i,weapon_id=i) for i in range(0,MAX_NUM_OF_WEAPON)]
    # 弾丸作成　!!!!bullet_idは画面から選択させる予定!!!!
    weapon_bullet = [WeaponBullet(screen,ship_weapon=ship_weapon[i],bullet_id=i) for i in range(0,MAX_NUM_OF_WEAPON)]
    # 船員作成
    clue_color_list = [COLOR.BLUE,COLOR.YELLOW,COLOR.GRAY]
    ship_clue = [ShipClue(space_ship,ship_weapon,clue_color_list[i],clue_id=i) for i in range(0,MAX_NUM_OF_CLUE)]
    # 敵船作成
    hostile_ship = HostileShip(screen,weapon_bullet)
    # バトルコントローラー作成
    battle_controller = BattleController(space_ship,ship_clue,hostile_ship,weapon_bullet)
    
    # シーン作成
    top_menu = Topmenu(screen)
    
    # シーン切換えテスト
    SceneManager.scene_change(SCENE.TOP)
    print(SceneManager.scene)
    print(SceneManager.scene == SCENE.BATTLE)
    
    # FPSカウンター（経過時間取得用）
    fpscounter:int = 0
    set_timer:int = 0
    while True:
        fpscounter = (fpscounter + 1) % 60
        set_timer = (set_timer + 1) % 600 #キャラ移動用のテストタイマー
        
        # 画面(screen)をクリア
        screen.fill((0, 0, 0))
        
        match SceneManager.scene:
            case SCENE.TOP: #トップ画面
                top_menu.show(screen)
                if  set_timer ==500:
                    SceneManager.scene = SCENE.BATTLE # 検証用に時間経過で画面が切り替わるように
        
            case SCENE.BATTLE: #バトル画面
                # ゲームに登場する人/物/背景の位置Update
                # 画面(screen)上に登場する人/物/背景を描画
                space_ship.show(screen)
                if hostile_ship.status != HOSTILE_STAT.DESTROYED:
                    hostile_ship.move()
                [ship_weapon[i].show(screen) for i in range(0,MAX_NUM_OF_WEAPON)]
                [ship_weapon[i].show_weapon_sight(screen,space_ship.sur.get_rect().center,space_ship.weapon_pos[i]) for i in range(0,MAX_NUM_OF_WEAPON)]
                # !!!!乗組員は武装に向かって移動するように変更予定!!!!
                [ship_clue[i].move(screen,fpscounter,set_timer,(hostile_ship.grobal_position_x_center,hostile_ship.grobal_position_y_center)) for i in range(0,MAX_NUM_OF_CLUE)]
                # 宇宙船上の画面をクリア
                space_ship.sur.fill((0,255,0))
                [ship_clue[i].show() for i in range(0,MAX_NUM_OF_CLUE)]        
                [weapon_bullet[i].shot(screen,fpscounter) for i in range(0,MAX_NUM_OF_WEAPON)]
                battle_controller.damage_deal()
            
            # 画面(screen)の実表示
        pygame.display.update()

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 描画スピードの調整（FPS)
        clock.tick(120)
        # print(clock.get_fps())
        
if __name__ == "__main__":
    main()