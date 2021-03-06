import arcade.key
import random
import time
import math
Check = False
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
            self.angle = -45

    def switch_direction2(self):
            self.direction = Paper.Left
            self.angle = 45

    def switch_direction3(self):
            self.direction = Paper.Forward
            self.angle = 0


    def animate(self, delta):
        if self.direction == Paper.Forward:
            if self.y > self.world.height:
                self.y = 0
            self.y += 1
            #self.x -= 2

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
        self.angle = 0
        self.y = 100+y
        self.x = x
    def animate(self, delta):
        self.y -= 1
        if self.y == 0:
           self.y = 600

class Screen:
    def __init__(self, world, x, y):
        self.angle = 0
        self.y = 300
        self.x = 300

class Background:
    def __init__(self, world, x, y):
        self.angle = 0
        self.y = 300
        self.x = 300
    def animate(self, delta):
        self.y -= 1
        if self.y == 0:
           self.y = 600


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.life = 100
        self.score = 0

        self.paper = Paper(self, 300, 0)
        self.gameover = Screen(self, 300, 300)
        self.mainmenu = Screen(self, 300, 300)
        self.background = Background(self, 300, 300)

        self.building = []
        posi = [[100,350],[150,550],[200,150],[300,500],[350,300],[400,100],[500,200],[550,450]]
        for i in range (0,8):
            self.building.append(Building(self, posi[i][0],posi[i][1]))





    def animate(self, delta):
        self.paper.animate(delta)
        self.background.animate(delta)
        self.score += delta
        for i in range (0,8):
            if len(self.building) > 0:
                self.building[i].animate(delta)
                if self.paper.hit(self.building[i], 40):
                    self.life -= 1



    def on_key_press(self, key, key_modifiers):
        global Check
        if key == arcade.key.D:
            self.paper.switch_direction()
        if key == arcade.key.A:
            self.paper.switch_direction2()
        if key == arcade.key.W:
            self.paper.switch_direction3()
        if key == arcade.key.SPACE and Check == False :
            Check = True
