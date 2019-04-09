#CONSTANTS
eps = 0.001

def pow(x, y):
	if( y == 1 or x == 1 ):
		return x

	if(y % 2 == 0):
		res = pow(x, y/2)
		return res*res

	else:
		res = pow(x, (y-1)/2) 
		return x*res*res

def binarySearch(x, y, min, max): #We want middle such that b = x ^ (1/y) or x = b^y

	middle = (max + min)/2
	dif_power =  x - pow(middle, y)

	if( abs( dif_power ) <= eps ):
		return max

	if( dif_power > eps ):
		return binarySearch(x, y, middle, max)

	if( dif_power < eps ):
		return binarySearch(x, y, min, middle)

def rad(x, y):
	return binarySearch(x, y, 0, x)

