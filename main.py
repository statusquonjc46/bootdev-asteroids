# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shots import Shot

def main():
    pygame.init()
    pyclock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()
    all_shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (all_asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (all_shots, updateable, drawable)

    asteroid_field = AsteroidField()
    player = Player(x, y)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for up in updateable:
            up.update(dt)
        
        for asteroid in all_asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for draw_scrn in drawable:
             draw_scrn.draw(screen)

        pygame.display.flip()
        dt = pyclock.tick() / 1000

if __name__ == "__main__":
    main()