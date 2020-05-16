import pygame as pg
from enum import Enum
import constants as c

class Zombie(pg.sprite.Sprite):
    def __init__(self, x, y, name, health, damage=1):
        pg.sprite.Sprite.__init__(self)
        self.name = name
        self.health = health
        self.damage = damage
        self.posX=x
        self.posY=y
        self.dead = False
        self.losHead = False
        self.helmet = False
        self.speed = 1
        self.walk_timer = 0
        self.freeze_timer = 0
        self.state = c.WALK
        self.ice_rate

    def handleState(self):
        if self.state == c.WALK:
            self.walking()
        elif self.state == c.ATTACK:
            self.attacking()
        elif self.state == c.DIE:
            self.dying()
        elif self.state == c.FREEZE:
            self.freezing()

    def walking(self):
        if self.health <= 0:
            self.state = c.DIE
        elif self.health <= c.LOSTHEAD_HEALTH and not self.losHead:
            self.setLostHead()
        elif self.health <= c.NORMAL_HEALTH and self.helmet:
            self.helmet = False

        self.posX-=self.speed*self.ice_rate

    def attacking(self):
        if self.health <= 0:
            self.setDie()
        elif self.health <= c.LOSTHEAD_HEALTH and not self.losHead:
            self.changeFrames(self.losthead_attack_frames)
            self.setLostHead()
        elif self.health <= c.NORMAL_HEALTH and self.helmet:
            self.changeFrames(self.attack_frames)
            self.helmet = False

        if self.prey.health <= 0:
            self.prey = None
            self.setWalk()

    def dying(self):
        pass

    def freezing(self):
        if self.health <= 0:
            self.setDie()
        elif self.health <= c.LOSTHEAD_HEALTH and not self.losHead:
            if self.old_state == c.WALK:
                self.changeFrames(self.losthead_walk_frames)
            else:
                self.changeFrames(self.losthead_attack_frames)
            self.setLostHead()
        if (self.current_time - self.freeze_timer) > c.FREEZE_TIME:
            self.setWalk()

    def setLostHead(self):
        self.losHead = True
        if self.head_group is not None:
            self.head_group.add(ZombieHead(self.rect.centerx, self.rect.bottom))

    def setDamage(self, damage, ice=False):
        self.health -= damage
        if ice:
            self.freeze_timer=0


    def setWalk(self):
        self.state = c.WALK
        self.animate_interval = 150

        if self.helmet:
            self.changeFrames(self.helmet_walk_frames)
        elif self.losHead:
            self.changeFrames(self.losthead_walk_frames)
        else:
            self.changeFrames(self.walk_frames)

    def setAttack(self, prey, is_plant=True):
        self.prey = prey  # prey can be plant or other zombies
        self.prey_is_plant = is_plant
        self.state = c.ATTACK
        self.attack_timer = self.current_time
        self.animate_interval = 100



    def setBoomDie(self):
        self.state = c.DIE
        self.animate_interval = 200


    def setFreeze(self, ice_trap_image):
        self.state = c.FREEZE
        self.freeze_timer = self.current_time



