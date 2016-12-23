import arcade
from models import World, Paper
import models
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

        arcade.set_background_color(arcade.color.BLACK)

        self.world = World(width, height)
        self.paper_sprite = ModelSprite('images/Paper.png',model=self.world.paper)
        self.background_sprite = ModelSprite('images/background.jpg',model=self.world.background)
        self.mainmenu_sprite = ModelSprite('images/Mainmenu.png',model=self.world.mainmenu)
        self.gameover_sprite = ModelSprite('images/gameover.png',model=self.world.gameover)
        self.building_sprite = []
        #self.papers_sprite = []
        for i in range(0,6):
            self.building_sprite.append(ModelSprite('images/Building.png',model=self.world.building[i]))
            #self.papers_sprite = ModelSprite('images/papers.png',model=self.world.papers[i])

    def on_draw(self):

        arcade.start_render()
        self.background_sprite.draw()
        if models.Check == False :
         self.mainmenu_sprite.draw()


        i = 0

        if models.Check == True :
         for sprite in self.building_sprite:
             sprite.center_y = self.world.building[i]
             #sprite.center_y = self.world.papers[i]
             sprite.draw()
             i+=1





         self.paper_sprite.draw()

         arcade.draw_text(str("Life :"),
                          self.width - 120, self.height - 30,
                          arcade.color.YELLOW, 20)
         arcade.draw_text(str(self.world.life),
                          self.width - 40, self.height - 30,
                          arcade.color.WHITE, 20)
         arcade.draw_text(str("Score :"),
                          self.width - 120, self.height - 50,
                          arcade.color.ORANGE, 20)
         arcade.draw_text(str(self.world.score),
                          self.width - 40, self.height - 50,
                          arcade.color.WHITE, 20)
         if self.world.life == 0:
             self.gameover_sprite.draw()

    def animate(self, delta):
        if self.world.life > 0:
            self.world.animate(delta)

    def on_key_press(self, key, key_modifiers):
        if self.world.life > 0:
            self.world.on_key_press(key, key_modifiers)



if __name__ == '__main__':
    window = FlyByGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
