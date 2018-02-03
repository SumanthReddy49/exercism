n=int(input())
l=len(str(n))
b=n
sum=0
while n>0:
	r=n%10
	sum=sum+(r**l)
	n=n//10
if sum==b:
	print("It is an armstrong number")
else:
	print("It is not an armstrong number")
