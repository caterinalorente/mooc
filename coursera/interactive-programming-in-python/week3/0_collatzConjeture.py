def collatz(n):
    if n % 2 == 0:  n = n/2
    else:           n = (n*3) + 1
    
    return n

n = 217
lista = []
while n != 1:
    n = collatz(n)
    lista.append(n)

print lista
print max(lista)