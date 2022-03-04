def swap_case(s):
    a=""
    for i in s:
        if i.isupper():
            i= i.lower()
        else:
            i= i.upper()
        a+=''.join(i)
    return a 
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)