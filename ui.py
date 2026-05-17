import arcade

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
        "콘솔",
        100,
        500,
        arcade.color.BLACK,
        30
    )


def update_texts(game):

    game.levelText.text = f"+{game.currentLevel}"
    game.goldText.text = f"현재 골드: {game.currentGold}"
    game.upgradeGoldText.text = f"업그레이드 비용: {game.upgradeGold}"
    game.sellCostText.text = f"판매 가격: {game.sellCost}"
    game.upgradePercentText.text = f"성공 확률: {game.upgradePercent}%"