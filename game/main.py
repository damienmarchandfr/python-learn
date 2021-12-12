import game
import pygame


from Player import Player
pygame.init()

screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

running = True

player = Player(screen.get_height() / 2,screen.get_width()/2)
player.set_animation('run')

while running:
    game.DT = clock.tick(60)/1000

    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
           
               

    player.draw(screen)

    pygame.display.update()

pygame.quit()