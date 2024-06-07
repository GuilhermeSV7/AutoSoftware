import pyautogui
import time


pyautogui.FAILSAFE = False
def press_windows_e():
    #Abre o Windows Explorer
    time.sleep(1)
    pyautogui.hotkey('win', 'e')
    #Centraliza o Windows Explorer
    time.sleep(1)
    pyautogui.hotkey('win', 'right')
    #Abre o servidor
    time.sleep(1)
    pyautogui.click(825, 40)
    time.sleep(1)
    pyautogui.click(825, 40)

    time.sleep(1)
    pyautogui.click(1000, 75)
    #Faz a configuracao do Servidor
    time.sleep(1)
    pyautogui.click(515, 403)
    time.sleep(1)
    pyautogui.typewrite(r"\\10.140.32.253\software")
    #Caso necessario ative o texto da linha 23
    time.sleep(1)
    #pyautogui.click(512, 456)
    pyautogui.click(512, 486)
    time.sleep(1)
    pyautogui.click(885, 635)

    #Nome do Usuario 
    time.sleep(2)
    pyautogui.click(425, 255)
    time.sleep(2)
    pyautogui.typewrite(r"suporte")

    #Senha do Usuario
    time.sleep(2)
    pyautogui.click(430, 375)
    time.sleep(2)
    pyautogui.typewrite(r"ucb@2021")

    #Concluir
    time.sleep(1)
    pyautogui.click(500, 515)

    #Selecionando arquivos
    time.sleep(1)
    pyautogui.hotkey('win', 'right')

    time.sleep(1)
    pyautogui.click(1160, 70)
    time.sleep(1)
    pyautogui.click(1160, 70)
    time.sleep(2)
    pyautogui.typewrite(r"2024\ARDUINO")
    time.sleep(1)
    pyautogui.press('enter')

    time.sleep(2)
    #Instalando
    pyautogui.click(935, 132)
    pyautogui.click(935, 132)
    time.sleep(5)
    #Apertando Iniciar
    pyautogui.click(785, 466)
    time.sleep(5)

    pyautogui.click(832, 596)
    time.sleep(5)
    pyautogui.click(516, 401)
    time.sleep(2)
    pyautogui.click(832, 596)
    time.sleep(2)
    pyautogui.hotkey('right')
    time.sleep(2)
    pyautogui.press('enter')
if __name__ == "__main__":
    press_windows_e()
