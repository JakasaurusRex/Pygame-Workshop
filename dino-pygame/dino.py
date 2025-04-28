import pygame

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

class Dino:
    def setup_dino(self):
        self.dino_idle = load_image('dino-pygame/assets/dino/dino_idle.png', 4)
        self.dino_jump = load_image('dino-pygame/assets/dino/dino_jump.png', 4)
        self.dino_run1 = load_image('dino-pygame/assets/dino/dino_run1.png', 4)
        self.dino_run2 = load_image('dino-pygame/assets/dino/dino_run2.png', 4)

    def current_sprite(self):
        if self.state == "idle":
            return self.dino_idle
        elif self.state == "jump":
            return self.dino_jump
        elif self.state == "run":
            if self.frame == 1:
                self.frame = 2
                return self.dino_run1
            else:
                self.frame = 1
                return self.dino_run2

    def get_height(self):
        return self.dino_idle.get_height()
    
    def get_width(self):
        return self.dino_idle.get_width()

    def draw(self, screen):
        screen.blit(self.current_sprite(), (self.x, self.y))

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def __init__(self):
        self.setup_dino()
        self.x = 0
        self.y = 0
        self.state = "run"
        self.frame = 1

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((768, 432))
    clock = pygame.time.Clock()
    running = True

    # call functions that setup the background and floor surfaces and return them
    backgrounds = setup_backgrounds()
    floor = setup_floor()
    dino = Dino()


    # MAIN GAME LOOP
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # draw background and floor
        draw_backgrounds(screen, backgrounds)
        draw_floor(screen, floor)
        dino.set_position(50, screen.get_height()-floor.get_height()-dino.get_height())
        dino.draw(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits Frames Per second displayed to 60
        clock.tick(60)  

    # Close pygame and clean up resources 
    pygame.quit()
    

if __name__ == "__main__":
    main()