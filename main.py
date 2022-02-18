import pygame
import sys
import random
from sprites.road import Road
from sprites.cloud import Cloud
from sprites.dino import Dino
from sprites.cactus import Cactus
from sprites.game import Score
from sprites.gameover import Gameover
from sprites.reset import Reset
pygame.init()

# Константы
WIDTH = 700
HEIGHT = 500
FPS = 100

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Chrome")
clock = pygame.time.Clock()

# Спрайты
def main():
    game_over = Gameover()
    game_over = False

    road = Road()
    clouds = pygame.sprite.Group()
    player = Dino()
    cactuses = pygame.sprite.Group()
    score = Score()
    reset = Reset()
    running = True
    while running:
        # Частота обновления экрана
        clock.tick(FPS)

        # События
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_over:
                    main()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and game_over:
                    main()
        for obstacle in cactuses:
            if pygame.sprite.collide_mask(player,obstacle) and not game_over:
                game_over = True
                end = Gameover()
        # Рендеринг
        if not game_over:
            screen.fill((255,255,255))
            road.draw(screen)
            clouds.draw(screen)
            player.draw(screen)
            cactuses.draw(screen)
            score.draw(screen)
        if game_over:
            reset.draw(screen)
        if game_over:
            end.draw(screen)
        # Обновление спрайтов

        # Обновление экрана
        road.update()
        clouds.update()

        player.update()

        cactuses.update()

        score.update()

        if len(cactuses) < 1:
            cactus = Cactus()
            cactus.add(cactuses)


        random_number = random.randint(3,6)
        if len(clouds) < 3:
            cloud = Cloud(random_number)
            clouds.add(cloud)
        pygame.display.update()
if __name__ == '__main__':
    main()