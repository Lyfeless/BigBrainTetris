import random
import math

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

MOVE_SPEED = 4

# Board

board = []
movingBlocks = []

timer = 0

# Images

blockBatch = pyglet.graphics.Batch()
moveBatch = pyglet.graphics.Batch()

blockImg = pyglet.image.load('Assets/Tetromino Block.png')
blockTexture = blockImg.get_texture()
blockImg.width = TILE_SIZE
blockImg.height = TILE_SIZE
blockTexture.width = TILE_SIZE
blockTexture.height = TILE_SIZE

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

    global board
    global timer

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

    timer += 1

    if timer > 20:
        timer = 0
        block_x = random.randint(0, len(board[0]) - 1) * TILE_SIZE
        block_y = len(board) * TILE_SIZE
        addMoveBlock(block_x, block_y, block_x, block_y - TILE_SIZE, MOVE_SPEED)

        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x].visible == True and y > 0 and board[y - 1][x].visible == False:
                    addMoveBlock(x * TILE_SIZE, y * TILE_SIZE, x * TILE_SIZE, (y - 1) * TILE_SIZE, MOVE_SPEED)
        

    for moveBlock in movingBlocks:
        moveBlock.update()

def addMoveBlock(x, y, target_x, target_y, scale):
    movingBlocks.append(MoveBlock(x, y, target_x, target_y, scale, blockImg))

"""

    CLASSES

"""

class MoveBlock:
    def __init__(self, x, y, target_x, target_y, scale, image):
        global board
        
        self.x        =  x
        self.y        =  y
        self.target_x =  target_x
        self.target_y =  target_y
        self.scale    =  scale
        self.sprite   =  pyglet.sprite.Sprite(image, self.x, self.y, batch = moveBatch)


        tile_x = math.ceil(self.x / TILE_SIZE)
        tile_y = math.ceil(self.y / TILE_SIZE)

        if (tile_x >= 0 and tile_x < len(board[0])) and (tile_y >= 0 and tile_y < len(board)):
            board[tile_y][tile_x].visible = 0

    def update(self):
        global board
        global movingBlocks

        distance_x = (self.target_x - self.x)
        distance_y = (self.target_y - self.y)

        self.x += distance_x / self.scale
        self.y += distance_y / self.scale

        self.sprite.x = self.x
        self.sprite.y = self.y

        if abs(distance_x) < 1 and abs(distance_y) < 1:
            
            tile_x = math.ceil(self.x / TILE_SIZE)
            tile_y = math.floor(self.y / TILE_SIZE)
            
            if (tile_x >= 0 and tile_x < len(board[0])) and (tile_y >= 0 and tile_y < len(board)):
                board[tile_y][tile_x].visible = 1
                
            movingBlocks.remove(self)
            

"""

    EVENTS

"""

@window.event
def on_draw():
    window.clear()
    text.draw();
    blockBatch.draw()
    moveBatch.draw()
    #blockImg.blit(0,0)

@window.event
def on_key_press(symbol, modifiers):
    inputs[symbol] = True
    
@window.event
def on_key_release(symbol, modifiers):
    inputs[symbol] = False

"""

    RUNTIME

"""

window.set_size(BOARD_WIDTH * TILE_SIZE, BOARD_HEIGHT * TILE_SIZE)

board  = [[pyglet.sprite.Sprite(blockImg, x * TILE_SIZE, y * TILE_SIZE, batch=blockBatch) for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]

for y in range(len(board)):
    for x in range(len(board[y])):
        if random.randint(0, 1) == 1:
            board[y][x].visible = False
        else:
            board[y][x].visible = False

#board[0][0].visible = True
#board[1][0].visible = True


movingBlocks.append(MoveBlock(0, TILE_SIZE, TILE_SIZE * 5, TILE_SIZE * 7, 12, blockImg))

pyglet.clock.schedule_interval(update,1/120.0)
pyglet.app.run() # Run
