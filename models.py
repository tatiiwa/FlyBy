import arcade.key
import random
from random import randint

MOVE_VY = 10
MAX_VY = 10
WIND = 1
MAGNET = -1


class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y

class Dot(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
        self.vx = 0
        self.vy = 0
        self.is_move = False

        self.platform = None

    def move(self):

        if not self.is_move:
            self.is_move = True
            self.vy = MOVE_VY

    def animate(self, delta):
        if self.vy < MAX_VY:
            self.vy += WIND

        self.y += self.vy

        if self.is_move:
            self.x += self.vx
            self.vy += MAGNET

            

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.dot = Dot(self, 0, 120)
        self.init_platforms()

        self.dot.set_platform(self.platforms[0])

        self.score = 0

    def animate(self, delta):
        self.dot.animate(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.dot.jump()
