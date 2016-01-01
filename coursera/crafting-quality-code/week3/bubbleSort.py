def bubble_sort(L):
    """ (list) -> NoneType
    
    Sort the items from smallest to largest.
    
    >>> bubble_sort([5,9,2,7,1])
    [1, 2, 5, 7, 9]
    >>> bubble_sort([3,2,1])
    [1, 2, 3]
    >>> bubble_sort([4,3,2,1])
    [1, 2, 3, 4]
    >>> bubble_sort([7,3,5,2])
    [2, 3, 5, 7]
    >>> bubble_sort([3,6,7,8,3])
    [3, 3, 6, 7, 8]
    """
    
    end = len(L) - 1
    while end != 0:
        for i in range(end):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
        end -= 1
    return L

if __name__ == "__main__":
    import doctest
    doctest.testmod()