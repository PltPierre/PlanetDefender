"""
Projet : Space Invaders PPE

Date Dernière Modif : 04/03/2020

https://trello.com/b/iXXRGWiQ/ppe-planet-defender

"""

import pygame
import sys
from game import Game
from enemy import Enemy
from player import Player
from button import Button
from shop_tile import Shop
from ammo_enemy import AmmoEnemy
from ammo import Ammo
import random
import json

pygame.init()

# Polices de caractères ----------------------------------
font = pygame.font.SysFont("Times New Roman", 45)
font2 = pygame.font.SysFont("Times New Roman", 75)
# --------------------------------------------------------

# Résolution Fenêtre de jeu
screen_width = 1000
screen_heigth = 800
screen = pygame.display.set_mode((screen_width, screen_heigth))

# Titre Fenêtre
pygame.display.set_caption("Planet Defender")

# Icone Fenetre
programIcon = pygame.image.load('images/enemy/Alien1icon.png')
pygame.display.set_icon(programIcon)

# Charge image BackGround
background = pygame.transform.scale(pygame.image.load('images/background/backgroundplanetdefender.png'), (screen_width, screen_heigth))
back_title = pygame.transform.scale(pygame.image.load('images/background/backgroundtitle.png'), (screen_width - int(screen_width/5), int(screen_width/6)))

# Différent Textes ---------------------------------------------------------------------------------
game_over = font2.render("GAME OVER", True, (255, 255, 255))
wintxt = font2.render("YOU WIN", True, (255, 255, 255))
shop_txt = font.render("SHOP", True, (255, 255, 255))
# --------------------------------------------------------------------------------------------------


# Instance game
game = Game(screen)

# Instance Enemy
enemy = Enemy(screen)

# Defini le nombre d'énnemis (multiples de 10 de préference) 32 => 4 lignes
nb_enemy = 32
enemy_ready = False

# Positions Shop
imgtile = pygame.image.load('images/shop/shoptile.png')
arrow = pygame.image.load('images/shop/Rarrow.png')
list_TileX = [int((screen.get_width() / 2 - imgtile.get_width() / 2)),
              int((screen.get_width() / 4 - imgtile.get_width() / 2)),
              int(((3 * screen.get_width()) / 4 - imgtile.get_width() / 2)),
              int((screen.get_width() / 2 - imgtile.get_width() / 2 + 1))]
list_TileY = [int((screen.get_height() / 2 - imgtile.get_height() / 2 + 100)),
              int((screen.get_height() / 2 - imgtile.get_height() / 2)),
              int((screen.get_height() / 2 - imgtile.get_height() / 2 - 1)),
              int((screen.get_height() / 2 - imgtile.get_height() / 2 - 100))]

for i in list_TileX:
    Shop.list_PosX.append(i)
for i in list_TileY:
    Shop.list_PosY.append(i)

# Différent Boutons ---------------------------------------------------------------------------------
play_btn = Button((50, 50, 50), int(screen_width/2)-100, back_title.get_height()+100, 200, 75, 'Play')
shop_btn = Button((50, 50, 50), int(screen_width/2)-100, int(play_btn.getHeight() + screen_heigth/30), 200, 75, 'Shop')
reset_all_btn = Button((50, 50, 50), int(screen_width/2)-100, int(shop_btn.getHeight() + screen_heigth/30), 200, 75, 'Reset All')
quitter_btn = Button((50, 50, 50), int(screen_width/2)-100, int(reset_all_btn.getHeight() + screen_heigth/30), 200, 75, 'Quitter')

restart_btn = Button((50, 50, 50), 360, 300, 280, 100, 'Restart Game')
menu_button = Button((50, 50, 50), 360, 425, 280, 100, 'Menu')
quitter_GO_btn = Button((50, 50, 50), 360, 550, 280, 100, 'Quitter')

retour_btn = Button((50, 50, 50), 25, int(screen_heigth - screen_heigth*0.15), 200, 75, 'Retour')
SkinShop_btn = Button((50, 50, 50), int(screen_width - 25 - 200), int(screen_heigth - screen_heigth*0.15), 200, 75, 'Skins')

