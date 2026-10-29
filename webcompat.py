# helpers that let the arcade run on the desktop and in the browser (pygbag)
import sys
import threading
import time

IS_WEB = sys.platform == "emscripten"

# the browser has no threads, so the engines think on the main loop, sharing each frame with drawing
# (see EngineSearch); these caps keep them about as strong as when they had the whole frame
WEB_ENGINE_TIME_LIMIT_MS = 4000  # chess
WEB_CONNECT_FOUR_TIME_LIMIT_MS = 3000

if not IS_WEB:
    import tkinter as tk
    from tkinter import simpledialog


def ask_string(title, prompt, initial_value=""):
    '''Ask the user for a line of text (tkinter dialog on the desktop, prompt() in the browser)'''
    if IS_WEB:
        import platform
        answer = platform.window.prompt(prompt, initial_value)
        return None if answer is None else str(answer)

    root = tk.Tk()
    root.withdraw()
    answer = simpledialog.askstring(title, prompt, parent=root, initialvalue=initial_value)
    root.destroy()
    return answer


# how long a frame in the browser lets the engine think before drawing: drawing a board takes about
# 15 ms in the browser, so while an engine thinks each frame spans two screen refreshes (33 ms, 30 fps),
# and this fills the rest of it
WEB_SEARCH_SLICE_SECONDS = 0.015


class EngineSearch:
    '''Run an engine search generator in a thread, or a slice of it each frame in the browser'''

    def __init__(self, steps, engine=None):
        self.steps = steps
        self.engine = engine
        if not IS_WEB:
            threading.Thread(target=self.run_to_end, daemon=True).start()

    def run_to_end(self):
        for _ in self.steps:
            pass

    def step(self):
        '''Think for one frame's slice (only needed in the browser, where there is no thread doing it)'''
        if IS_WEB:
            if self.engine is not None:
                self.engine.slice_end = time.perf_counter() + WEB_SEARCH_SLICE_SECONDS
            next(self.steps, None)
