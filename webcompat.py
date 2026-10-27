# helpers that let the arcade run on the desktop and in the browser (pygbag)
import sys
import threading

IS_WEB = sys.platform == "emscripten"

# the browser has no threads, so the engines think on the main loop and get less time per move
WEB_ENGINE_TIME_LIMIT_MS = 2000

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


class EngineSearch:
    '''Run an engine search generator (one step per depth) in a thread, or one step per frame in the browser'''

    def __init__(self, steps):
        self.steps = steps
        if not IS_WEB:
            threading.Thread(target=self.run_to_end, daemon=True).start()

    def run_to_end(self):
        for _ in self.steps:
            pass

    def step(self):
        '''Search one more depth (only needed in the browser, where there is no thread doing it)'''
        if IS_WEB:
            next(self.steps, None)
