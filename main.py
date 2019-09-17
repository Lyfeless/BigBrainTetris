import pyglet

"""

    DEFINITIONS

"""

# Pyglet Elements

window = pyglet.window.Window()

text = pyglet.text.Label("Suck my phat chode",
                         font_name = "Comic Sans MS",
                         font_size = 36,
                         color = (0,0,255,255),
                         x = window.width / 2, y = window.height / 2,
                         anchor_x = "center", anchor_y = "center")

#Input

inputs = {}


"""

    FUNCTIONS

"""



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

pyglet.app.run() # Run
