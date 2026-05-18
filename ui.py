import arcade

"""
game 의미
파이썬에선 객체도 함수의 인수로 넘길 수 있음
gameview.py 44줄 보면 create_texts(self)로 GameView 클래스의 객체를 인수로 넘긴 걸 볼 수 있음
그걸 game 매개변수로 받아 사용한거
game 대신 원하는 이름 붙여도됨
game 대신 self를 써도 되긴 한데 혼동되기 때문에 관례적으로 사용하지 않음 - 실무에서 조심
"""
def create_texts(game):

    game.levelText = arcade.Text(
        f"+{game.currentLevel}",
        580,
        570,
        arcade.color.BLACK,
        70
    )

    game.goldText = arcade.Text(
        f"현재 골드: {game.currentGold}",
        530,
        670,
        arcade.color.BLACK,
        30
    )

    game.upgradeGoldText = arcade.Text(
        f"업그레이드 비용: {game.upgradeGold}",
        530,
        120,
        arcade.color.BLACK,
        20
    )

    game.upgradePercentText = arcade.Text(
        f"성공 확률: {game.upgradePercent}%",
        530,
        90,
        arcade.color.BLACK,
        20
    )

    game.sellCostText = arcade.Text(
        f"판매 가격: {game.sellCost}",
        530,
        150,
        arcade.color.BLACK,
        20
    )

    game.maxLevel = arcade.Text(
        "클리어",
        100,
        600,
        arcade.color.BLACK,
        30
    )

    game.consoleText = arcade.Text(
        "콘솔 텍스트(추후 사용 예정)",
        100,
        500,
        arcade.color.BLACK,
        30
    )


def update_texts(game):

    game.levelText.text = f"+{game.currentLevel}"

    game.goldText.text = (
        f"현재 골드: {game.currentGold}"
    )

    game.upgradeGoldText.text = (
        f"업그레이드 비용: {game.upgradeGold}"
    )

    game.sellCostText.text = (
        f"판매 가격: {game.sellCost}"
    )

    game.upgradePercentText.text = (
        f"성공 확률: {game.upgradePercent}%"
    )