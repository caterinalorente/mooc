def is_anagram_v1(s1, s2):
    """ (str, str) -> bool

    Return True if and only if s1 is an anagram of s2.

    >>> is_anagram("silent", "listen")
    True
    >>> is_anagram("bear", "breach")
    False
    """

    l1 = list(s1)
    l2 = list(s2)
    
    return (sorted(l1) == sorted(l2))

def is_anagram_v2(s1, s2):
    """ (str, str) -> bool

    Return True if and only if s1 is an anagram of s2.

    >>> is_anagram("silent", "listen")
    True
    >>> is_anagram("bear", "breach")
    False
    """

    l1 = list(s1)
    l2 = list(s2)
    
    for char in l1:
        if char in l2:
            l2.remove(char)
    
    return l2 == []  

def is_anagram_v3(s1, s2):
    """ (str, str) -> bool

    Return True if and only if s1 is an anagram of s2.

    >>> is_anagram("silent", "listen")
    True
    >>> is_anagram("bear", "breach")
    False
    """

    l1 = list(s1)
    l2 = list(s2)
    d1 = {}
    d2 = {}
    
    for char in l1:
        d1[char] = l1.count(char)
    for char in l2:
        d2[char] = l2.count(char)

    return d1 == d2    