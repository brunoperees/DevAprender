import pyautogui
from time import sleep

pyautogui.moveTo(1780,185, duration=2) #Localizando Lupa
pyautogui.click()

pyautogui.moveTo(150,185, duration=2) #Aba tipo de pesquisa
pyautogui.click()

pyautogui.moveTo(122,424, duration=2) #Opção "Ativo"
pyautogui.click()

with open('dados.txt','r') as dados:
    for linha in dados:
        patrimonio = linha.split(',')[0]
        pyautogui.click(363,185, duration=2)
        pyautogui.write(patrimonio)
        sleep(1)
        pyautogui.press('enter')
        sleep(5)                            #Aguardando a pagina carregar

        pyautogui.moveTo(1334,409, duration=2) #Exibir ativo completo
        pyautogui.click()
        sleep(3)
        pyautogui.moveTo(1215,261, duration=2) #Editar ativo
        pyautogui.click()

        pyautogui.moveTo(1224,275, duration=2) #Rolagem ditar ativo
        sleep(1) 
        pyautogui.scroll(-1005) #Scroll (Barra lateral)
        sleep(1)

        pais = linha.split(',')[1]
        pyautogui.click(80,250, duration=2)
        pyautogui.write(pais)
        sleep(1)

        cidade = linha.split(',')[2]
        pyautogui.click(507,250, duration=2)
        pyautogui.write(cidade)
        sleep(1)

        setor = linha.split(',')[3]
        pyautogui.click(932,250, duration=2)
        pyautogui.write(setor)
        sleep(1) 

        recebimento = linha.split(',')[4]
        pyautogui.click(79,672, duration=2)
        pyautogui.write(recebimento)
        pyautogui.click(43,732, duration=2)
        sleep(1) 
        
        compra = linha.split(',')[5]
        pyautogui.click(556,776, duration=2)
        pyautogui.write(compra)
        pyautogui.click(43,732, duration=2)
        sleep(1) 
        
        garantia = linha.split(',')[6]
        pyautogui.click(540,483, duration=2)
        pyautogui.write(garantia)
        pyautogui.click(43,732, duration=2)
        sleep(1) 
        
        nf = linha.split(',')[7]
        pyautogui.click(113,897, duration=2)
        pyautogui.write(nf)
        sleep(1) 
        
        oc = linha.split(',')[8]
        pyautogui.click(503,901, duration=2)
        pyautogui.write(oc)
        sleep(1) 
        
        ve = linha.split(',')[9]
        pyautogui.click(971,900, duration=2)
        pyautogui.write(ve)
        sleep(1) 

        pyautogui.moveTo(1045,714, duration=2) #Posição de rolagel Rolagem lateral (Proprietario)
        sleep(1) 
        pyautogui.scroll(-500) #Scroll (Barra lateral)
        sleep(1)

        pyautogui.click(1115,743, duration=2) #
        pyautogui.click(89,820, duration=2)
       
        
        proprietario = linha.split(',')[10]
        pyautogui.click(1261,385, duration=2) #Clique na caixa de texto do Proprietario
        pyautogui.write(proprietario)         #Escrever Proprietario
        
        sleep(1)
        pyautogui.press('enter')              #Enter para listar Proprietario
        sleep(1)

        pyautogui.click(1013,557, duration=2) #Clique em Selecionar Proprietario
        pyautogui.click(1841,954, duration=2) #Clique Salvar Proprietario
        pyautogui.click(1831,963, duration=2) #Clique Salvar Modificações
       

# 1 - Clica na Lupa em Buscar 
# 2 - Mudar a busca para Ativo
# 3 - Digitar o nome do computador 
# 4 - Clicar em Exibir ativo completo 
# 5 - Clicar em editar ativo 