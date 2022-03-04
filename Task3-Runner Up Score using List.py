if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    b=arr[(arr.index (max(arr)))-1]
    print(b)