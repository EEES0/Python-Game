import arcade
from config import get_path

class Battle(arcade.View) :
    def __init__(self, game_view) :
        super().__init__()
        self.backbtnList = arcade.SpriteList()
        self.setup()
        self.game_view = game_view

    def setup(self) :
        self.backBtn = arcade.Sprite(
            get_path("Assets", "Back.png")
        )
        self.backBtn.scale = 0.5
        self.backBtn.center_x = 1100
        self.backBtn.center_y = 100
        self.backbtnList.append(self.backBtn)

    def on_draw(self):
        self.clear(arcade.color.BEIGE)
        self.backbtnList.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if (arcade.get_sprites_at_point((x, y), self.backbtnList)):
            self.window.show_view(self.game_view)
