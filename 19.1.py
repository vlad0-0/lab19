m = int(input())
n = int(input())
a = []
b = []
for i in range(m):
    for j in range(n):
        b.append(float(input()))
    a.append(b)
    b = []
for i in range(m):
    mx = a[i][0]
    mn = a[i][0]
    mxp = 0
    mnp = 0
    for j in range(1, n):
        if mx < a[i][j]:
            mx = a[i][j]
            mxp = j
        elif mn > a[i][j]:
            mn = a[i][j]
            mnp = j
    if mnp != mxp:
        a[i][mnp], a[i][mxp] = a[i][mxp], a[i][mnp]
print(a)
