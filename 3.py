m = int(input()) #m = int(input()) #максимальная масса, которую выдержит лодка
n = int(input()) #n = int(input()) #количество рыбаков

a = []
b = []

for i in range(n):
    a.append(int(input())) #вес каждого рыбака 

for y in range(len(a)):
    if a[y] + min(a) <= m:
        b += [[a[y], min(a)]]
        a[y] += m
        a[a.index(min(a))] += m
    else:
        if a[y] > m:
            continue #прерываем
        else:
            b += [[a[y]]]
print(len(b))

