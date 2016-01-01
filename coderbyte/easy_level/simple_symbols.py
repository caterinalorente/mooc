def SimpleSymbols(string):
    flag = False
    for letter in string:
        if letter.isalpha():
            if (string.index(letter) !=0 ) and (string[string.index(letter) - 1] == "+") and (string[string.index(letter) + 1] == "+"):
                flag = True
            else:
                return False
    return flag
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print(SimpleSymbols("+d+=3=+s+"))
print(SimpleSymbols("f++d+"))
print(SimpleSymbols("+d+"))
print(SimpleSymbols("+d===+a+"))
print(SimpleSymbols("b"))