import pygame
import random

# DIMENSIONS OF THE SCREEN
SCREEN_WIDTH = 768
SCREEN_HEIGHT = 432

# the height of the floor on the screen
FLOOR_HEIGHT = 0

DINO_JUMP_VEL = -40 # the dinosaurs jumping height
GRAVITY = 4 
DINO_X_OFFSET = 50 # offset from the left edge of the screen

# velocity the stump moves to the left
STUMP_VEL = -15

# the interval at which obstacles can spawn in MS
OBSTACLE_SPAWN_RATE = [500, 1500]

# load an image with a given path and scale it the given amount and return it
def load_image(path, scale = 2):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))
    return image

# setup the background images and return an array with all the background images
# note: the order the backgrounds are loaded in is the order they are loaded in, backgrounds with the most depth first!!!
def setup_backgrounds():
    background_1 = load_image('dino-pygame/assets/background/bg1.png', 2)
    background_2 = load_image('dino-pygame/assets/background/bg2.png', 2)
    background_3 = load_image('dino-pygame/assets/background/bg3.png', 2)
    background_4 = load_image('dino-pygame/assets/background/bg4.png', 2)
    background_5 = load_image('dino-pygame/assets/background/bg5.png', 2)

    return [background_1, background_2, background_3, background_4, background_5]

# setup the floor
def setup_floor():
    floor = load_image('dino-pygame/assets/background/floor.png', 2)
    return floor

# draw the backgrounds in the given array to the screen in a loop
def draw_backgrounds(screen, backgrounds):
    for background in backgrounds:
        screen.blit(background, (0,0))

# draw the floor to the screen at the bottom of the screen
def draw_floor(screen, floor):
    screen.blit(floor, (0,screen.get_height()-floor.get_height()))

