def reverse_word(word):
    rev = ''
    for i in range(len(word), 0, -1):
        rev = rev + word[i-1]
        
    return rev

def is_word_palindrome_v1(word):
    '''
    (str) -> bool

    This function tells if a word is or is not a palindrome
    1- Reverse the string.
    2- Compare it with the original one.
        
    >>> is_word_palindrome_v1('noon')
    True
    >>> is_word_palindrome_v1('racecar')
    True
    >>> is_word_palindrome_v1('dented')
    False
    '''
    
    return (reverse_word(word) == word)

def is_word_palindrome_v2_1(word):
    '''
    (str) -> bool

    This function tells if a word is or is not a palindrome
    1- Split the string in two halves.
    2- Reverse the second half.
    3- Compare the first half to the reversed second half.
        
    >>> isWordPalindrome2('noon')
    True
    >>> isWordPalindrome2('racecar')
    True
    >>> isWordPalindrome2('dented')
    False
    '''
    
    length = len(word)
    half = length / 2
    firstHalf = [word[i] for i in range(0,half)]
    
    if half%2 == 0:    
        secondHalf = [word[i] for i in range(half,length)]
    else:
        secondHalf = [word[i] for i in range(half+1,len(word))]
        
    return (''.join(firstHalf) == reverse_word(''.join(secondHalf)))

def is_word_palindrome_v2_2(word):
    '''
    (str) -> bool

    This function tells if a word is or is not a palindrome
    1- Split the string in two halves.
    2- Reverse the second half.
    3- Compare the first half to the reversed second half.
        
    >>> isWordPalindrome2('noon')
    True
    >>> isWordPalindrome2('racecar')
    True
    >>> isWordPalindrome2('dented')
    False
    '''
    
    length = len(word)
    half = length / 2
    
    firstHalf = word[:half]
    # Omit the middle character of an odd-length string
    secondHalf = word[length-half:]
    
    # Comparing the first half of the word with the reverse of the second half 
    return (firstHalf == reverse_word(secondHalf))

def is_word_palindrome_v3_1(word):
    '''
    (str) -> bool

    This function tells if a word is or is not a palindrome
    1- Compare the first first character with the last.
    2- Then compare the lest the second to the second last.
    3- We stop when we reach the middle of the string.
        
    >>> isWordPalindrome3('noon')
    True
    >>> isWordPalindrome3('racecar') 
    True
    >>> isWordPalindrome3('dented')
    False
    '''   
    
    length = len(word)
    for i in range(length):
        if word[i] != word[length-1]: 
            return False
        length -= 1
    return True
        
def is_word_palindrome_v3_2(word):
    '''
    (str) -> bool

    This function tells if a word is or is not a palindrome
    1- Compare the first first character with the last.
    2- Then compare the lest the second to the second last.
    3- We stop when we reach the middle of the string.
        
    >>> isWordPalindrome3('noon')
    True
    >>> isWordPalindrome3('racecar') 
    True
    >>> isWordPalindrome3('dented')
    False
    
        _______j_______        _______ij_______
    odd |______________|   even|_______________|    
    
    '''   
    
    i = 0
    j = len(word) - 1
    
    while i < j and word[i] == word[j]:
        i += 1
        j -= 1
        
    # When the middle of string is reached we have found a palindrome
    # Otherwise the middle of the string has not been reached and we have not found a palindrome
    return (j <= i)