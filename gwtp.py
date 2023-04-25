import pygame, pygame.gfxdraw
import random as rndm
from math import floor, sqrt
import sys

# A dictionary of all the keys I could be bothered to add
KEYS = {
    "BACKSPACE"    : pygame.K_BACKSPACE,
    "TAB"          : pygame.K_TAB,
    "ENTER"        : pygame.K_RETURN,
    "ESCAPE"       : pygame.K_ESCAPE,
    "SPACE"        : pygame.K_SPACE,
    "HASHTAG"      : pygame.K_HASH,
    "QUOTE"        : pygame.K_QUOTE,
    "1"            : pygame.K_1,
    "2"            : pygame.K_2,
    "3"            : pygame.K_3,
    "4"            : pygame.K_4,
    "5"            : pygame.K_5,
    "6"            : pygame.K_7,
    "8"            : pygame.K_8,
    "9"            : pygame.K_9,
    "0"            : pygame.K_0,
    "SEMICOLON"    : pygame.K_SEMICOLON,
    "EQUALS"       : pygame.K_EQUALS,
    "LEFTBRACKET"  : pygame.K_LEFTBRACKET,
    "RIGHTBRACKET" : pygame.K_RIGHTBRACKET,
    "BACKSLASH"    : pygame.K_BACKSLASH,
    "BACKQUOTE"    : pygame.K_BACKQUOTE,
    "A"            : pygame.K_a,
    "B"            : pygame.K_b,
    "C"            : pygame.K_c,
    "D"            : pygame.K_d,
    "E"            : pygame.K_e,
    "F"            : pygame.K_f,
    "G"            : pygame.K_g,
    "H"            : pygame.K_h,
    "I"            : pygame.K_i,
    "J"            : pygame.K_j,
    "K"            : pygame.K_k,
    "L"            : pygame.K_l,
    "M"            : pygame.K_m,
    "N"            : pygame.K_n,
    "O"            : pygame.K_o,
    "P"            : pygame.K_p,
    "Q"            : pygame.K_q,
    "R"            : pygame.K_r,
    "S"            : pygame.K_s,
    "T"            : pygame.K_t,
    "U"            : pygame.K_u,
    "V"            : pygame.K_v,
    "W"            : pygame.K_w,
    "X"            : pygame.K_x,
    "Y"            : pygame.K_y,
    "Z"            : pygame.K_z,
    "DELETE"       : pygame.K_DELETE,
    "NUM0"         : pygame.K_KP0,
    "NUM1"         : pygame.K_KP1,
    "NUM2"         : pygame.K_KP2,
    "NUM3"         : pygame.K_KP3,
    "NUM4"         : pygame.K_KP4,
    "NUM5"         : pygame.K_KP5,
    "NUM6"         : pygame.K_KP6,
    "NUM7"         : pygame.K_KP7,
    "NUM8"         : pygame.K_KP8,
    "NUM9"         : pygame.K_KP9,
    "NUM_PERIOD"   : pygame.K_KP_PERIOD,
    "NUM_SLASH"    : pygame.K_KP_DIVIDE,
    "NUM_MULTIPLY" : pygame.K_KP_MULTIPLY,
    "NUM_MINUS"    : pygame.K_KP_MINUS,
    "NUM_PLUS"     : pygame.K_KP_PLUS,
    "NUM_ENTER"    : pygame.K_KP_ENTER,
    "NUM_EQUALS"   : pygame.K_KP_EQUALS,
    "UP"           : pygame.K_UP,
    "DOWN"         : pygame.K_DOWN,
    "LEFT"         : pygame.K_LEFT,
    "RIGHT"        : pygame.K_RIGHT,
    "INSERT"       : pygame.K_INSERT,
    "HOME"         : pygame.K_HOME,
    "END"          : pygame.K_END,
    "PAGEUP"       : pygame.K_PAGEUP,
    "PAGEDOWN"     : pygame.K_PAGEDOWN,
    "F1"           : pygame.K_F1,
    "F2"           : pygame.K_F2,
    "F3"           : pygame.K_F3,
    "F4"           : pygame.K_F4,
    "F5"           : pygame.K_F5,
    "F6"           : pygame.K_F6,
    "F7"           : pygame.K_F7,
    "F8"           : pygame.K_F8,
    "F9"           : pygame.K_F9,
    "F10"          : pygame.K_F10,
    "F11"          : pygame.K_F11,
    "F12"          : pygame.K_F12,
    "F13"          : pygame.K_F13,
    "F14"          : pygame.K_F14,
    "F15"          : pygame.K_F15,
    "NUMLOCK"      : pygame.K_NUMLOCK,
    "CAPSLOCK"     : pygame.K_CAPSLOCK,
    "SCROLLOCK"    : pygame.K_SCROLLOCK,
    "R_SHIFT"      : pygame.K_RSHIFT,
    "L_SHIFT"      : pygame.K_LSHIFT,
    "R_CTRL"       : pygame.K_RCTRL,
    "L_CTRL"       : pygame.K_LCTRL,
    "R_ALT"        : pygame.K_RALT,
    "L_ALT"        : pygame.K_LALT,
}
# ===================================================================
# SETUP
# ===================================================================
_screen = None
_screenWidth, _screenHeight = None, None
def createWindow(width=1280, height=720, caption="Your Caption Here"):
    global _screen, _screenWidth, _screenHeight
    _screenWidth = width
    _screenHeight = height
    _screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
