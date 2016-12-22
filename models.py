import arcade.key

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
            self.y += 5
        elif self.direction == Paper.Right:
            if self.x > self.world.width:
                self.x = 0
            self.x += 5
        elif self.direction == Paper.Left:
            if self.x == 0:
               self.x = self.world.width
            self.x -= 5

class Building(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.life = 5

        self.paper = Paper(self, 100, 100)
        self.building = Building(self, 400, 400)

    def animate(self, delta):
        self.paper.animate(delta)
        if self.paper.hit(self.building, 15):
            self.life -= 1

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.D:
            self.paper.switch_direction()
        if key == arcade.key.A:
            self.paper.switch_direction2()
        if key == arcade.key.W:
            self.paper.switch_direction3()
