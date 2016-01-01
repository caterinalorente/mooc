'''
 -- Riddle 1 --
 http://www.pythonchallenge.com/pc/def/map.html
 K = M, O = Q, E = G
 --------------
'''

from string import maketrans, ascii_letters
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. map"
print text.translate(maketrans(ascii_letters[0:26], ascii_letters[2:26] + ascii_letters[0:2]))