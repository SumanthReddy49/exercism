x = int(input())
y = int(input())
z = int(input())
n = int(input())
ar = []
a=0
for i in range(x+1):
    for j in range (y+1):
         for k in range (z+1):
                if ((i+j+k)!=n):
                    ar.append([])
                    ar [a]=[i,j,k]
                    a+=1
print(ar)   
