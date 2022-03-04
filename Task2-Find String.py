def count_substring(string, sub_string):
    a=len(string)
    b=len(sub_string)
    c=0
    for i in range(a-b+1):
        if (string[i:(i+b)]==sub_string):
            c+=1
    return c