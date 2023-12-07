# 防閒置程式
import pyautogui
import time
import keyboard


running = True
# 按下esc鍵結束程式
def end_line():
    global running
    running = False
    print("Esc鍵被按下, 程式即將結束。")

# 每隔30秒移動滑鼠 按下esc鍵結束程式
def start_line():
    global running
    while running:
        for _ in range(6):  # 6次
            time.sleep(2)   # 每次暫停5秒
            if not running:  # 按下esc鍵結束程式
                return       # 程式結束
        pyautogui.moveRel(20, 0, duration=0.5)
        for _ in range(6):
            time.sleep(2)
            if not running:
                return
        pyautogui.moveRel(-20, 0, duration=0.5)
        pyautogui.click()

def main():
    keyboard.add_hotkey('esc', end_line)
    start_line()

if __name__ == '__main__':
    main()