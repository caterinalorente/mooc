''' 
 -- Riddle 10 --
 http://www.pythonchallenge.com/pc/return/bull.html
 len(a[30]) = ?
 --------------
a = ['1', '11', '21', '1211', '111221']
'''

def count_digits(a):
    series = ''
    item = []
    counter = 0
    for i in range(0, len(a)):
        item.append(a[i])
        if item[i] == item[i-1]:
            counter += 1
        elif (item[i] != item[i-1]) or (i == len(a)):
            series += str(counter) + str(item[i-1])
            counter = 1
    series += str(counter) + str(item[i])
    return (series)

number = '1'
for i in range(1, 31):
    number = count_digits(number)
    print i, len(number)