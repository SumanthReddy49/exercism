n = int(input())
array=[]
for i in range (0,n):
    a_array=input().split()
    b=a_array[0]
    if(b=="print"):
        print(array)
    elif(b=="insert"):
        i=int(a_array[1])
        e=int(a_array[2])
        array.insert(i,e)
    elif(b=="remove"):
        e=int(a_array[1])
        array.remove(e)
    elif(b=="append"):
        e=int(a_array[1])
        array.append(e)    
    elif(b=="sort"):
        array.sort()
    elif(b=="pop"):
        array.pop()
    elif(b=="reverse"):
        array.reverse()
