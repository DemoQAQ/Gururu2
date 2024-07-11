from pynput.mouse import Listener as MouseListener, Button
from pynput.keyboard import Listener as KeyboardListener, Key
from threading import Thread
import time
import pyperclip

class UserEvent:
    def __init__(self):
        self.mouse_listener = None
        self.keyboard_listener = None
        self.mouse_thread = None
        self.keyboard_thread = None
        self.pressed_keys = set()

    def on_mouse_click(self, x, y, button, pressed):
        if pressed:
            print(f'Mouse clicked at ({x}, {y})')
            if button == Button.left:
                print('Left button clicked')
            elif button == Button.right:
                print('Right button clicked')
            elif button == Button.middle:
                print('Middle button clicked')

    def on_keyboard_press(self, key):
        try:
            self.pressed_keys.add(key.char)
            print(f'Key {key.char} pressed')
        except AttributeError:
            self.pressed_keys.add(key)
            print(f'Special key {key} pressed')
        self.check_combination()


    def on_keyboard_release(self, key):
        try:
            self.pressed_keys.discard(key.char)
        except AttributeError:
            self.pressed_keys.discard(key)
        print(f'{key} released')

    def check_combination(self):
        if Key.ctrl_l in self.pressed_keys or Key.ctrl_r in self.pressed_keys:
            print('ctrl 按下')
            print(self.pressed_keys)
            print(ascii(self.pressed_keys))

    def copy_clipboard_content(self):
        clipboard_content = pyperclip.paste()
        print(f'Copied content: {clipboard_content}')

    def paste_clipboard_content(self):
        clipboard_content = pyperclip.paste()
        print(f'Pasted content: {clipboard_content}')

    def start_mouse_listener(self):
        self.mouse_listener = MouseListener(on_click=self.on_mouse_click)
        self.mouse_thread = Thread(target=self.mouse_listener.start)
        self.mouse_thread.start()

    def stop_mouse_listener(self):
        if self.mouse_listener:
            self.mouse_listener.stop()
            self.mouse_thread.join()

    def start_keyboard_listener(self):
        self.keyboard_listener = KeyboardListener(on_press=self.on_keyboard_press, on_release=self.on_keyboard_release)
        self.keyboard_thread = Thread(target=self.keyboard_listener.start)
        self.keyboard_thread.start()

    def stop_keyboard_listener(self):
        if self.keyboard_listener:
            self.keyboard_listener.stop()
            self.keyboard_thread.join()

    def stop_all_listeners(self):
        self.stop_mouse_listener()
        self.stop_keyboard_listener()

if __name__ == "__main__":
    us = UserEvent()
    us.start_keyboard_listener()
    us.start_mouse_listener()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        us.stop_all_listeners()
