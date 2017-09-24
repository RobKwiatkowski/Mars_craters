# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 15:17:52 2017

@author: Robert

This program calculates the craters density in the function of LONGITUDE
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def area(lat1,lat2):
    R = 3389
    lat1 = np.radians(lat1)
    lat2 = np.radians(lat2)
    area = 2*np.pi*R**2*((1-np.cos(lat2))-(1-np.cos(lat1)))
    print abs(round(area,0))
    return abs(area)

def counter(lat1,lat2):
    lat=source[(source['LONGITUDE_CIRCLE_IMAGE']>=lat1) 
    & (source['LONGITUDE_CIRCLE_IMAGE']<lat2)]
    print "(", lat1, lat2, ")" , "craters' count: ", lat['CRATER_ID'].count()
    return lat['CRATER_ID'].count()

# opening the original CSV dataset
source=pd.read_csv(r'D:\marscraters.csv',low_memory=False)

source['LONGITUDE_CIRCLE_IMAGE']=pd.to_numeric(source['LONGITUDE_CIRCLE_IMAGE'])
AREA = 4*3.15*3389**2/360
STEP=1

#counting craters in the north
craters_count =[]
for a in np.arange(-180,180,STEP):
    b = a+STEP
    craters_count.append(counter(a,b))

#calculating density in the north
density_craters = []
for n in np.arange(-180,180/STEP,1):
    density = craters_count[n]/AREA
    print n, density
    density_craters.append(density)

X = np.arange(-180,180,STEP)
Y = density_craters
plt.xlim(-180,180)
plt.grid()
plt.xlabel("Latitude")
plt.ylabel("Craters density [craters/km2]")
#plt.plot(X,Y)
plt.scatter(X,Y)
#plt.bar(X,density_craters)