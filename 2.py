def z(a):
    fom = [a[-1]]
    fom += a[:n-1]
    return fom 
n = int(input())
b = [x for x in input().split()]
print(*z(b))