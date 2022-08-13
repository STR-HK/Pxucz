import Pxucz
from Pxucz.graphics import window as px_window
from Pxucz.benchmark import graphics as benchmark_graphics
from Pxucz.initial import set_variables as px_set_var
from OpenGL.GL import *

window = px_window.create_window(1600, 900, "asd")
px_window.set_window_aspect_ratio(window=window, aspect_x=16, aspect_y=9)
px_window.make_context_current(window=window)
px_window.swap_interval(interval=0)  # vsync off
px_set_var.setvar()

fps_previoustime = px_window.get_time()
fps_framecount = 0

while not px_window.window_should_close(window=window):
    px_window.window_poll_events()
    px_window.Clear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    px_window.swap_buffers(window=window)

    if Pxucz.input.KeyboardInput.key("esc"):
        break

    fps_currentTime = px_window.get_time()
    fps_framecount += 1
    px_window.set_fps_limit(60)  # Limit FPS by 60

    # FPS BENCHMARKING
    FPS = benchmark_graphics.get_fps()
    if FPS is not None:
        print(FPS)

px_window.destroy_window(window=window)
px_window.terminate()
