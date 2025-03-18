#1 Crie uma lista que tenha os nomes dos 3 objetos que você mais usa durante o dia e imprima ele na tela
itens_usados = ['lapis','caneta','caderno']
print(itens_usados[0])
#2 Usando apenas uma linha de código, crie uma lista de 10 a 131
numeros = list(range(10,132))
#3 Imprima na tela o resultado da combinação da lista do desafio 1 e desafio 2
print(f'{itens_usados} + {numeros}')
#4 Crie uma lista de listas(matriz) que tenha os nomes dos 3 objetos que você mais usa durante o dia, mas agora dentro de cada item você vai colocar uma informação extra, coloque o valor em reais desse objeto também e imprima ele
matriz = [['Computador', 7000], ['Celular', 2000], ['Bicicleta', 750]]
print(matriz[1][0], matriz[1][1])

