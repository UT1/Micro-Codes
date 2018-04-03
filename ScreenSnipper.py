# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 12:01:57 2018

@author: srivastavau
"""

import time
import wx

class App(wx.App):    
    def OnInit(self):
        screen=wx.ScreenDC()
        
        size=screen.GetSize()
        bmp=wx.EmptyBitmap(size[0],size[1])
        mem=wx.MemoryDC(bmp)
        mem.Blit(0,0,size[0],size[1],screen,0,0)
        del mem
        
        bmp.SaveFile('Screenshot.png',wx.BITMAP_TYPE_PNG)
        return True

print("You have 10 seconds to switch to the desired Screen")
time.sleep(10)
app=App()
app.MainLoop()
    