shop_tile1 = Shop(list_TileX[0], list_TileY[0], 'images/shop/ShopTileVit.png', 'Shop tile test', False)
shop_tile2 = Shop(list_TileX[1], list_TileY[1], 'images/shop/ShopTileDegBack.png', 'Shop tile 2')
shop_tile3 = Shop(list_TileX[2], list_TileY[2], 'images/shop/ShopTileVieBack.png', 'Shop tile 3')
shop_tile4 = Shop(list_TileX[3], list_TileY[3], 'images/shop/ShopTileBonusBack.png', 'Shop tile 4', True, '', True)
arrow_left = Shop((shop_tile1.x - 100), (screen.get_height() / 2 - arrow.get_height() / 2 + 100), 'images/shop/Larrow.png')
arrow_right = Shop((shop_tile1.x + shop_tile1.width + 100), (screen.get_height() / 2 - arrow.get_height() / 2 + 100), 'images/shop/Rarrow.png')
# ---------------------------------------------------------------------------------------------------

list_tile = [shop_tile1, shop_tile2, shop_tile3, shop_tile4]


def save_load(file):
    # Ouvre le fichier .json
    with open(file) as f:
        data = json.load(f)

    # Récupère et applique les données aux attributs statiques du joueur et des ennemis
    for d in data["game"]:
        Player.set_score(d["player"]["score"])
        Player.set_attack(d["player"]["attack"])
        Player.set_max_health(d["player"]["health"])
        Player.set_velocity(d["player"]["velocity"])
        Player.set_NumSkin(d["player"]["skin"])
        for n in d["player"]["OwnedSkin"]:
            Player.appendOwnedSkin(n)

        Player.set_bonus_lvl(d["upgrade"]["bonus"])
        Player.set_degat_level(d["upgrade"]["degats"])
        Player.set_vie_level(d["upgrade"]["vie"])
        Player.set_vitesse_level(d["upgrade"]["vitesse"])
        Player.set_bonus_lvl_left(d["upgrade"]["bonus_level_left"])

        Enemy.set_attack(d["enemy"]["attack"])
        Enemy.set_health(d["enemy"]["health"])
        Enemy.set_velocity(d["enemy"]["velocity"])
        Enemy.set_freq_tir(d["enemy"]["frequence_tir"])

        AmmoEnemy.set_velocity(d["ammo_enemy"]["velocity"])
        Ammo.set_velocity(d["ammo"]["velocity"])


def save_json(file):
    # Ouvre le fichier .json
    with open(file, 'r') as f:
        data = json.load(f)
    # Change les valeurs des clés des données
    for d in data['game']:
        d["player"]["score"] = Player.get_score()
        d["player"]["health"] = Player.get_max_health()
        d["player"]["attack"] = Player.get_attack()
        d["player"]["velocity"] = Player.get_velocity()
        d["player"]["skin"] = Player.get_NumSkin()
        for n in Player.OwnedSkin:
            if n not in d["player"]["OwnedSkin"]:
                d["player"]["OwnedSkin"].append(n)

        d["upgrade"]["bonus"] = Player.get_bonus_lvl()
        d["upgrade"]["degats"] = Player.get_degat_level()
        d["upgrade"]["vie"] = Player.get_vie_level()
        d["upgrade"]["vitesse"] = Player.get_vitesse_level()
        d["upgrade"]["bonus_level_left"] = Player.get_bonus_lvl_left()

        d["enemy"]["health"] = Enemy.G_health()
        d["enemy"]["attack"] = Enemy.G_attack()
        d["enemy"]["velocity"] = Enemy.G_velocity()
        d["enemy"]["frequence_tir"] = Enemy.G_fre_tir()

        d["ammo_enemy"]["velocity"] = AmmoEnemy.get_velocity()
        d["ammo"]["velocity"] = Ammo.get_velocity()

    # Modifie le fichier .json avec les données ci-dessus
    with open(file, 'w') as f:
        json.dump(data, f, indent=2)
    print('Save Complete')


def reset_all(file):
    # Ouvre le fichier .json
    with open(file, 'r') as f:
        data = json.load(f)
    # Change les valeurs des clés des données
    for d in data['game']:
        d["player"]["score"] = 0
        d["player"]["health"] = 2
        d["player"]["attack"] = 1
        d["player"]["velocity"] = 5
        d["player"]["skin"] = 1
        d["player"]["OwnedSkin"] = [1]

        d["upgrade"]["bonus"] = 1
        d["upgrade"]["degats"] = 1
        d["upgrade"]["vie"] = 1
        d["upgrade"]["vitesse"] = 1
        d["upgrade"]["bonus_level_left"] = 0

        d["enemy"]["health"] = 1
        d["enemy"]["attack"] = 1
        d["enemy"]["velocity"] = 2
        d["enemy"]["frequence_tir"] = 10

        d["ammo_enemy"]["velocity"] = 10
        d["ammo"]["velocity"] = 10

    # Modifie le fichier .json avec les données ci-dessus
    with open(file, 'w') as f:
        json.dump(data, f, indent=2)


