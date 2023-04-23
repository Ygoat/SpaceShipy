import pygame
from space_ship import SpaceShip
from ship_clue import ShipClue
from hostile_ship import HostileShip 
from weapon_bullet import WeaponBullet

class BattleController():
    
    def __init__(self,space_ship:SpaceShip,ship_clue:ShipClue,hostile_ship:HostileShip,weapon_bullet:list[WeaponBullet]) -> None:
        self.space_ship = space_ship
        self.ship_clue = ship_clue
        self.hostile_ship = hostile_ship
        self.weapon_bullet = weapon_bullet
        
    def hit_judge(self):
        if self.hostile_ship.rect == None or self.weapon_bullet[0].hitbox_rects == None :
            return
        self.hostile_ship.rect.collidelistall(self.weapon_bullet[0].hitbox_rects[:])
        print('0:',self.hostile_ship.rect.collidelistall(self.weapon_bullet[0].hitbox_rects[:]))
        print('1:',self.hostile_ship.rect.collidelistall(self.weapon_bullet[1].hitbox_rects[:]))
        print('2:',self.hostile_ship.rect.collidelistall(self.weapon_bullet[2].hitbox_rects[:]))
        print('3:',self.hostile_ship.rect.collidelistall(self.weapon_bullet[3].hitbox_rects[:]))
        print('4:',self.hostile_ship.rect.collidelistall(self.weapon_bullet[4].hitbox_rects[:]))