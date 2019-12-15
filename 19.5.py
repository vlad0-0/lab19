m = int(input())
a = []
b = []
for i in range(m):
    for j in range(m):
        b.append(float(input()))
    a.append(b)
    b = []
s = 0
i = 0
j = m-1
while i < m and j > -1:
    y = j
    x = 0
    while x < i+1 and y < m+1:
        s += a[y][x]
        x += 1
        y += 1
    print(s)
    s = 0
    i += 1
    j -= 1
i = 1
j = m-1
while i < m and j > -1:
    y = 0
    x = i
    while x < m and y < j:
        s += a[y][x]
        x += 1
        y += 1
    print(s)
    s = 0
    i += 1
    j -= 1
