''' 
 -- Riddle 18 --
 http://www.pythonchallenge.com/pc/return/balloons.html
 Can you tell the difference?
 --------------
'''

import gzip, difflib
from binascii import unhexlify

f = gzip.open('../Files/18deltas.gz', 'rb').read()
data1 = []
data2 = []

# Separate the file into the two different blocks
lines = f.splitlines()
for i in range(0, len(lines)):
    sublines = lines[i].split('   ')
    data1.append(sublines[0])
    data2.append(sublines[1])

# The two blocks have got differences, find them
d = difflib.Differ()
diff = list(d.compare(data1, data2))

# Next we need to split these lines into three piles; 
# 1- Identical in the two columns (initial space)
# 2- In the first but not the second (initial minus) 
# 3- In the second but not the first (initial plus).
f1 = open('../Files/splitA.png', 'wb')
f2 = open('../Files/splitB.png', 'wb')
f3 = open('../Files/splitC.png', 'wb')

for line in diff:
# The hex data cannot have spaces it needs to be 89504e470d0a1a
    if line[0] == '+':
        f1.write(unhexlify(line.strip('+').replace(' ','')))
    elif line[0] == '-':
        f2.write(unhexlify(line.strip('-').replace(' ','')))
    else:
        f3.write(unhexlify(line.strip().replace(' ','')))
f1.close()
f2.close()
f3.close()

'''
 The samet solution only deals with the last part of the riddle
 The three sets then mereley have to be converted to data 
 (interpret the digits as hex values) and written out to image files
 
def splitdiff(a, b):
    seq = difflib.SequenceMatcher(None, a, b)
    result1 = result2 = result3 = ""
    for tag, i1, i2, j1, j2 in seq.get_opcodes():
        if tag == 'equal':
            result1 += "".join(a[i1:i2])
        if tag == 'delete':
            result2 += "".join(a[i1:i2])
        if tag == 'insert':
            result3 += "".join(b[j1:j2])
        if tag == 'replace':
            result2 += "".join(a[i1:i2])
            result3 += "".join(b[j1:j2])
    return result1, result2, result3
'''