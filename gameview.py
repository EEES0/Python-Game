import arcade

from config import get_path #config 파일의 get_path 함수 import
from upgrade import * #upgrade 파일의 모든 함수 import
from ui import *
from assets import load_level_textures
from inventory import MyGame
from battle import Battle


class GameView(arcade.View): #arcade.View 클래스를 상속받는 GameView 클래스

    def __init__(self): #파이썬에서 객체가 생성될 때 자동으로 호출되는 함수

        super().__init__() #부모 클래스의 __init__ 함수도 호출

        self.buttonList = None
        self.levelList = None

        self.buttons = {}

        self.currentLevel = 0
        self.currentGold = 10000

        self.upgradeGold = 0
        self.upgradePercent = 100
        self.sellCost = 0

    def setup(self):

        self.buttonList = arcade.SpriteList()
        self.levelList = arcade.SpriteList()

        create_texts(self)

        self.levelTexture = load_level_textures()

        self.levels = arcade.Sprite()

        self.levels.center_x = 640
        self.levels.center_y = 380
        self.levels.scale = 1

        self.levelList.append(self.levels)

        self.create_buttons()

    def create_buttons(self):

        self.upgradeBtn = arcade.Sprite(
            get_path("Assets", "Upgrade.png")
        )

        self.upgradeBtn.scale = 0.3
        self.upgradeBtn.center_x = 1100
        self.upgradeBtn.center_y = 500

        self.sellBtn = arcade.Sprite(
            get_path("Assets", "Sell.png")
        )

        self.sellBtn.scale = 0.5
        self.sellBtn.center_x = 1105
        self.sellBtn.center_y = 350
        
        self.invenBtn = arcade.Sprite(
            get_path("Assets", "Inven.png")
        )

        self.invenBtn.scale = 0.5
        self.invenBtn.center_x = 1100
        self.invenBtn.center_y = 100

        self.battleBtn = arcade.Sprite(
            get_path("Assets", "Battle.png")
        )

        self.battleBtn.scale = 0.5
        self.battleBtn.center_x = 200
        self.battleBtn.center_y = 100

        self.buttons[self.upgradeBtn] = self.upgrade
        self.buttons[self.sellBtn] = self.sell
        self.buttons[self.invenBtn] = self.inven
        self.buttons[self.battleBtn] = self.battle

        self.buttonList.append(self.upgradeBtn)
        self.buttonList.append(self.sellBtn)
        self.buttonList.append(self.invenBtn)
        self.buttonList.append(self.battleBtn)

    def inven(self):
        self.window.show_view(MyGame(self))
    def battle(self):
        self.window.show_view(Battle(self))

    def on_update(self, delta_time):

        self.upgradeGold = get_upgrade_cost(
            self.currentLevel
        )

        self.sellCost = get_sell_price(
            self.currentLevel
        )

        self.upgradePercent = get_upgrade_percent(
            self.currentLevel
        )

        update_texts(self)

        self.levels.texture = (
            self.levelTexture[self.currentLevel]
        )

    def on_draw(self):

        self.clear(arcade.color.BEIGE)

        self.buttonList.draw()

        self.levelList.draw()

        self.levelText.draw()
        self.goldText.draw()

        self.upgradeGoldText.draw()
        self.upgradePercentText.draw()

        self.sellCostText.draw()
        if self.currentLevel == 14:
            self.maxLevel.draw()

    def on_mouse_press(
        self,
        x,
        y,
        button,
        modifiers
    ):

        clicked = arcade.get_sprites_at_point(
            (x, y),
            self.buttonList
        )

        for btn in clicked:

            action = self.buttons.get(btn)

            if action:
                action()

    def upgrade(self):

        self.currentLevel, self.currentGold = (
            try_upgrade(
                self.currentLevel,
                self.currentGold
            )
        
        )

    def sell(self):

        self.currentLevel, self.currentGold = (
            sell_item(
                self.currentLevel,
                self.currentGold
            )
        )