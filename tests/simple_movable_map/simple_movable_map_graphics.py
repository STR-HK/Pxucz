import math

import glfw

from Pxucz.graphics import texture as px_texture


def draw(AssetSpriteArray):
    px_texture.drawImage(
        centerX=0,
        centerY=math.sin(glfw.get_time()) / 2,
        textureID=AssetSpriteArray[117],
        ratio=1,
    )
    px_texture.drawImage(
        centerX=0.1,
        centerY=math.sin(glfw.get_time() + 1) / 2,
        textureID=AssetSpriteArray[117],
        ratio=1,
    )
    px_texture.drawImage(
        centerX=0.2,
        centerY=math.sin(glfw.get_time() + 2) / 2,
        textureID=AssetSpriteArray[117],
        ratio=1,
    )
    px_texture.drawImage(
        centerX=0.3,
        centerY=math.sin(glfw.get_time() + 3) / 2,
        textureID=AssetSpriteArray[117],
        ratio=1,
    )
    px_texture.drawImage(
        centerX=-0.1,
        centerY=math.sin(glfw.get_time()) / 2,
        textureID=AssetSpriteArray[117],
        ratio=1,
    )
    px_texture.drawImage(
        centerX=-0.2,
        centerY=math.sin(glfw.get_time() + 1) / 2,
        textureID=AssetSpriteArray[117],
        ratio=1,
    )
    px_texture.drawImage(
        centerX=-0.3,
        centerY=math.sin(glfw.get_time() + 2) / 2,
        textureID=AssetSpriteArray[117],
        ratio=1,
    )
    px_texture.drawImage(
        centerX=-0.4,
        centerY=math.sin(glfw.get_time() + 3) / 2,
        textureID=AssetSpriteArray[117],
        ratio=1,
    )