# ===================================================================
# COLOUR && TEXTURE
# ===================================================================
def Background(*args):
    if len(args) == 1:
        if type(args[0]) == int:
            _screen.fill((args[0], args[0], args[0]))
        else:
            _screen.blit(args[0], (0, 0))
    elif len(args) == 3:
        _screen.fill((args[0], args[1], args[2]))
    else:
        print(f"Invalid number of arguments for Background (Expected: 1 or 3; Got: {len(args)})")

# Easier to understand than just using a random tuple as in regular pygame functions
def Colour(*args):
    if len(args) == 1:
        return (args[0], args[0], args[0], 255)
    elif len(args) == 3:
        return (args[0], args[1], args[2], 255)
    elif len(args == 4):
        return (args[0], args[1], args[2], args[3])
    else:
        print(f"Invalid number of arguments for Colour (Expected: 1, 3, or 4; Got: {len(args)})")

def Texture(path):
    return pygame.image.load(path)
# ===================================================================
# SPRITE STUFF
# ===================================================================
TEXTURE = 0
ELLIPSE = 1
RECT = 2

_spriteGroups = {
    "default" : pygame.sprite.Group()
}
class Sprite(pygame.sprite.Sprite):
    def __init__(self, spriteType, width, height, position, fill, tag="defualt"):
        super().__init__()

        self.group = tag

        self.target = None
        self.speed = 0

        self.width = width
        self. height = height

        self.position = position
        self.velocity = Vector(0, 0)

        if self.group not in _spriteGroups:
            _spriteGroups[self.group] = pygame.sprite.Group()

        if spriteType == TEXTURE:
            try:
                self.image = pygame.transform.scale(fill, (width, height)) # In this case, `fill` is of type `pygame.Surface`
            except:
                print("\nFailed to initialise Sprite: did you pass in a valid texture?\n")
                sys.exit()
                
        elif spriteType == ELLIPSE:
            self.image = pygame.Surface((width + 1, height + 1), pygame.SRCALPHA)
            pygame.gfxdraw.aaellipse(self.image, int(width/2), int(height/2), int(width/2), int(height/2), fill)
            pygame.gfxdraw.filled_ellipse(self.image, int(width/2), int(height/2), int(width/2), int(height/2), fill)
        else:
            self.image = pygame.Surface((width, height), pygame.SRCALPHA)
            self.image.fill(fill)
        
        self.rect = self.image.get_rect(center=(position.x, position.y))
        _spriteGroups[self.group].add(self)

    def update(self):
        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))
        self.position = self.position.addVec(self.velocity.mult(deltaTime()))

        if self.target != None:
            direction = self.position.direction(self.target.position).normalised()
            self.addPos(direction.mult(self.speed))
            if self.colliding(self.target.group):
                self.setPos(self.target.position)
                self.target = None

