# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:10:38 2018

@author: UT
"""

import requests
import json

ur="http://freegeoip.net/json"
r = requests.get(ur)
j = json.loads(r.text)
city=j['city']
cn=j['country_name']
ip=j['ip']
lat=j['latitude']
long=j['longitude']
mc=j['metro_code']
rc=j['region_code']
rn=j['region_name']
tz=j['time_zone']
zc=j['zip_code']


print("Details.........\n"+"City:"+str(city)+"\nCountry:"+str(cn)+"\nIP:"+str(ip)+
      "\nLatitude:"+str(lat)+"\nLongitude:"+str(long)+"\nMetroCode:"+str(mc)+"\nRegionCode"+str(rc)+
      "\nRegion Name:"+str(rn)+"\nTimeZOne:"+str(tz)+"\nZipCode"+str(zc))
