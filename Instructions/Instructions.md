# Instructions

#### This is a very very early prototype of some instructions for a task. The actual instructions would have an accompanying video and a reference to look up a more in-depth explanation of the various functions available. Testy people don't bother doing the `Extra:` bits, that was just me trying to come up with stuff.
___
### The Template

Inside `project.py`, you will see a statement that imports everything from our library. 

Below that are two constants: `WIDTH` and `HEIGHT`, which represent the width and height of our game window. Feel free to change these if you wish. 

Below this, you will see the `setup()` procedure. This procedure is called once when we first run our game and contains:
* A `createWindow()` function with our `WIDTH` and `HEIGHT` constants as parameters. This is what we use to create a window for our game to run in.
* A `Title()` function which we use to give our window a name. Feel free to change the name.

Finally, you will see the `update()` procedure. This procedure is called once every frame while our game is running. We will add more to this later but for now it contains the `Background()` function. Feel free to change the colour.
___
### Step 1

You might have come across sprites if you've used scratch before. Sprites are used to represent an 'object' with 'attributes' such as position or speed.

We are going to create a sprite called `player` which will represent our paddle. It needs to:
* be rectangular,
* have a longer width and a shorter height,
* be positioned in the middle of the screen, a bit up from the bottom,
* and have a colour to distinguish it from the background.

we can do this like this: 
```python
player = Sprite(RECT, 200, 30, Vector(WIDTH / 2, HEIGHT - 60), Colour(255))
```
* The first arument, `RECT` tells the sprite to be rectangular.
* The next 2 arguments are the `width` and `height` of the sprite in pixels. I've chosen `200` by `30`.
* Next, the `position` of the sprite is given by a `Vector()` (a data structure that holds 2 numbers). I've chosen the `x` position to be `WIDTH / 2` (i.e. the centre), and the `y` position to be `HEIGHT - 60`, or '60 pixels above the bottom'
* Next, I've used the `Colour` function to set the colour to `255` (white)
* Finally, go down to the `update()` function and add `drawSprites()` to it like so:
```python
def update():
    Background(0)

    drawSprites()
```

If you now run the game you should see a white rectangle on the screen.

#### Extra:
* Try changing the `RECT` to `ELLIPSE`... What happens?
___
### Step 2

Now we are going to add our own function to handle the movement of the player.

First, we are going to define the function using the `def` keyword, then give it a name followed by some empty brackets and a colon. I'm going to call mine `playerMovement()`, so I would write `def playerMovement():`

Next, inside the function, we need to do a few things:
1. We need to check if the user has pressed the `A` key, *and* if the player sprite isn't off the left edge of the screen; then move the player to the left.
2. We need to check if the user has pressed the `D` key, *and* if the player sprite isn't off the right edge of the screen; then move the player to the right.

Doing so looks like this:
```python
def playerMovement():
    if keyDown("A") and player.position.x > player.size.x / 2:
        player.addPs(-500, 0)
    if keyDown("D") and player.position.x < WIDTH - player.size.x / 2:
        player.addPos(500, 0)
```
* Each if statement checks whether the user has pressed a specific key, and that the player isn't on the edge of the screen.
* Then inside the if statement, we change the `x` position of the player by `500` or `-500` depending on whether we want to move left or right

Finally, add a call to `playerMovement()` into the `update()` function so the movement gets updated every frame. Try running the game and pressing the `A` and `D` keys to move left and right.

#### Extra:
* Try changing each `player.size.x / 2` to `0`... What happens?
* Try changing the numbers within each `player.addPos()`... What happens?
___
### Step 3

Now we are going to create a sprite for the ball using the image `ball.png` that we have provided in the `assets` folder. This looks as so: 
```python
ball = Sprite(TEXTURE, 45, 45, Vector(WIDTH/2, 50), Texture("assets/ball.png"))
```
In this, we have:
* created a variable `ball` and assigned it to a `Sprite()`,
* told it to be a `TEXTURE`,
* set it's `width` and `height` to `45` because we want it to be circular,
* set it's position to the centre and a bit below the top using another `Vector()`,
* and told it to use the ball image as its texture using `Texture()`

If you now run this, you should see an image of a football at the top of your screen.

#### Extra:
* Try changing the `width` and `height` values... What happens?
___
### Step 4

After we've created the `ball` sprite, we can create the logic to move it.

