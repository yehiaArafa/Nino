#!usr/bin/env python
import numpy as np
from numpy.linalg import inv
from sympy import *
import math
from decimal import Decimal
import plot

xArr = []
yArr = []

#creating basic variables; x and y and l=lambda
x, y, l = symbols('x y l', real=True)

#gradient vector (delta f) of the input function
deltaF = np.array([0,0])

#given a function and the variables in it; x and y, return the value of that function
def f(function,X,Y):
	return function.evalf(subs={x:X,y:Y})

#given a function and 2 variables, substitute the x and y in the function with the given variables
def subF(function,X,Y):
	return function.subs({x:X,y:Y})

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

#given a function, return the derivative of that function
def derivative(function):
	return diff(function)

#given a function, solve the function in terms of lambda, 
#if lambda have more than 1 value return real value max/min   
def solveEqn(function,MaxMinFlag):
	lamda=solve(function,l,check=False)
	realvalue=complex(lamda[0]).real
	for i in range(len(lamda)):		
		temp=complex(lamda[i]).real
		if MaxMinFlag==1:
			if realvalue<temp:
				realvalue=complex(lamda[i]).real
		else:
			if realvalue>temp:
				realvalue=complex(lamda[i]).real
	return realvalue

#given 2 matrices; matrix1 and matrix2, return |matrix1|^2 / |matrix2|^2	
def getMagnitudes(matrix1,matrix2):
	 magnitudeOfMatrix1=math.pow(matrix1[0],2)+math.pow(matrix1[1],2)
	 magnitudeOfMatrix2=math.pow(matrix2[0],2)+math.pow(matrix2[1],2)
	 return magnitudeOfMatrix1/magnitudeOfMatrix2


def main():

	#function to be evaluated (user defined)
	function=6*(x**2)-6*(x*y)+2*(y**2)-x-2*y
	#intial condition (user defined)
	intialCondition = np.array([0,0])
	#number of iterations (user defined) 
	numberOfIterations=100
	#maximize or minimize; 1 for maximize or -1 for minimize (user defined) 
	MaxMinFlag=-1 
	#optimum solution (stoping creteria encountered--> partialGradient=[0 0])
	optimum=0

	gradientF(function)
	pointOld=intialCondition

			
	for i in range(numberOfIterations):
		if all(v==0 for v in partialGradient(pointOld[0],pointOld[1])):
			optimum=1
			break
		print("Iteration number "+ str(i+1) +" : ")
		if i==0:
			partialGradNew=partialGradient(pointOld[0],pointOld[1]) 
			directionNew=MaxMinFlag*partialGradNew			
		else:
			partialGradNew=partialGradient(pointOld[0],pointOld[1])
			directionNew=(MaxMinFlag*partialGradNew)+(getMagnitudes(partialGradNew,partialGradOld)*directionOld)


		pointNew=pointOld + l*directionNew
		functionWithLamda=subF(function,pointNew[0],pointNew[1])
		dFunctionWithLamda=derivative(functionWithLamda)
		lamda=solveEqn(dFunctionWithLamda,MaxMinFlag)
		#print "Here ",lamda
		
		pointNew=pointOld+(lamda*directionNew) 	
		
		pointOld=pointNew
		directionOld=directionNew
		partialGradOld=partialGradNew
		xArr.append(pointNew[0])
		yArr.append(pointNew[1])
		print "Point",(i+1)," : ",pointNew

	if optimum:
		print "Optimum solution"	   	
	print "Point :",pointNew,", f(",pointNew[0],",",pointNew[1],")","=",f(function,pointNew[0],pointNew[1])
	plot.plot3D(xArr,yArr)

if __name__=="__main__":
	main()