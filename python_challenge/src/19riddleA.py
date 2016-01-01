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
'''

import base64, wave, winsound

# First we have to decode the downloaded text which is a .wav file
f1 = open('../Files/19indianwav.txt', 'rb')
f2 = open('../Files/19indian.wav', 'wb')
base64.decode(f1, f2)
f1.close()
f2.close()

# Play it with python winsound module and we hear static plus sorry
def play_sound(source):
    print 'Playing sound'
    winsound.PlaySound(source, winsound.SND_ALIAS)

play_sound('../Files/19indian.wav')

# What happens if you play the audio reversed?
def reverse_sound(source):
    reverse = wave.open('../Files/19indianReversed.wav', 'wb')
    reverse.setparams(source.getparams())
    for i in range(source.getnframes()):
        reverse.writeframes(source.readframes(1)[::-1])    
    reverse.close()

reverse_sound(wave.open('../Files/19indian.wav', 'rb'))
play_sound('../Files/19indianReversed.wav')


'''
There's a much faster, but more memory-intensive, way to do it, without loops: 
import array
frames = array.array("H", source.readframes(source.getnframes()))
frames.byteswap()
reversed.writeframes(frames.tostring())
'''