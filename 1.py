from pynput.mouse import Listener, Button, Controller  
from pynput.keyboard import Key, Listener as KeyboardListener  
  
# 鼠标事件监听  
def on_click(x, y, button, pressed):  
    """处理鼠标点击事件"""  
    if pressed:  
        print(f'Mouse clicked at ({x}, {y})')  
        if button == Button.left:  
            print('Left button clicked')  
        elif button == Button.right:  
            print('Right button clicked')  
        elif button == Button.middle:  
            print('Middle button clicked')  
  
# 创建一个鼠标监听器  
mouse_listener = Listener(on_click=on_click)  
  
# 键盘事件监听  
def on_press(key):  
    """处理键盘按键按下事件"""  
    try:  
        print(f'Key {key.char} pressed')  
    except AttributeError:  
        print(f'Special key {key} pressed')  
  
def on_release(key):  
    """处理键盘按键释放事件"""  
    print(f'{key} released')  
    if key == Key.esc:  
        # 停止监听  
        return False  
  
# 创建一个键盘监听器  
keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)  
  
# 启动监听器  
mouse_listener.start()  
keyboard_listener.start()  
  
# 等待鼠标监听器退出（通常通过Ctrl+C或其他方式手动停止）  
mouse_listener.join()  