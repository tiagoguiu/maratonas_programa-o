from math import ceil
X,Y = map(int,input('').split(' '))
resultado = ceil(Y/(Y-X))
print(resultado)