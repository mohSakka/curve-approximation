# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:30:03 2021

@author: mhdsq
"""
#%% import libraries and files
import generateMathematicalSeqDemo 
from simpleANSA import simpleANSA
import numpy as np
np.random.seed(1)
#%% input params
xLims = [-3,3]
polyDeg = 3
numOfPointsInSequence = 50
d = generateMathematicalSeqDemo.generate_d(numOfPointsInSequence,xLims,polyDeg)
SAoptions = {}
SAoptions['T'] = 0.1
SAoptions['alpha'] = 0.7
SAoptions['maxSubIt'] = 1
SAoptions['maxIt'] = 500
SAoptions['sigma'] = 0.05*(xLims[1]-xLims[0])

n = 4 # number of control points
eps = 0.1
delta = 0.1 # quantization parameter
margin = 0.1 

sol = simpleANSA(SAoptions,n,eps,delta,d,margin)

