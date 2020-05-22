import pygame


# class ammo
class Ammo(pygame.sprite.Sprite):
    velocity = None

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.image = pygame.image.load("images/ammo/ammo1.png")
        self.image = pygame.transform.scale(self.image, (12, 23))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.image.get_width()/2 - self.image.get_width()/2
        self.rect.y = player.rect.y - 10

    def move(self):
        self.rect.y -= Ammo.velocity

        # verify if ammo is on screen
        if self.rect.y < 0:
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
        Ammo.velocity = v

    @staticmethod
    def get_velocity():
        return Ammo.velocity
