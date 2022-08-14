import math
import time

import glfw

import Pxucz
from Pxucz.graphics import window as px_window
from Pxucz.benchmark import graphics as benchmark_graphics
from Pxucz.initial import init as px_init
from Pxucz.graphics import texture as px_texture
from OpenGL.GL import *

px_init.init(abspath=__file__, loader_size_x=300, loader_size_y=100)

window, window_size_x, window_size_y = px_window.create_window(
    window_width=1280, window_height=720, window_name="simple_movable_map"
)

px_window.set_window_aspect_ratio(window=window, aspect_x=16, aspect_y=9)
px_window.make_context_current(window=window, view_ratio=5)
glfw.swap_interval(0)  # vsync off

AssetSpriteArray = []
for i in range(0, 130):
    AssetSpriteArray.append(px_texture.loadTexture(f"assets/tile{str(i).zfill(3)}.png")[0])

px_window.task_start(window=window)
while not px_window.window_should_close(window=window):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(255, 255, 255, 1)
    px_texture.drawImage(centerX=math.cos(glfw.get_time()*2), centerY=math.sin(glfw.get_time()), textureID=AssetSpriteArray[121], ratio=1)
    px_texture.drawImage(centerX=math.cos(glfw.get_time()*2-200), centerY=math.sin(glfw.get_time()-200), textureID=AssetSpriteArray[120], ratio=1)
    px_texture.drawImage(centerX=math.cos(glfw.get_time()*2+200), centerY=math.sin(glfw.get_time()+200), textureID=AssetSpriteArray[127], ratio=1)
    px_texture.drawImage(centerX=math.cos(glfw.get_time() * 4 + 200), centerY=math.sin(glfw.get_time()*4 + 200),
                         textureID=AssetSpriteArray[113], ratio=1)
    px_texture.drawImage(centerX=math.cos(glfw.get_time() * 7 + 200), centerY=math.sin(glfw.get_time()*7 + 200),
                         textureID=AssetSpriteArray[115], ratio=1)
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
