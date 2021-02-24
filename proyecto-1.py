'''
            Proyecto 1
    Análisis y Diseño de Algoritmos
        
Creado por:

    Maria Jose Castro               181202
    Juan Fernando De Leon Quezada   17822
    Josue Sagastume                 18173

'''

from helpers import screen_clear_1, screen_clear_2, is_int
from lambda_functions import *

def menu():
    return '''
    
    Proyecto 1

1.  𝑓(𝑥)=𝑥+1
2.  𝑔(𝑥)=2𝑥
3.  ℎ(𝑥,𝑦)=𝑥^2+𝑦^2
4.  𝑐𝑒𝑟𝑜(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑥
5.  𝑢𝑛𝑜(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑓𝑥
6.  𝑑𝑜𝑠(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑓𝑓𝑥
7.  𝑡𝑟𝑒𝑠(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑓𝑓𝑓𝑥
8.  𝑠𝑢𝑐𝑒𝑠𝑜𝑟(𝑛,𝑓,𝑥)=𝜆𝑛.𝜆𝑓.𝜆𝑥(𝑓(𝑛𝑓(𝑥)))
9.  𝑠𝑢𝑚𝑎(𝑎,𝑏,𝑓,𝑥)
10. 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑐𝑎𝑐𝑖ó𝑛(𝑎,𝑏,𝑓,𝑥)
11. Salir
    '''

def main():
    '''Main'''
    wants_to_continue = True

    while wants_to_continue:

        print(menu())

        op = input('\nIngrese una opcion: ')

        if op == '1':
            '''1.  𝑓(𝑥) = 𝑥 + 1'''
            x = ''
            while not is_int(x):
                screen_clear_2()
                print ("\n\t\tProyecto 1")
                print("\n1.  𝑓(𝑥) = 𝑥 + 1")
                x = input("\nx = ")
            print('\n𝑓(𝑥) = ' + str(f(int(x))))
            screen_clear_1()
        elif op == '2':
            '''2.  𝑔(𝑥)=2𝑥'''
            x = ''
            while not is_int(x):
                screen_clear_2()
                print ("\n\t\tProyecto 1")
                print("\n2.  𝑔(𝑥)=2𝑥")
                x = input("\nx = ")
            print('\ng(𝑥) = ' + str(g(int(x))))
            screen_clear_1()
        elif op == '3':
            '''3.  ℎ(𝑥,𝑦)=𝑥^2+𝑦^2'''
            x = ''
            y = ''
            while not is_int(x) and not is_int(y):
                screen_clear_2()
                print ("\n\t\tProyecto 1")
                print("\n3.  ℎ(𝑥,𝑦)=𝑥^2+𝑦^2")
                x = input("\nx = ")
                y = input("\ny = ")
            print('\nh(𝑥, y) = ' + str(h(int(x), int(y))))
            screen_clear_1()
        elif op == '4':
            print("4")
            screen_clear_1()
        elif op == '5':
            print("5")
            screen_clear_1()
        elif op == '6':
            print("6")
            screen_clear_1()
        elif op == '7':
            print("7")
            screen_clear_1()
        elif op == '8':
            print("8")
            screen_clear_1()
        elif op == '9':
            print("9")
            screen_clear_1()
        elif op == '10':
            print("10")
            screen_clear_1()
        elif op == '11':
            wants_to_continue = False
            screen_clear_1()
        else:
            print("\nERROR: Ingrese una opcion valida.\n")
            screen_clear_1()


if __name__ == '__main__':
    main()