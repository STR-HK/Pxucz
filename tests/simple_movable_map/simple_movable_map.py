import math

import glfw

import Pxucz
from Pxucz.graphics import window as px_window
from Pxucz.benchmark import graphics as benchmark_graphics
from Pxucz.initial import init as px_init
from Pxucz.graphics import texture as px_texture
from OpenGL.GL import *

ASPECT_X, ASPECT_Y = 16, 9

px_init.init(abspath=__file__, loader_size_x=300, loader_size_y=100)

window, window_size_x, window_size_y = px_window.create_window(
    window_width=1280, window_height=720, window_name="simple_movable_map"
)
px_window.set_window_aspect_ratio(window=window, aspect_x=ASPECT_X, aspect_y=ASPECT_Y)
px_window.make_context_current(window=window)
glfw.swap_interval(0)  # vsync off

AssetSpriteArray = []
for i in range(0, 130):
    AssetSpriteArray.append(
        px_texture.loadTexture(f"assets/tile{str(i).zfill(3)}.png")[0]
    )

px_window.task_start(window=window)
while not px_window.window_should_close(window=window):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(255, 255, 255, 1)
    px_texture.drawImage(
        centerX=0,
        centerY=math.sin(glfw.get_time()) / 2,
        textureID=AssetSpriteArray[117],
        ratio=1,
        ASPECT_X=ASPECT_X,
        ASPECT_Y=ASPECT_Y,
    )
    px_texture.drawImage(
        centerX=0.1,
        centerY=math.sin(glfw.get_time() + 1) / 2,
        textureID=AssetSpriteArray[117],
        ratio=1,
        ASPECT_X=ASPECT_X,
        ASPECT_Y=ASPECT_Y,
    )
    px_texture.drawImage(
        centerX=0.2,
        centerY=math.sin(glfw.get_time() + 2) / 2,
        textureID=AssetSpriteArray[117],
        ratio=1,
        ASPECT_X=ASPECT_X,
        ASPECT_Y=ASPECT_Y,
    )
    px_texture.drawImage(
        centerX=0.3,
        centerY=math.sin(glfw.get_time() + 3) / 2,
        textureID=AssetSpriteArray[117],
        ratio=1,
        ASPECT_X=ASPECT_X,
        ASPECT_Y=ASPECT_Y,
    )
    px_texture.drawImage(
        centerX=-0.1,
        centerY=math.sin(glfw.get_time()) / 2,
        textureID=AssetSpriteArray[117],
        ratio=1,
        ASPECT_X=ASPECT_X,
        ASPECT_Y=ASPECT_Y,
    )
    px_texture.drawImage(
        centerX=-0.2,
        centerY=math.sin(glfw.get_time() + 1) / 2,
        textureID=AssetSpriteArray[117],
        ratio=1,
        ASPECT_X=ASPECT_X,
        ASPECT_Y=ASPECT_Y,
    )
    px_texture.drawImage(
        centerX=-0.3,
        centerY=math.sin(glfw.get_time() + 2) / 2,
        textureID=AssetSpriteArray[117],
        ratio=1,
        ASPECT_X=ASPECT_X,
        ASPECT_Y=ASPECT_Y,
    )
    px_texture.drawImage(
        centerX=-0.4,
        centerY=math.sin(glfw.get_time() + 3) / 2,
        textureID=AssetSpriteArray[117],
        ratio=1,
        ASPECT_X=ASPECT_X,
        ASPECT_Y=ASPECT_Y,
    )
    glfw.swap_buffers(window=window)
    if Pxucz.input.KeyboardInput.key("esc"):
        break
    # px_window.set_fps_limit(60)  # Limit FPS by 60
    # FPS BENCHMARKING
    FPS = benchmark_graphics.get_fps()
    if FPS is not None:
        print(FPS)

px_window.destroy_window(window=window)
px_window.terminate()
