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

    def on_draw(self):
        arcade.set_viewport(self.world.dot.x - SCREEN_WIDTH // 2,
                            self.world.dot.x + SCREEN_WIDTH // 2,
                            0, SCREEN_HEIGHT)

        arcade.start_render()
        self.dot_sprite.draw()
        gl.glDisable(gl.GL_TEXTURE_2D)

        

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

if __name__ == '__main__':
    window = FlyByWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
