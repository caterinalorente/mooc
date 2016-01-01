''' 
 -- Riddle 6 --
 http://www.pythonchallenge.com/pc/def/channel.html
 Zip
 --------------
'''

import zipfile, re

nameTXT = '90052.txt'
comment = ""
zfile = zipfile.ZipFile('../Files/06channel.zip', 'r')
information = zfile.infolist()

for i in range(1, len(information)):
    try:
        comment += zfile.getinfo(nameTXT).comment
        data = zfile.read(nameTXT)
        nameTXT = ''.join(re.findall('([0-9])', data))  + '.txt'
    except:
        print "Error"

print comment

# SOLUCION VICENTE ##

#def FindFileIdx(nameTXT, listToSearch):
#    for idx in range(len(listToSearch)):
#        if listToSearch[idx].filename == nameTXT:
#            return idx
#
#zfile = zipfile.ZipFile('Files/06channel.zip', 'r')
#nameTXT = '90052.txt'
#comment = ""
#info = zfile.infolist()
#idx = FindFileIdx(nameTXT, info)
#print "IDX:",idx
#listToSearch = info
#
#for item in range(len(info)):
#    try:
#        comment += listToSearch[idx].comment
#        data = zfile.read(nameTXT)
#        nameTXT = ''.join(re.findall('([0-9])', data))  + '.txt'
#        listToSearch.pop(idx)
#        idx = FindFileIdx(nameTXT, listToSearch)
#        print idx
#    except:
#        pass