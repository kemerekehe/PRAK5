def maksimal(a, b) :
    if a>b :
        return a
    return b

def minimal (a, b) :
    if a<b :
        return a
    return b

batas = 0
maks = -100000
minim = 100000
bilangan=int(input())

while batas < bilangan :
    nilai = map(int, input().split())
    for nilai in nilai :
        maks = maksimal(maks, nilai)
        minim = minimal(minim, nilai)
        batas=batas+1
    print(maks, minim)