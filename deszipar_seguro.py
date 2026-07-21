#deszipar pasta com os json e mandar para a pasta "jsons"

import pyautogui
import time

diretorio = "seu-diretorio"

pyautogui.press("win")
pyautogui.write("Explorador de arquivos")
time.sleep(2)
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=1823, y=12) #clica pra deixar a janela cheia
time.sleep(1)
pyautogui.click(x=128, y=395) #clica em downloads
time.sleep(2)
pyautogui.click(x=570, y=143) #clica em classificar
time.sleep(2)
pyautogui.click(x=590, y=392) #clica em ordem crescente (pega o ultimo arquivo)
time.sleep(2)
pyautogui.click(x=558, y=244) #clica no ultimo arquivo baixado
time.sleep(2)
pyautogui.click(x=875, y=139) #clica para deszipar
pyautogui.write(diretorio) #escreve o lugar onde os arquivos serao deszipados
time.sleep(2)
pyautogui.click(x=659, y=462) #clica no quadrado pra abrir a pasta no diretorio escolhido
pyautogui.click(x=1142, y=768) #clica para deszipar
time.sleep(1)


pyautogui.click(x=726, y=216)
pyautogui.press("enter")
pyautogui.click(x=726, y=216)
pyautogui.press("enter")