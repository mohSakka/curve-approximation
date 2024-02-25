# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 18:41:17 2021

@author: mhdsq
"""
import evaluate
import generateMathematicalSeqDemo 

numOfPointsInSequence = 50
xLims = [-3,3]
polyDeg = 1
d = generateMathematicalSeqDemo.generate_d(numOfPointsInSequence,xLims,polyDeg)

for i in range(len(sol)):
    dists = evaluate.evaluate(d,sol[0])
    