'''
Created on 12. mars 2014

@author: olerasmu
'''
import os
import binascii
from _elementtree import Element
import uu
from base64 import encode
import math

class Hourglass(object):
    
    
    def __init__(self, filepath=None, size=0):
        self.filepath = filepath
        self.f = open(filepath, 'rb')
        print filepath
    
    def computeS(self, a, n, l, t, e):
        
        s1 = math.pow(a, 1/t)*n*l*(1-e)
        s2 = n*l*(1-e)+(math.log(math.pow(a, 1/t), 2))
        return [s1, s2]
        
    def getSize(self): 
        self.f.seek(0, os.SEEK_END)
        size = self.f.tell()
        self.size = size
        self.f.seek(0, os.SEEK_SET)
        print "The file size in bytes is: ", size
        return size
    
    def wirteByteByByteToNewFile(self):
        newfile2 = open('C:\\Users\\olerasmu\\Documents\\newfile.txt', 'w+b')
        
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

 

    
hg = Hourglass(filepath="C:\\Users\\olerasmu\\Documents\\test.txt")

print hg.computeS(0.99, 512, 64, 111, 0.05)

#size = hg.getSize()
#hg.wirteByteByByteToNewFile()

