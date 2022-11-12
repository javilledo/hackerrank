if __name__ == '__main__':
    cases = int(input())
    for case in range(cases):
        s = input()
        s1 = ''
        s2 = ''
        cont = 1
        for c in s:
            if(cont % 2 != 0): 
                s1 += c
            else:
                s2 += c
            cont += 1
        print(s1 + ' ' + s2)