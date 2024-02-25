# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:11:04 2021

@author: mhdsq
"""
import bezierCurveFuncs
from genInitSol import genInitSol
from evaluate import evaluate
import numpy as np
import matplotlib.pyplot as plt
import copy

plt.ion()
plt.show()

def simpleANSA(SAoptions,n,eps,delta,d,margin):
    # extracting the parameters
    T = SAoptions['T']
    alpha = SAoptions['alpha']
    maxSubIt = SAoptions['maxSubIt']
    maxIt = SAoptions['maxIt']
    sigma = SAoptions['sigma']
    
    # start
    sols=[]
    Xcurrent = {}
    q = {}
    Xcurrent['pos'] = genInitSol(d,n,margin)
    points = np.zeros((n,2))
    for i in range(n):
        points[i][0] = Xcurrent['pos']['x'][i]
        points[i][1] = Xcurrent['pos']['y'][i]
    q['x'],q['y'] = bezierCurveFuncs.evaluate_bezier(points, int(1/delta)) # get bezier curve discretized # 2x1 ^~^
    Xcurrent['cost'] = evaluate(d,q)
    Xcurrent['q'] = q.copy()
    for globIt in range(maxIt):
        T = T*alpha
        for subIt in range(maxSubIt):
            randIdx = np.random.randint(low=1,high=n-1)
            
            Xnew = copy.deepcopy(Xcurrent)

            
            if randIdx!=0 and randIdx!=n-1:
                if np.random.uniform()<1:
                    Xnew['pos']['x'][randIdx] += np.random.normal(0,sigma)
                
                
                
                    
               # else:  
                    Xnew['pos']['y'][randIdx] += np.random.normal(0,sigma)
               
            
            else:
                Xnew['pos']['x'][randIdx] = Xcurrent['pos']['x'][randIdx] + eps*np.random.choice([-1,1])
                Xnew['pos']['y'][randIdx] = Xcurrent['pos']['y'][randIdx] + eps*np.random.choice([-1,1])
            
            points = np.zeros((n,2))
            for i in range(n):
                points[i][0] = Xnew['pos']['x'][i]
                points[i][1] = Xnew['pos']['y'][i]
            q2 = {}
            q2['x'],q2['y'] = bezierCurveFuncs.evaluate_bezier( points, int(1/delta)) # get bezier curve discretized # 2x1 ^~^
            Xnew['q'] = q2
            Xnew['cost'] = evaluate(d,q2)
            deltaE = Xnew['cost'] - Xcurrent['cost']
            
            if deltaE<0:
                Xcurrent['pos'] = Xnew['pos'].copy()
                Xcurrent['q'] = Xnew['q'].copy()
                Xcurrent['cost'] = Xnew['cost'].copy()
               # ci = 1
            else:
                P = np.exp(-deltaE/Xcurrent['cost']/T)
                if np.random.uniform()<=P:
                    Xcurrent = Xnew.copy()
                    
            plt.cla()
            plt.plot(Xcurrent['q']['x'],Xcurrent['q']['y'],'b.')
            plt.plot(d['x'],d['y'],'g.')
            for ip in range(n):
                plt.plot(points[ip,0],points[ip,1],'ro')
            
            plt.title(globIt)
            print(globIt,': ',Xcurrent['cost'])
            plt.pause(0.0000000001)
            
            #print(Xcurrent['pos']['x']) 
           
            sols.append(Xcurrent)
    return sols
        
                    
                    