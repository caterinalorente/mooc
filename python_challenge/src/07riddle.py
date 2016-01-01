'''
 -- Riddle 7 --
 http://www.pythonchallenge.com/pc/def/oxygen.html
 Smarty
 --------------
'''

#from PIL import Image
import Image

pixel = Image.open("../Files/07oxygen.png").load()
message = ""
for i in range(0, 607, 7):
    message += chr(pixel[i,43][0])
print message

newMessage = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print "".join(map(chr, newMessage))

# Ultra fast way
#import PIL.Image
#print PIL.Image.open('Files/07oxygen.png').tostring()[108188:110620:28]
