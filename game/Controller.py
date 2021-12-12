from pygame.event import Event
import pygame

class Controller:
    def __init__(self,player_number : int) -> None:
        self.player_number = player_number

    def get_controller_action(self,event : Event):
        if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        return 'left'
                    if event.key == pygame.K_RIGHT:
                        return 'right'
                    if event.key == pygame.K_UP:
                        return 'jump'

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                return 'left_stop'
            if event.key == pygame.K_RIGHT:
                return 'right_stop'