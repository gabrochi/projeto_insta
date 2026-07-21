import pyautogui
import time


senha = "sua-senha" #colocar a senha da conta aqui

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("ctrl", "l")
pyautogui.write("https://www.instagram.com/")
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=47, y=888)
time.sleep(2)
pyautogui.click(x=151, y=447)
time.sleep(4)
pyautogui.click(x=140, y=306) #clica no central de contas
time.sleep(2)
pyautogui.click(x=295, y=346) #clica em suas informacoes e permissoes
time.sleep(5)
pyautogui.click(x=466, y=593) #clica no exportar suas info
time.sleep(2)
pyautogui.click(x=953, y=399) #clica no exportar para dispositivo
time.sleep(3)
pyautogui.click(x=953, y=405) #clica no criar exportacao
time.sleep(2)
pyautogui.click(x=953, y=405) #clica no exportar para dispositivo
time.sleep(5)
pyautogui.click(x=926, y=694) #clica no personalizar info
time.sleep(2)
pyautogui.click(x=1250, y=350) #clica em limpar tudo (atividade do insta)
pyautogui.scroll(-1100)
pyautogui.click(x=1248, y=708) #clica em limpar tudo (info pessoal do insta)
pyautogui.scroll(-500)
pyautogui.click(x=1248, y=708) #clica em limpar contatos
pyautogui.scroll(-150)
pyautogui.click(x=1248, y=708) #clica em limpar tudo (infos registradas)
pyautogui.scroll(-450)
pyautogui.click(x=1248, y=708) #clica em limpar tudo (login e seguranca)
pyautogui.scroll(-160)
pyautogui.click(x=1248, y=708) #clica em limpar tudo (apps e sites fora do insta)
pyautogui.scroll(-160)
pyautogui.click(x=1248, y=708) #clica em limpar tudo (preferencias)
pyautogui.scroll(-250)
pyautogui.click(x=1248, y=708) #clica em limpar tudo (informacoes de anuncio)
pyautogui.click(x=915, y=922) #clica em salvar
pyautogui.click(x=938, y=851) #clica em formato
pyautogui.click(x=972, y=489) #clica em json
pyautogui.click(x=1080, y=607) #clica em salvar
pyautogui.click(x=882, y=753) #clica em intervalo de datas
pyautogui.click(x=963, y=741) #clica em personalizado
pyautogui.click(x=963, y=911) #clica em salvar
time.sleep(1)
pyautogui.scroll(-500)
time.sleep(1)
pyautogui.click(x=925, y=912)
time.sleep(1)
pyautogui.click(x=829, y=597) #clica no campo da senha
pyautogui.write(senha) #digita a senha
pyautogui.click(x=833, y=704) #confirma a exportacao
