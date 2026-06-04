import time
try:
    import pyautogui
    print("Importou! Tamanho da tela:", pyautogui.size())
except Exception as e:
    print("Falhou:", e)
def escrever_com_atraso(texto):
    print("Aguardando 5 segundos...")
    time.sleep(5)
    print("Escrevendo...")
    pyautogui.write(texto, interval=0.75)
texto_para_escrever = input("Digite o que você quer que o programa escreva: ")
escrever_com_atraso(texto_para_escrever)
