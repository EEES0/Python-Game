import arcade
from config import get_path


def load_level_textures():

    textures = []

    for i in range(1, 16): 

        textures.append(
            arcade.load_texture(
                get_path("Assets", f"Level{i}.png")
            )
        )

    return textures