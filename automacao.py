#Utilizando caracteres especiais
import pyperclip
def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')

escrever_frase('Olá, bom dia') 

#Movimentar Mouse
import pyautogui
from mouseinfo import mouseInfo
mouseInfo()

pyautogui.moveTo(375,747,duration=2) #Movimentar para uma coordenada
pyautogui.click()
pyautogui.moveTo(877,153,duration=2)
pyautogui.click()
pyautogui.moveTo(518,601,duration=2)
pyautogui.click()
pyautogui.scroll(-7.000) #Scroll (Barra lateral)
pyautogui.dragTo(518,601,duration=2) #Arrastar
pyautogui.click(x=1066,y=226,duration=2, clicks=10,button='left')

#Utilizar o teclado/Escrever
pyautogui.typewrite("Desta forma que se escreve")
pyautogui.press('tab', 'space')

pyautogui.keyDown('ctrl')
pyautogui.keyDown('a')
pyautogui.keyUp('ctrl')
pyautogui.keyUp('a')

pyautogui.hotkey('ctrl', 'a')

#Criando dialogos/alertas
pyautogui.alert(text='Iniciando automacao', title='Titulo de texto', button="OK")

#Pedindo informação ao usuário
email = pyautogui.prompt(text='Digite seu e-mail', title='Informações obrigadorias')
pyautogui.password(text='Digite sua senha:',title='Dados de login', mask='*')

#Confirmar se algo deve ou não ocorrer
resposta = pyautogui.confirm(text='Continuar rodando nossa automacao', title='Confirmação', buttons=['sim','não'])
if resposta == "sim":
    print('Continuando automacao')

#Tirando Print da tela
pyautogui.screenshot('nomedaFoto.jpg') #Tela inteira
pyautogui.screenshot('nomedaFoto.jpg', region=(600,230,201,230)) #Determinado local Cima-esquerda, Direita-baixo

pyautogui.locateOnScreen('nomedaimagem.jpg') #Encontra a imagem (não é tão preciso)
pyautogui.locateCenterOnScreen('nomedaimagem.jpg') #Encontra o centro da imagem
pyautogui.click(x=1066,y=226,duration=2)

captcha = pyautogui.locateCenterOnScreen('nomedaimagem.jpg') #Encontra o centro da imagem
pyautogui.click(captcha[0], captcha[1],duration=2) #Usa os parametos armazenados acima

#Usando comparação com cor 

pyautogui.pixelMatchesColor(312,231(32,723,31)) #2 Primeiras são coordenadas do clique e as outras da cor


