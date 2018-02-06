snt=input()
snt=snt.lower()
x=[]
for i in snt:
	if i.isalpha():
		x.append(i)
x=set(x)
if len(x)==26:
	print("Pangram")
else:
	raise ValueError("Not a pangram")		

