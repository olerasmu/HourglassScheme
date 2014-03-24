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
        print (filepath)
    
    #Computes the butterfly cost by extra storage for cheating server    
    def computeButterflyS(self, filename, a, n, l, t, e):
        file_size_bits = n*l
        s1 = math.pow(a, 1/t)*n*l*(1-e)
        s2 = n*l*(1-e)+(math.log(math.pow(a, 1/t), 2))
        
        overhead_relationship_s1 = s1/file_size_bits
        overhead_relationship_s2 = s2/file_size_bits
        data_strings = "Inputs:", str(a), str(n), str(l), str(t), str(e), "File size in bits:", str(file_size_bits), "Results:", str(s1), str(s2), "Overhead relationship:", str(overhead_relationship_s1), str(overhead_relationship_s2), "\n"
        data_strings = ';'.join(data_strings)
        print (data_strings)
        with open(filename, 'a') as data_file:
            data_file.write(data_strings)
        return [s1, s2]
    
    #Computes the permutation cost by extra storage for cheating server
    def computePermutationS(self, filename, a, n, m, l, t_s, t_r, T):

        print (a, n, m, l, t_s, t_r, T) 

        file_size_bits = n*l

        k1 = math.floor(t_s/t_r)
        print (k1)
        k2 = 1+math.floor(n/(2*math.pow(m, 2)+(4*l/3)))
        print (k2)
        k = min(k1, k2)

        print (k)
        s = (2*a - 1)*n*l*(m-(T/(k*t_r))/(m-1))
        print (s)
        return s

        print ("This is k: ", k)
        
        A = (2*a - 1)*n*l
        B = m-(T/(k*t_r))
        C = (m-1)
        print (A,B,C)
        s = A*(B/C)

        #=======================================================================
        # s = (2*a - 1)*n*l*((m-(T/(k*t_r)))/(m-1))
        #=======================================================================
        
        extra_storage_relationship  = s/file_size_bits

        
        data_strings = "Inputs:", str(a), str(n), str(m), str(l), str(t_s), str(t_r), "File size in bits:", str(file_size_bits), "Results:", str(s), "Overhead relationship:", str(extra_storage_relationship), "\n"
        data_strings = ';'.join(data_strings)
        
        print ("File size in bits: ", file_size_bits)
        print ("Overhead data in bilts: ", s)
        print ("Overhead relationship (s/file size): ", extra_storage_relationship)
        with open(filename, 'a') as newfile:
            newfile.write(data_strings)
        return s

    def getSize(self): 
        self.f.seek(0, os.SEEK_END)
        size = self.f.tell()
        self.size = size
        self.f.seek(0, os.SEEK_SET)
        print ("The file size in bytes is: ", size)
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
            print (byte)
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

 
    #===========================================================================
    # def testDiv(self):
    #     s1 = "Started his hear"
    #     s2 = "ted any civilly."
    #     
    #     var  = "".join(i for j in zip(s1,s2) for i in j)
    #     print var
    #     
    #     block_one = var[::2]
    #     block_two = var[1::2]
    #     
    #     print block_one, " ", block_two 
    #===========================================================================
        
        
hg = Hourglass(filepath="test.txt")

#===============================================================================
# hg.testDiv()
#===============================================================================

#Theorem 1: computeS(a, n, l, t, e)


#===============================================================================
# for i in range(1,100):
#     print i
#     a = i
#     print a
#     temp = hg.computeButterflyS('butterflyfile_var_n.txt', 0.99, 500000, 128, 1, 0.05)
#     print temp
#===============================================================================


#Theorem 3: computePermutationS(filename, a, n, m, l, t_s, t_r, T)

for i in range(1,100):
    a = float(i)/100
    s = hg.computePermutationS('permuattion_s.txt', a, math.pow(2, 21), math.pow(2, 9), 32768, 0.006, 0.00003215, 0.006)
    print (a)

#===============================================================================
# temp = hg.computeButterflyS('butterflyfile2.txt', 0.99, 1, 128, 1, 0.05)
#===============================================================================

#size = hg.getSize()
#hg.wirteByteByByteToNewFile()

