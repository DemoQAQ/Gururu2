import pyautogui  
import time  
  
last_position = None  
last_time = None  
click_threshold = 10  # 位置变化阈值  
time_threshold = 0.1  # 时间阈值，秒  
  
try:  
    while True:  
        current_position = pyautogui.position()  
        current_time = time.time()  
  
        if last_position is not None:  
            # 计算位置变化和时间差  
            distance = ((current_position.x - last_position.x) ** 2 +  
                        (current_position.y - last_position.y) ** 2) ** 0.5  
            time_diff = current_time - last_time  
  
            # 检查是否可能是点击  
            if distance < click_threshold and time_diff < time_threshold:  
                # 这里可以添加进一步的确认逻辑，比如等待一段时间看是否有进一步移动  
                print("可能检测到鼠标点击！")  
  
        # 更新位置和时间  
        last_position = current_position  
        last_time = current_time  
  
        # 打印当前位置（可选）  
        print(f"当前鼠标位置: {current_position}")  
  
        # 设置刷新时间间隔  
        time.sleep(0.05)  
  
except KeyboardInterrupt:  
    print("程序已停止")