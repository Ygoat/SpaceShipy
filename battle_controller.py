import pygame
from space_ship import SpaceShip
from ship_clue import ShipClue
from hostile_ship import HostileShip 
from weapon_bullet import WeaponBullet

class BattleController():
    
    def __init__(self,space_ship:SpaceShip,ship_clue:ShipClue,hostile_ship:HostileShip,weapon_bullet:WeaponBullet) -> None:
        self.space_ship = space_ship
        self.ship_clue = ship_clue
        self.hostile_ship = hostile_ship
        self.weapon_bullet = weapon_bullet
        
    def hit_judge(self):
        if self.hostile_ship.rect == None or self.weapon_bullet.rect == None :
            return
        pygame.Rect.collidedict
        self.hostile_ship.rect.colliderect(self.weapon_bullet.rect)
        print(self.hostile_ship.rect.colliderect(self.weapon_bullet.rect))