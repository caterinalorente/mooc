'''
 -- Riddle 26 --
http://www.pythonchallenge.com/pc/hex/decent.html
<!-- you've got his e-mail -->
Hurry up, I'm missing the boat 

If I send an email to leopold.moz@pythonchallenge.com with subject = sorry
I get something the following

Never mind that.
Have you found my broken zip?
md5: bbb8b499a0eef99b52c7f13f4e78c24b
Can you believe what one mistake can lead to?

The broken zip is obtained on riddle 24
'''

import hashlib, md5, array

f1 = file('../Files/mybroken.zip', 'rb')
m = hashlib.md5()
m.update(f1.read())

print m.hexdigest() # bbf6616928e23ecfef4b717f281c53cc

# This is the md5 of the file which has nothing to do with the one provided by Leopold.
# Therefore the file is corrupted and I have to fix it.

def sub(data, good_md5):
    allchars = map(chr, range(256))
    for i, oldch in enumerate(data):
        for newch in allchars:
            data[i] = newch
            if md5.new(data).hexdigest() == good_md5:
                return True
        data[i] = oldch
    return False

data = array.array("c", open("/Volumes/SHARED/Development/workspace/pythonChallenge/pythonChallenge/Files/mybroken.zip", "rb").read())
sub(data, "bbb8b499a0eef99b52c7f13f4e78c24b")
f = open("/Volumes/SHARED/Development/workspace/pythonChallenge/pythonChallenge/Files/repaired.zip", "wb")
f.write(data)
f.close()
print "Zip fixed"

'''
The title says, be a man - apologize!
and there are clues you've got his e-mail 
and Hurry up, I'm missing the boat. 
I think this is a reference to level 24 and all I have to do is guess

Solution is speedboat but the zip must be repaired in some way I do not know.
'''