'''
Have the function LetterChanges(sentence) take the sentence parameter being passed and modify it using the following algorithm. 
Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). 
Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. 
'''

def LetterChanges(sentence): 
    alphabet = "abcdefghijklmnopqrstuvwxyza"
    letters_changed = [alphabet[alphabet.index(letter) + 1] if letter in alphabet else letter for letter in sentence]
    letters_changed_and_vowels_to_uppercase = [[letter.lower(),letter.upper()][letter in 'aeiou'] for letter in letters_changed]
    
    print(" ".join(letters_changed_and_vowels_to_uppercase))
    
LetterChanges("hello world")
LetterChanges("sentence")
LetterChanges("replace!*")
LetterChanges("123456789ae")
LetterChanges("this long cake@&")
LetterChanges("a b c dee")
LetterChanges("a confusing /:sentence:/[ this is not!!!!!!!~")