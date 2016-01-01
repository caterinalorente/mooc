''' 
 -- Riddle 17 --
 http://www.pythonchallenge.com/pc/return/romance.html
 eat?
 1) The compressed message says: is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.
    That is related with riddle 15th which was about Mozart's birth on the 26th January 1756 
 2) Then I use riddle 13th code to call Mozart's father (Leopold) and I get 555-VIOLIN
 3) I put violin.html instead of romance.html and get the new php url - http://www.pythonchallenge.com/pc/stuff/violin.php
 4) I create a cookie and send it to the php address and get back: oh well, don't you dare to forget the balloons :)
 --------------
'''

import urllib, urllib2, re, cookielib, bz2

cookies = []
nextNumber = '12345'
cookiejar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))

# Iterate until we find the hidden message
while True:
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=' + nextNumber
    content = urllib2.urlopen(url).read()
    r = opener.open(url)

    cookie = str(cookiejar._cookies.values()[0].values()[0].values()).split(',')[2]
    value = cookie.split('\'')[1]
    cookies.append(value)
    
    if 'next busynothing' in content:
        nextNumber = re.findall(r' (\d*)$', content)[0] #find for a set of digits starting from the end - next busynothing is XXXXX, 
    else:
        print 'Solution is', content
        break
        
hiddenMessage = "".join(cookies)
#hiddenMessage = 'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'

# The hidden message is compressed, decompress it
print bz2.BZ2Decompressor().decompress(urllib.unquote_plus(hiddenMessage))

# Now tell Leopold, Mozart's father, the message
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'info=sorry'))
f = opener.open("http://www.pythonchallenge.com/pc/stuff/violin.php")
print f.read()

'''
The samet solution

def linkedcookielist(seed='12345'):
    result = ""
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php' \
            '?busynothing='
    nextnothing = re.compile('the next busynothing is (\d+)')
    cookievalue = re.compile('info=([^;]+);').search
    while True:
        resp = urllib.urlopen(url + seed)
        next = resp.read()
        cookie = resp.info().getheader('Set-Cookie')
        if cookie and cookievalue(cookie):
            result += urllib.unquote_plus(
                cookievalue(cookie).group(1))
        try:
            seed = nextnothing.search(next).group(1)
        except:
            return result

print bz2.decompress(linkedcookielist())

# Mozart's father is Leopold, and his number according to the XML-RPC phonebook 
# is '555-VIOLIN'. violin.html tells you to go to ../stuff/violin.php. 
# There we find Leopold asking you what you want. 
# Now inform him that "the flowers are on their way."
# You can do so by sending him a cookie with the message: 

message = "the flowers are on their way"
url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
req = urllib2.Request(url,
    headers={'Cookie': 'info=' + urllib.quote_plus(message)})
print urllib2.urlopen(req).read()


# To talk to leopold you need to use cookies. 
# But I wasn't sure how to set the cookie with python, 
# so I used some javascript injection. Just type:

javascript:void(document.cookie="info=the+flowers+are+on+their+way")

# in your browser's address bar, press enter and reload the page. 
'''