First, we are going to give the ball a random initial velocity. To do so, inside the `setup()` function, add the line `ball.setVel(random(-125, 125), 0)`

After that, we are going to create a variable `score` and set it to `0`, and a constant `GRAVITY` which we will set to `405`. Next, we will create another function as with the player. For example, `def ballMovement():`. Inside the function we can type `global score` to let the function know that we want to use our score variable inside it.

Because we want the ball to fall, we need to use 2 functions:
1. `addVel()` which changes the sped of the ball, and
1. `addPos()` which we used earlier and changes the position of the ball

First we can add `GRAVITY` to the speed of the ball like so: `ball.addVel(0, GRAVITY)`. Then, we can change the ball's position like so: `ball.addPos(ball.velocity)`. This will cause the ball to accelerate as it falls like in real life

If we were to run the game now, the ball would just fall off the screen and be lost forever, so we need to create:
1. Our own version of Scratch's `If On Edge Bounce` block to stop the ball from falling off the sides.
2. Some logic to allow the player to bounce the ball back upwards 

For our `If On Edge Bounce` implementation, we first need to do two things:
1. Check if the ball is going to go off the edge
2. Reverse it's direction to cause it to 'bounce'

For the first step we are going to need an if/elif statement:
```python
if ball.position.x >= WIDTH:
    # Bounce
elif ball.position.y <= 0:
    # Bounce the other way
```

Inside the `if` statement we can set the ball's position to `WIDTH` using `setWidth()` (in case it's gone past the right-hand screen edge since we last checked), then flip the direction of the ball using `setVel()`. In the `elif` statement we can do the same but with `0` instead of `WIDTH` for the left-hand side of the screen like so:
```python
if ball.position.x >= WIDTH:
    ball.setPos(WIDTH, ball.position.y)
    ball.setVel(-ball.velocity.x, ball.velocity.y)
elif ball.position.x <= 0:
    ball.setPos(0, ball.position.y)
    ball.setVel(-ball.velocity.x, ball.velocity.y)
```

#### Extra:
* Try changing the numbers of our initial velocity... What happens?
* Try changing the value of `GRAVITY`... What happens?
___
### Step 5

Now we can add a way for the player to bounce the ball back upwards. To do this we need to check if the position of the ball is within the 'paddle'. This looks like so: 
```python
if ball.position.x >= player.position.x - player.size.x/2 and ball.position.x <= player.position.x + player.size.x/2 and ball.position.y >= player.position.y - player.size.y/2 and ball.position.y <= player.position.y + player.size.y/2: 
```
This checks if the ball's `x` position is within the left side *and* the right side of the 'paddle', *and* that the ball's `y` position is within the top side *and* the bottom side of the 'paddle'. Inside the if statement, we can then decide what we want to happen once all the conditions are met.

1. First, we want to set the ball's position to the top of the paddle (for the same reason we set the ball's position to the edge earlier) using `setPos()`,
2. Next, we want to keep the ball's `x`-velocity the same but with a random value added using `random()` to make the game a bit less boring,
3. After, we want to flip the ball's `y`-velocity as this will cause it to 'bounce'.
4. Lastly, we want to increase `score` by `1` because the player has successfully bounced the ball

These 4 steps look like this:
```python
# The if statement from earlier
    ball.setPos(ball.position.x, player.position.y - player.size.y/2) # Step 1
    ball.setVel(ball.velocity.x + random(-125, 125), -ball.velocity.y) # Steps 2 && 3 
    score += 1 # Step 4
```

Finally, we can add one last `if` statement to check whether the player has dropped the ball. If the ball is below the bottom of the screen, we want to set its velocity to `0`, and display some text to tell the player they've lost. We can do this using `setVel()`, and a `Text()`. We need to give our text a position (using a `Vector()`), and a `String` of text. The final `if` statement should look as below:
```python
if ball.position.y >= HEIGHT:
        ball.setVel(0, 0)
        text(Vector(WIDTH/2, 100), "You Loose!")
```

Inside the `update()` function, we now need to call `updateBall()`. We can also add some text to display the score using another `Text()`. Your `update()` function should now look similar to this:
```python
def update():
    Background(23, 140, 211)

    updatePlayer()
    updateBall()

    drawSprites()

    text(Vector(WIDTH/2, 50), f"Score: {score}")
```
___
# Fin

#### Imagine some further challenges etc.