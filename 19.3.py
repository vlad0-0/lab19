m = int(input())
while m % 2 != 0:
    m = int(input())
n = int(input())
while n % 2 != 0:
    n = int(input())
a = []
b = []
for i in range(m):
    for j in range(n):
        b.append(input())
    a.append(b)
    b = []
m = int(m/2)
n = int(n/2)
for i in range(m):
    for j in range(n):
        a[i][j], a[i+m][j+n] = a[i+m][j+n], a[i][j]
print(a)
