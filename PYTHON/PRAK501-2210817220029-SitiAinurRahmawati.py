def MaxBilangan(a, b, c, d) :
    if a>b and a>c and a>d :
        return a
    elif b>c and b>d and b>a :
        return b
    elif c>b and c>d and c>a :
        return c
    elif d>b and d>c and d>a :
        return d

a, b, c, d = map(int, input().split())
hasil = MaxBilangan(a, b, c, d)
print(hasil)