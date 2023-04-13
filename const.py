from enum import Enum
class WEAPON_STAT(Enum):
    # 武器使用ステータス
    UNUSED = 0
    USING = 1
    # リロードステータス
    FULL = 0
    RELOAD = 1
    RELOADING = 2