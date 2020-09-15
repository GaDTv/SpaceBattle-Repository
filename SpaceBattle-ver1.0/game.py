import pygame
from player import Player
from enemie import Enemie
from asteroid_event import AsteroidFallEvent

class Game:

    def __init__(self):
        # def si le jeu a commencer
        self.is_playing = False
        # charger le joueur
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        # genere l event
        self.asteroid_event = AsteroidFallEvent(self)
        # groupe enemie
        self.all_enemies = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_enemie()
        self.spawn_enemie()

    def game_over(self):
        self.all_enemies = pygame.sprite.Group()
        self.asteroid_event.all_asteroids = pygame.sprite.Group()
        self.asteroid_event.reset_percent()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # charger le joueur
        screen.blit(self.player.image, self.player.rect)

        # update la barre de vie
        self.player.update_health_bar(screen)

        # update la bar d event du jeu
        self.asteroid_event.update_bar(screen)

        # recuperer tous les projectile
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer tous les enemies
        for enemie in self.all_enemies:
            enemie.foward()
            enemie.update_health_bar(screen)

            if enemie.rect.y > 620:
                enemie.damage(100)

        # recuperer les aseteroids de notre jeu
        for asteroid in self.asteroid_event.all_asteroids:
            asteroid.fall()

        # charger tous les enemies
        self.all_enemies.draw(screen)

        # charger le groupe de projectile
        self.player.all_projectiles.draw(screen)

        # charger les image de mon groupe de asteroids
        self.asteroid_event.all_asteroids.draw(screen)

        # verifier si le joueur veux se deplacer
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 400:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 0:
            self.player.move_up()
        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y < 580:
            self.player.move_down()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_enemie(self):
        enemie = Enemie(self)
        self.all_enemies.add(enemie)