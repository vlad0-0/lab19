m = int(input())
n = int(input())
a = []
b = []
for i in range(m):
    for j in range(n):
        b.append(float(input()))
    a.append(b)
    b = []
mx = [a[i][0], 0, 0]
mn = [a[i][0], 0, 0]
for i in range(m):
    for j in range(n):
        if mx[0] < a[i][j]:
            mx = [a[i][j], i, j]
        elif mn[0] > a[i][j]:
            mn = [a[i][j], i, j]
a[mn[1]][mn[2]], a[mx[1]][mx[2]] = a[mx[1]][mx[2]], a[mn[1]][mn[2]]
print(a)
