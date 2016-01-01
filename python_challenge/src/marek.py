import re

#import easy to use xml parser called minidom:
from xml.dom.minidom import parseString
import xml.etree.ElementTree as ET
#all these imports are standard on most modern python implementations

file = open('C:/gas/Stroked_CodigosPostalesMadrid.svg','r') #<-- change path to local one!
data = file.read()
file.close()

#parse the xml you got from the file
dom = parseString(data)
#retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
xmlTag = dom.getElementsByTagName('path')

c = re.compile("d=\"(.*)\" id", re.DOTALL)
for tag in xmlTag:
    prettyXml = tag.toxml()
    tagContent = prettyXml.replace('<path','').replace('</>','')
    print tagContent
    print c.findall(tagContent)[0] # This prints the exact data, we can do other stuff
                                   # rather than printing but I leave it like this