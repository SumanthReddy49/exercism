def count_substring(string, sub_string):
    a=len(string)
    l=len(sub_string)
    count=0
    for i in range(a-l+1):
        if(string[i:i+l] == sub_string ):      
            count+=1
    return count  
