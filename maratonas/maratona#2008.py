
a = input().split()

d = int(a[0]) #dsp
p = int(a[1]) # ppp
r = int(a[2]) #rivalidade
b = int(a[3]) #orçamento

dsp = []
ppp = []
rival = []
removido1 = []
removido2 = []

input1 = input().split()
for i in range(d):
    dsp.append(int(input1[i]))
dsp.sort()
    

input2 = input().split()
for i in range(p):
    ppp.append(int(input2[i]))
ppp.sort()

for i in range(r):
    input3 = input().split() 
    riv = int(input3[0])
    riv2 = int(input3[1])
    if riv in removido1:
        continue
    else:
        removido1.append(dsp.pop(riv-1)) 



