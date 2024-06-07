import pyautogui
import time


pyautogui.FAILSAFE = False

def press_windows_e():

    #Abrindo Arquivos
    time.sleep(1)
    pyautogui.hotkey('win', 'e')

    #Centralizando Arquivos
    time.sleep(1)
    pyautogui.hotkey('win', 'right')

    #Clickando em Area de Trabalho 
    time.sleep(1)
    pyautogui.click(806, 140)

    #Clickando no Arduino
    time.sleep(1)
    pyautogui.click(973, 282)

    #Clickando com o Botao direito
    time.sleep(1)
    pyautogui.rightClick(973, 282)

    #Concendendo administrador
    time.sleep(1)
    pyautogui.click(1035, 313)

    #Apertando Sim
    time.sleep(5)
    pyautogui.click(844, 603)

    #Todos os usuarios 
    time.sleep(2)
    pyautogui.click(515, 399)

    #Avanca
    time.sleep(1)
    pyautogui.click(834, 600)

    #Confirma
    time.sleep(1)
    pyautogui.click(834, 600)

if __name__ == "__main__":
    press_windows_e()