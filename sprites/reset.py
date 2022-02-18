import pygame
class Reset(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'F:\assets\images\RNFA_reset.png')
        self.rect = self.image.get_rect()
        surface = pygame.display.get_surface()
        self.rect.center = surface.get_width() / 2, surface.get_height() / 4 + 45

    def draw(self,surface):
        surface.blit(self.image,self.rect)
