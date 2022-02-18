import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.step = 0
        self.points = 0
        self.font = pygame.font.Font(r'assets\fonts\gamefont.ttf',20)
        self.image = self.font.render(f'HI{self.points}',True,(83,83,83))
        self.rect = self.image.get_rect()

    def draw(self,surface):
        surface.blit(self.image,self.rect)
        self.image = self.font.render(f'HI {self.points}',True,(83,83,83))

    def update(self):
        self.step += 1
        if self.step % 10 == 0:
            self.points += 1