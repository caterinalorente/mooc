def FirstFactorial(num): 
    if num <= 1:
        return 1
    return num * FirstFactorial(num-1)

FirstFactorial(8)