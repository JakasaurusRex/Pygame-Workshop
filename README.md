# Introductory to Godot Workshop!
Learn how to create games with Godot by creating your first basic game!

- [**What is Godot?**](#what-is-godot)
- [**Installing Godot**](#installing-godot)
- [**Exploring the engine**](#exploring-the-engine)
- [**Godot Terms**](#godot-terms)
- [**Planning out our game!**](#planning-out-our-game)
- [**Dino Time**](#dino-time)

# What is Godot? 
![image](https://github.com/user-attachments/assets/afc258b2-e435-4bb6-b407-0a5dec36d055)

A game engine is a tool that allows for ease of creation of games. Game engines have features that make it easy to make whatever you can dream up! An example of some features common in game engines are the following:
- Physics Engines - The engine automatically does physics calculations for you, abstracting a lot of math!
- Display Rendering and Shading Engines - Game engines abstract the compleixty that goes into creating a display on your screen
- Ease of accessing controls - Game engines make it easy to allow users to interact with the softare by having hardware events for interaction with keyboards, mice, controllers, or any other type of input.
- Sound Engines - Game engines feature sound engines allowing it easy to play sounds on a computer.
- More! - Game engines have tons of technically challenging features abstracted

Some well known game engines are Unity, Unreal Engine, Godot, CryEngine, GameMaker, PyGame, RPGMaker, and Scratch.

You can also create your own game engine using any programming language! It is pretty involved as you have to figure out how to interact with the computer to display and make sounds on your own but these challenges can be really rewarding to solve!

## What sets Godot apart from other game engines?

A number of features set Godot apart from the pack.

1) Godot is completely **free**
   
This is really critical. A lot of game engines are free for personal use but cost money if you want to actually make professional games with them. Godot is free no matter if you are a huge development team or a solo developer making games for fun!


2) Godot is **lightweight**
   
Upon downloading the game enigne, you will notice how easy it is to use on your computer! Game engines are historically large programs that consume a lot of memory and processing power. Godot on the otherhand is very easy to run on any computer and its download size is around 500 MB, smaller than most social media apps! It can also run on any type of computer!

3) Godot is **Open-Source**


<img width="997" alt="Screenshot 2025-02-03 at 7 06 02 PM" src="https://github.com/user-attachments/assets/069296d0-a919-4b00-b7f7-602119322aa5" />
An open-source application is an application that's sourcecode is publicly available online. The developers of Godot are people in the game development community that use Godot and publicly contribute to the project. What this means is that Goodt will always be free and the community is super supportive and open to allow the app to be prosperious!<br />

4) Godot is **EASY!!!**

Game engines are sterotypically super complicated, packed with tons of features that are poorly explained. Godot is suprisingly insanely easy to get started with. It features a Python-like programming language called GDScript with documentation built into the application. Hovering over any library function allows you to pull up the wiki page for what that function does and how it works. Features mostly behave as you would expect making it super easy to start making games with Godot after getting over the initial learner barrier as you will soon see!

5) Godot is a **new technology**

The last thing that sets Godot apart is that its constantly changing. The fact that it is constantly changing and evolving is super interesting to developers in the industry looking for future ways to streamline the process of making games. This interest in the technology might be something that helps you secure an interview where you can talk about your experience with this technology (this is something I experienced when interviewing with **Riot Games!!**).

For these reasons, we will be teaching and recommending Godot to be used for LionJam and future game jams!

# Installing Godot

The best way of downloading Godot in my opinion is through the website!

[You can find the download link here!](https://godotengine.org/download)

![image](https://github.com/user-attachments/assets/1d4a7724-d5b4-4969-8d23-bb64309af2df)

You can additionally download it off of Github or Steam but I recommend downloading the latest version from their website since the app is constantly changing and that we you can decide when to update the engine. 

# Exploring the Engine 

<img width="1507" alt="Screenshot 2025-02-05 at 3 55 29 PM" src="https://github.com/user-attachments/assets/5694bced-b5d5-400f-a75f-03ee3560af95" />

Upon opening the engine and creating a new project you should see something like above!

Before we start building lets explore the editor! 

Let us first take a look at the panel on the bottom left.

<img width="275" alt="Screenshot 2025-02-05 at 3 58 37 PM" src="https://github.com/user-attachments/assets/b0f96e4d-ff35-49e5-a88f-50cd96f39d2b" />

This is the file explorer, all the files in our project including our assets (like art, sfx, music, and code) will all be contained in this area. Its up to you how you organize this, but its just to make it easy to find things when working with a lot of files!

res:// is the base directory for your project. If you open the file explorer on your computer and navigate to the place you opened your project in, you should see icon.svg, like we see in the editor!

Epic!!

Next let's take a look at the viewport!

<img width="958" alt="Screenshot 2025-02-05 at 4 02 21 PM" src="https://github.com/user-attachments/assets/e73284cf-c04f-4a63-8f5b-f0966d860d35" />

The viewport is the area shown above. It allows us to see what our game looks like! Once we start adding some stuff to our game we will see the viewport populate. Within the viewport there are a couple of tools to allow you to edit assets on the fly like a scale tool, move tool, and rotate tool. Once you add a camera to your game, it will also show up here so you can see what your game will look like when being played. Last thing to note is there is two version of the viewport, the 2D and 3D version. You can switch between the versions at the top of your screen!

<img width="972" alt="Screenshot 2025-02-05 at 4 09 10 PM" src="https://github.com/user-attachments/assets/c41894e0-4ce9-46bb-895a-b6aba65f1edc" />

The next area we can take a look at is the bottom panel. This is home to some important tools we will use while editing. First is the Output tab. This is where all our error messaegs and print messages will show up - stuff thats pretty important for debugging! Next is the debugger which will let you figure out the values of differnet variables at different times during the run of your game. It will also help you find out where errors are coming from! The audio tab lets you control the volume of different sounds from your game. The animation player is super important - its very powerful. It will probably primarily be used for creating animations though! The shader editor is where you will write shaders for your game!

<img width="269" alt="Screenshot 2025-02-05 at 4 16 09 PM" src="https://github.com/user-attachments/assets/1c63cc8d-f29c-40fa-827b-7e7d9e94830e" />

The last two panels are definitley the most important besides the viewport. First the Hierarchy/Scene Panel is on the left side of the screen. This panel showcases all the **nodes** (we will describe this term soon) that are in the scene. It also shows the hierarchy of nodes (parental relations of objects). Every scene has a root node as a main reference to the scene. It is useful for organizational purposes. Here is what the panel looks like with 1 Node2D in it. 

<img width="272" alt="Screenshot 2025-02-05 at 4 23 47 PM" src="https://github.com/user-attachments/assets/cdcf43ce-e4f4-4b87-a465-82e55037522c" />

The last main panel is the Inspector panel on the right side of the editor. Here we can find all the properties of an object or node like its position, its size, its texture and more! Under the Node tab of the inspector is also a bunch of events also known as **Signals** that can be connected to code when the node is interacted with in certain ways.

<img width="279" alt="Screenshot 2025-02-05 at 4 24 29 PM" src="https://github.com/user-attachments/assets/4b3aca69-bb66-41a3-933d-b4431a6463fb" />

It would also be a good idea to familiarize yourself with the contents of the drop downs at the top of the screen. These are the places where you will be able to change the resolution of your game, save, export, and change the controls. 

<img width="483" alt="Screenshot 2025-02-05 at 4 27 13 PM" src="https://github.com/user-attachments/assets/5091986d-fa67-4263-afbf-71901fc012a2" />

With that, you should be familiar with the layout of the editor!

# Godot Terms

While using Godot, you will come across Nodes and Scenes before working on games with Godot its important to understand what they are and how they work.

## Nodes

In Godot a Node is the base unit object and class. Nodes have base properties and functions. Within Nodes, you can attach scripts that let you program the node and its properties. Additionally, you can attach the signals to functions within the script, allowing them to handle when signals are activated. 

Godot offers a bunch of preset nodes that you will use while making games. The one that will be most important to us is the Node2D. This node features properties such as transform (which is a collection of information such as position, rotation, and scale), it also inherits from the Node base class.

Another example of a Node is a CharacterBody2D node. This node features properties that allow for movement and physics handling. Additionally, it inherits from CollisionObject2D which allows for the node to collide with other collision objects, assuming it has a collision shape. 

Pretty much everything in Godot is a node, so you will see them everywhere! [Heres a video where you can learn about every Node available in Godot!](https://www.youtube.com/watch?v=tO2gthp45MA)

## Scenes

<img width="419" alt="Screenshot 2025-02-05 at 5 06 29 PM" src="https://github.com/user-attachments/assets/2dc9fa8f-cfe1-425a-8529-fb0fe56723c5" />

Now that we know about Nodes, we can explore scenes. Scenes are collections of nodes, with a root node to allow for a hierarchal relationship within the collection. While this relationship allows for organizaiton, it also allows for you to combine different nodes together. The properties of children follow the properties of the parent. For example, if one Node2D is the child of another Node2D, and the parents position is being updated, the child will move around relative to the parent. 

This allows for us to combine nodes to create all sorts of objects. For example, you might use a scene as a collection of nodes that represent a playable character, that will feature a node that controls the animations and a collision shape node and maybe the item the character is holding in its hand.

With a scene like a character, we can then put that scene within another scene like the level. This is called nesting!

The nesting of scenes allows for you to keep your project super organized with each type of object (including menus and UI) having its own scene!

Scenes are another super important topics. [I highly recommend checking out Brackey's Godot intro where he goes super into the scene system!](https://www.youtube.com/watch?v=LOhfqjmasi0)

# Planning out our game!

The game that we will be making for the workshop is a clone of the google dinosaur game! 

https://github.com/user-attachments/assets/f459a610-bea2-45fe-bb45-70a064fe10fe

Here's the assets we are gonna need for our game:
- A sprite for the character
- A jumping sfx for when the character jumps
- A sprite for the ground
- A sprite for the things we are jumping over
- A sprite for the clouds

With all of that, we will be able to bring it all into Godot to make our game!

I have provided some assets that I will be using in the [Github repository](https://github.com/JakasaurusRex/GodotWorkshop)! Feel free to download the assets folder within the dinotime folder!

This section is inspired by the following youtube video by [Coding with Russ](https://www.youtube.com/watch?v=nKBhz6oJYsc&t=2619s)

Here are where the assets are from that we use!
Parallax Background - https://jesse-m.itch.io/jungle-pack
Dinosaur - https://arks.itch.io/dino-characters
Tree stump - https://free-game-assets.itch.io/free-swamp-2d-tileset-pixel-art

# Dino Time!

Make sure to start off with an empty project! 

## Parallax Background

The first thing we are going to do is create our moving background. You may have seen in some games how backgrounds look like they are 3D despite being 2D. Developers accomplish this by using an effect called Parallax. Parallax moves different layers of background images at different speeds to make it look like theres some dimensionalituy to the background. It's easier to undersand in practice so lets check it out!

First thing we want to do is setup this structure of a scene. The parallax background node will be our root node. Then we are going to add in a Sprite2D, this is just a Node2D with a texture property, for the blank background. Once you have added in the Texture2D, add in bg1.png to its texture slot! Additionally, we are gonna turn off the property "Centered" under offset. Next we are going to add in a ParallaxLayer node below our Sprite2D for the blank background. The ordering of the nodes determines the order on the screen, the lower the node is the closer it will be to the front. In the parallax node we just added, we are going to add in another Sprite2D where we can add in the first background texture, bg2.png. We are going to want to uncheck the centered property again here. You also might notice the texture looks a little small and blurry. To fix this, I opened the Node2D Transform property and scaled the image by 3, and then went to the Texture property and changed the filter to nearest. This fixed up our resolution issues!
<img width="259" alt="Screenshot 2025-02-06 at 9 13 39 PM" src="https://github.com/user-attachments/assets/4c2240f6-3ad2-4d56-8c42-aca24b0139ed" />

Now that we have that setup, we should now setup how the background will move. Under the motion properties of our ParallaxLayer lets set the x value of mirroring to 1156 - this value comes from multiplying the width of our texture by 3 because we scaled it by 3. Then we set our scale's x value to 0.6, this is the speed our background will be moving out. Sometimes values in Godot are linked such as the x and y value of the Scale. We can unlink them by clicking the chain icon and then we can just individually change the X value. 

Once we have done this, we can copy and paste the Parallax layer 3 more times for our layered background. After copying and pasting, change the scale values to increase by 0.1 as our layers get closer to the front. When we play our game, we will see how the layers closer to the screen will move faster.

After doing all of that, we are finished with our background! It should look something like below. Let's save it to a scenes folder we can create within our assets folder as background.tscn.
<img width="1512" alt="Screenshot 2025-02-06 at 10 02 31 PM" src="https://github.com/user-attachments/assets/c4437eef-bae8-45b4-92b8-be271799e4fd" />

## Setting up our Dino!

Next we are gonna set up the dinosaur character. First lets create a new scene with a CharacterBody2D as the root node. Then we are going to add in a AnimatedSprite2D, CollisionShape2D, and an AudioStreamPlayer node. It should look like the setup below.

<img width="268" alt="Screenshot 2025-02-06 at 10 12 39 PM" src="https://github.com/user-attachments/assets/a9637817-b78d-4a1d-80dd-553b139aaf45" />

First lets setup the character animations. In our AnimatedSprite2D lets look at the Animation property and create a new SpriteFrames object to store our sprite frames for our character. Then upon opening the SpriteFrames, the animation tab on the bottom appears. Here is where we can add the different animations for our character. We are going to create 3 different animations: idle (for when the character isn't moving), running, and jumping. You can create each new animation by clicking the icon with the green plus in the top left of the animation panel. From there we can add frames to our animations by clicking the icon that looks like the grid. We will import the sprites from our sprite sheet that is in the assets folder. Once you open up the sprite sheet, a popup like this should appear! Make sure to change our Horizontal and Vertical to be 24 and 1 respectively, this is because we have 24 sprites all in 1 row. We will use the first 4 frames for idle, 

<img width="983" alt="Screenshot 2025-02-06 at 10 21 24 PM" src="https://github.com/user-attachments/assets/46a6a5ef-3e0f-480a-a7f4-2e97b48c9bfa" />

After chosing those 4 frames, pick out the next 6 frames for a running animation and one of the frames where the dinosaur has 1 leg up for the jump animation. Once you are done, you should be able to see our dinosaur in the viewport. Once again this texture looks a little blurry so lets fix that up by scaling by 6 and changing the filter mode to nearest. You should now see something like this!

<img width="285" alt="Screenshot 2025-02-06 at 10 27 20 PM" src="https://github.com/user-attachments/assets/e44b05bf-2d0b-45a9-b041-e34836cd5e82" />

Now that we have our animations set up, lets setup our collision shape. This will be used to track when we hit the obstacles in our game! Click on your CollisionShape2D node and add a Rectangle collision shape to the Shape property. Then adjust the size to fit the dinosaur. We should see something like this! With that we are pretty much all set!

<img width="393" alt="Screenshot 2025-02-06 at 10 30 17 PM" src="https://github.com/user-attachments/assets/55ef6e3f-20c7-479f-9718-d211c6e50fa0" />

Last thing to do is setup our jumping sound effect (by the way I made this using [sfxr](https://sfxr.me/))! I changed the name of my AudioStreamPlayer to be JumpSFX and dragged in my wav file into the stream property. With that our character is all good to go for now! Let's save the scene and move on!

## Ground Pound

Next lets create the ground our character will be running on. Similar deal. Lets create a new scene with a StaticBody2D as the root. StaticBodys are useful for floors and walls that don't move! Let's add in a Sprite2D and a CollisionShape2D to our scene. Lets add in our grass floor as the texture for the sprite, scale the StaticBody2D by 3 and fix the resolution on our texture like we have done previously. Next, I dragged my sprite to the bottom of the canvas because thats where our floor is going to be in the game. Then add in a rectangular collision shape to the ground. You may notice that the ground is wider than the canvas size. This will allow us to make it seem like the ground is moving while we are running and we will use it later when we are coding our gameplay loop. Thats all we need to setup for the ground for now. I changed the name of the StaticBody2D to be ground and saved the scene.

<img width="1234" alt="Screenshot 2025-02-06 at 10 43 52 PM" src="https://github.com/user-attachments/assets/52966c56-2ed9-49fe-9957-59eec1800ee2" />

## Creating the Main Scene

Lets now create our main scene where its all gonna come together. First create a new scene with a unit Node as the root node. Next lets add in our dino, ground, and backgrounds scenes. We can do that by clicking the chain button next to the plus sign in the hierarchy. Make sure while adding that they are correctly orded so the dinosaur is in front of the ground, which is in front of the background. Additionally, to make sure the dinosaur is always at the front, we can go back to the dino scene and by clicking the movie icon next to the node and change the Z-Index property in Ordering to be 1. This will ensure that it is positioned in fron of everything that has a Z-Index less than it and everything is 0 by default. After that, lets add a Camera2D node which will allow us to see when we play the game. Change its transform position property to be 576 x and 324 y so that the camera is center on the screen. After doing this, we can save the scene and run the game! You should be able to see all the sprites we just setup on the screen. 

<img width="1511" alt="Screenshot 2025-02-06 at 10 54 42 PM" src="https://github.com/user-attachments/assets/7aff9533-cada-433f-9318-dd843c9b90b0" />

Epic! Lets now add some code to add some movement to our character. Lets go back to the dino scene and lets click the add script button in the hierarchy. Click create and you should get a file that looks like the following. 

<img width="949" alt="Screenshot 2025-02-06 at 11 01 23 PM" src="https://github.com/user-attachments/assets/8c049871-20e6-4ab8-9a75-d36f4c84ffbf" />

This looks a little scary but for those who know Python its also a little familiar. This is GDScript, Godot's programming language. lets go through every line of code and we can learn some things about this language. In the first line of code we are extending from the class CharacterBody2D, inhieriting its functionality. Next, we declare 2 consts SPEED and JUMP_VELOCITY. const is just a value that is unchanging throughout the run of our program, this will be pretty useful for values like speeds we will be adding. Next, we have a function called _physics_process with a parameter delta. The physics_process function is called on every object that has it 60 times a second at least, and delta is the amount of time between the current frame and the last frame. We can use this function to ensure we are consistently performing our physics calculations. Next it looks like we add gravity if the object is not on the floor after multiplying it by delta. Godot offers some cool functions to make physics a lot easier, like the is_on_floor() function. We multiply gravity by delta because its going to be consistently reducing the velocity every frame. The following lines check if the enter key or "ui_accept" is being pressed and if the player is on the floor, if so updates their velocity. The last couple of lines of code allow for you to move left and right. Since we will be moving the background to simulate motion we can delete these, execept the move_and_slide function. move_and_slide takes our newly updated physics values to change the position of the object.

With all of this in mind lets make a couple changes. First lets update our jump velocity to be -500 instead of -400. This will just make us jump higher. We can also delete the speed variable because we are not using it anymore. Lastly, lets create a new @onready variable called jumpsfx and set it = $JumpSFX. What does this mean? @onready means that the variable will be set when the scene is instantiated. $JumpSFX means that we will go into the scene tree and get the node named JumpSFX. What this line of code will be doing will be creating a reference to the jump sfx node in the scene. Then we can do jumpsfx.play() right after we set our jump_velocity. Remember that theres indentation like Python!

<img width="652" alt="Screenshot 2025-02-06 at 11 36 08 PM" src="https://github.com/user-attachments/assets/d750c0b6-3340-4db7-9a77-af12e6bbe2b9" />

Now when we start the game, if you press the enter key you will be able to see the player jump and hear the sfx! 

Next lets change our animations when we press the enter key. Using the same strategy we used for the audio player, lets include our animation player and play the different animations when our character is in different states like below.

<img width="666" alt="Screenshot 2025-02-06 at 11 43 32 PM" src="https://github.com/user-attachments/assets/a35f72cc-418c-4add-a4b3-40bdc511cfaf" />

Now our player will be running when they are on the ground and in the jumping animation after they jump!

We have done a lot here! Lets go setup the stump we are gonna use later as an obstacle!

## Stumpin'

Lets repeat what we did before and create a stump with a collision shape that looks like this. Make sure to fix the resolution and to scale it!
<img width="1230" alt="Screenshot 2025-02-06 at 11 49 12 PM" src="https://github.com/user-attachments/assets/b549ad70-09fc-42ed-9f4e-2f0bdff70194" />

Easy peasy now!

## Loopin'

Lets setup the main gameplay loop now. Lets go back to the main game scene and add a script on the root node. In this node we are going to setup a couple things. First we are going to setup a newgame function that gets called every time the game is started. Then we will setup the process function that gets called every frame, this is where we will move the floor and the background. We are lastly going to setup scoring and obstacles and restarting the game. Heres the code for the first half of what we set to accomplish. Lets add some UI so we can display the score on the screen next. 

```
extends Node

@onready var dino = $Dino
@onready var ground = $Ground
@onready var background = $Background
@onready var camera = $Camera2D

const DINO_START_POS = Vector2i(103, 497)
const CAM_START_POS = Vector2i(576, 324)

var speed : float 
const START_SPEED = 10.0
const MAX_SPEED = 25
var screen_size : Vector2i

var score : int

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	screen_size = get_window().size
	newgame()

func newgame():
	dino.position = DINO_START_POS
	camera.position = CAM_START_POS
	dino.velocity = Vector2i(0,0)
	ground.position = Vector2i(0,0)
	
	speed = START_SPEED
	score = 0 

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	dino.position.x += speed
	camera.position.x += speed
	
	score += speed * 3
	
	if camera.position.x - ground.position.x > screen_size.x * 1.5:
		ground.position.x += screen_size.x
```

Lets create a new scene with a CanvasLayer as the root node. 

<img width="1484" alt="Screenshot 2025-02-07 at 12 23 47 AM" src="https://github.com/user-attachments/assets/be5fc39e-9fdc-4198-b68d-d7307a2dbde5" />

Using the label nodes I created the following UI. Then I linked it to my main scene. 

Combining our new UI with our existing code we can update the scoring and also add speed increasing!

```
extends Node

@onready var dino = $Dino
@onready var ground = $Ground
@onready var background = $Background
@onready var camera = $Camera2D
@onready var ui = $UI

const DINO_START_POS = Vector2i(103, 497)
const CAM_START_POS = Vector2i(576, 324)

var speed : float 
const START_SPEED = 10.0
const MAX_SPEED = 25
const SPEED_CONST =  100000
var screen_size : Vector2i

var score : int
var playing : bool

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	screen_size = get_window().size
	newgame()

func newgame():
	dino.position = DINO_START_POS
	camera.position = CAM_START_POS
	dino.velocity = Vector2i(0,0)
	ground.position = Vector2i(0,0)
	
	ui.get_node("Start").show()
	dino.animator.play("idle")
		
	speed = START_SPEED
	score = 0 
	update_score()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	if playing:
		speed  = min(START_SPEED + score/SPEED_CONST, MAX_SPEED)
		dino.position.x += speed
		camera.position.x += speed
		
		score += speed * 3
		update_score()
		
		if camera.position.x - ground.position.x > screen_size.x * 1.5:
			ground.position.x += screen_size.x
	else:
		if Input.is_action_just_pressed("ui_accept"):
			playing = true
			ui.get_node("Start").hide()
		
		
func update_score():
	ui.get_node("Score").text = "SCORE: " + str(score)
	
```

Now lets add our obstacle to our scene. Heres the code that will do that!

```
extends Node

var stump_asset = preload("res://assets/scenes/stump.tscn")

@onready var dino = $Dino
@onready var ground = $Ground
@onready var background = $Background
@onready var camera = $Camera2D
@onready var ui = $UI

const DINO_START_POS = Vector2i(103, 497)
const CAM_START_POS = Vector2i(576, 324)

var speed : float 
const START_SPEED = 10.0
const MAX_SPEED = 25
const SPEED_CONST =  100000
var screen_size : Vector2i
var ground_height : int

var stumped : bool
var score : int
var playing : bool
var current_stump 

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	screen_size = get_window().size
	ground_height = ground.get_node("Sprite2D").texture.get_height()
	stumped = false
	newgame()

func newgame():
	dino.position = DINO_START_POS
	camera.position = CAM_START_POS
	dino.velocity = Vector2i(0,0)
	ground.position = Vector2i(0,0)
	
	ui.get_node("Start").show()
	dino.animator.play("idle")
		
	speed = START_SPEED
	score = 0 
	update_score()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	if playing:
		speed  = min(START_SPEED + score/SPEED_CONST, MAX_SPEED)
		
		if stumped:
			if(current_stump.position.x < dino.position.x):
				stumped = false
		else:
			create_stump()
		
		dino.position.x += speed
		camera.position.x += speed
		
		score += speed
		
		update_score()
		
		if camera.position.x - ground.position.x > screen_size.x * 1.5:
			ground.position.x += screen_size.x
	else:
		if Input.is_action_just_pressed("ui_accept"):
			playing = true
			ui.get_node("Start").hide()
		
func create_stump():
	var stump = stump_asset.instantiate()
	var stump_height = stump.get_node("Sprite2D").texture.get_height()
	var stump_scale = stump.get_node("Sprite2D").scale
	var stump_x = screen_size.x + score + randi_range(100, 300)
	var stump_y = screen_size.y - ground_height - (stump_height * stump_scale.y * 4) + 12
	stump.position = Vector2i(stump_x, stump_y)
	stumped = true
	add_child(stump)
	current_stump = stump
	
func update_score():
	ui.get_node("Score").text = "SCORE: " + str(score)
	
```

Try out the game and see how the stumps spawn. Now we just have to make sure we can get hit by them! 

With this next code we now have a game over screen that appears when we enter the hitbox of an obstacle!

```
extends Node

var stump_asset = preload("res://assets/scenes/stump.tscn")

@onready var dino = $Dino
@onready var ground = $Ground
@onready var background = $Background
@onready var camera = $Camera2D
@onready var ui = $UI

const DINO_START_POS = Vector2i(103, 497)
const CAM_START_POS = Vector2i(576, 324)

var speed : float 
const START_SPEED = 10.0
const MAX_SPEED = 25
const SPEED_CONST =  100000
var screen_size : Vector2i
var ground_height : int

var stumped : bool
var score : int
var playing : bool
var game_overed : bool
var current_stump 

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	screen_size = get_window().size
	ground_height = ground.get_node("Sprite2D").texture.get_height()
	stumped = false
	game_overed = false
	newgame()

func newgame():
	dino.position = DINO_START_POS
	camera.position = CAM_START_POS
	dino.velocity = Vector2i(0,0)
	ground.position = Vector2i(0,0)
	
	stumped = false
	if(current_stump):
		current_stump.queue_free()
		current_stump = null
	
	ui.get_node("Start").text = "Press Enter to Play"
	ui.get_node("Start").show()
	dino.animator.play("idle")
		
	speed = START_SPEED
	score = 0 
	update_score()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	if playing:
		speed  = min(START_SPEED + score/SPEED_CONST, MAX_SPEED)
		
		if stumped:
			if(current_stump.position.x < dino.position.x):
				stumped = false
		else:
			create_stump()
		
		dino.position.x += speed
		camera.position.x += speed
		
		score += speed
		
		update_score()
		
		if camera.position.x - ground.position.x > screen_size.x * 1.5:
			ground.position.x += screen_size.x
	elif(game_overed):
		if Input.is_action_just_pressed("ui_accept"):
			newgame()
			game_overed = false
	else:
		if Input.is_action_just_pressed("ui_accept"):
			playing = true
			ui.get_node("Start").hide()
		
func create_stump():
	var stump = stump_asset.instantiate()
	var stump_height = stump.get_node("Sprite2D").texture.get_height()
	var stump_scale = stump.get_node("Sprite2D").scale
	var stump_x = screen_size.x + score + randi_range(400, 600)
	var stump_y = screen_size.y - ground_height - (stump_height * stump_scale.y * 4) + 12
	stump.position = Vector2i(stump_x, stump_y)
	stumped = true
	stump.body_entered.connect(hit_stump)
	add_child(stump)
	current_stump = stump
	
func hit_stump(body):
	if(body.name == "Dino"):
		game_over()
		
func game_over():
	playing = false
	game_overed = true
	ui.get_node("Start").text = "GAME OVER - press enter to start over"
	ui.get_node("Start").show()
	
func update_score():
	ui.get_node("Score").text = "SCORE: " + str(score)
	
```
