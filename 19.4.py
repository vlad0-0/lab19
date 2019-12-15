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
    mxp = i
    mnp = i
    for j in range(i, m-i):
        if mx < a[j][0]:
            mx = a[j][0]
            mxp = j
        elif mn > a[j][0]:
            mn = a[j][0]
            mnp = j
    a[i], a[mnp] = a[mnp], a[i]
    a[m-i-1], a[mxp] = a[mxp], a[m-i-1]
print(a)
