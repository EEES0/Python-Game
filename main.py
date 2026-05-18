import arcade 
from gameview import GameView #gameview 파일의 Gameview 클래스 import

def main(): #메인 함수
    window = arcade.Window(1280, 720, "방패 키우기")
    """
    중요하니까 읽어보기
    arcade = 라이브러리
    Window = arcade 라이브러리의 Window 클래스
    Window() = Window 클래스를 기반으로 객체 생성
    window = 객체를 저장하는 변수
    객체 지향 기본이니까 알아두면 좋음
    모르는 단어나 개념 gpt에 물어보기
    """

    game = GameView() #이건 무슨 의미일지 생각해보기
    game.setup()

    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()