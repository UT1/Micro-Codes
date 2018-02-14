# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 14:13:49 2018

@author: srivastavau
"""

import psutil as psu
import pandas as pd
import time
class mcpu:    
    def vm(this):
        memo=psu.virtual_memory()
        x=1000000000

        print("Total Memory:"+str(memo[0]/x)+" GB\nAvailable Memory:"+str(memo[1]/x)+" GB\nPercent Used:"
              +str(memo[2])+"%\nUsed Memory:"+str(memo[3]/x)+" GB\nFree Memory:"+str(memo[4]/x))

    def du(this):
        hd=psu.disk_usage('/')
        x=1000000000
        print("Total memory space:"+str(hd[0]/x)+" GB\nUsed Memory:"+str(hd[1]/x)+" GB\nFree Memory:"+str(hd[2]/x)+"GB\nPercent:"+str(hd[3])+"%")        
print("What is happening to my CPU...?")
time.sleep(3)
ob=mcpu()
print("\n\t \tVirtual Memory Info\n")
ob.vm()
print("\n\t \tHard Disk Info\n")
ob.du()
