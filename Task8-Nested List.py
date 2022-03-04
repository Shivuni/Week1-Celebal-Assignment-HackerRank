if __name__ == '__main__':
    a={}
    b=list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in a:
            a[score].append(name)
        else:
            a[score]=[name]
        if score not in b:
            b.append(score)
    m=min(b)
    b.remove(m)
    m=min(b)
    a[m].sort()
    for i in a[m]:
        print(i)