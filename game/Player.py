import pygame
import os
import game

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

        self.running = False
        self.jumping = False
        
        self.x_direction = 1

        # Position
        self.x = x
        self.y = y
        self.speed = 200

        self.vertical_acceleration = 100
        self.vertical_speed = 0

        # IDLE default animation
        self.set_animation('idle')

        self.collider = pygame.Rect(self.x,self.y,15,25)
        self.collider.center = (self.x,self.y + 3)


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
        self.image = pygame.transform.flip(self.image,self.x_direction != 1,False)
        self.rect.center = (self.x,self.y)
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(self)
        self.sprite_group.draw(surface)

        if game.DEBUG:
            # Collision
            color = (255,0,0)
            pygame.draw.rect(surface, color, self.collider, 1)

            # Sprite box
            # color=(153,153,255)
            # pygame.draw.rect(surface, color, self.rect, 2)

    def move(self):
        self.y += int(game.DT* self.vertical_acceleration) 
        print(int(game.DT) *  self.vertical_acceleration)
        
        if self.running:
            self.x += int(self.speed * game.DT) * self.x_direction
        self.collider.center = (self.x,self.y + 3)

    def _run(self):
        if self.running == False:
            self.set_animation('run')
        self.running = True

    def _set_idle(self):
        self.set_animation('idle')
        self.running = False
        self.jumping = False
        
    def set_action(self,action : str):
        if action is None:
            self._set_idle()
        if action == 'right' or action == 'left':
            self.x_direction = 1 if action == 'right' else -1  
            self._run()
        if action == 'right_stop' and self.x_direction == 1:
            self._set_idle()
        if action == 'left_stop' and self.x_direction == -1:
            self._set_idle()
            
