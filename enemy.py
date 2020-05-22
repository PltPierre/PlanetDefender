import pygame
from ammo import Ammo as a
from ammo_enemy import AmmoEnemy


class Enemy(pygame.sprite.Sprite):

    nbEnemy = 0
    health = None
    attack = None
    velocity = None
    freq_tir = None

    def __init__(self, screen):
        super().__init__()
        self.all_ammo_enemy = pygame.sprite.Group()
        self.all_enemies = pygame.sprite.Group()
        self.image = pygame.image.load("images/enemy/Alien1.png")
        self.image = pygame.transform.scale(self.image, (int(screen.get_width()/15), int((screen.get_width()/15)*0.8)))
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 100

    def list_enemy(self, screen):
        self.all_enemies.add(Enemy(screen))

    def init_placement(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def move(self):
        self.rect.x += self.velocity

        if self.rect.right >= 990 or self.rect.left <= 10:
            self.reverse()
            self.rect.y += 50

    def reverse(self):
        self.velocity *= -1

    def delete(self):
        self.remove()

    def collision_ammo(self, ammo):
        if self.rect.x <= a.getX(ammo) <= self.rect.x + self.rect.width and self.rect.y <= a.getY(ammo) <= self.rect.y + self.rect.height:
            return True
        return False

    def collision_player(self, player):
        if self.rect.y + self.rect.height >= player.get_y():
            return True
        return False

    def damage(self, player):
        self.health -= player.get_attack()

    def fire_ammo(self):
        self.all_ammo_enemy.add(AmmoEnemy(self))

# Fonctions NbEnemy -------------
    @staticmethod
    def PEnemy():
        Enemy.nbEnemy += 1

    @staticmethod
    def MEnemy():
        Enemy.nbEnemy -= 1

# -------------------------------

# Setter ------------------------

    @staticmethod
    def set_health(health):
        Enemy.health = health

    @staticmethod
    def set_attack(attack):
        Enemy.attack = attack

    @staticmethod
    def set_velocity(v):
        Enemy.velocity = v

    @staticmethod
    def set_freq_tir(ft):
        Enemy.freq_tir = ft

# -------------------------------

# Getter ------------------------
    @staticmethod
    def G_health():
        return Enemy.health

    @staticmethod
    def G_attack():
        return Enemy.attack

    @staticmethod
    def G_velocity():
        return Enemy.velocity

    @staticmethod
    def G_fre_tir():
        return Enemy.freq_tir

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def getV(self):
        return self.velocity

# -------------------------------
