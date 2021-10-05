
while True:
    try:
        a = input().split()

        b = int(a[0])

        c = int(a[1])

        d = int(a[2])

        if b >=2 and b<=1000 and c>=1 and c<=30 and d>=1 and d<=70:
            tex = input().split()
            test = 0
            l = 1
            pag = 1
            for i in range (len(tex)):
                if test + len(tex[i]) <= d:
                    test += len(tex[i])
                else:
                    l+=1
                    test = 0 +len(tex[i])
            if l > c:
                pag += 1

        print(pag)
    except EOFError:
        break