import pygame

# load an image with a given path and scale it the given amount and return it
def load_image(path, scale):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))
    return image

# setup the background images and return an array with all the background images
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

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((768, 432))
    clock = pygame.time.Clock()
    running = True

    # call functions that setup the background and floor surfaces and return them
    backgrounds = setup_backgrounds()
    floor = setup_floor()


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
        

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits Frames Per second displayed to 60
        clock.tick(60)  

    # Close pygame and clean up resources 
    pygame.quit()
    

if __name__ == "__main__":
    main()