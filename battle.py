import arcade
from config import get_path
from damage import *
class Battle(arcade.View) :
    def __init__(self, game_view) :
        super().__init__()
        self.backbtnList = arcade.SpriteList()
        self.btnList = arcade.SpriteList()
        self.hp = 1000000
        self.game_view = game_view
        self.setup()

    def setup(self) :
        self.backBtn = arcade.Sprite(
            get_path("Assets", "Back.png")
        )
        self.backBtn.scale = 0.5
        self.backBtn.center_x = 1100
        self.backBtn.center_y = 100
        self.backbtnList.append(self.backBtn)
        self.sword = arcade.Sprite(
            get_path("Assets", "Sword.png")
        )
        self.sword.scale = 1
        self.sword.center_x = 640
        self.sword.center_y = 380
        self.btnList.append(self.sword)
    def on_update(self, delta_time) :
        self.damage = get_damage(self.game_view.currentLevel)
        self.levelText = arcade.Text(
            f"현재 레벨 : {self.game_view.currentLevel}",
            800,
            300,
            arcade.color.BLACK,
            30
        )
        self.damageText = arcade.Text(
            f"현재 대미지 : {self.damage}",
            800,
            230,
            arcade.color.BLACK,
            30
        )
        self.hpText =arcade.Text(
            f"현재 체력 : {self.hp}",
            500,
            640,
            arcade.color.BLACK,
            30
        )
    def take_damage(self) :
        self.hp -= self.damage
    

    def on_draw(self):
        self.clear(arcade.color.BEIGE)
        self.backbtnList.draw()
        self.levelText.draw()
        self.damageText.draw()
        self.btnList.draw()
        self.hpText.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if (arcade.get_sprites_at_point((x, y), self.backbtnList)):
            self.window.show_view(self.game_view)
        if (arcade.get_sprites_at_point((x, y), self.btnList)):
            self.take_damage()