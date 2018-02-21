# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 16:09:53 2018

@author: srivastavau
"""


import pyspeedtest as pt
def net_check():
    fro=pt.SpeedTest()
    print("Ping(In sec):"+str(fro.ping()))
    print("Download Speed(In Mbps):")
    print(fro.download()/1000000)
#    print("Upload Speed(In Mbps):")
#    print(fro.upload()/1000000)
#net_check()
