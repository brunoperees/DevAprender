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