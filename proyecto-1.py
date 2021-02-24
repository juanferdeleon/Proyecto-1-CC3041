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

# product = (lambda m: lambda n: lambda f: lambda x: n(m(f))(x))

# zero = lambda f: lambda x: x
# one   = lambda f: lambda x: f(x)
# two   = lambda f: lambda x: f(f(x))
# three = lambda f: lambda x: f(f(f(x)))

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

def funtion_menu():
    return '''

    Funciones

1.  𝑓(𝑥)=𝑥+1
2.  𝑔(𝑥)=2𝑥
    '''

def lambda_menu():
    return '''

    Funciones Lambda

0.  𝑐𝑒𝑟𝑜(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑥
1.  𝑢𝑛𝑜(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑓𝑥
2.  𝑑𝑜𝑠(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑓𝑓𝑥
3.  𝑡𝑟𝑒𝑠(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑓𝑓𝑓𝑥
    '''



def function_options(fun, op):
    if op == '1':
        '''1.  𝑓(𝑥) = 𝑥 + 1'''
        x = ''
        while not is_int(x):
            print("\n1.  𝑓(𝑥) = 𝑥 + 1")
            x = input("\nx = ")
        
        print("\nResutaldo: " + str(fun(f, int(x))))
        return False
    elif op == '2':
        '''2.  𝑔(𝑥)=2𝑥'''
        x = ''
        while not is_int(x):
            print("\n2.  𝑔(𝑥)=2𝑥")
            x = input("\nx = ")
        print('\nResultado ' + str(fun(g, int(x))))
        return False
    else:
        print("\nERROR: Ingrese una opcion valida.\n")
        return True

def choose_fun():

    while True:

        print(funtion_menu())

        op = input('\nIngrese una opcion: ')

        if op == '1':
            return f
        elif op == '2':
            return g
        else:
            print("\nERROR: Ingrese una opcion valida.\n")

def choose_lambda_fun(x):

    while True:

        print(lambda_menu())

        op = input('\n' + str(x) + " = " )

        if op == '0':
            return cero
        elif op == '1':
            return uno
        elif op == '2':
            return dos
        elif op =='3':
            return tres
        else: 
            print("\nERROR: Ingrese una opcion valida.\n")


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
            while not is_int(x) and not is_int(y) and not x == '' or y == '' :
                screen_clear_2()
                print ("\n\t\tProyecto 1")
                print("\n3.  ℎ(𝑥,𝑦)=𝑥^2+𝑦^2")
                x = input("\nx = ")
                y = input("\ny = ")
            print('\nh(𝑥, y) = ' + str(h(int(x), int(y))))
            screen_clear_1()
        elif op == '4':
            '''4.  𝑐𝑒𝑟𝑜(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑥'''

            screen_clear_2()
            print ("\n\t\tProyecto 1")
            print("\n4.  𝑐𝑒𝑟𝑜(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑥")
            print("\nResultado: " + str(funcion(cero)))

            screen_clear_1()
        elif op == '5':
            '''5.  𝑢𝑛𝑜(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑓𝑥'''

            screen_clear_2()
            print ("\n\t\tProyecto 1")
            print("\n5.  𝑢𝑛𝑜(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑓𝑥")
            print("\nResultado: " + str(funcion(uno)))

            screen_clear_1()
        elif op == '6':
            '''6.  𝑑𝑜𝑠(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑓𝑓𝑥'''

            screen_clear_2()
            print ("\n\t\tProyecto 1")
            print("\n6.  𝑑𝑜𝑠(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑓𝑓𝑥")
            print("\nResultado: " + str(funcion(dos)))

            screen_clear_1()
        elif op == '7':
            '''7.  𝑡𝑟𝑒𝑠(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑓𝑓𝑓𝑥'''

            screen_clear_2()
            print ("\n\t\tProyecto 1")
            print("\n7.  𝑡𝑟𝑒𝑠(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑓𝑓𝑓𝑥")
            print("\nResultado: " + str(funcion(tres)))

            screen_clear_1()
        elif op == '8':
            '''8.  𝑠𝑢𝑐𝑒𝑠𝑜𝑟(𝑛,𝑓,𝑥)=𝜆𝑛.𝜆𝑓.𝜆𝑥(𝑓(𝑛𝑓(𝑥)))'''

            screen_clear_2()
            print("\n\t\tProyecto 1")
            print("\n8.  𝑠𝑢𝑐𝑒𝑠𝑜𝑟(𝑛,𝑓,𝑥)=𝜆𝑛.𝜆𝑓.𝜆𝑥(𝑓(𝑛𝑓(𝑥)))")

            fn = f
            n = cero_1

            x = ''
            while not is_int(x):
                x = input("\nx = ")
            
            print("\nResultado: " + str(sucesor(fn, n, int(x))))

            screen_clear_1()
        elif op == '9':
            '''9.  𝑠𝑢𝑚𝑎(𝑎,𝑏,𝑓,𝑥)'''

            screen_clear_2()
            print("\n\t\tProyecto 1")
            print("\n9.  𝑠𝑢𝑚𝑎(𝑎,𝑏,𝑓,𝑥)")
            
            a = 'a'
            b = 'b'

            a = choose_lambda_fun(a)
            b = choose_lambda_fun(b)

            print("\nResultado: ", funcion(suma(a)(b)))

            screen_clear_1()
        elif op == '10':
            '''10. 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑐𝑎𝑐𝑖ó𝑛(𝑎,𝑏,𝑓,𝑥)'''

            screen_clear_2()
            print("\n\t\tProyecto 1")
            print("\n10. 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑐𝑎𝑐𝑖ó𝑛(𝑎,𝑏,𝑓,𝑥)")
            
            a = 'a'
            b = 'b'

            a = choose_lambda_fun(a)
            b = choose_lambda_fun(b)

            print("\nResultado: ", funcion(multiplicacion(a)(b)))

            screen_clear_1()
        elif op == '11':
            wants_to_continue = False
            screen_clear_1()
        else:
            print("\nERROR: Ingrese una opcion valida.\n")
            screen_clear_1()


if __name__ == '__main__':
    main()