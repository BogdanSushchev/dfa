import pygame
class Gameover(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(r'assets\fonts\gamefont.ttf',20)
        self.image = self.font.render('GAME OVER',True,(83,83,83))
        self.rect = self.image.get_rect()
        surface = pygame.display.get_surface()
        self.rect.center = surface.get_width() / 2, surface.get_height() / 4

    def draw(self,surface):
        surface.blit(self.image,self.rect)



