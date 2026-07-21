import pyautogui
import time

for i in range(10):
    x, y = pyautogui.position()
    print(f"Posição: ({x}, {y})")
    time.sleep(1)