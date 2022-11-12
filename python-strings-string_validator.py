if __name__ == '__main__':
    s = input()

    #isalnum
    boolean_list = [c.isalnum() for c in s]
    print(any(boolean_list))

    #isalpha
    boolean_list = [c.isalpha() for c in s]
    print(any(boolean_list))

    #isdigit
    boolean_list = [c.isdigit() for c in s]
    print(any(boolean_list))

    #islower
    boolean_list = [c.islower() for c in s]
    print(any(boolean_list))
    
    #isupper
    boolean_list = [c.isupper() for c in s]
    print(any(boolean_list))