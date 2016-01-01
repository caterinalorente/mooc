# Iterating over lists

def count_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 1:
            count += 1
    return count

def check_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            return True
    return False

def remove_odd(numbers):
    # This does not remove 7 because
    # you CANNOT modify a list while you are
    # ITERATING over it
    for num in numbers:
        if num % 2 == 1:
            numbers.remove(num)

def remove_odd2(numbers):
    # This does not work because everytime I pop
    # a number from numbers the list shrinks thus
    # the indeces I obtained from removed are not
    # valid for numbers
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(numbers.index(num))
            
    for idx in remove:
        numbers.pop(idx)
        
def remove_odd3(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(num)
            
    for num in remove:
        numbers.remove(num)
        
def remove_odd4(numbers):
    newnums = []
    for num in numbers:
        if num % 2 == 0:
            newnums.append(num)
    return newnums
   
def remove_last_odd(numbers):
    has_odd = False
    last_odd = 0
    for i in range(0, len(numbers)):
        if numbers[i] % 2 == 1:
            has_odd = True
            last_odd = i
            
    if has_odd:
        numbers.pop(last_odd)
        

def run():
    numbers = [1, 7, 2, 34, 8, 7, 2, 5, 14, 22, 93, 48, 76, 15, 7]
    print numbers
    remove_last_odd(numbers)
    print numbers
    
run()