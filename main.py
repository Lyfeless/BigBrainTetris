import pyglet
from pyglet.window import key

"""

    DEFINITIONS

"""

# Pyglet Elements

window = pyglet.window.Window()
text = pyglet.text.Label("Yo bro thats ficc",
                         font_name = "Comic Sans MS",
                         font_size = 17,
                         color = (255,255,0,255),
                         anchor_x = "center", anchor_y = "center")

# "CONSTANTS"

BOARD_WIDTH = 10
BOARD_HEIGHT = 20
TILE_SIZE = 30

# Board

board = [[0 for x in range(BOARD_WIDTH)] for x in range(BOARD_HEIGHT)]

# Input

inputs = {key.UP    :  False,
          key.LEFT  :  False,
          key.RIGHT :  False,
          key.DOWN  :  False}

# Position

text_x = window.width/2
text_y = window.height/2

"""

    FUNCTIONS

"""

def update(dt):
    global text
    global text_x
    global text_y

    text.x = text_x
    text.y = text_y

    if inputs[key.UP]:
        text_y += 1
    if inputs[key.DOWN]:
        text_y -= 1
    if inputs[key.RIGHT]:
        text_x += 1
    if inputs[key.LEFT]:
        text_x -= 1


"""

    EVENTS

"""

@window.event
def on_draw():
    window.clear()
    text.draw();

@window.event
def on_key_press(symbol, modifiers):
    inputs[symbol] = True
    print("pressed " + str(symbol))
    
@window.event
def on_key_release(symbol, modifiers):
    inputs[symbol] = False
    print("depressed " + str(symbol))

"""

    RUNTIME

"""

window.set_size(BOARD_WIDTH * TILE_SIZE, BOARD_HEIGHT * TILE_SIZE)

pyglet.clock.schedule_interval(update,1/120.0)
pyglet.app.run() # Run