# Obstacle handler class that spawns, despawns, and checks for collisions with obstacles
class ObstacleHandler():
    def __init__(self):
        self.obstacle_classes = [] # this is a list of the classes of obstacles it can spawn!
        self.obstacles = [] # list of the current existing obstacles
        self.time_to_next_obstacle = pygame.time.get_ticks() + random.randint(OBSTACLE_SPAWN_RATE[0], OBSTACLE_SPAWN_RATE[1]) # time until the next obstacle spawns
    
    # add an obstacle class to the list of possible obstacles
    def add_obstacle_class(self, obstacle_class):
        self.obstacle_classes.append(obstacle_class)

    # spawn an obstacle - called every frame, checks clock to see if we have passed time for next obstacle
    def spawn_obstacle(self, clock):
        if pygame.time.get_ticks() >= self.time_to_next_obstacle:
            # update the next obstacle timer
            self.time_to_next_obstacle = pygame.time.get_ticks() + random.randint(OBSTACLE_SPAWN_RATE[0], OBSTACLE_SPAWN_RATE[1])
            if len(self.obstacle_classes) > 0:
                new_obstacle_class = random.choice(self.obstacle_classes) # chose a new random obstacle
                new_obstacle = new_obstacle_class()

                # set its position to be on the floor - the + 5 is just to make sure it lines up nicely
                new_obstacle.set_position(SCREEN_WIDTH + new_obstacle.get_width(), FLOOR_HEIGHT - new_obstacle.get_height() + 5) 
                self.obstacles.append(new_obstacle)

    # draw all the obstacles
    def draw_obstacles(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    # update the physcis for all the obstacles
    def obstacles_physics(self):
        for obstacle in self.obstacles:
            obstacle.physics()

        # if a obstacle is off screen we set it to inactive - we remove all the ianctive obstacles from the list and they despawn
        self.obstacles = [o for o in self.obstacles if o.active]

    # check if an objects collider rect has collided with any of the obstacles collider rects
    def check_collisions(self, object_collider_rect):
        for obstacle in self.obstacles:
            # collide_rect returns true if a collision occurs between 2 rects
            if object_collider_rect.colliderect(obstacle.get_collider_rect()): 
                return True
            
        return False

# base obstacle class
class Obstacle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_vel = 0
        # collider rect is pretty much a box around the object that represents where it can be hit
        self.collider_rect = pygame.Rect(0,0,1,1) 

        # if a obstacle is active it is on the screen, otherwise its inactive and can be despawned
        self.active = True

    # update the positon of the obstacle and collider
    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.collider_rect.topleft = (self.x, self.y)

    # return the collider rect
    def get_collider_rect(self):
        return self.collider_rect
    
    def draw(self, screen):
        # Should be overridden by subclasses
        pass

    def physics(self):
        # Should be overridden by subclasses
        pass

# stump class - inherits from obstacle and uses the stump asset 
class Stump(Obstacle):
    def setup_stump(self):
        self.stump_sprite = load_image('dino-pygame/assets/obstacles/stump.png', 2)
        # setup the collider rect with the width and height of the stump
        self.collider_rect = pygame.Rect( 0, 0, self.get_width(), self.get_height())

     # get the height of the stump surface
    def get_height(self):
        return self.stump_sprite.get_height()
    
    # get the width of the stump surface
    def get_width(self):
        return self.stump_sprite.get_width()
    
    # draw to the screen
    def draw(self, screen):
        screen.blit(self.stump_sprite, (self.x, self.y))
    
    # set position and collider position
    def set_position(self, x, y):
       self.x = x
       self.y = y
       self.collider_rect.topleft = (x, y)
    
    # stump just moves left - also check if its off screen for setting inactive
    def physics(self):
        new_x_pos = self.x + STUMP_VEL
        self.set_position(new_x_pos, self.y)

        if new_x_pos < 0 - self.get_width():
            self.active = False
            
    # return the collider rect
    def get_collider_rect(self):
        return self.collider_rect

    # call obstacle init and setup the stump
    def __init__(self):
        super().__init__() 
        self.setup_stump()



class Dino:
    # intialize the surfaces for each of the states - run 1 and run 2 are used to make it look like the dinosaur is running
    def setup_dino(self):
        self.dino_idle = load_image('dino-pygame/assets/dino/dino_idle.png', 4)
        self.dino_jump = load_image('dino-pygame/assets/dino/dino_jump.png', 4)
        self.dino_run1 = load_image('dino-pygame/assets/dino/dino_run1.png', 4)
        self.dino_run2 = load_image('dino-pygame/assets/dino/dino_run2.png', 4)

        # instantiate the collider rect with the default position and the width and height
        self.collider_rect = pygame.Rect( 0, 0, self.get_width(), self.get_height())

    # return the current surface of the dinosaur depending upon the state
    def current_sprite(self):
        if self.state == "idle":
            return self.dino_idle
        elif self.state == "jump":
            return self.dino_jump
        elif self.state == "run":
            if self.runnning_frame == 1:
                self.runnning_frame = 2
                return self.dino_run1
            else:
                self.runnning_frame = 1
                return self.dino_run2

    # get the height of the dinosaur surface
    def get_height(self):
        return self.dino_idle.get_height()
    
    # get the width of the dinosaur surface
    def get_width(self):
        return self.dino_idle.get_width()

    # draw the dinosaur to the screen
    def draw(self, screen):
        screen.blit(self.current_sprite(), (self.x, self.y))

    # return the dinos collider rect
    def get_collider_rect(self):
        return self.collider_rect

    # update the position of the dinosaur
    def set_position(self, x, y, is_floor=False):
        self.x = x
        self.y = y

        # update the collider rect with the new position
        self.collider_rect.topleft = (x, y)

        # if the y we are passing in is the same as the floor, we can set this bool to true and update value
        if is_floor:
            self.floor_y = y

    # call this if jump button was pressed - we can only jump if we are not falling
    def jumped(self):
        if not self.falling:
            self.jump = True
            self.state = 'jump'
    
    # call this function every frame to update the position and velocity of the dinosaur based on inputs
    def physics(self):
        if self.jump is True:
            self.vel_y += DINO_JUMP_VEL
            self.falling = True
            self.jump = False
        
        if self.falling:
            self.vel_y += GRAVITY
        
        new_y_position = self.y + self.vel_y
        if new_y_position >= self.floor_y:
            new_y_position = self.floor_y
            self.falling = False
            self.vel_y = 0
            self.state = 'run'

        self.set_position(self.x, new_y_position, False)

    # initialize all of the instance variables of the dinosaur
    def __init__(self):
        self.setup_dino()
        self.x = 0
        self.y = 0
        self.floor_y = 0
        self.state = "run"
        self.runnning_frame = 1
        self.jump = False
        self.falling = False
        self.vel_y = 0

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    # call functions that setup the background and floor surfaces and return them
    backgrounds = setup_backgrounds()
    floor = setup_floor()
    
    # global lets us edit globally created variables - we are editing the FLOOR_HEIGHT at the top of the file to be used when spawning objects
    global FLOOR_HEIGHT
    FLOOR_HEIGHT = screen.get_height()-floor.get_height()

    # Create a Dino Object and set its position 
    dino = Dino()
    dino.set_position(DINO_X_OFFSET, FLOOR_HEIGHT-dino.get_height(), True)

    # create the obstacle handler and add the stump as one of the classes that cna be instantiated
    obstacle_handler = ObstacleHandler()
    obstacle_handler.add_obstacle_class(Stump)

    # MAIN GAME LOOP
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                dino.jumped()

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # draw background and floor
        draw_backgrounds(screen, backgrounds)
        draw_floor(screen, floor)

        # Draw the dino to the screen
        dino.physics()
        dino.draw(screen)

        obstacle_handler.spawn_obstacle(clock)
        obstacle_handler.obstacles_physics()
        obstacle_handler.draw_obstacles(screen)

        if(obstacle_handler.check_collisions(dino.get_collider_rect())):
            running = False

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits Frames Per second displayed to 60
        clock.tick(60)  

    # Close pygame and clean up resources
    pygame.quit()
    

if __name__ == "__main__":
    main()