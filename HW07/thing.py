def inc(x):
    return x + 1

z = inc

print z(10)

def h(x):
    return lambda y: x + y

print h(1) #closure
print h(2) #closure
print h(1)(3)
print h(2)(5)

b=h(1) #closure

def f(x):
    def g(y):
        return x + y
    return g
    
print f(1) ##closure
print f(2) ##closure
print f(1)(3)
print f(2)(5)

a=f(1) #closure

def repeat(x):
    def num(y):
        s = ""
        for i in range(y):
            s += x
        return s
    return num

r1 = repeat("hello")
r2 = repeat("goodbye")

print r1(3)
print r2(2)
print r1(1)
print r2(1)
print repeat("cool")(3)