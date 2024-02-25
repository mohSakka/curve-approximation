// optimization using ANSA

input:
n // number of control points
T // initial temperature
alpha // reduction rate
maxSubIt // Maximum Number of Sub-iterations
maxIt //maximum global iterations
sigma // mutation deviation
eps // discrete movement ratio
qNum // number of discrete bezier curve points
d // sequence of points

output:

start:
Xcurrent = genRandSol(d,n,margin)
Xcurrent = evaluate(Xcurrent)
for globIt = 1--> maxGlop:
	T = T * alpha
	for subIt = 1--> maxSubIt:
		randIdx = genRan(0,n-1) // select random control point
		// check if selected parameter continous or discrete
		Xnew = Xcurrent
		if randIdx !=0 && randIdx !=n-1:
			Xnew[randIdx] = Xcurrent[randIdx] + sigma*randn()
		else:
			Xnew[randIdx] = Xcurrent[randIdx] + randInt(-1,1)*eps
			bezierCurvePoints = generateBezierCurve(Xnew,qNum)
			discrepency = objFun(bezierCurvePoints,d)
			deltaE = discrepency - Xcurrent.discrepency
				
			if deltaE<0:
				Xcurrent = Xnew
				ci = 1
			else:
				
				
			
	
