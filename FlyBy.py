import arcade
from models import World
import pyglet.gl as gl

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 700

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()

class FlyByWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.dot_sprite = ModelSprite('images/dot.png',
                                      model=self.world.dot)

        self.coin_texture = arcade.load_texture('images/coin.png')

    def animate(self, delta):
        self.world.animate(delta)

    def draw_platforms(self, platforms):
        for p in platforms:
            arcade.draw_rectangle_filled(p.x + p.width // 2,
                                         p.y - p.height // 2,
                                         p.width, p.height,
                                         arcade.color.WHITE)
