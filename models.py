import arcade.key
import random

class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)

class Paper(Model):
    Right = 0
    Forward = 1
    Left = -1

    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

        self.direction = Paper.Forward


    def switch_direction(self):
            self.direction = Paper.Right
            self.angle = -90

    def switch_direction2(self):
            self.direction = Paper.Left
            self.angle = 90

    def switch_direction3(self):
            self.direction = Paper.Forward
            self.angle = 0


    def animate(self, delta):
        if self.direction == Paper.Forward:
            if self.y > self.world.height:
                self.y = 0
            self.y += 2
            self.x -= 2

        elif self.direction == Paper.Right:
            if self.x > self.world.width:
                self.x = 0
            self.x += 3
            self.y += 1
        elif self.direction == Paper.Left:
            if self.x == 0:
               self.x = self.world.width
            self.x -= 3
            self.y += 1

class Building(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.life = 5

        self.paper = Paper(self, 100, 100)
        self.building = []
        for i in range (0,4):
            self.building.append(Building(self, 100*(i+1), 100*(i+1)))


    def animate(self, delta):
        self.paper.animate(delta)
        for i in range (0,4):
            if len(self.building) > 0 and self.paper.hit(self.building[i], 15):
                self.life -= 1

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.D:
            self.paper.switch_direction()
        if key == arcade.key.A:
            self.paper.switch_direction2()
        if key == arcade.key.W:
            self.paper.switch_direction3()
