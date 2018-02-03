n=input()
n=n.split()
p=list(set(n))
for i in range (len(p)):
	print(p[i]," ",n.count(p[i]), end=" ")
