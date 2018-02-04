sentence=input()
sentence=sentence.strip()
if len(sentence)==0:
	print("Fine. Be that Way!")
elif sentence.isupper():
	print("Whoa, Chill out!")
elif sentence.endswith("?"):
	print("Sure")
else:
	print("Whatever.")
