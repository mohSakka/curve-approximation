# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 22:32:21 2021

@author: mhdsq
"""
import numpy as np 

def evaluate(d,q):
    # d: original sequence
    # q: quantized bezier curve
    adjaMat = np.zeros((len(d['x']),len(q['x'])))
    for i in range(len(d['x'])):
        p1 = np.array([d['x'][i],d['y'][i]])
        for j in range(len(q['x'])):
            
            p2 = np.array([q['x'][j],q['y'][j]])
                           
            adjaMat[i,j] = np.linalg.norm(p1-p2)
   
    deltas = []
    for di in range(len(d['x'])):
        k = np.argmin(adjaMat[di,:]) # closest d point to q
        dPoint = np.array([d['x'][di],d['y'][di]])
        qPoint_mid = np.array([q['x'][k],q['y'][k]])
        if k==0 or k==len(q['x'])-1:
           delta = 0
           continue
        
        qPoint_left = np.array([q['x'][k-1],q['y'][k-1]])
        qPoint_right = np.array([q['x'][k+1],q['y'][k+1]])
        
        s1 = (np.linalg.norm(dPoint-qPoint_left) + \
            np.linalg.norm(dPoint-qPoint_mid) +\
                np.linalg.norm(qPoint_mid-qPoint_left))/2
        A1 = s1*(s1-np.linalg.norm(dPoint-qPoint_left))*\
            (s1-np.linalg.norm(dPoint-qPoint_mid))*\
            (s1- np.linalg.norm(qPoint_mid-qPoint_left)) 
        
        A1 = np.sqrt(A1)
        
        cAlpha1 = np.inner(dPoint-qPoint_mid, qPoint_left-qPoint_mid)
        
        s2 = (np.linalg.norm(dPoint-qPoint_mid) + \
              np.linalg.norm(qPoint_right-qPoint_mid) +\
              np.linalg.norm(dPoint-qPoint_right))/2
        
        A2 = s2*(s2-np.linalg.norm(dPoint-qPoint_mid))*\
            (s2-np.linalg.norm(qPoint_right-qPoint_mid))*\
                (s2-np.linalg.norm(dPoint-qPoint_right))
        
        A2 = np.sqrt(A2)
        
        cAlpha2 = np.inner(dPoint-qPoint_mid, qPoint_right-qPoint_mid)
        
       
        if cAlpha1<0 and cAlpha2<0:
            delta =  np.linalg.norm(dPoint-qPoint_mid)
        elif A1>A2 and cAlpha1<0:
            delta = (2*A1)/np.linalg.norm(qPoint_mid-qPoint_left)
        else:
            delta = (2*A2)/np.linalg.norm(qPoint_right-qPoint_mid)
        
        #delta = np.linalg.norm(dPoint-qPoint_mid)
        deltas.append(delta)
    return np.sum(deltas)
        
    