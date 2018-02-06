a1=input()
a2=input()
import sys
if len(a1)!=len(a2):
	raise ValueError("Length is not equal")
	sys.exit()
ar1=[]
count=0
ar2=[]
for i in a1:
	ar1.append(i)
for i in a2:
	ar2.append(i)
for i in range(len(a1)):
	if ar1[i]!=ar2[i]:
		count+=1
print(count)

	
