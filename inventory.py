import arcade
# item.py 파일에서 아이템 리스트(item_list)를 가져옵니다.
import item

class Inventory:
    def __init__(self):
        self.button_x = 100
        self.button_y = 550   # 화면 안쪽으로 조정
        self.button_width = 180
        self.button_height = 50
        self.is_open = False

        # item.py에 정의된 아이템 목록을 가져옵니다.
        # 만약 item.py의 item_list가 비어있어도 에러가 나지 않습니다.
        self.items = getattr(item, 'item_list', [])

    def draw_button(self):
        # 버튼 배경 그리기
        button_box = arcade.XYWH(
            self.button_x,
            self.button_y,
            self.button_width,
            self.button_height
        )
        arcade.draw_rect_filled(button_box, arcade.color.GRAY)
        
        # 텍스트 그리기
        arcade.draw_text("인벤토리",
                         self.button_x - 40,
                         self.button_y - 10,
                         arcade.color.BLACK,
                         20)

    def check_click(self, x, y):
        if (self.button_x - self.button_width / 2 <= x <= self.button_x + self.button_width / 2
                and self.button_y - self.button_height / 2 <= y <= self.button_y + self.button_height / 2):
            self.is_open = not self.is_open

    def draw_inventory(self):
        if self.is_open:
            # 1. 인벤토리 창 배경 그리기
            inv_box = arcade.XYWH(400, 300, 400, 250)
            arcade.draw_rect_filled(inv_box, arcade.color.LIGHT_GRAY)

            # 2. 인벤토리가 비어있는지 확인
            if not self.items:
                # 아이템이 하나도 없을 때 띄울 안내 텍스트
                arcade.draw_text("인벤토리가 비어 있습니다.",
                                 400, 300,
                                 arcade.color.DARK_GRAY,
                                 16,
                                 anchor_x="center",
                                 anchor_y="center")
            else:
                # 아이템이 존재할 때 이미지 표시
                x = 250
                y = 300
                for texture in self.items:
                    item_box = arcade.XYWH(x, y, 64, 64)
                    arcade.draw_texture_rect(texture, item_box)
                    x += 80  # 아이템 간격


class MyGame(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.inventory = Inventory()
        self.game_view = game_view

    def on_draw(self):
        self.clear()
        self.inventory.draw_button()
        self.inventory.draw_inventory()

    def on_mouse_press(self, x, y, button, modifiers):
        self.inventory.check_click(x, y)
    def on_key_press(self, key, modifiers):

        if key == arcade.key.ESCAPE:
            self.window.show_view(self.game_view)


if __name__ == "__main__":
    game = MyGame()
    arcade.run()
