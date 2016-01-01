def binary_search_v1(L, target):
    """ (list, object) -> int
    
    Precondition: L is sorted from smallest to largest,
    and all the items in L can be compared to V.
    
    Return the index of the first occurrence of target in L,
    or return -1 if target is not in L
    
    >>> binary_search_v1([2, 3, 5, 7], 2)
    0
    >>> binary_search_v1([2, 3, 5, 5], 5)
    2
    >>> binary_search_v1([2, 3, 5, 7], 8)
    -1
    """    
    
    low = 0
    high = len(L)
    
    while (low + 1 < high):
        middle = (low + high)/2
        if (L[middle] < target):
            low = middle
        elif (L[middle] == target):
            return middle            
        else:
            high = middle
            
    if (L[low] == target):
        return low
    else:
        return -1
    
def binar_search_v2(L, target):
    """ (list, object) -> int
    
    Precondition: bL is sorted from smallest to largest,
    and all the items in L can be compared to V.
    
    Return the index of the first occurrence of target in L,
    or return -1 if target is not in L
    
    >>> binar_search_v2([2, 3, 5, 7], 2)
    0
    >>> binar_search_v2([2, 3, 5, 5], 5)
    2
    >>> binar_search_v2([2, 3, 5, 7], 8)
    -1
    """    
    
    low = 0
    high = len(L) - 1

    while (low < high):
        middle = (low + high)/2
        if (L[middle] < target):
            low = middle + 1
        else:
            high = middle - 1
            
    if (low == len(L)) or (L[low] != target):
        return -1
    else:
        return low