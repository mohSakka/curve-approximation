# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:13:32 2021

@author: mhdsq
"""
import numpy as np

def genInitSol(d,n,margin):
    p = {}
    p['x'] = np.zeros(n)
    p['y'] = np.zeros(n)
    # first and last control points
    p['x'][0] = d['x'][0]
    p['x'][n-1] = d['x'][-1]
    
    p['y'][0] = d['y'][0]
    p['y'][n-1] = d['y'][-1]
    # 
    x = d['x']
    y = d['y']
    minX = min(x)
    minY = min(y)
    maxX = max(x)
    maxY = max(y)
    
    xBorders = [minX ,maxX]
    yBorders = [minY-margin ,maxY+margin]
    for i in range(1,n-1):
        p['x'][i] = np.random.uniform(low=xBorders[0], high=xBorders[1]) 
        p['y'][i] = np.random.uniform(low=xBorders[0], high=xBorders[1]) 
    
    return p