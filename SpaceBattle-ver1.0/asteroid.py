import pygame
import random

# creer une classe pour gere cette comete
class Asteroid(pygame.sprite.Sprite):

    def __init__(self, asteroid_event):
        super().__init__()
        # definir l image
        self.image = pygame.image.load('assets/asteroid.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 335)
        self.rect.y = - random.randint(0, 400)
        self.velocity = random.randint(1, 2)
        self.asteroid_event = asteroid_event

    def remove(self):
        self.asteroid_event.all_asteroids.remove(self)

        # verifier si le nombre de asteroid set de 0
        if len(self.asteroid_event.all_asteroids) == 0:
            #remetre la bar a 0
            self.asteroid_event.reset_percent()
            #apparaitre les enemies
            self.asteroid_event.game.spawn_enemie()
            self.asteroid_event.game.spawn_enemie()

    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 550:
            print("sol")
            # retirer la boule de feu
            self.remove()

            # si il n y a plus de boule de feu
            if len(self.asteroid_event.all_asteroids) == 0:
                print("Fin de l event !!")
                #remettre la jauge de vie depart
                self.asteroid_event.reset_percent()
                self.asteroid_event.fall_mode = False

        #verifier si la boule de feu touche le joueur
        if self.asteroid_event.game.check_collision(self, self.asteroid_event.game.all_player):
            print("joueur touche !")
            # retirer la boule de feu
            self.remove()
            # subir 20 de degats
            self.asteroid_event.game.player.damage(20)

