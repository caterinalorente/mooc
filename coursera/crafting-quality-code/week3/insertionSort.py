def insertion_sort_v1(L):
    """ (list) -> NoneType
    
    Return a list whose values have been ordered from smallest to largest
    
    >>> insertion_sort_v1([34,17,23,35,45,9,1])
    [1, 9, 17, 23, 34, 35, 45]
    >>> insertion_sort_v1([4,3,2,1])
    [1, 2, 3, 4]
    >>> insertion_sort_v1([5,9,2,7,1])
    [1, 2, 5, 7, 9]
    >>> insertion_sort_v1([3,2,1])
    [1, 2, 3]
    >>> insertion_sort_v1([4,3,2,1])
    [1, 2, 3, 4]
    >>> insertion_sort_v1([7,3,5,2])
    [2, 3, 5, 7]
    >>> insertion_sort_v1([3,6,7,8,3])
    [3, 3, 6, 7, 8]
    """
    
    for i in range(1, len(L)):
        for j in range(i, 0, -1):
            if L[j] < L[j-1]:
                L[j], L[j-1] = L[j-1], L[j]
                
    return L

def insert(L,i):
    """ (list, int) -> NoneType
    
    Precondition: L[:i] is sorted from smallest to largest.
    
    Move L[i] to where it belongs in L[:i + 1]
    
    >>> L = [7,3,5,2]
    >>> insert(L,1)
    >>> L
    [2, 3, 5, 7]
    """
    
    # The value to be inserted into the sorted path of the list.
    value = L[i]
    
    # Find the index, j, where the value belongs.
    # Make room for the value by shifting.
    j = i
    k = 0
    while (j != 0) and L[j - 1] > value:
        # Shift L[j-1] one position to the right of L[j]
        L[j] = L[j-1]
        j -= 1 
        k += 1       
    # Put the value where it belongs.
    L[j] = value
    
    return L
    
def insertion_sort_v2(L):
    """ (list) -> NoneType
    
    Return a list whose values have been ordered from smallest to largest
    
    >>> insertion_sort_v2([34,17,23,35,45,9,1])
    [1, 9, 17, 23, 34, 35, 45]
    >>> insertion_sort_v2([4,3,2,1])
    [1, 2, 3, 4]
    >>> insertion_sort_v2([5,9,2,7,1])
    [1, 2, 5, 7, 9]
    >>> insertion_sort_v2([3,2,1])
    [1, 2, 3]
    >>> insertion_sort_v2([4,3,2,1])
    [1, 2, 3, 4]
    >>> insertion_sort_v2([7,3,5,2])
    [2, 3, 5, 7]
    >>> insertion_sort_v2([3,6,7,8,3])
    [3, 3, 6, 7, 8]
    """
   
    for i in range(len(L)):
        insert(L,i)
        
    return L

if __name__ == "__main__":
    import doctest
    doctest.testmod()