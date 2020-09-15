import pygame
from asteroid import Asteroid

#creer une class pour gerer cet event
class AsteroidFallEvent:
    
    #lors du chargement -> creer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 5
        self.game = game
        self.fall_mode = False

        # definir un groupe de sprite pour renger nos asteroids
        self.all_asteroids = pygame.sprite.Group()
        
    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def asteroid_fall(self):
        for i in range(1, 10):
            # apparaitre 1 premiere boule de feu
            self.all_asteroids.add(Asteroid(self))

    def attempt_fall(self) :
        # la jauge d event est pleine
        if self.is_full_loaded() and len(self.game.all_enemies) == 0:
            print("Pluie d Asteroides !!")
            self.asteroid_fall()
            self.fall_mode = True
        
    def update_bar(self, surface):

        # ajouterdu pourcentage a la bar
        self.add_percent()

        # bar noir
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # l axe des x
            surface.get_height() - 20, #l axe des y
            surface.get_width(), # longeur de la fenetre
            10 # epaisseur de la barre
        ])
        # bar rouge
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # l axe des x
            surface.get_height() - 20,  # l axe des y
            (surface.get_width() / 100) *self.percent,  # longeur de la fenetre
            10  # epaisseur de la barre
        ])
        