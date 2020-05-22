import pygame
from ammo import Ammo
from enemy import Enemy
from ammo_enemy import AmmoEnemy as Ae


# Class Player
class Player(pygame.sprite.Sprite):

    attack = None
    velocity = None
    score = None
    max_health = None
    vie_level = None
    vitesse_level = None
    degats_level = None
    bonus_level = None
    bonus_level_left = None
    NumSkin = None
    OwnedSkin = []

    def __init__(self, screen):
        super().__init__()
        self.health = Player.max_health
        self.all_ammo = pygame.sprite.Group()
        self.image = pygame.image.load("images/player/RainbowSkin.png")
        self.image = pygame.transform.scale(self.image, (int(screen.get_width()/15), int(screen.get_width()/15)))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = screen.get_height() - screen.get_height()*0.12

    def fire_ammo(self):
        self.all_ammo.add(Ammo(self))

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    @staticmethod
    def gain_score(score):
        Player.score += score

    def collision_ammo(self, ammo):
        if self.rect.x <= Ae.getX(ammo) <= self.rect.x + self.rect.width and self.rect.y <= Ae.getY(ammo) <= self.rect.y + self.rect.height:
            return True
        return False

    def damage(self):
        self.health -= Enemy.G_attack()

# Setter ------------------
    def set_health(self, health):
        self.health = health

    @staticmethod
    def set_max_health(health):
        Player.max_health = health

    @staticmethod
    def set_attack(attack):
        Player.attack = attack

    @staticmethod
    def set_velocity(v):
        Player.velocity = v

    @staticmethod
    def set_score(s):
        Player.score = s

    @staticmethod
    def set_vie_level(vielvl):
        Player.vie_level = vielvl

    @staticmethod
    def set_vitesse_level(vitlvl):
        Player.vitesse_level = vitlvl

    @staticmethod
    def set_degat_level(deglvl):
        Player.degats_level = deglvl

    @staticmethod
    def set_bonus_lvl(blvl):
        Player.bonus_level = blvl

    @staticmethod
    def set_bonus_lvl_left(blvlleft):
        Player.bonus_level_left = blvlleft

    @staticmethod
    def set_NumSkin(nskin):
        Player.NumSkin = nskin

    @staticmethod
    def appendOwnedSkin(num):
        if 1 <= num <= 5 and num not in Player.OwnedSkin:
            Player.OwnedSkin.append(num)

    def set_skin(self):
        if Player.NumSkin == 1:
            self.image = pygame.image.load("images/player/GreenSkin.png")
        elif Player.NumSkin == 2:
            self.image = pygame.image.load("images/player/RedSkin.png")
        elif Player.NumSkin == 3:
            self.image = pygame.image.load("images/player/BlueSkin.png")
        elif Player.NumSkin == 4:
            self.image = pygame.image.load("images/player/YellowSkin.png")
        elif Player.NumSkin == 5:
            self.image = pygame.image.load("images/player/RainbowSkin.png")
# -------------------------

# Getter ------------------
    def get_y(self):
        return self.rect.y

    @staticmethod
    def get_NumSkin():
        return Player.NumSkin

    @staticmethod
    def get_score():
        return Player.score

    def get_health(self):
        return self.health

    @staticmethod
    def get_max_health():
        return Player.max_health

    @staticmethod
    def get_attack():
        return Player.attack

    @staticmethod
    def get_velocity():
        return Player.velocity

    @staticmethod
    def get_vie_level():
        return Player.vie_level

    @staticmethod
    def get_vitesse_level():
        return Player.vitesse_level

    @staticmethod
    def get_degat_level():
        return Player.degats_level

    @staticmethod
    def get_bonus_lvl():
        return Player.bonus_level

    @staticmethod
    def get_bonus_lvl_left():
        return Player.bonus_level_left

# -------------------------

    def start_health(self):
        self.health = Player.max_health
