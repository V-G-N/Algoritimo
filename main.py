# Bibliotecas 
import time, os, colorama
from termcolor import colored

#print(colored('Error Test!!!', 'red'))
# LOGICA DE PROGRAMAÇÃO 
##    try:

def menu():
    while menu:
        pula = 'G4L4X1 EXTREME'
        print(colored('iniciando o Painel', 'green'))
        print(colored("""
        1. testes
        2. criar virus
        3. exit


        """, 'yellow'))
        dec = input (colored ('Options > ', 'blue'))
        if dec == '1':
            print('Okay esta fucionando')
            print(f'{pula:.^20}')
            print('Retorna ?')
            dec = input('Y = Sim /// N = Nao  : ')
            if dec == 'y':
                menu()
            elif dec == 'n':
                print('ok fechando')
                exit()
            else:
                print('Opção invalida')
        elif dec == '2':
            print('kkkk quer se fuder mesmo em')
            print(f'{pula:.^20}')
            print('Retorna ?')
            dec = input('Y = Sim /// N = Nao  : ')
            if dec == 'y':
                menu()
            elif dec == 'n':
                print('ok fechando')
                exit()
            else:
                print('Opção invalida')
        elif dec == '3':
            print(colored('Ok Goodbye', 'red'))
            print(f'{pula:.^20}')
            print('Retorna ?')
            dec = input('Y = Sim /// N = Nao  : ')
            if dec == 'y':
                menu()
            elif dec == 'n':
                print('ok fechando')
                exit()
            else:
                print('Opção invalida')
            exit()
        else:
            print(colored('ERROR', 'red'))
        os.system('cls')    
menu()
