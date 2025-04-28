# Pygame Workshop!
Learn how to create games with Python by creating your first basic game with Pygame!


# What is Pygame? 

![image](https://github.com/user-attachments/assets/d3520753-4e56-41fd-8d96-cdc5427f493c)


Pygame is a open-source library that streamlines the process of drawing images and shapes to a display! What that means is that unlike game engines (or applications that allow you to build games), Pygame does not have its own physics system or lighting systems. 

What is interesting about this is that it gives us as programmers a ton of control about the systems that make up our game! It also is very easy to get started with, free, and open-source! Open-source means that all of the code that is running behind the scenes is publicly available meaning that the developers will never be able to charge money for Pygame and the community can always choose to take the code and make their own versions! 

<img width="1304" alt="Screenshot 2025-04-28 at 12 39 26 PM" src="https://github.com/user-attachments/assets/ed858821-b1b3-487e-8ef5-39ad60451840" />
Above is the source code for Pygame publicly available on Github!

# What is this workshop?

In this workshop we will learn the basics of Pygame by making our own version of the offline Google Dinosaur game! 

https://github.com/user-attachments/assets/f459a610-bea2-45fe-bb45-70a064fe10fe

Let's get started!

# Installing Pygame

Make sure before getting started to install pygame by running the following command in your terminal! This will just install the pygame library so we can import it in our python files.

```
pip install pygame
```

# Getting Started!!

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


## Acknowledgements
This workshop was created by Jake Torres for students in ENGI1006 Spring 2025
