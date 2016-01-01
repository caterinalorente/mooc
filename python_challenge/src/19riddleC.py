''' 
 -- Riddle 19 --
 http://www.pythonchallenge.com/pc/hex/bin.html
 please!
 
 <!--
From: leopold.moz@pythonchallenge.com
Subject: what do you mean by "open the attachment?"
Mime-version: 1.0
Content-type: Multipart/mixed; boundary="===============1295515792=="

It is so much easier for you, youngsters.
Maybe my computer is out of order.
I have a real work to do and I must know what's inside!

--===============1295515792==
Content-type: audio/x-wav; name="indian.wav"
Content-transfer-encoding: base64
 --------------

 Remember "dealing evil"? Back on level 12, 
 you "dealt" the bytes of evil2.gfx into 5 graphics files. 
 You can also deal the bytes of indian.wav into two .wav files:
'''

import wave
f = wave.open('../Files/19indian.wav', "rb")
guts = f.readframes(f.getnframes())
f.close()
for i in 0, 1:
    out = wave.open("../Files/indian%d.wav" % i, "wb")
    out.setparams((1, 2, 11025//2, 55788//2, 'NONE', 'not compressed'))
    out.writeframes(guts[i::2])
    out.close()

'''
After this, i0.wav is a lower-quality rendering of the "the idiot song", 
while i1.wav sounds a lot like the original. 
''' 