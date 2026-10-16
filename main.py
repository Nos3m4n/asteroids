import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    dt : float = 0.0


    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        updatable.update(dt)
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()



if __name__ == "__main__":
    main()
