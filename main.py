import pygame
pygame.init()
from game import Game

# importer l icon
icon = pygame.image.load('assets/spaceship.png')

# generer la fenetre du jeu
pygame.display.set_caption("SpaceBattle")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((460, 640))


# importer le background
background = pygame.image.load('assets/bg.jpg')

# importer la banniere
banner = pygame.image.load('assets/Banner.png')
banner = pygame.transform.scale(banner, (1280, 1280))



# importer le bouton
play_button = pygame.image.load('assets/Bouton.png')
play_button = pygame.transform.scale(play_button, (600, 600))
play_button_rect = play_button.get_rect()

# charger le jeu
game = Game()

# boucle du jeu
runnig = True

while runnig:

    # charger le background
    screen.blit(background, (-1080, -200))

    # verifier si le jeu a commencer
    if game.is_playing:
        game.update(screen)
    else:
        # charger l ecran de bvn
        screen.blit (play_button, (-50, 10))
        screen.blit(banner, (-400, -400))


    # update l ecran
    pygame.display.flip()

    # si le joueur ferme le jeu
    for event in pygame.event.get():
        # verifier si l event est une fermeture de jeu
        if event.type == pygame.QUIT:
            runnig = False
            pygame.quit()
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter la touche espace
            if event.key == pygame.K_SPACE:
                game.player.lunch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()