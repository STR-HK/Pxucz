import Pxucz
import os

window = Pxucz.graphics.window.create_window(1600, 900, "asd")
Pxucz.graphics.window.set_window_aspect_ratio(window=window, aspect_x=16, aspect_y=9)
Pxucz.graphics.window.make_context_current(window=window)

while not Pxucz.graphics.window.window_should_close(window=window):
    Pxucz.graphics.window.window_poll_events()

    if Pxucz.input.KeyboardInput.key('esc'):
        break

Pxucz.graphics.window.destroy_window(window=window)
Pxucz.graphics.window.terminate()

