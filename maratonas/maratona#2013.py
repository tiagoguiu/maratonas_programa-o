
a = int(input())
b = []

for i in range(a):
    b.append(i+1)
    if b.count(i) >= 2:
        print("não")