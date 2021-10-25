first, second = map(int, input().split())

test = str(second)
list = []

for x in test:
    list.append(int(x))

for z in list:
    if z == first:
        list.remove(z)
print(list)
    
if list[0] == first:
    list.append(0)
    list.remove(first)
print(list)

