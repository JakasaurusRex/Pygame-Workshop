# Pygame Workshop!
Learn how to create games with Python by creating your first basic game with Pygame!

# The Prelude 
## What is Pygame? 

![image](https://github.com/user-attachments/assets/d3520753-4e56-41fd-8d96-cdc5427f493c)


Pygame is a open-source library that streamlines the process of drawing images and shapes to a display! What that means is that unlike game engines (or applications that allow you to build games), Pygame does not have its own physics system or lighting systems. 

What is interesting about this is that it gives us as programmers a ton of control about the systems that make up our game! It also is very easy to get started with, free, and open-source! Open-source means that all of the code that is running behind the scenes is publicly available meaning that the developers will never be able to charge money for Pygame and the community can always choose to take the code and make their own versions! 

<img width="1304" alt="Screenshot 2025-04-28 at 12 39 26 PM" src="https://github.com/user-attachments/assets/ed858821-b1b3-487e-8ef5-39ad60451840" />
Above is the source code for Pygame publicly available on Github!

# What is this workshop?

In this workshop we will learn the basics of Pygame by making our own version of the offline Google Dinosaur game! 

https://github.com/user-attachments/assets/f459a610-bea2-45fe-bb45-70a064fe10fe

Let's get started!

## Installing Pygame

Make sure before getting started to install pygame by running the following command in your terminal! This will just install the pygame library so we can import it in our python files.

```
pip install pygame
```

# Dino Time

## Getting Started!!

To get started lets open a new python file and you can call it whatever you want. You can copy this skeleton code into your file to get started. Don't worry if it looks complicated we are going to step through every line and learn what is happening!

```
import pygame

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((768, 432))
    clock = pygame.time.Clock()
    running = True

    # MAIN GAME LOOP
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits Frames Per second displayed to 60
        clock.tick(60)  

    # Close pygame and clean up resources 
    pygame.quit()
    

if __name__ == "__main__":
    main()
```

After running the code your program should display a purple screen! So whats going on here? Lets step through every line. In the following lines of code, we are importing the library and initializing everything we are going to need to run our program. First we need a screen to display our game on, and set_mode lets us pick the size of the window. The clock will be used to make sure that the game behaves the same regardless of what computer we run the program on, some computers display faster or slower than other computers. We will later use the clock to ensure that those speeds do not effect our physics. Lastly running will be a boolean thats true or false depending upon if our game is running our not!

```
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
```

These next lines of code are the "game loop". What that means is that while the game is running, we are going to iterate through this loop constantly until that is no longer true. The first thing that happens in our loop is that it checks if the user has sent a quit event, this happens when a user clicks the close button on the window, if we do that we stop the loop. If a user didnt close the window, we set the color of the window to purple, and call flip to push all of our changes to the screen to the computer monitor. We call clock.tick(60) every time in the game loop to insure that every second we pass through this loop 60 times, or we update the screen 60 Frames per second. The clock also returns the time since the last update to the screen which we will later use like I mentioned before.  

```
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
```

The last line outside the game loop just closes the program and cleans up all the resources used by pygame!
```
pygame.quit()
```

Nothing from this program should look too foreign to you, its all things that you have learned by learning Python just using a new library. Now using our Python knowledge and some other library functions we can change the background to something cooler!

## Surfaces && Changing up the Background

Before we continue and setup the background its critical to learn about **_Surfaces_** in **Pygame**. Surfaces are the objects in Pygame that are displayed on the screen. When you want to display a picture on the screen, you will load it using the ```pygame.image.load()``` function which will return a surface for you to display on the screen. In Pygame, the screen itself is also a type of surface, so in order to put your surface on the screen, you need to use the **blit** function which is short for _**Block Transfer**_. 

Heres a picture to help you visualize how this works!

![image](https://github.com/user-attachments/assets/e77f339d-4bbb-4962-8d63-a0238cce09c5)


The following code will load a potato image into the surface called "potato" and then copy the contents of that surface to the screen using blit at the location provided in the tuple (0,0). 
```
potato = pygame.image.load("potato_path.png")
screen.blit(potato, (0,0))
```

In Pygame the coordinate system for drawing to the screen starts in the top left corner of the display and increases in X and Y value as we move down and to the right, like shown in the figure below.
![image](https://github.com/user-attachments/assets/83336539-98d7-4b98-a720-4429fefe1c3d)

Using all of this information, we can now create a fancy background and floor for our game. In the [assets folder of the github repository](https://github.com/JakasaurusRex/Pygame-Workshop/tree/main/dino-pygame/assets) you can find a bunch of images that I will be using to create the game, you can use your own images but you might need to change the size of your window to fit your backgrounds!

For our game, I have 5 background images that will produce a sense of depth when we are running in our game! In the following code, I setup functions to load all of the images and scale them by 2 to fit our window. I called these functions before the game loop and stored my background surfaces in a list. Similarly, I loaded a floor and also scaled it by 2 and stored it in a variable. Then during the game loop, after I fill the screen with pink, I draw the backgrounds and then the floor.

Pygame gives us some cool functionality like, screen.get_height(), which returns the height of the screen that we can use to find the coordiantes where to draw the floor. You can see me using other functionality like that throughout the code. The only other unfamiliar piece of code is when I called convert_alpha on my surface after loading it. This just ensures that the pixels in the image that are transparent in my original image retain their transparency after being loaded, you typically want to use this when loading pngs!

```
# load an image with a given path and scale it the given amount and return it
def load_image(path, scale):
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
```

After running this we will now see a much prettier background with our layered background and colorful floor! 

<img width="763" alt="Screenshot 2025-04-28 at 6 07 04 PM" src="https://github.com/user-attachments/assets/7d530bd6-03c9-4eed-a16a-bb3d9c679a88" />

## Setting up our Dinobro

Now that we have a fancy backgrounds, lets add our character into our game. The character sprite we are going to be using is in the same [assets folder of the github repository](https://github.com/JakasaurusRex/Pygame-Workshop/tree/main/dino-pygame/assets) as before in the character subfolder! 

The first thing we are going to do is pretty similar to the work you did in Homework 9. We are going to setup a class for our dinosaur that will encapsulate all of the functionality it will do such as, drawing it, updating the position and velocity, and changing the sprite for when we are running or jumping! You can copy this class into your code and read through it to understand how it works!

```
class Dino:
    # intialize the surfaces for each of the states - run 1 and run 2 are used to make it look like the dinosaur is running
    def setup_dino(self):
        self.dino_idle = load_image('dino-pygame/assets/dino/dino_idle.png', 4)
        self.dino_jump = load_image('dino-pygame/assets/dino/dino_jump.png', 4)
        self.dino_run1 = load_image('dino-pygame/assets/dino/dino_run1.png', 4)
        self.dino_run2 = load_image('dino-pygame/assets/dino/dino_run2.png', 4)

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

     # update the position of the dinosaur
    def set_position(self, x, y, is_floor=False):
        self.x = x
        self.y = y

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
        pass

    # initialize all of the instance variables of the dinosaur
    def __init__(self):
        self.setup_dino()
        self.x = 0
        self.y = 0
        self.floor_y = 0
        self.state = "run"
        self.running_frame = 1
        self.jump = False
        self.falling = False
        self.vel_y = 0
```

Theres a lot of code here so lets break it down. In our init function, we first setup our dinosaur, which involves just loading surfaces for different states and sprites our dinosaur will be in. Then we setup our x and y variables, set our intitial state to running and the animation frame to 1, our jump and falling booleans to false and our y_velocity to 0. 

We also have a bunch of helper functions:
- current_sprite() - Returns the current surface depending upon the state of the dinosaur for drawing purposes
- get_width/get_height() - returns the width/height of the surfaces
- draw(screen) - draws the dinosaurs current surface to the screen
- set_position(x, y, is_floor) - sets the current coordinates of the dinosaur to the given x and y coords. It also updates a variable for the floors position that we will use later.
- jumped() - Call this function to make the dinosaur jump - we can only jump if we are not falling!
- physics() - This function will be called every frame before draw to update the position of the dinosaur based on the velocity

I additionally, I created some global variables at the top of my code that we might find useful:

```
DINO_JUMP_VEL = -40 # the dinosaurs jumping height
GRAVITY = 4 
DINO_X_OFFSET = 50 # offset from the left edge of the screen
```

Now that you have your Dinosaur class setup, you can create an instance of the Dinosaur object before the main game loop and set its position to the height of the dinosaur above the floor and some offset from the left of the screen like so:

```
dino = Dino()
dino.set_position(DINO_X_OFFSET, screen.get_height()-floor.get_height()-dino.get_height(), True)
```

Draw out this math using the coordinate system I showed earlier if this math doesn't make sense! I also passed in True to inform the class that this is the floor Y position for the dinosaur. 

Last thing we need to do to get the dinosaur all setup is to update our game loop to handle keyboard input and to update the physics and draw the dinosuar. 

```
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

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits Frames Per second displayed to 60
        clock.tick(60)  

    # Close pygame and clean up resources 
    pygame.quit()
```

With all of this, if you run the script again, you should see the dinosaur running on your screen, but if you click the space bar, nothing will happen yet! Lets add jumping next!

Test what happens if we add the following code to our physics function:
```
 if self.jump is True:
            self.vel_y += DINO_JUMP_VEL
            self.falling = True
            self.jump = False
        
        if self.falling:
            self.vel_y += GRAVITY
        
        new_y_position = self.y + self.vel_y
        self.set_position(self.x, new_y_position, False)

```

Play the game and try to think about what is wrong with it! At the moment, we never check if we have landed and hit the ground. Luckily, we setup some functionality to allow us to make a check for this. 

```
if new_y_position >= self.floor_y:
            new_y_position = self.floor_y
            self.falling = False
            self.vel_y = 0
            self.state = 'run'
```

We can simply check if our new position is going to be greater than the Y position of the floor - if it is, we know that we are about to hit the floor and we can just set our Y position to the floor, set our falling variable to False and our velocity to 0. We can also change our state back to run so that we start the running animation again! Once again, if you are confused by this math, draw a picture out to convince yourself how this works.

Try messing around with variables and set your own jump velocity and gravitys to make it feel right!

<img width="768" alt="Screenshot 2025-04-30 at 4 06 35 PM" src="https://github.com/user-attachments/assets/dfc7b5fe-637a-42da-a368-981b4eebd5f3" />


## Acknowledgements
This workshop was created by Jake Torres for students in ENGI1006 Spring 2025
