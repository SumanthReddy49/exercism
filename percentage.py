n = int(input())
a = []
for i in range (0,n):
    a.append(list(map(str, input().split())))
k = input()
m = 0
for i in range(0,n):
    if a[i][0]==k:
        m=(float(a[i][1])+float(a[i][2])+float(a[i][3]))/3
print("{0:.2f}".format(m))
