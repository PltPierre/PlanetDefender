from player import Player


# class game
class Game:

    def __init__(self, screen):
        self.player = Player(screen)
        self.pressed = {}
