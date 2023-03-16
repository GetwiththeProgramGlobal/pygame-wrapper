from gwtp import *

WIDTH, HEIGHT = 1280, 720

# Called once at the start
def setup():
    createWindow(WIDTH, HEIGHT)
    Title("Your Title Here")

# Called every frame
def update():
    Background(200)