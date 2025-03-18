#####################################################
from time import sleep
sleep(1)
#####################################################
from datetime import datetime  #Desta forma importa apenas um função da biblioteca
#import datetime               #Importa toda a biblioteca datetime 

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

aniversario = datetime(2024, 10, 28)
print("Sua data", aniversario)

print('\n')
data_atual = datetime.now()
faltaAniversario = data_atual - aniversario

print('Faltam para seu aniversario',faltaAniversario) 
#####################################################
import random

print(random.uniform(4,10))
print(random.random())
print(random.randint(4,10))

cores = ['verde', 'vermelho', 'azul']
print(random.choice(cores))

baralho = ['carta1','carta2','carta3','carta4']
print(random.shuffle(baralho))
print('As cartas foram embaralhadas',baralho)
#####################################################
import pyautogui
from mouseinfo import mouseInfo