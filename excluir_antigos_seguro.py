import pyautogui
import time

diretorio = "seu-diretorio"

pyautogui.press("win")
pyautogui.write("Explorador de arquivos")
time.sleep(2)
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=564, y=70) #clica no diretorio
pyautogui.write(diretorio)
time.sleep(2)
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("ctrl", "a")
pyautogui.press("del")

