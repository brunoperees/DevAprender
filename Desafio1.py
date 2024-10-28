# PROJETO 1 

## Objetivo de projeto

# * Estamos criando um módulo de login do nosso aplicativo, e você deve obter as seguintes informações do funcionário.

## Módulo 1 - Gerar registro do funcionário

### Funcionalidades do módulo 1
'''

1. Obtenha o nome do usuário

2. Obtenha a idade do usuário

3. Registre de forma automática a data do cadastro do usuário, usando a data do registro como data de registro

4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:
'''

'''
5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)
'''

from datetime import datetime
import random
TESTEEEEEEEEEEEEEEEEEEEEEEEEEE
nome_usuario = input('Informe seu nome completo')
idade_usuario = int(input('Informe sua idade'))
cadastro =datetime.now()
aniversario = datetime.strptime(
    input('Insira a data do seu aniversário no seguinte formato: DD/MM/AAAA \n'), '%d/%m/%Y')
cartoes = ['R$50,00','R$250,00','R$120,00']
premiacao = random.choice(cartoes)

print(f'Olá {nome_usuario}, você tem: {idade_usuario} anos, realizou seu cadastro: {cadastro.day}/{cadastro.month}/{cadastro.year} e seu aniversario é: {aniversario} você foi presenteado com um cartão no valor de: {premiacao}')
