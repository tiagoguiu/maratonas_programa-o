def Fib(n):
    global cont
    if n==0 or n==1:
        return n
    else:
        cont+=2
        return Fib(n-1)+Fib(n-2)

cont = 0
a = int(input())
for i in range(a):
    n = int(input())
    fi = Fib(n)
    print('Fib({}) = {} calls = {}'.format(n, cont, fi))
    cont = 0