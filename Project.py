from PgLib import *

WIDTH, HEIGHT = 1280, 720

# Called once at the start
def setup():
    createWindow(WIDTH, HEIGHT, False)
    title("Your Title Here")

# Called every frame
def update():
    background(0, 0, 0)