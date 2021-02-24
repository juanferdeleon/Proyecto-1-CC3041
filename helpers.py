'''
            Proyecto 1
    Análisis y Diseño de Algoritmos
        
Creado por:

    Maria Jose Castro               181202
    Juan Fernando De Leon Quezada   17822
    Josue Sagastume                 18173

'''

import os
from time import sleep
# The screen clear function
def screen_clear_1():
   # for mac and linux(here, os.name is 'posix')

   input("\nPresione Enter para continuar...")

   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def screen_clear_2():
   # for mac and linux(here, os.name is 'posix')

   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def is_int(user_input):
    '''User input int numbers'''
    while True:
        try:
            int(user_input)
        except ValueError:
            return False
        else:
            return True