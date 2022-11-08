def swap_case(s):
    return ''.join(list(map(swap_character, s)))

def swap_character(c):
    if (c.islower()): return c.upper()
    if (c.isupper()): return c.lower()
    return c
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)