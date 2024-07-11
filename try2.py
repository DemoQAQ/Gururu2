import socket
import pyautogui

# 设置监听的IP地址和端口号
A_HOST = '127.0.0.1'
A_PORT = 4408

# 创建TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((A_HOST, A_PORT))
server_socket.listen()

print(f"Listening for connections on {A_HOST}:{A_PORT}")

# 等待A主机连接
client_socket, _ = server_socket.accept()

while True:
    # 接收从A主机发送的按键名称
    key = client_socket.recv(1024).decode()
    print(key)
    pyautogui.press(key)    
    pyautogui.press('esc')

        
