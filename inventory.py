import arcade
import item
from config import get_path
class Inventory:
    def __init__(self):
        self.backbtnList = arcade.SpriteList()
        self.itemList = arcade.SpriteList()
        self.shopList = arcade.SpriteList()
    def setup(self):
        self.backBtn = arcade.Sprite(
            get_path("Assets", "Inven.png")
        )
        self.backBtn.scale = 0.5
        self.backBtn.center_x = 1100
        self.backBtn.center_y = 100
        self.backbtnList.append(self.backBtn)

        self.itemImg = arcade.Sprite(
            get_path("Assets", "Levelup.png")
        )
        self.itemImg.scale = 0.5
        self.itemImg.center_x = 640
        self.itemImg.center_y = 500
        self.itemList.append(self.itemImg)

        self.shopBtn = arcade.Sprite(
            get_path("Assets", "ShopBtn.png")
        )
        self.shopBtn.scale = 0.5
        self.shopBtn.center_x = 640
        self.shopBtn.center_y = 380
        self.shopList.append(self.shopBtn)

class MyGame(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.inventory = Inventory()
        self.inventory.setup()
        self.game_view = game_view

    def on_draw(self):
        self.clear(arcade.color.BEIGE)
        self.inventory.backbtnList.draw()
        self.inventory.itemList.draw()
        self.inventory.shopList.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if (arcade.get_sprites_at_point((x, y), self.inventory.backbtnList)):
            self.window.show_view(self.game_view)
        if (arcade.get_sprites_at_point((x, y), self.inventory.shopList)):
            if self.game_view.currentGold >= 1000:
                if self.game_view.currentLevel < 14:
                    self.game_view.currentLevel += 1
                    self.game_view.currentGold -= 1000


if __name__ == "__main__":
    game = MyGame()
    arcade.run()
