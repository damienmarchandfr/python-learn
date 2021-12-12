import pygame
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')


class Player(pygame.sprite.Sprite):

    # Number of frame for animation
    sprite_infos = {
        'idle' : 11,
        'run': 12
    }
    # Images loaded for each animations
    images = {
        'idle' : [],
        'run': []
    }


    def _load_images(self):
        for animation, frame_nbr in Player.sprite_infos.items():
            file_name = 'player-'+animation+'-32x32.png'
            sheet =  pygame.image.load(os.path.join(img_folder, file_name)).convert_alpha()
            sheet_width = sheet.get_size()[0]
            sheet_height = sheet.get_size()[1] 

            for i in range(frame_nbr):
                rect = pygame.Rect(i*32,0,sheet_width/frame_nbr,sheet_height)
                image = pygame.Surface(rect.size).convert()
                image.blit(sheet, (0, 0), rect)
                Player.images[animation].append(image)
                self.rect = rect
 

    def __init__(self,x: int,y: int) -> None:
        super().__init__()
        self._load_images()
       
        self.animation_speed = 3
        
        # status
        self.frame_counter = 0
        self.current_animation_index = 0
        self.max_index = 0
        
        # Position
        self.x = x
        self.y = y
        self.speed = 5

        # Controller directions
        self.controller_direction = None

        # IDLE default animation
        self.set_animation('idle')


    def set_direction(direction: str):
        match direction
        return


    def set_animation(self,animation : str):
        self.animation = animation
        self.current_animation_index = 0
        self.max_index = Player.sprite_infos[animation] -1
        self.frame_counter = 0       

    def draw(self,surface: pygame.Surface):
        self.frame_counter+=1

        if(self.frame_counter == self.animation_speed):
            # If end of animation
            if self.current_animation_index == self.max_index:
                self.current_animation_index = 0
            else:
                self.current_animation_index+=1
            
            self.frame_counter = 0

        self.image = Player.images[self.animation][self.current_animation_index]   
        self.rect.center = (self.x,self.y)
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(self)
        self.sprite_group.draw(surface)

