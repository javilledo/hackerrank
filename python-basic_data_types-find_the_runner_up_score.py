if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    res = (list(set(arr)))
    res.sort(reverse = True)
    print(res[1])