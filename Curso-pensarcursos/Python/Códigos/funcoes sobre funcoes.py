"""
def f1():
    x = 10
    def f2():
        print(x)

    f2()

f1()
"""

"""
def soma(x, y, z):
    return x+y+z

a = soma
a(1,2,3)
"""

f = (lambda x,y,z : x+y+z)
f(1,2,3)

