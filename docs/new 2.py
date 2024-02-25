// initialization pseudocode for simple one curve:
	input:
	d // sequence of points as (x,y) coordinates
	n // number of control points 
	output:
	p // sequence of control points
	margin // to get the search space borders
	start:
	p = []
	p[0] = d[0]
	p[n-1] = d[end]
	
	
	x = d.x // vextor of x coordinates for all points
	y = d.y // vextor of y coordinates for all points
	min_x = min(x)
	min_y = min(y)
	max_x = max(x)
	max_y = max(y)
	xBorders = [min_x-margin max_x+margin]
	yBorders = [min_y-margin max_y+margin]
	for i in [1-->n-2]:
		p[i] = [genRan(xBorders),genRan(yBorders)]
				
				
				
				
						