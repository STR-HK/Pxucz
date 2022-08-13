import glfw


def create_window(window_width: int, window_height: int, window_name: str):
    return glfw.create_window(width=window_width, height=window_height, title=window_name, monitor=None, share=None)


def set_window_icon(window, image):
    glfw.set_window_icon(window=window, count=1, images=image)


def set_window_aspect_ratio(window, aspect_x, aspect_y):
    glfw.set_window_aspect_ratio(window=window, numer=aspect_x, denom=aspect_y)

def make_context_current(window):
    glfw.make_context_current(window=window)

def window_should_close(window):
    glfw.window_should_close(window=window)

def window_poll_events():
    return glfw.poll_events()

def destroy_window(window):
    glfw.destroy_window(window=window)

def terminate():
    glfw.terminate()
