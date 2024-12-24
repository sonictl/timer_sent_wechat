import time
import pyautogui
import os
from Quartz.CoreGraphics import (
    CGEventSourceCreate,  # 单独把这个函数名也添加到导入列表中
    CGEventCreateKeyboardEvent,
    CGEventPost,
    kCGEventKeyDown,
    kCGEventKeyUp,
    kCGHIDEventTap,
    kCGEventSourceStateHIDSystemState
)

def press_key(key):
    event_source = CGEventSourceCreate(kCGEventSourceStateHIDSystemState)
    key_down = CGEventCreateKeyboardEvent(event_source, key, True)
    key_up = CGEventCreateKeyboardEvent(event_source, key, False)
    CGEventPost(kCGHIDEventTap, key_down)
    CGEventPost(kCGHIDEventTap, key_up)

def activate_window(window_title):
    # macOS does not directly provide a way to find windows by title
    # However, we can use AppleScript to focus a window by title and then simulate key presses
    script = f"""
    tell application "System Events"
        set frontmost of the first process whose name contains "{window_title}" to true
    end tell
    """
    os.system(f"osascript -e '{script}'")

def input_text(text):
    for char in text:
        keycode = ord(char)
        press_key(keycode)
        time.sleep(0.1)  # 适当添加间隔时间，模拟更真实的输入速度

# 激活窗口（按标题匹配）
window_title = "WeChat"  # 请替换为目标程序的窗口标题
activate_window(window_title)

# 等待窗口激活
time.sleep(1)

# 等待3小时（10800秒）
# print("等待...")
# time.sleep(60)  # 3 小时 = 10800 秒

# 模拟输入文字
text_to_type = "veuiyidrzidsuurudewfzi " # 需要输入的文字，“这是一段自动输入的文字”双拼 = veuiyidrzidsuurudewfzi
print(f"模拟输入文字: {text_to_type}")
pyautogui.typewrite(text_to_type, interval=0.1)  # 模拟输入，每个字符间隔 0.1 秒
time.sleep(1)

# 模拟按下 Enter 键
press_key(36)  # 36 是 Enter 键的代码

# 等待
time.sleep(1)

# 模拟按下 Enter 键
press_key(36)  # 36 是 Enter 键的代码
