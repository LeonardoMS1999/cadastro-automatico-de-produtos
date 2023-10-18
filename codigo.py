import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(5)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(5)
pyautogui.press("tab")
pyautogui.write("leohmsales@gmail.com")

pyautogui.press("tab")
pyautogui.write("12345678")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(5)

import pandas

pyautogui.press("tab")

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index: 
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")  
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")  
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")  
    pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")  
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.click(x=1908, y=123)
    pyautogui.click(x=745, y=300)

 


