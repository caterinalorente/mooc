def for_loop(L, v):
    """ (list, object) -> int
    
    Return the index of the first occurrence of v in L,
    or return -1 if v is not in L
    
    >>> linearSearch([2, 3, 5, 3], 2)
    0
    >>> linearSearch([2, 3, 5, 3], 5)
    2
    >>> linearSearch([2, 3, 5, 3], 8)
    -1
    """
    
    for i in range(0, len(L)):
        if v == L[i]:
            return i
    return -1  

def while_loop(L, v):
    """ (list, object) -> int
    
    Return the index of the first occurrence of v in L,
    or return -1 if v is not in L
    
    >>> linearSearch([2, 3, 5, 3], 2)
    0
    >>> linearSearch([2, 3, 5, 3], 5)
    2
    >>> linearSearch([2, 3, 5, 3], 8)
    -1
    """ 

    i = 0
    while i < len(L):
        if v == L[i]:
            return i 
        i += 1
    return -1