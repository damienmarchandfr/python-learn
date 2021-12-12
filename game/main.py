from pygame.constants import K_LEFT, K_RIGHT
import game
import pygame
from Controller import Controller

from Player import Player
pygame.init()

screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

running = True

player = Player(screen.get_height() / 2,screen.get_width()/2)
player.set_animation('idle')
controller = Controller(1)

while running:
    game.DT = clock.tick(60)/1000

    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        player_action = controller.get_controller_action(event)
        player.set_action(player_action)

    player.move()
    player.draw(screen)

    pygame.display.update()

pygame.quit()