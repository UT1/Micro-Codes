# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 11:36:33 2018

@author: srivastavau
"""

import wmi

computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]

os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB

print('OS Name: {0}'.format(os_name))
print('OS Version: {0}'.format(os_version))
print('CPU: {0}'.format(proc_info.Name))
print('RAM: {0} GB'.format(system_ram))
print('Graphics Card: {0}'.format(gpu_info.Name))

#Courtesy: https://stackoverflow.com/questions/38103690/get-system-informationcpu-speed-total-ram-graphic-card-model-etc-under-window
