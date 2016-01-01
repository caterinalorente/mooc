'''
http://metaleks.net/programming/the-evolution-of-a-python-programmer
'''

def calculate_factorial(x, factorial):
    for i in range(1, x+1): factorial *= i
    return factorial
print calculate_factorial(6, 1)

# Lazy
f = lambda x: x and x * f(x - 1) or 1
print f(6)

# Expert
fact = lambda x: reduce(int.__mul__, xrange(2, x + 1), 1) 
print fact(6)

# reduce(function, sequence, starting value)