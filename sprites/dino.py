import pygame
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.step = 0
        self.height = 15
        self.jumping = False
        self.sound_jump = pygame.mixer.Sound(r'F:\assets\sounds\jump.wav')
        self.image_run1 = pygame.image.load(r'F:\assets\images\dinorun1.png')
        self.image_run2 =pygame.image.load(r'F:\assets\images\dinorun2.png')
        self.image = self.image_run1
        self.rect = self.image.get_rect()

        surface = pygame.display.get_surface()
        x = surface.get_width() - 600
        y = surface.get_width() / 2 - 115
        self.rect.midright = (x,y)

    def draw(self, surface):
        surface.blit(self.image, self.rect )

    def update(self):
        self.step += 1
        if self.step % 7 == 0:
            if self.image == self.image_run1:
                self.image = self.image_run2
            else:
                self.image = self.image_run1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.jumping:
            self.jumping = True
            self.sound_jump.play()
        if self.jumping:
            self.jump()

    def jump(self):
        self.rect.y -= self.height
        self.height -= 1
        if self.height < -15:
            self.height = 15
            self.jumping = False
