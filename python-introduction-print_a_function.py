if __name__ == '__main__':
    n = int(input())
    res = ''.join([str(el) for el in range(n+1)])[1:]
    print(res)    