def gameover():
    over = False

    while not over:
        # Affichage
        screen.fill((0, 0, 0))
        screen.blit(game_over, (280, 100))
        restart_btn.draw(screen)
        menu_button.draw(screen)
        quitter_GO_btn.draw(screen)
        # Evenements Touches
        for event in pygame.event.get():
            # Quitter
            if event.type == pygame.QUIT:
                sys.exit()
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                if restart_btn.isOver(pos):
                    restart_btn.color = (255, 50, 50)
                else:
                    restart_btn.color = (50, 50, 50)
                if menu_button.isOver(pos):
                    menu_button.color = (255, 50, 50)
                else:
                    menu_button.color = (50, 50, 50)
                if quitter_GO_btn.isOver(pos):
                    quitter_GO_btn.color = (255, 50, 50)
                else:
                    quitter_GO_btn.color = (50, 50, 50)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_btn.isOver(pos):
                    save_json('Saves/save.json')
                    gameLoop()
                    over = True
                if menu_button.isOver(pos):
                    save_json('Saves/save.json')
                    menu()
                    over = True
                if quitter_GO_btn.isOver(pos):
                    save_json('Saves/save.json')
                    sys.exit()
        pygame.display.flip()


def win():
    while True:
        # Affichage
        screen.fill((0, 0, 0))
        screen.blit(wintxt, (int((screen_width/2)-(wintxt.get_width()/2)), 100))
        restart_btn.draw(screen)
        menu_button.draw(screen)
        quitter_GO_btn.draw(screen)
        # Evenements Touches
        for event in pygame.event.get():
            # Quitter
            if event.type == pygame.QUIT:
                sys.exit()
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                if restart_btn.isOver(pos):
                    restart_btn.color = (255, 50, 50)
                else:
                    restart_btn.color = (50, 50, 50)
                if menu_button.isOver(pos):
                    menu_button.color = (255, 50, 50)
                else:
                    menu_button.color = (50, 50, 50)
                if quitter_GO_btn.isOver(pos):
                    quitter_GO_btn.color = (255, 50, 50)
                else:
                    quitter_GO_btn.color = (50, 50, 50)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_btn.isOver(pos):
                    save_json('Saves/save.json')
                    gameLoop()
                if menu_button.isOver(pos):
                    save_json('Saves/save.json')
                    menu()
                if quitter_GO_btn.isOver(pos):
                    save_json('Saves/save.json')
                    sys.exit()
        pygame.display.flip()


