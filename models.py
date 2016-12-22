import arcade.key

class Ship:
    Stay = 0
    Forward = 1
    Left = -1

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = Ship.Forward
        self.angle = 0

    def switch_direction(self):
            self.direction = Ship.Stay
            self.angle = -90

    def switch_direction2(self):
            self.direction = Ship.Left
            self.angle = 90

    def switch_direction3(self):
            self.direction = Ship.Forward
            self.angle = 0


    def animate(self, delta):
        if self.direction == Ship.Forward:
            if self.y > self.world.height:
                self.y = 0
            self.y += 5
        else:
            if self.x > self.world.width:
                self.x = 0
            self.x += 5
        if self.direction == Ship.Left:
            if self.y > self.world.height:
                self.y = 0
            self.y += 5
        else:
            if self.x == 0:
                self.x = self.world.width
            self.x -= 5



class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.ship = Ship(self, 100, 100)


    def animate(self, delta):
        self.ship.animate(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.D:
            self.ship.switch_direction()
        if key == arcade.key.A:
            self.ship.switch_direction2()
        if key == arcade.key.W:
            self.ship.switch_direction3()
