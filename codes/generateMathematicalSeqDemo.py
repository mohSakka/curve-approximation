# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 00:24:44 2021

@author: mhdsq
"""
import numpy as np
import matplotlib.pyplot as plt
from math import factorial

#%% input params
polyDeg = 3
xLim = [-3,3]
numOfPoints = 50
#%%
def calcPoly(x,polyDeg):
    return sum(x**i for i in range(polyDeg+1))

def generate_d(numOfPoints,xLim,polyDeg):
    d = {}
    d['x'] = np.linspace(xLim[0], xLim[1], numOfPoints)
    d['y'] = np.array([calcPoly(x,polyDeg) for x in  d['x']])
    return d

# d = generate_d(numOfPoints,xLim,polyDeg)
# plt.plot(d['x'],d['y'])



    