def Shop():
    shop = True
    while shop:
        screen.blit(background, (0, 0))
        screen.blit(shop_txt, (int(screen_width/2-shop_txt.get_width()/2), 10))
        score_text = font.render("Score : " + str(game.player.get_score()), True, (255, 255, 255))
        screen.blit(score_text, (10, -5))
        if Player.get_vitesse_level() >= 15:
            list_tile[0].locked = True
        if Player.get_degat_level() >= 15:
            list_tile[1].locked = True
        if Player.get_vie_level() >= 20:
            list_tile[2].locked = True
        if Player.get_bonus_lvl() >= 10:
            list_tile[3].locked = True
        elif Player.get_bonus_lvl_left() > 0:
            list_tile[3].locked = False

        if list_tile[0].locked:
            list_tile[0].image = pygame.image.load('images/shop/ShopTileVitBackLocked.png')
        if list_tile[1].locked:
            list_tile[1].image = pygame.image.load('images/shop/ShopTileDegBackLocked.png')
        if list_tile[2].locked:
            list_tile[2].image = pygame.image.load('images/shop/ShopTileVieBackLocked.png')
        if list_tile[3].locked:
            list_tile[3].image = pygame.image.load('images/shop/ShopTileBonusBackLocked.png')
        # Draw celui qui est devant en premier
        if not shop_tile1.back:
            shop_tile2.draw(screen)
            shop_tile3.draw(screen)
            shop_tile4.draw(screen)
            shop_tile1.draw(screen)
        elif not shop_tile2.back:
            shop_tile3.draw(screen)
            shop_tile4.draw(screen)
            shop_tile1.draw(screen)
            shop_tile2.draw(screen)
        elif not shop_tile3.back:
            shop_tile4.draw(screen)
            shop_tile1.draw(screen)
            shop_tile2.draw(screen)
            shop_tile3.draw(screen)
        elif not shop_tile4.back:
            shop_tile1.draw(screen)
            shop_tile2.draw(screen)
            shop_tile3.draw(screen)
            shop_tile4.draw(screen)
        # Change les textes
        list_tile[0].text = 'Vitesse Niveau  : ' + str(Player.get_vitesse_level())
        list_tile[1].text = 'Dégats Niveau  : ' + str(Player.get_degat_level())
        list_tile[2].text = 'Vie Niveau  : ' + str(Player.get_vie_level())
        list_tile[3].text = 'Bonus Niveau  : ' + str(Player.get_bonus_lvl())
        list_tile[0].textPrice = 'Prix  : ' + str(Player.get_vitesse_level() * 1000)
        list_tile[1].textPrice = 'Prix  : ' + str(Player.get_degat_level() * 2000)
        list_tile[2].textPrice = 'Prix  : ' + str(Player.get_vie_level() * 5000)
        list_tile[3].textPrice = 'Prix  : ' + str(Player.get_bonus_lvl() * 5000)
        arrow_left.draw(screen)
        arrow_right.draw(screen)
        retour_btn.draw(screen)
        SkinShop_btn.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retour_btn.isOver(pos):
                    save_json('Saves/save.json')
                    menu()
                if SkinShop_btn.isOver(pos):
                    save_json('Saves/save.json')
                    SkinShop()
                # quand on clique sur une des flèche
                if arrow_right.isOver(pos):
                    # bouge les tiles de gauche a droite
                    for j in range(len(list_tile)):
                        list_tile[j].move(True)

                    # met celui qui est devant en background = false et le reste en true
                    for m in range(len(list_tile)):
                        if list_tile[m].x == list_TileX[0] and list_tile[m].y == list_TileY[0]:
                            list_tile[m].back = False
                        else:
                            list_tile[m].back = True
                elif arrow_left.isOver(pos):
                    # bouge les tiles de droite a gauche
                    for n in range(len(list_tile)):
                        list_tile[n].move()

                    # met celui qui est devant en background = false et le reste en true
                    for v in range(len(list_tile)):
                        if list_tile[v].x == list_TileX[0] and list_tile[v].y == list_TileY[0]:
                            list_tile[v].back = False
                        else:
                            list_tile[v].back = True

                # change les images en fonction du boolean background
                list_tile[0].fakeAnTile('images/shop/ShopTileVitBack.png', 'images/shop/ShopTileVit.png')
                list_tile[1].fakeAnTile('images/shop/ShopTileDegBack.png', 'images/shop/ShopTileDeg.png')
                list_tile[2].fakeAnTile('images/shop/ShopTileVieBack.png', 'images/shop/ShopTileVie.png')
                list_tile[3].fakeAnTile('images/shop/ShopTileBonusBack.png', 'images/shop/ShopTileBonus.png')

                if list_tile[0].isOver(pos) and not list_tile[0].back and not list_tile[0].locked:
                    if Player.get_score() >= 1000 * Player.get_vitesse_level():
                        Player.set_score(Player.get_score() - (1000 * Player.get_vitesse_level()))
                        Player.set_vitesse_level(Player.get_vitesse_level() + 1)
                        if Player.get_vitesse_level() % 10 == 0:
                            Enemy.set_attack(Enemy.G_attack() + 2)
                        elif Player.get_vitesse_level() % 5 == 0:
                            Enemy.set_freq_tir(Enemy.G_fre_tir() - 2)
                        elif Player.get_vitesse_level() % 1 == 0:
                            Player.set_velocity(Player.get_velocity() + 1)
                        if Player.get_vitesse_level() == 15:
                            list_tile[0].locked = True
                            list_tile[0].image = pygame.image.load('images/shop/ShopTileVitBackLocked.png')

                if list_tile[1].isOver(pos) and not list_tile[1].back and not list_tile[1].locked:
                    if Player.get_score() >= 2000 * Player.get_degat_level():
                        Player.set_score(Player.get_score() - (2000 * Player.get_degat_level()))
                        Player.set_degat_level(Player.get_degat_level() + 1)
                        if Player.get_degat_level() % 10 == 0:
                            Enemy.set_velocity(Enemy.G_velocity() + 1)
                        elif Player.get_degat_level() % 5 == 0:
                            Enemy.set_health(Enemy.G_health() + 1)
                        elif Player.get_degat_level() % 1 == 0:
                            Player.set_attack(Player.get_attack() + 1)
                        if Player.get_degat_level() == 15:
                            list_tile[1].locked = True
                            list_tile[1].image = pygame.image.load('images/shop/ShopTileDegBackLocked.png')

                if list_tile[2].isOver(pos) and not list_tile[2].back and not list_tile[2].locked:
                    if Player.get_score() >= 5000 * Player.get_vie_level():
                        Player.set_score(Player.get_score() - (5000 * Player.get_vie_level()))
                        Player.set_vie_level(Player.get_vie_level() + 1)
                        if Player.get_vie_level() % 2 == 0:
                            Player.set_bonus_lvl_left(Player.get_bonus_lvl_left() + 1)
                        elif Player.get_vie_level() % 5 == 0:
                            Enemy.set_health(Enemy.G_health() + 1)
                        elif Player.get_vie_level() % 1 == 0:
                            Player.set_max_health(Player.get_max_health() + 1)
                        if Player.get_degat_level() == 20:
                            list_tile[2].locked = True
                            list_tile[2].image = pygame.image.load('images/shop/ShopTileVieBackLocked.png')

                if list_tile[3].isOver(pos) and not list_tile[3].back and not list_tile[3].locked:
                    if Player.get_score() >= 5000 * Player.get_bonus_lvl():
                        Player.set_score(Player.get_score() - (5000 * Player.get_bonus_lvl()))
                        Player.set_bonus_lvl(Player.get_bonus_lvl() + 1)
                        Player.set_bonus_lvl_left(Player.get_bonus_lvl_left()-1)
                        if Player.get_bonus_lvl() == 20 or Player.get_bonus_lvl_left() == 0:
                            list_tile[3].locked = True
                            list_tile[3].image = pygame.image.load('images/shop/ShopTileBonusBackLocked.png')

            if event.type == pygame.MOUSEMOTION:
                arrow_right.fakeAnimationR(pos)
                arrow_left.fakeAnimationL(pos)
                if retour_btn.isOver(pos):
                    retour_btn.color = (255, 50, 50)
                else:
                    retour_btn.color = (50, 50, 50)
                if SkinShop_btn.isOver(pos):
                    SkinShop_btn.color = (255, 50, 50)
                else:
                    SkinShop_btn.color = (50, 50, 50)
            if event.type == pygame.QUIT:
                save_json('Saves/save.json')
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Echap pour Menu
                    save_json('Saves/save.json')
                    menu()


