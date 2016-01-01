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

 In this solution we see how to use urllib, re and email modules to
 load and strip it down to just the message 
 (making sure the first characters are 'From') 
 So that we can load the attachment from it: 
'''

import urllib, re, email, wave, StringIO

url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html'
src = urllib.urlopen(url).read()
c = re.compile("<!--\n(.*)\n-->", re.DOTALL)
data = c.findall(src)[0]

message = email.message_from_string(data)
audio = message.get_payload(0).get_payload(decode=True) 

'''
 If we print audio we get RIFFWAVE which tells us it's a .wav file
 WAV specification says that: 
 1- Little endian wavs have "RIFF" in the header. 
 2- Big-endian ones have "RIFX"
 Ours has RIFF so we have to convert it big-endian
'''

wav = wave.open(StringIO.StringIO(audio))
wav2 = wave.open('../Files/19endian.wav', 'w')

nchannels, sampwidth, framerate, nframes, comptype, compname = wav.getparams()
frames = wav.readframes(nframes)
wave.big_endian = 1

wav2.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
wav2.writeframes(frames)
wav.close()
wav2.close()


'''
== SOLUTION B ==
If I send an email to leopold.moz@pythonchallenge.com with subject = sorry
I get something not related with this riddle but probably with a future one

Never mind that.
Have you found my broken zip?
md5: bbb8b499a0eef99b52c7f13f4e78c24b
Can you believe what one mistake can lead to?
'''
