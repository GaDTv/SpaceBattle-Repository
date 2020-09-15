import pygame
import random

class Enemie(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.1
        self.image = pygame.image.load('assets/Ship-Enemie.png')
        self.rect = self.image.get_rect()
        self.rect.x = 25 + random.randint(0, 335)
        self.rect.y = 0
        self.velocity = 1

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.rect.y = 0
            self.rect.x = 25 + random.randint(0, 335)
            self.health = self.max_health

            #si la bar d event est full
            if self.game.asteroid_event.is_full_loaded():
                # retirer du jeu
                self.game.all_enemies.remove(self)

                # appel de la methode pour essayer de declencher la pluie de asteroid
                self.game.asteroid_event.attempt_fall()

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 10, self.rect.y - 20, self.health, 5])


    def foward(self):
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.y += self.velocity

        else:
            self.game.player.damage(self.attack)