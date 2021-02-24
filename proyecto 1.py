# a) f(x) = x + 1
f = lambda x: x+1
print("\nf(x)=x+1")
print("f(5) = " + str(f(5)))

# b) g(x) = 2x
g = lambda x: 2*x
print("\ng(x)=2x")
print("g(6) = " + str(g(6)))

# c) h(x,y) = x^2 + y^2
h = lambda x, y: x**2 + y**2
print("\nh(x,y)=x^2 + y^2")
print("h(3,4) = " + str(h(3,4)))

# d) cero(f,x) = lambda f. lambda x. x
cero = lambda fn, x: x
print("\ncero(f,x)=x")
print("cero(f,4) = " + str(cero(f,4)))
print("cero(g,4) = " + str(cero(g,4)))

# e) uno(f,x) = lambda f. lambda x. f x
uno = lambda fn, x: fn(x)
print("\nuno(f,x)=f(x)")
print("uno(f,4) = " + str(uno(f,4)))
print("uno(g,4) = " + str(uno(g,4)))

# f) dos(f,x) = lambda f. lambda x. f f x
dos = lambda fn, x: fn(fn(x))
print("\ndos(f,x)=f(f(x))")
print("dos(f,4) = " + str(dos(f,4)))
print("dos(g,4) = " + str(dos(g,4)))

# g) tres(f,x) = lambda f. lambda x. f f f x
tres = lambda fn, x: fn(fn(fn(x)))
print("\ntres(f,x)=f(f(f(x)))")
print("tres(f,4) = " + str(tres(f,4)))
print("tres(g,4) = " + str(tres(g,4)))

# h) sucesor(n,f,x) = lambda n. lambda f. lambda x (f(nf(x)))
sucesor = lambda fn, n, x: fn(n(fn,x))
print("\nsucesor(n,f,x)=f(nf(x))")
print("sucesor(f, dos, 5) = " + str(sucesor(f,dos,5)))
print("sucesor(g, dos, 5) = " + str(sucesor(g,dos,5)))

# i) suma(a,b,f,x)
suma = lambda fn, a, b, x: a(fn,(b(fn,x)))
print("\nsuma(f, dos, uno, 3) = " + str(suma(f,dos,uno,3)))
print("suma(g, dos, uno, 3) = " + str(suma(g,dos,uno,3)))
