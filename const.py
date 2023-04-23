from enum import Enum
class WEAPON_STAT(Enum):
    # 武器使用ステータス
    UNUSED = 0
    USING = 1
    # リロードステータス
    FULL = 0
    RELOAD = 1
    RELOADING = 2
    
class CLUE_STAT(Enum):
    STAY = 0
    MOVING = 1
    HEALING = 2
    RESTING = 3
    REPARING = 4

class COLOR():
    # RGBカラーコード
    RED = (255,0,0)
    ORANGE = (255,128,0)
    YELLOW = (255,255,0)
    LIGHTGREEN = (128,255,0)
    GREEN = (0,255,0)
    LIGHTBLUE = (0,255,255)
    BLUE = (0,0,255)
    PURPLE = (128,0,255)
    PINK = (255,0,255)
    GRAY = (128,128,128)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
