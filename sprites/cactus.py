import pygame
import os
import random

class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        images = ['largecactus1.png','largecactus2.png','largecactus3.png',
                  'smallcactus1.png','smallcactus2.png','smallcactus3.png']
        image = os.path.join(r'assets\images',random.choice(images))
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        surface = pygame.display.get_surface()
        x = surface.get_width() * 2
        y = surface.get_width() / 2 - 115
        self.rect.midleft = (x,y)

    def draw(self,surface):
        surface.blit(self.image,self.rect)

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.kill()
