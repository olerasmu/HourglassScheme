'''
Created on 12. mars 2014

@author: olerasmu
'''
import os
import binascii
from _elementtree import Element
import uu
from base64 import encode

class Hourglass(object):
    
    
    def __init__(self, filepath=None, size=0):
        self.filepath = filepath
        self.f = open(filepath, 'rb')
        print filepath
        
    def getSize(self): 
        self.f.seek(0, os.SEEK_END)
        size = self.f.tell()
        self.size = size
        self.f.seek(0, os.SEEK_SET)
        print "The file size in bytes is: ", size
        return size
    
    def wirteByteByByteToNewFile(self):
        newfile2 = open('C:\\Users\\olerasmu\\Documents\\newfile.jpg', 'w+b')
        
        fileTab = []
        bitTab = []
        
        with open(self.filepath, 'rb') as newfile1:
            byte = newfile1.read(1)
            while byte:
                fileTab.append(byte)
                byte = newfile1.read(1)
                

        
            
        
        #write byte for byte to new file
        for byte in fileTab:
           # byte += "\n"
            print byte
            newfile2.write(byte)
        
        #=======================================================================
        # for line in self.f:
        #     fileTab.append(line)
        #     count += 1
        #      
        # for element in fileTab:
        #     newf.write(element)
        #     newf.seek(0,0)
        #=======================================================================
          
            #print "This is element: ", element

 

    
hg = Hourglass(filepath="C:\\Users\\olerasmu\\Downloads\\koala.jpg")    

size = hg.getSize()
hg.wirteByteByByteToNewFile()