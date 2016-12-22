import arcade
from models import World, Paper
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            self.angle = self.model.angle

    def draw(self):
        self.sync_with_model()
        super().draw()

class FlyByGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        self.world = World(width, height)
        self.paper_sprite = ModelSprite('images/Paper.png',model=self.world.paper)
        self.building_sprite = ModelSprite('images/Building.png',model=self.world.building)

    def on_draw(self):
        arcade.start_render()
        self.building_sprite.draw()
        self.paper_sprite.draw()

    def animate(self, delta):
        self.world.animate(delta)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)



if __name__ == '__main__':
    window = FlyByGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
