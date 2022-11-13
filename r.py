# Bibliotecas 
from os import system
import time


# Instalando Colorama e TermColor ( sera Necessario )
system('pip install colorama')
system('pip install termcolor')
system('pip install keyboard')
system("cls")
time.sleep(1)


# Informando que voce sera redirecionado para uma nova area 
print('Executando O Main.py Em 5 Seg')
time.sleep(5)


# Executando o arquivo Principal 
# ( Lembrando que ele tem que na mesma pasta)
system('py main.py')