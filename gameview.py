import arcade
import arcade.gui
import requests
from config import get_path #config 파일의 get_path 함수 import
from upgrade import * #upgrade 파일의 모든 함수 import
from ui import *
from assets import load_level_textures
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

class GameView(arcade.View):

    def __init__(self):

        super().__init__()

        self.ranking = []
        self.rank_texts = []

        self.rank_update_timer = 0

        self.buttonList = None
        self.levelList = None

        self.buttons = {}

        self.currentLevel = 0
        self.currentGold = 10000

        self.upgradeGold = 0
        self.upgradePercent = 100
        self.sellCost = 0

        self.bonus_percent = 0

    def setup(self):

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.input_box = arcade.gui.UIInputText(
            x=100,
            y=300,
            width=300,
            height=50,
            text=""
        )

        self.manager.add(self.input_box)

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

        self.update_ranking()

    def update_ranking(self):

        response = requests.get(
            f"{SERVER_URL}/ranking"
        )

        self.ranking = response.json()

        self.rank_texts.clear()

        for i, data in enumerate(self.ranking):

            text = arcade.Text(
                f"{i+1}. {data[0]} +{data[1]}",
                50,
                500 - i * 30,
                arcade.color.WHITE,
                20
            )

            self.rank_texts.append(text)

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

        self.resetBtn = arcade.Sprite(
            get_path("Assets", "Reset.png")
        )

        self.resetBtn.scale = 0.2
        self.resetBtn.center_x = 400
        self.resetBtn.center_y = 300

        self.buttons[self.upgradeBtn] = self.upgrade
        self.buttons[self.sellBtn] = self.sell
        self.buttons[self.resetBtn] = self.reset

        self.buttonList.append(self.upgradeBtn)
        self.buttonList.append(self.sellBtn)
        self.buttonList.append(self.resetBtn)

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

        self.rank_update_timer += delta_time

        if self.rank_update_timer >= 3:

            self.rank_update_timer = 0

            self.update_ranking()

    def on_draw(self):

        self.clear(arcade.color.DARK_GRAY)

        self.manager.draw()

        self.buttonList.draw()

        self.levelList.draw()

        self.levelText.draw()
        self.goldText.draw()

        self.upgradeGoldText.draw()
        self.upgradePercentText.draw()

        self.sellCostText.draw()

        if self.currentLevel == 14:
            self.maxLevel.draw()

        for text in self.rank_texts:
            text.draw()

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
                self.currentGold,
                self.input_box.text,
                self.bonus_percent
            )
        )

    def sell(self):

        self.currentLevel, self.currentGold = (
            sell_item(
                self.currentLevel,
                self.currentGold
            )
        )

    def reset(self):

        requests.post(
            f"{SERVER_URL}/reset"
        )

        self.update_ranking()