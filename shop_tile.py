import pygame


class Shop:
    list_PosX = []
    list_PosY = []

    def __init__(self, x, y, imageurl, text='', back=True, textPrice='', locked=False):
        self.image = pygame.image.load(imageurl)
        self.x = x
        self.y = y
        self.text = text
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.back = back
        self.textPrice = textPrice
        self.locked = locked

    def draw(self, screen, outline=None):
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        screen.blit(self.image, (self.x, self.y))

        if self.text != '' and not self.back:
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, (255, 255, 255))
            screen.blit(text, (self.x + (self.width/2-text.get_width()/2), self.y + self.height + text.get_height()/2))
        if self.textPrice != '' and not self.back and not self.locked:
            font = pygame.font.SysFont('comicsans', 30)
            text2 = font.render(self.textPrice, 1, (255, 255, 255))
            screen.blit(text2, (self.x + (self.width/2-text2.get_width()/2), self.y + self.height + text2.get_height()/2 + 20))

    def isOver(self, pos):
        if (self.x - 50) < pos[0] < (self.x + self.width + 50):
            if (self.y - 50) < pos[1] < (self.y + self.height + 50):
                return True
        return False

    # animation fleches
    def fakeAnimationR(self, pos):
        if self.isOver(pos):
            self.image = pygame.image.load('images/shop/fakeAnimImgRA.png')
        else:
            self.image = pygame.image.load('images/shop/Rarrow.png')

    def fakeAnimationL(self, pos):
        if self.isOver(pos):
            self.image = pygame.image.load('images/shop/fakeAnimImgLA.png')
        else:
            self.image = pygame.image.load('images/shop/Larrow.png')

    # change image tiles
    def fakeAnTile(self, imgb, imgf):
        if self.back and not self.locked:
            self.image = pygame.image.load(imgb)
        elif not self.back and not self.locked:
            self.image = pygame.image.load(imgf)

    # renvoie la prochaine position des tiles en fonction de là ou ils sont et si on clique sur droite ou gauche
    def checkNextPos(self, reverse):
        if reverse:  # arrow left
            """========================================== CHECK X POSITION =========================================="""
            if self.x == Shop.list_PosX[0]:  # if tile 1 ==> tile 2
                x = Shop.list_PosX[1]
            elif self.x == Shop.list_PosX[1]:  # if tile 2 ==> tile 4
                x = Shop.list_PosX[3]
            elif self.x == Shop.list_PosX[3]:  # if tile 4 ==> tile 3
                x = Shop.list_PosX[2]
            elif self.x == Shop.list_PosX[2]:  # if tile 3 ==> tile 1
                x = Shop.list_PosX[0]

            """========================================== CHECK Y POSITION =========================================="""
            if self.y == Shop.list_PosY[0]:  # if tile 1 ==> tile 2
                y = Shop.list_PosY[1]
            elif self.y == Shop.list_PosY[1]:  # if tile 2 ==> tile 4
                y = Shop.list_PosY[3]
            elif self.y == Shop.list_PosY[3]:  # if tile 4 ==> tile 3
                y = Shop.list_PosY[2]
            elif self.y == Shop.list_PosY[2]:  # if tile 3 ==> tile 1
                y = Shop.list_PosY[0]
        else:  # arrow right
            """========================================== CHECK X POSITION =========================================="""
            if self.x == Shop.list_PosX[0]:  # if tile 1 ==> tile 3
                x = Shop.list_PosX[2]
            elif self.x == Shop.list_PosX[2]:  # if tile 3 ==> tile 4
                x = Shop.list_PosX[3]
            elif self.x == Shop.list_PosX[3]:  # if tile 4 ==> tile 2
                x = Shop.list_PosX[1]
            elif self.x == Shop.list_PosX[1]:  # if tile 2 ==> tile 1
                x = Shop.list_PosX[0]

            """========================================== CHECK Y POSITION =========================================="""
            if self.y == Shop.list_PosY[0]:  # if tile 1 ==> tile 3
                y = Shop.list_PosY[2]
            elif self.y == Shop.list_PosY[2]:  # if tile 3 ==> tile 4
                y = Shop.list_PosY[3]
            elif self.y == Shop.list_PosY[3]:  # if tile 4 ==> tile 2
                y = Shop.list_PosY[1]
            elif self.y == Shop.list_PosY[1]:  # if tile 2 ==> tile 1
                y = Shop.list_PosY[0]
        return [x, y]

    # bouge les tiles en fonction des positions données dans checkNextPos
    def move(self, reverse=False):
        List_Pos = self.checkNextPos(reverse)
        new_x_diff = List_Pos[0] - self.x
        new_y_diff = List_Pos[1] - self.y
        while new_x_diff != 0 or new_y_diff != 0:
            if new_x_diff < 0:
                self.x -= 1
                new_x_diff += 1
            elif new_x_diff > 0:
                self.x += 1
                new_x_diff -= 1

            if new_y_diff < 0:
                self.y -= 1
                new_y_diff += 1
            elif new_y_diff > 0:
                self.y += 1
                new_y_diff -= 1
