import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 4
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x - 70
        self.rect.y = player.rect.y - 90

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.y -= self.velocity

        # verifier si il rentre en collision avec un enemie
        for enemie in self.player.game.check_collision(self, self.player.game.all_enemies):
            self.remove()
            enemie.damage(self.player.attack)

        # verifier si les projectile son encore sur l ecran
        if self.rect.y < 0:
            # suprimer le projectile
            self.remove()