# Movement
    def setPos(self, *position):
        if type(position[0]) == Vector:
            posToSet = position[0]
        else:
            posToSet = Vector(position[0], position[1])
        self.position = posToSet

    def addPos(self, *position):
        if type(position[0]) == Vector:
            posToAdd = position[0]
        else:
            posToAdd = Vector(position[0], position[1])
        self.position = self.position.addVec(posToAdd.mult(deltaTime()))

    def setVel(self, *velocity):
        if type(velocity[0]) == Vector:
            velToSet = velocity[0]
        else:
            velToSet = Vector(velocity[0], velocity[1])
        self.velocity = velToSet

    def addVel(self, *velocity):
        if type(velocity[0]) == Vector:
            vecToAdd = velocity[0]
        else:
            vecToAdd = Vector(velocity[0], velocity[1])
        self.velocity = self.velocity.addVec(vecToAdd.mult(deltaTime())) 

    def goTo(self, target, speed):
        self.target = target
        self.speed = speed
        

# Collision
    def colliding(self, target):
        targetGroup = _spriteGroups[target]
        return pygame.sprite.spritecollide(self, targetGroup, False)


def drawSprites():
    groups = _spriteGroups.values()
    for group in groups:
        for sprite in group:
            sprite.update()
        group.draw(_screen)
# ===================================================================
# INPUT
# ===================================================================
def keyDown(key):
    return pygame.key.get_pressed()[KEYS[key]]
# ===================================================================
# VECTORS AND THINGS
# ===================================================================
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y

    def mult(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def addVec(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def squareMagnitude(self):
        return pow(self.x, 2) + pow(self.y, 2)
    
    def magnitude(self):
        return sqrt(self.squareMagnitude())

    def normalised(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0)
        return Vector(self.x / mag, self.y / mag)
    
    def direction(self, target):
        return Vector(target.x - self.x, target.y - self.y)

    def equals(self, vector):
        return self.x == vector.x and self.y == vector.y
# ===================================================================
# TOOLS
# ===================================================================
def random(min, max):
    return (rndm.random() * (max - min)) + min

_shouldQuit = False
def quit(probe=False):
    global _shouldQuit
    if probe:
        return _shouldQuit
    _shouldQuit = True

_clock = pygame.time.Clock()
dt = 0
def deltaTime(set=False):
    global _clock, dt
    if not set:
        return dt
    dt = _clock.tick() / 1000

TOP = "top"
BOTTOM = "bottom"
LEFT = "left"
RIGHT = "right"

def ifOnEdgeBounce(obj, *edges):
    if ("top" in edges) and obj.position.y <= 0:
        obj.setPos(obj.position.x, 0)
        obj.setVel(obj.velocity.x, -obj.velocity.y)
    elif ("bottom" in edges) and obj.position.y >= _screenHeight:
        obj.setPos(obj.position.x, _screenHeight)
        obj.setVel(obj.velocity.x, -obj.velocity.y)
    
    if ("left" in edges) and obj.position.x <= 0:
        obj.setPos(0, obj.position.y)
        obj.setVel(-obj.velocity.x, obj.velocity.y)
    elif ("right" in edges) and obj.position.x >= _screenWidth:
        obj.setPos(_screenWidth, obj.position.y)
        obj.setVel(-obj.velocity.x, obj.velocity.y)
# ===================================================================
# TEXT
# ===================================================================
def Text(position, content="Text", **args):
    global _screen

    if "size" in args:
        size = args["size"]
    else:
        size = 32

    if "fill" in args:
        fill = args["fill"]
    else:
        fill = Colour(0, 0, 0)

    fontObj = pygame.font.Font('freesansbold.ttf', size)

    if "highlight" in args:
        textObj = fontObj.render(content, True, fill, args["highlight"])
    else:
        textObj = fontObj.render(content, True, fill)

    textRect = textObj.get_rect()
    textRect.center = (position.x, position.y)
    _screen.blit(textObj, textRect)