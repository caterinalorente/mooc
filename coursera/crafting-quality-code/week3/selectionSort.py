def selection_sort_v1(L):
    """ (list) -> NoneType
    
    Return a list whose values have been ordered from smallest to largest
    
    >>> selection_sort_v1([34,17,23,35,45,9,1])
    [1, 9, 17, 23, 34, 35, 45]
    >>> selection_sort_v1([4,3,2,1])
    [1, 2, 3, 4]
    >>> selection_sort_v1([5,9,2,7,1])
    [1, 2, 5, 7, 9]
    >>> selection_sort_v1([3,2,1])
    [1, 2, 3]
    >>> selection_sort_v1([4,3,2,1])
    [1, 2, 3, 4]
    >>> selection_sort_v1([7,3,5,2])
    [2, 3, 5, 7]
    >>> selection_sort_v1([3,6,7,8,3])
    [3, 3, 6, 7, 8]
    """
    
    start = 0
    end = len(L) - 1
        
    while start != end:
        auxL = L[start:]
        smallest = min(auxL)
        index_of_smallest = auxL.index(smallest)          
        
        if index_of_smallest != 0:
            auxL[0], auxL[index_of_smallest] = smallest, auxL[0] 
            L[start:] = auxL
        start += 1

    return L

def selection_sort_v2(L):
    
    for i in range(len(L)):
        # Find the item of the smallest item in L[i:] and swap
        # that item with the item at index i
        
        index_of_smallest = get_index_of_smallest(L, i)
        L[index_of_smallest], L[i] = L[i], L[index_of_smallest] 
        
    return L  

def get_index_of_smallest(L, i):
    """ (list, int) ->
    
    Return the index of the smallest item in L[i:]
    
    >>> get_index_of_smallest([2, 7, 3, 5,], 1)
    2
    """
    
    # The index of the smallest item so far
    index_of_smallest = i

    for j in range(i+1, len(L)):
        if L[j] < L[index_of_smallest]:
            index_of_smallest = j
            
    return index_of_smallest

if __name__ == "__main__":
    import doctest
    doctest.testmod()