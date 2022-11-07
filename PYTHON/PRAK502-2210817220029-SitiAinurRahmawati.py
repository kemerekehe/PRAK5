import math
def hitung(nilai1, nilai2) :
    Hasil=nilai1-nilai2
    return Hasil
def mutlak(angka) :
    if (angka<0) :
        angka=abs(angka)
    return angka
a, c, b, d = map(int, input().split())
Hasil = hitung(a,b) + hitung(c,d)
print(mutlak(Hasil))