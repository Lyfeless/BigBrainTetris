import pyglet

window = pyglet.window.Window()

text = pyglet.text.Label("Suck my phat chode",
                         font_name = "Comic Sans MS",
                         font_size = 36,
                         color = (0,0,255,255),
                         x = window.width / 2, y = window.height / 2,
                         anchor_x = "center", anchor_y = "center")

@window.event
def on_draw():
    window.clear()
    text.draw();

pyglet.app.run()
