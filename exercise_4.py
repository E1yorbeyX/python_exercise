def remove_ton(word='example', n=0):
    """Write a program to remove characters from a string starting from zero up to n and return a new string."""
    
    for i in list(range(len(word))):
        if n < i :
            print(word[i], end='')

remove_ton('olmaliqtuman', 4)



# the version of shown
def remove_tox(text, n):
    """Write a program to remove characters from a string starting from zero up to n and return a new string."""
    
    x = text[n:]
    print('\n',x)
    
remove_tox('olmazror', 2)