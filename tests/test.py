import glfw

import Pxucz
from Pxucz.graphics import window as px_window
from Pxucz.benchmark import graphics as benchmark_graphics
from Pxucz.initial import init as px_init
from Pxucz.graphics import texture as px_texture
from OpenGL.GL import *

px_init.init(abspath=__file__, loader_size_x=400, loader_size_y=200)
window, window_size_x, window_size_y = px_window.create_window(
    window_width=1600, window_height=900, window_name="Tests"
)
px_window.set_window_aspect_ratio(window=window, aspect_x=16, aspect_y=9)
px_window.make_context_current(window=window, view_ratio=5)
glfw.swap_interval(0)  # vsync off

logo, logo_size_x, logo_size_y = px_texture.loadTexture("image.png")
px_window.task_start()
while not px_window.window_should_close(window=window):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    px_texture.drawImage(centerX=0, centerY=0, textureID=logo, ratio=1)

    glfw.swap_buffers(window=window)
    v_width, v_height = glfw.get_window_size(window)
    glViewport(0, 0, v_width, v_height)
    if Pxucz.input.KeyboardInput.key("esc"):
        break

    px_window.set_fps_limit(60)  # Limit FPS by 60
    # FPS BENCHMARKING
    FPS = benchmark_graphics.get_fps()
    if FPS is not None:
        print(FPS)

px_window.destroy_window(window=window)
px_window.terminate()
