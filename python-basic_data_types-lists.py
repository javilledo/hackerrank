if __name__ == '__main__':
    N = int(input())
    res = []
    for iter in range(N):
        instruction = input().split(' ')
        if(instruction[0]== 'append'):
            res.append(int(instruction[1]))
        if(instruction[0]== 'insert'):
            res.insert(int(instruction[1]), int(instruction[2]))
        if(instruction[0]== 'print'):
            print(res)
        if(instruction[0]== 'remove'):
            res.remove(int(instruction[1]))
        if(instruction[0]== 'sort'):
            res.sort()
        if(instruction[0]== 'pop'):
            res.pop()
        if(instruction[0]== 'reverse'):
            res.reverse()