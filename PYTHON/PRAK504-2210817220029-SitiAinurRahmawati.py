def reverse (a) :
    n=0
    b=0
    while (a != 0) :
        b = a % 10
        n = n * 10 + b
        a = a // 10
    return n

A, B = map(int, input().split())
A=reverse(A)
B=reverse(B)
C = A+B
print(reverse(C))