'''
 -- Riddle 25 --
http://www.pythonchallenge.com/pc/hex/lake.html
<!-- can you see the waves? -->
Imagine how do they sound

'''

import urllib, wave, StringIO, Image

def get_challenge(s): 
    return urllib.urlopen('http://butter:fly@www.pythonchallenge.com/pc/' + s).read()

def jig(w): 
    return Image.fromstring('RGB', (60,60), w.readframes(w.getnframes()))

wavs = [wave.open(StringIO.StringIO(get_challenge('hex/lake%d.wav' % i))) for i in range(1,26)]
jigsaw = Image.new('RGB', (300,300), 0)

for i in range(len(wavs)): 
    jigsaw.paste(jig(wavs[i]), (60 * (i % 5), 60 * (i // 5)))

jigsaw.save('../Files/25jigsaw.png')

"""
for i in range(1, 26):
    req = urllib.urlretrieve('http://butter:fly@www.pythonchallenge.com/pc/hex/lake' + str(i) + '.wav', 'C:\\Users\\admin\\workspace\\pythonChallenge\\pythonChallenge\\files\\25\\lake' + str(i) + '.wav')
"""   
