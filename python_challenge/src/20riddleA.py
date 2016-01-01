''' 
 -- Riddle 20 --
 http://www.pythonchallenge.com/pc/hex/idiot2.html
 go away! but inspecting it carefully is allowed
'''

import httplib, base64, pprint, re, zipfile, StringIO

def get_range(page, start, end):
    conn = httplib.HTTPConnection("www.pythonchallenge.com")
    headers = {'Authorization': 'Basic ' + base64.b64encode('butter:fly'), 
#               'Range': '%s %d-%d/%d' % ( bytes, start, end, 2123456789 - 1)}
                'Range': 'bytes=%s-%s' % (start, end)}
    conn.request("GET", page, '', headers)
    return conn.getresponse()

def next_range(page, start, end, messages):
    res = get_range(page, start, end)
    messages.append(res.read())
    headers = res.getheaders()
    return int(re.search('(\d{1,})-(\d{1,})', headers[4][1]).group(2)) + 1
    
start = 30203
end = 2123456789 # We obtain this value from pp.pprint(headers)
arrayOfStarts = []
messages = []
# 1) Let's see how far does it go
#for i in range(6):
#    arrayOfStarts.append(start)
#    start = next_range('/pc/hex/unreal.jpg', start, end, messages)
#print arrayOfStarts    
#pprint.pprint(messages)

# 2) 2123456789 is quite close to pow(2,31)
#start = get_range('/pc/hex/unreal.jpg', 2123456789, pow(2,31))
#print start.read()[::-1]
# This tells us our password is invader in reverse -- redavni

# 3) The password to what? 
#pprint.pprint(start.getheaders())
#print get_range('/pc/hex/unreal.jpg', 2123456743, '').read() # and it is hiding at 1152983631.
data = get_range('/pc/hex/unreal.jpg', 1152983631, '').read() # data is a PK (zip file)
open('../Files/20away.zip', "wb").write(data)

z = zipfile.ZipFile(StringIO.StringIO(data))
print z.namelist()
# print z.read('readme.txt') # gives an error because a password is required for extraction, let's look for it