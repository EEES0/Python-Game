import arcade

from config import get_path #config 파일의 get_path 함수 import
from upgrade import * #upgrade 파일의 모든 함수 import
from ui import *
from assets import load_level_textures
from inventory import MyGame
"""
개발할 때 알아둘 것
arcade 라이브러리에서 화면 출력 방법
1. arcade.View 클래스를 상속받는 클래스를 만든다.
2. 스프라이트 리스트 생성
3. 이미지를 넣은 스프라이트 생성
4. 스프라이트 리스트에 스프라이트 추가 (append)
5. on_draw 함수에서 스프라이트 리스트를 그린다.

지역 변수 전역 변수 구별하기
self는 객체 자신 즉 GameView 클래스 객체

"""

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
        self.levels.scale = 0.3

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

        self.sellBtn.scale = 0.2
        self.sellBtn.center_x = 1125
        self.sellBtn.center_y = 300
        
        self.invenBtn = arcade.Sprite(
            get_path("Assets", "Inven.png")
        )

        self.buttons[self.upgradeBtn] = self.upgrade
        self.buttons[self.sellBtn] = self.sell
        self.buttons[self.invenBtn] = self.inven

        self.buttonList.append(self.upgradeBtn)
        self.buttonList.append(self.sellBtn)
        self.buttonList.append(self.invenBtn)

    def inven(self):
        self.window.show_view(MyGame(self))

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

        self.clear(arcade.color.DARK_GRAY)

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
        mustSuccess = True

    def sell(self):

        self.currentLevel, self.currentGold = (
            sell_item(
                self.currentLevel,
                self.currentGold
            )
        )