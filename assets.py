import arcade
from config import get_path
"""
레벨별 이미지
인덱스로 관리
함수 실행 이후 리스트 반환
"""

def load_level_textures():

    textures = []

    for i in range(1, 16): 

        textures.append(
            arcade.load_texture(
                get_path("Assets", f"Level{i}.png")
            )
        )

    return textures