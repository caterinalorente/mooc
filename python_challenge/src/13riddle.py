''' 
 -- Riddle 13 --
 http://www.pythonchallenge.com/pc/return/disproportional.html
 Phone that evil
 --------------
'''

import xmlrpclib 

server = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print server.system.listMethods()
print server.phone('Bert')