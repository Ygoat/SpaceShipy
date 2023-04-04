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
    circ_sur = pygame.Surface((20,20))
    circ_sur.set_colorkey((0,0,0))
    circ_rect = circ_sur.get_rect()
    dx,dy=5,5
    circ_rect.move_ip(300,150) #座標を上書き
    pygame.draw.circle(circ_sur,(255,255,255),(10,10),10)
    rect_sur = pygame.Surface((100,60))
    pygame.draw.rect(rect_sur,(255,0,0),(0,0,100,60))
    line_sur = pygame.Surface((100,50))
    line_sur.set_colorkey((0,0,0)) #透過色の設定
    pygame.draw.line(line_sur,(0,255,0),(0,0),(100,50))
    
    while True:
        # 画面をクリア
        screen.fill((0,100,100))
        # 背景・物のアップデート
        pressed_key = pygame.key.get_pressed() #キー入力をすべて受け取る

        if pressed_key[K_LEFT]:
            circ_rect.move_ip(-dx,0)
        if pressed_key[K_RIGHT]:
            circ_rect.move_ip(dx,0)
        if pressed_key[K_UP]:
            circ_rect.move_ip(0,-dy)
        if pressed_key[K_DOWN]:
            circ_rect.move_ip(0,dy)
        circ_rect.collidedict(circ_rect)

        circ_rect.clamp_ip(screen.get_rect())
        # 画面上に登場する背景・物を描画
        screen.blit(circ_sur,circ_rect)
        screen.blit(rect_sur,(150,150))
        screen.blit(line_sur,(250,250))
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
    
    def __init__(self, shpae:list, weapon_place:list, speed:float, attack:float, defence:float, special_id:int, level_max:int, surface:pygame.Surface):
        self.shape = shpae
        self.weapon_place = weapon_place
        self.speed = speed
        self.attack = attack
        self.defence = defence
        self.special_id = special_id
        self.level_max = level_max
        self.level_now = 0
        
    def draw_ship(self):
        pygame.draw.rect()

    # @classmethod
    def move_ship(self):
        return 0


        
if __name__ == '__main__':
    main()

