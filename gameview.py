import arcade
import random

from config import get_path
from upgrade import *
from ui import *

class GameView(arcade.View):

    def __init__(self):
        super().__init__()

        self.buttonList = None
        self.buttons = {}

        self.currentLevel = 0
        self.currentGold = 10000

        self.upgradeClicked = False
        self.upgradeRandom = 0
        self.upgradePercent = 100
        self.upgradeGold = 0
        self.sellCost = 0


    def setup(self):

        self.buttonList = arcade.SpriteList()
        self.levelList = arcade.SpriteList()

        self.buttons = {}

        create_texts(self)

        self.levelTexture = [
            arcade.load_texture(get_path("Assets", "Level1.png")),
            arcade.load_texture(get_path("Assets", "Level2.png")),
            arcade.load_texture(get_path("Assets", "Level3.png")),
            arcade.load_texture(get_path("Assets", "Level4.png")),
            arcade.load_texture(get_path("Assets", "Level5.png")),
            arcade.load_texture(get_path("Assets", "Level6.png")),
            arcade.load_texture(get_path("Assets", "Level7.png")),
            arcade.load_texture(get_path("Assets", "Level8.png")),
            arcade.load_texture(get_path("Assets", "Level9.png")),
            arcade.load_texture(get_path("Assets", "Level10.png")),
            arcade.load_texture(get_path("Assets", "Level11.png")),
            arcade.load_texture(get_path("Assets", "Level12.png")),
            arcade.load_texture(get_path("Assets", "Level13.png")),
            arcade.load_texture(get_path("Assets", "Level14.png")),
            arcade.load_texture(get_path("Assets", "Level15.png"))
        ]

        self.levels = arcade.Sprite()

        self.levels.center_x = 640
        self.levels.center_y = 380
        self.levels.scale = 0.3

        self.levelList.append(self.levels)

        self.upgradeBtn = arcade.Sprite(
            get_path("Assets", "Upgrade.png")
        )

        self.upgradeBtn.scale = 0.3
        self.upgradeBtn.center_x = 1100
        self.upgradeBtn.center_y = 500

        self.buttons[self.upgradeBtn] = self.upgrade

        self.sellBtn = arcade.Sprite(
            get_path("Assets", "Sell.png")
        )

        self.sellBtn.scale = 0.2
        self.sellBtn.center_x = 1125
        self.sellBtn.center_y = 300

        self.buttons[self.sellBtn] = self.sell

        self.buttonList.append(self.upgradeBtn)
        self.buttonList.append(self.sellBtn)


    def on_update(self, delta_time):

        self.upgradeGold = get_upgrade_cost(self.currentLevel)
        self.sellCost = get_sell_price(self.currentLevel)
        self.upgradePercent = get_upgrade_percent(self.currentLevel)

        update_texts(self)

        self.levels.texture = self.levelTexture[self.currentLevel]

        self.consoleText.text = "콘솔 로그"


    def on_draw(self):

        self.clear(arcade.color.DARK_GRAY)

        self.buttonList.draw()

        self.levelText.draw()
        self.goldText.draw()

        self.upgradeGoldText.draw()
        self.upgradePercentText.draw()

        self.levelList.draw()

        self.sellCostText.draw()
        self.consoleText.draw()

        if self.currentLevel == 14:
            self.maxLevel.draw()


    def on_mouse_press(self, x, y, button, modifiers):

        if arcade.get_sprites_at_point((x, y), self.buttonList):

            for btn in arcade.get_sprites_at_point((x, y), self.buttonList):

                actions = self.buttons.get(btn)

                if actions:
                    actions()


    def upgrade(self):

        self.upgradeRandom = random.randint(1, 100)

        if self.currentLevel < 14:

            if self.currentGold >= self.upgradeGold:

                if self.upgradeRandom <= self.upgradePercent:

                    self.currentLevel += 1
                    self.currentGold -= self.upgradeGold

                else:

                    self.currentLevel = 0
                    self.upgradePercent = 100


    def sell(self):

        self.currentGold += get_sell_price(self.currentLevel)

        self.currentLevel = 0
        self.upgradePercent = 100