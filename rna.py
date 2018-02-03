n=input()
l=len(n)
for i in n:
	if i!=("C"or"G"or"T"or"A"):
		print("Value error")
		break
	if i=="C":
		print("G", end="")	
	if i=="G":
		print("C", end="")
	if i=="T":
		print("A", end="")
	if i=="A":
		print("U", end="")
	
