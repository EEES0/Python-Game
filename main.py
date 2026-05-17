import arcade 
from gameview import GameView

def main():
    window = arcade.Window(1280, 720, "방패 키우기")

    game = GameView()
    game.setup()

    window.show_view(game)
    arcade.run()

main()