# -*- coding: utf-8 -*-
'''
Created on 2014年9月3日

@author: aadebuger
'''
import unittest
import ctypes
import time
class Test(unittest.TestCase):


    def testName(self):
        print 'test dll'
        dll = ctypes.windll.LoadLibrary( 'CH9326DLL.dll' )
        handle =dll.CH9326OpenDevice(0x1a86,0xe010);
        print 'handle=',handle
        ret = dll.CH9326SetIODir(handle,0xffff)

        for i in range(1000):
            print 'ret=',ret
            print 'on'
            ret = dll.CH9326WriteIOData(handle,0xffff)
            time.sleep(1)
            print 'off'
            ret = dll.CH9326WriteIOData(handle,0x0)
            time.sleep(5)
                            
        dll.CH9326CloseDevice(handle)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()