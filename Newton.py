#!usr/bin/env python
import numpy as np 
from numpy.linalg import inv
from sympy import *

#creating basic variables; x and y 
x, y = symbols('x y', real=True)

#gradient vector (delta f) of the input function
deltaF = np.array([0,0])

#given a function and the variables in it; x and y, return the value of that function
def f(function,X,Y):
	return function.evalf(subs={x:X,y:Y})

#given a function, set the gradient (delta f) of that function 
def gradientF(function):
	fx=diff(function,x)
	fy=diff(function,y)
	global deltaF
	deltaF=np.array([fx,fy])

#given 2 points x and y, return the value of the gradient matrix at these points(delta f1)
def partialGradient(X,Y):
	global deltaF
	#.n(chop=True) is used to chop the small numbers (to get exactly 0)
	partial= np.array([deltaF[0].evalf(subs={x:X,y:Y}).n(chop=True),deltaF[1].evalf(subs={x:X,y:Y}).n(chop=True)])
	return partial

#return the inverse of the hessian matrix of the input function
def getInverseOfHessianMatrix(X,Y):
	fxx=diff(deltaF[0],x)
	xx=float(fxx.evalf(subs={x:X,y:Y}))
	fxy=diff(deltaF[0],y)
	xy=float(fxy.evalf(subs={x:X,y:Y}))
	fyx=diff(deltaF[1],x)
	yx=float(fyx.evalf(subs={x:X,y:Y}))
	fyy=diff(deltaF[1],y)
	yy= float(fyy.evalf(subs={x:X,y:Y}))
	hessain=np.array([[xx,xy],[yx,yy]])
	return inv(hessain)
	
def main():
	#function to be evaluated (user defined)
	function= 100*(y-x**2)**2+(1-x)**2
	#intial condition (user defined)
	intialCondition = np.array([1,1])
	#number of iterations (user defined)
	numberOfIterations=10
	#optimum solution (stoping creteria encountered--> partialGradient=[0 0])

	gradientF(function)
	pointOld=intialCondition
		
	for i in range(numberOfIterations):
		if all(v==0 for v in partialGradient(pointOld[0],pointOld[1])):
			optimum=1
		print("Iteration number "+ str(i+1) +" : ")
		pointNew = pointOld - (partialGradient(pointOld[0],pointOld[1]).dot(getInverseOfHessianMatrix(pointOld[0],pointOld[1])))
		pointOld = pointNew
		print "Point :",pointNew,", f(",pointNew[0],",",pointNew[1],")","=",f(function,pointNew[0],pointNew[1])
	if optimum==1:
		print "Optimum solution"
	
if __name__=="__main__":
	main()