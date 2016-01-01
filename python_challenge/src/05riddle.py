'''
 -- Riddle 5 --
 http://www.pythonchallenge.com/pc/def/peak.html
 Pronounce it, peak hell sounds familiar?
 --------------
'''
import pickle

pickHell = pickle.load(open("../Files/05banner.p"))
for row in pickHell:
    for column in row:
        draw = column[0]
        times = column[1]
        for i in range(0, times):
            print draw,
    print ""
