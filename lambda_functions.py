'''
            Proyecto 1
    Análisis y Diseño de Algoritmos
        
Creado por:

    Maria Jose Castro               181202
    Juan Fernando De Leon Quezada   17822
    Josue Sagastume                 18173

'''

# a) f(x) = x + 1
f = lambda x: x+1
# b) g(x) = 2x
g = lambda x: 2*x

# c) h(x,y) = x^2 + y^2
h = lambda x, y: x**2 + y**2

# d) cero(f,x) = lambda f. lambda x. x
cero = lambda fn, x: x

# e) uno(f,x) = lambda f. lambda x. f x
uno = lambda fn, x: fn(x)

# f) dos(f,x) = lambda f. lambda x. f f x
dos = lambda fn, x: fn(fn(x))

# g) tres(f,x) = lambda f. lambda x. f f f x
tres = lambda fn, x: fn(fn(fn(x)))

# h) sucesor(n,f,x) = lambda n. lambda f. lambda x (f(nf(x)))
sucesor = lambda fn, n, x: fn(n(fn,x))

# i) suma(a,b,f,x)
suma = lambda fn, a, b, x: a(fn,(b(fn,x)))