a=input()
a=a.lower()
s=[]
for i in a:
	if i.isalpha():
		s.append(i)
l=len(s)
b=set(s)
length=len(b)
if l==length:
	print("isogram")
else:
	raise ValueError("Not an isogram")
