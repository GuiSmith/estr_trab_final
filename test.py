import os

def tratar(texto):
    parts = texto.split(' ')
    if len(parts) == 1:
        if texto == 'INFIXA':
            print('executar infixa')
        elif texto == 'POSFIXA':
            print('executar POSFIXA')
        elif texto == 'PREFIXA':
            print('executar PREFIXA')
        else:
            print('invalido')
    else:
        if parts[0] == 'I':
            print('inserir item na arvore')
        elif parts[0] == 'P':
            print('verificar se item existe na arvore')
        else:
            print('invalido')
            
while True:
    os.system('clear')
    text = input(': ')
    if text == 'sair':
        break
    else:
        tratar(text)
    input("Digite uma tecla para continuar.")