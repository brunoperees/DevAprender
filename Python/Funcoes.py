#Pode-se utilizar um parametro chamado Return (vaos rever com calma)

#1 - Existem diferentes tipos de funções: posicionais e as nomeadas *
def apreentar_lugar (horario, local="nossa loja"):
    print(f'Conheça {local},  horario de funcionamento: {horario}')
apreentar_lugar('18:00','Diney')

def gerar_nome_completo(nome, sobrenome):
    print(f'Seja bem-vindo, O seu primeiro nome é {nome} e seu ultimo nome é {sobrenome}')
gerar_nome_completo('Bruno','Floriano')

def calcular_valores(produto,preco, quantidade=2):
    print(f'O {produto}, tem o valor de {preco} e sua quantidade total em estoque é: {quantidade}')
    total = preco * quantidade
    print(f'O valor total do produto é: {total}')
calcular_valores('sandalia',float(3.50))

#2 - Funções com *args (posicionais) dinamicos 
def gerar_objeto_personalizado(cor,*,altura,formato): #Significa que após o * os parametros são 
    print(f'A cor é: {cor} com uma altura de {altura} e {formato}')
gerar_objeto_personalizado('amarelo', altura=2.5, formato='retangular')

#3 - **kwargs (keywords arguments) nomeados
def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)
concatenar(a='Esta', b='frase',c='é um', d='exemplo')
#4 - Exemplo com *args e ##kwargs
def fazer_calculo(nome,*args,**kwargs):
    print(nome)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for kwarg in kwargs.values():
        print(kwarg)
#5 - Decorators - Consegue executar uma ou várias ações e depois chamar a função dentro de outra
import datetime

def monitorar_horario(funcao):
    def monitor():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return monitor

@monitorar_horario
def baixar_musicas():
    print('Baixando musicas')

baixar_musicas()