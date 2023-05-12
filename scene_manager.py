from const import *
from enum import Enum

class SceneManager():
    scene = SCENE.TOP
    @staticmethod
    def scene_change(scene_enum:Enum):
        SceneManager.scene = scene_enum