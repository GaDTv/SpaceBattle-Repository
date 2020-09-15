import pygame
from projectile import Projectile


# creer la class player
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 25
        self.velocity = 2
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()


    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 15, self.rect.y - 20, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 15, self.rect.y - 20, self.health, 7])

    def lunch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        if not self.game.check_collision(self, self.game.all_enemies):
            self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity
