from pynput.mouse import Listener, Button  
from pynput.keyboard import Listener as KeyboardListener, Key  
from threading import Thread  
import time

class UserEvent:  
    def __init__(self):  
        print("1")
        self.mouse_listener = None  
        self.keyboard_listener = None  
        self.mouse_thread = None  
        self.keyboard_thread = None  
  
  # 判断鼠标点击事件
    def on_mouse_click(self, x, y, button, pressed):  
        if pressed:  
            print(f'Mouse clicked at ({x}, {y})')  
            if button == Button.left:  
                print('Left button clicked')  
            elif button == Button.right:  
                print('Right button clicked')  
            elif button == Button.middle:  
                print('Middle button clicked')  
  
  # 判断键盘点击事件
    def on_keyboard_press(self, key):  
        try:  
            print(f'Key {key.char} pressed')  
        except AttributeError:  
            print(f'Special key {key} pressed')  
  
  # 键盘释放
    def on_keyboard_release(self, key):  
        print(f'{key} released')  
  
  # 开启鼠标监听
    def start_mouse_listener(self):  
        print("start")
        self.mouse_listener = Listener(on_click=self.on_mouse_click)  
        self.mouse_thread = Thread(target=self.mouse_listener.start)  
        self.mouse_thread.start()  
  
  # 关闭鼠标监听
    def stop_mouse_listener(self):  
        if self.mouse_listener:  
            self.mouse_listener.stop()  
            self.mouse_thread.join()  
  
  # 开启键盘监听
    def start_keyboard_listener(self):  
        self.keyboard_listener = KeyboardListener(on_press=self.on_keyboard_press, on_release=self.on_keyboard_release)  
        self.keyboard_thread = Thread(target=self.keyboard_listener.start)  
        self.keyboard_thread.start()  
  
  # 关闭键盘监听
    def stop_keyboard_listener(self):  
        if self.keyboard_listener:  
            self.keyboard_listener.stop()  
            self.keyboard_thread.join()  
  
  # 关闭所有监听
    def stop_all_listeners(self):  
        self.stop_mouse_listener()  
        self.stop_keyboard_listener()  

if __name__ == "__main__":
    us = UserEvent()
    us.start_keyboard_listener()
    us.start_mouse_listener()
    time.sleep(100)