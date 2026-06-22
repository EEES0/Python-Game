import arcade 
from gameview import GameView

def main(): #메인 함수
    window = arcade.Window(1280, 720, "방패 키우기")
    game = GameView() #이건 무슨 의미일지 생각해보기
    game.setup()

    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()