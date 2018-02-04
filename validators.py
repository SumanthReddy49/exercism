s = input()
A=False
B=False
C=False
D=False
E=False
for i in s:
    if i.isalnum():
        A=True
    if i.isalpha():
        B=True
    if i.isdigit():
        C=True
    if i.islower():
        D=True
    if i.isupper():
        E=True
print (A)
print (B)
print (C)
print (D)
print (E)
