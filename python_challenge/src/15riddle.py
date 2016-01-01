''' 
 -- Riddle 15 --
 http://www.pythonchallenge.com/pc/return/uzi.html
 <!-- he ain't the youngest, he is the second -->
<!-- todo: buy flowers for tomorrow -->
 whom? - 1756, Mozart
 --------------
'''

#import calendar
#
#calendario = calendar.TextCalendar(6)
#for i in range(1006, 1997, 10):
#        print calendario.formatmonth(i, 1)

'''
The years obtained are 1046, 1176, 1226, 1356, 1446, 1576, 1626, 1756, 1846, 1976
Searching on Google for information about what happened the 26th of January I found 
that Mozart was born on 26-Jan-1756
'''

#import calendar
#for i in range(1006, 1997, 10):
#    if calendar.isleap(i) and calendar.weekday(i, 1, 1) == 3: # 0 is Monday, 6 is Sunday 
#        print 'The year is', i
        
'''
The years obtained are 1176, 1356, 1756 and 1976
The source tells us we should take the second most recent date of our list
26-Jan-1756 Mozart was born
'''










