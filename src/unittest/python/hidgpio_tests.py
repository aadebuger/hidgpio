# -*- coding: utf-8 -*-
'''
Created on 2014年9月3日

@author: aadebuger
'''
import unittest
import ctypes
class Test(unittest.TestCase):


    def testName(self):
        print 'test dll'
        dll = ctypes.windll.LoadLibrary( 'CH9326DLL.dll' )
        handle =dll.CH9326OpenDevice(0x1a86,0xe010);
        print 'handle=',handle
        dll.CH9326CloseDevice(handle)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()