# -*- coding: utf-8 -*-
"""
@author:UT
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