def SkinShop():
    while True:
        screen.blit(background, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_json('Saves/save.json')
                sys.exit()


def startgame():
    # li = ligne, ro = row = colonne (ennemis)
    game.player.set_skin()
    li = 1
    ro = 0
    # Supprime les projectiles du Joueur
    for ammo in game.player.all_ammo:
        ammo.kill()
    # Tue tous les ennemis restant de la partie d'avant
    for e in enemy.all_enemies:
        e.kill()
        e.MEnemy()
        # Supprime les projectiles des ennemis
        for ammoE in e.all_ammo_enemy:
            ammoE.remove()

    # Redonne tous les points de vie au joueur
    game.player.start_health()
    # Ajoute tous les ennemis dans un groupe de sprites et incrémente la variable de classe NbEnemy
    for _ in range(nb_enemy):
        enemy.list_enemy(screen)
        Enemy.PEnemy()
    # Place les ennemis 10 par ligne
    for e in enemy.all_enemies:
        if li == 9:
            ro += 1
            li = 1
        e.init_placement(100 * li, 100 * ro + int(screen_heigth*0.1))
        li += 1
        # Donne une vitesse positive pour que tous les ennemis partent dans le même sens
        if e.getV() < 0:
            e.reverse()


def menu():
    save_load('Saves/save.json')
    _menu = True
    while 1:
        while _menu:
            # Affichage
            screen.blit(background, (0, 0))
            screen.blit(back_title, ((screen_width/2-back_title.get_width()/2), 0))
            play_btn.draw(screen)
            shop_btn.draw(screen)
            reset_all_btn.draw(screen)
            quitter_btn.draw(screen)
            pygame.display.flip()
            # Evenements Touches
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEMOTION:
                    if play_btn.isOver(pos):
                        play_btn.color = (255, 50, 50)
                    else:
                        play_btn.color = (50, 50, 50)
                    if shop_btn.isOver(pos):
                        shop_btn.color = (255, 50, 50)
                    else:
                        shop_btn.color = (50, 50, 50)
                    if reset_all_btn.isOver(pos):
                        reset_all_btn.color = (255, 50, 50)
                    else:
                        reset_all_btn.color = (50, 50, 50)
                    if quitter_btn.isOver(pos):
                        quitter_btn.color = (255, 50, 50)
                    else:
                        quitter_btn.color = (50, 50, 50)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_btn.isOver(pos):
                        _menu = False
                        gameLoop()
                    if shop_btn.isOver(pos):
                        _menu = False
                        Shop()
                    if reset_all_btn.isOver(pos):
                        reset_all('Saves/save.json')
                        menu()
                    if quitter_btn.isOver(pos):
                        save_json('Saves/save.json')
                        sys.exit()

                # Quitter le jeu
                if event.type == pygame.QUIT:
                    sys.exit()

                # Evenement touche ENTRER
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        _menu = False
                        startgame()
                        gameLoop()


def gameLoop():
    startgame()
    while True:
        # Affiche le background
        screen.blit(background, (0, 0))

        # Affiche le Score
        score_text = font.render("Score : " + str(game.player.get_score()), True, (255, 255, 255))
        screen.blit(score_text, (10, -5))

        # Affiche les munitions
        enemy.all_enemies.draw(screen)

        # Affiche les ennemis
        game.player.all_ammo.draw(screen)

        # Affiche le joueur
        screen.blit(game.player.image, game.player.rect)

        # Boucle collision balle Joueur et ennmi + dégats ennemi
        for ammo in game.player.all_ammo:  # Boucle Munitions Joueur
            ammo.move()
            for e in enemy.all_enemies:
                if e.collision_ammo(ammo):  # Cherche si il y a collision entre une munitions et un ennemi
                    e.damage(game.player)
                    ammo.kill()
                    if e.get_health() <= 0:  # Cherche si l'ennemi n'a plus de vie
                        e.kill()
                        Enemy.MEnemy()  # Décrémente la variable de classe NbEnemy
                        Player.gain_score(100 * Player.get_bonus_lvl())

        # Boucle collision balle ennemis et Joueur + dégats Joueur
        for e in enemy.all_enemies:
            for ammoE in e.all_ammo_enemy:  # Boucle Munitions Ennemies
                ammoE.move()
                if game.player.collision_ammo(ammoE):
                    game.player.damage()
                    ammoE.kill()
                if game.player.get_health() <= 0:  # Cherche si le Joueur n'a plus de vie
                    gameover()  # Rentre dans la boucle gameover


        # Mouvement droite ou gauche pour le Joueur
        if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
            game.player.move_right()
        elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
            game.player.move_left()

        # Mouvement Ennemies + Tire Projectiles
        for e in enemy.all_enemies:
            e.move()
            # Random chance de tirer par ennemi par boucle (dépendant du nombre restant d'ennemis et frequence de tir)
            r = random.randint(0, 1000 * Enemy.G_fre_tir() * ((Enemy.nbEnemy // 5) + 1))
            if 50 <= r <= 75:
                e.fire_ammo()
            e.all_ammo_enemy.draw(screen)


        if Enemy.nbEnemy == 0:
            win()
        # Update l'écran
        pygame.display.flip()

        # Evenement Touches
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_json('Saves/save.json')  # Sauvegarde à la fermeture du jeu
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True  # Mets les touches dans une liste et donne True si elle sont pressé

                if event.key == pygame.K_SPACE:  # Espace pour tirer
                    game.player.fire_ammo()

                if event.key == pygame.K_ESCAPE:  # Echap pour Menu
                    save_json('Saves/save.json')
                    menu()

            elif event.type == pygame.KEYUP:  # Mets les touches dans de la liste en False au relachement de celle-ci
                game.pressed[event.key] = False

        # Game Over si un ennemi est trop bas
        for en in enemy.all_enemies:
            if en.collision_player(game.player):
                gameover()


menu()
input()
