from PyQt4.QtCore import * 
from PyQt4.QtXml import * 
from Component import Component
import sys

componentList = []

class myXmlContentHandler(QXmlDefaultHandler):    

    def startElement(self,nameSpaceURI,localName,qName,atts):
      if (atts.length()>0):
        # print "Read Start Tag: "+ localName+ "\n"
        # print type(localName)
        # print "Tag Attributes: "        
        localList = []
        for num in range(0, atts.length()):
          if num==0:
            localList.append(str(atts.value(num))) 
          elif num==1:
            posList = []
            for val in tuple(unicode(atts.value(num))):
              if val.isnumeric():
                posList.append(int(val))
            localList.append(tuple(posList)) 
        componentList.append(localList)
        # print componentList  
        # print "#####################################\n"  
        return True
      else:
        return True

def parseXML(name):
    xmlParser 		= QXmlSimpleReader()
    xmlContentHandler	= myXmlContentHandler()
    xmlFile		= QFile(name)
    xmlInputSource	= QXmlInputSource(xmlFile)    
    xmlParser.setContentHandler(xmlContentHandler)  
      
    if(xmlParser.parse(xmlInputSource)):
      print "Parsed Successfully :-)"
    else:  
      print "Parsing Failed :-/"

def main():    
  parseXML("floor1.xml")
  print componentList

if __name__ == '__main__':
    main()