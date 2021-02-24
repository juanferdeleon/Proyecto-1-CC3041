'''
            Proyecto 1
    Análisis y Diseño de Algoritmos
        
Creado por:

    Maria Jose Castro               181202
    Juan Fernando De Leon Quezada   17822
    Josue Sagastume                 18173

'''

operador = lambda x: x + 1

funcion = lambda n: n(operador)(0)

# a) f(x) = x + 1
f = lambda x: x+1
# b) g(x) = 2x
g = lambda x: 2*x

# c) h(x,y) = x^2 + y^2
h = lambda x, y: x**2 + y**2

# d) cero(f,x) = lambda f. lambda x. x
cero = lambda f: lambda x: x
cero_1 = lambda fn, x: x

# e) uno(f,x) = lambda f. lambda x. f x
uno = lambda f: lambda x: f(x)

# f) dos(f,x) = lambda f. lambda x. f f x
dos = lambda f: lambda x: f(f(x))

# g) tres(f,x) = lambda f. lambda x. f f f x
tres = lambda f: lambda x: f(f(f(x)))

# h) sucesor(n,f,x) = lambda n. lambda f. lambda x (f(nf(x)))
sucesor = lambda fn, n, x: fn(n(fn,x))

# i) suma(a,b,f,x)
suma = lambda m: lambda n: lambda f: lambda x: n(f)(m(f)(x))

# j) multiplicacion(a, b, f, x)
multiplicacion = lambda a : lambda b : lambda f: lambda x : a(b(f))(x)