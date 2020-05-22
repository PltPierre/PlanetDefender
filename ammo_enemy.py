import pygame


# class ammo
class AmmoEnemy(pygame.sprite.Sprite):
    velocity = 10

    def __init__(self, e):
        super().__init__()
        self.enemy = e
        self.image = pygame.image.load("images/ammo/ennemyAmmo.png")
        self.image = pygame.transform.scale(self.image, (12, 23))
        self.rect = self.image.get_rect()
        self.rect.x = e.rect.x + e.image.get_width()/2 - self.image.get_width()/2
        self.rect.y = e.rect.y

    def move(self):
        self.rect.y += AmmoEnemy.velocity

        # verify if ammo is on screen
        if self.rect.y < 1000:
            # delete the ammo
            self.remove()

    def delete(self):
        self.remove()

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y

    @staticmethod
    def set_velocity(v):
        AmmoEnemy.velocity = v

    @staticmethod
    def get_velocity():
        return AmmoEnemy.velocity
