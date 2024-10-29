# Strings
print('''Quebra de linha
      manualmente\n''')
print('Exemplo com \nquebra de linha\n')
print('Utilizando o escape, simbolizado pelo \\\n')

# Strings Dinamicas
nome = '   Bruno Peres Floriano'
email = 'brunoperees@gmail.com'

print(f'Seja bem-vindo {nome}, seu e-mail cadastrado foi {email}')
print(nome.upper())
print(nome.lower())
print(nome.strip())
print(nome.find('no'))
print(nome.replace('Floriano', 'Peres'))

# Slice (Extraindo partes de um string)

link = 'www.ExemploDeLink.com/paraTreinar'

print(link[0])
print(link[-1])
print(link[0:5])
print(link[0:])
print(link[-5:])
print(link[5:])
print(link[:-5]) 

frase1 = 'Desafio manipulação de strings'
frase2 = 'jhonatan,rafael,carol,camilla'

palavras1 = frase1.split()
palavras2 = frase2.split(',')

print(','.join(palavras1))
print(' & '.join(palavras2))



