import pygame
import random as rndm
from math import floor

screen = None
clock = pygame.time.Clock()
dt = 0

spriteGroup = pygame.sprite.Group()

shouldQuit = False

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
    "KP0"          : pygame.K_KP0,
    "KP1"          : pygame.K_KP1,
    "KP2"          : pygame.K_KP2,
    "KP3"          : pygame.K_KP3,
    "KP4"          : pygame.K_KP4,
    "KP5"          : pygame.K_KP5,
    "KP6"          : pygame.K_KP6,
    "KP7"          : pygame.K_KP7,
    "KP8"          : pygame.K_KP8,
    "KP9"          : pygame.K_KP9,
    "KP_PERIOD"    : pygame.K_KP_PERIOD,
    "KP_SLASH"     : pygame.K_KP_DIVIDE,
    "KP_MULTIPLY"  : pygame.K_KP_MULTIPLY,
    "KP_MINUS"     : pygame.K_KP_MINUS,
    "KP_PLUS"      : pygame.K_KP_PLUS,
    "KP_ENTER"     : pygame.K_KP_ENTER,
    "KP_EQUALS"    : pygame.K_KP_EQUALS,
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

# SETUP
# ===================================================================
def createWindow(width=1280, height=720):
    global screen
    screen = pygame.display.set_mode((width, height))

def title(content):
    pygame.display.set_caption(content)
# ===================================================================
# DELTATIME
# ===================================================================
def deltaTime(set=False):
    global clock, dt
    if not set:
        return dt
    dt = clock.tick() / 1000
# ===================================================================
# COLOUR
# ===================================================================
def background(red, green, blue):
    screen.fill((red, green, blue))

# Easier to understand than just using a random tuple as in regular pygame functions
def colour(red, green, blue, alpha=255):
    return (red, green, blue, alpha)
# ===================================================================
# Sprite Stuff
# ===================================================================
def circle(position, radius, fill):
    pygame.draw.circle(screen, fill, (int(position.x), int(position.y)), radius)

def rect(position, width, height, fill):
    pygame.draw.rect(screen, fill, (int(position.x), int(position.y), width, height))
# ===================================================================
# INPUT
# ===================================================================
def keyDown(key):
    return pygame.key.get_pressed()[KEYS[key]]
# ===================================================================
# VECTORS AND THINGS
# ===================================================================
class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y
# ===================================================================
# Tools
# ===================================================================
def random(min = 0, max = 1):
    return (rndm.random() * (max - min)) + min

def quit(probe=False):
    global shouldQuit
    if probe:
        return shouldQuit
    shouldQuit = True
# ===================================================================
# Text
# ===================================================================
def text(position, content="Text", size=32, fill=colour(255, 255, 255), highlight=colour(0, 0, 0)):
    global screen

    fontObj = pygame.font.Font('freesansbold.ttf', size)
    textObj = fontObj.render(content, True, fill, highlight)
    textRect = textObj.get_rect()
    textRect.center = (position.x, position.y)
    screen.blit(textObj, textRect)