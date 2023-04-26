import pygame
from space_ship import SpaceShip
from ship_clue import ShipClue
from hostile_ship import HostileShip 
from weapon_bullet import WeaponBullet
from const import *
MAX_NUM_OF_WEAPON:int = 5

class BattleController():
    
    def __init__(self,space_ship:SpaceShip,ship_clue:ShipClue,hostile_ship:HostileShip,weapon_bullet:list[WeaponBullet]) -> None:
        self.space_ship = space_ship
        self.ship_clue = ship_clue
        self.hostile_ship = hostile_ship
        self.weapon_bullet = weapon_bullet

    def damage_deal(self) -> None:
        hit_bullets_idxs = self.hit_judge()
        for i in range(0,len(hit_bullets_idxs)):
            if hit_bullets_idxs[i]:
                for j in hit_bullets_idxs[i]:
                    hostile_damage = self.calc_deal_damage()
                    self.reduce_hostile_hp(hostile_damage)
                    self.weapon_bullet[i].bullet_flag[j] = False
                    self.weapon_bullet[i].reset_bullet(j)
        self.destroy_hostile_ship()

        # taken_bullets_idxs = self.hit_judge()
        # for i in range(0,len(taken_bullets_idxs)):
        #     if taken_bullets_idxs[i]:
        #         ship_damage = self.calc_taken_damage()
        #         self.reduce_ship_hp(ship_damage)

    def hit_judge(self) -> None:
        if self.hostile_ship.rect == None or self.weapon_bullet[0].hitbox_rects == None :
            return
        collide_index_lists = [self.hostile_ship.rect.collidelistall(self.weapon_bullet[i].hitbox_rects[:]) for i in range(0,MAX_NUM_OF_WEAPON)]
        # print(collide_index_lists)
        return collide_index_lists
        
    def calc_deal_damage(self):
        return 1
        
    def calc_taken_damage(self):
        return 1
        
    def reduce_hostile_hp(self,damage:float) -> None:
        print(self.hostile_ship.hp)
        self.hostile_ship.hp = self.hostile_ship.hp - damage
    
    def reduce_ship_hp(self,damage:float) -> None:
        self.space_ship.hp = self.space_ship.hp - damage
    
    def destroy_hostile_ship(self):
        if self.hostile_ship.hp < 0:
            self.hostile_ship.status = HOSTILE_STAT.DESTROYED