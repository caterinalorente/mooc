'''
 -- Riddle 21 --
Yes! This is really level 21 in here. 
And yes, After you solve it, you'll be in level 22!

Now for the level:
* We used to play this game when we were kids
* When I had no idea what to do, I looked backwards.
'''

import zlib, bz2

def unwrap(data):
    result = ''
    while True:
        if data.startswith('x\x9c'): 
            data = zlib.decompress(data)
            result += ' '
        elif data.startswith('BZ'): 
            data = bz2.BZ2Decompressor().decompress(data)
            data = bz2.decompress(data)
            result += '#'
        elif data.endswith('\x9cx'): 
            data = data[::-1]
            data =  zlib.decompress(data[::-1])
            result += '\n'
        else: 
            return data
            return result

data = open('../Files/21package.pack').read()
print unwrap(data)



