# -*-coding:utf-8 -*-

import math
import numpy as np
from sympy import *

'''
Function Interface:
'''
def f(x1,x2):
    y=x1**2+x2**2-x1*x2-10*x1-4*x2+60
    return y

def UST(x1,x2,eps):
    
    X0=np.array([x1,x2],dtype=float)
    e1=np.array([1,0])
    e2=np.array([0,1])
    step_num=1
    X=X0

    while 1:
        print("Step: "+str(step_num))
        i=1
        while i<=2:
            if i==1:
                e=e1
                t=symbols('t')
                t_out=solve(diff(f(X[0]+t*e[0],X[1]+t*e[1]),t),t)
                X=X+t_out*e
                print("e1="+str(e))
                print("t_"+str(step_num)+"_1: "+str(t_out))
                print("X_"+str(step_num)+"_1: "+str(X))
            else:
                e=e2
                t=symbols('t')
                t_out=solve(diff(f(X[0]+t*e[0],X[1]+t*e[1]),t),t)
                X=X+t_out*e
                print("e2="+str(e))
                print("t_"+str(step_num)+"_2: "+str(t_out))
                print("X_"+str(step_num)+"_2: "+str(X))
            i+=1
        ERR=math.sqrt((X[0]-X0[0])**2+(X[1]-X0[1])**2)
        if ERR<=eps:
            break
        print("ERR: "+str(ERR))
        print("===============///////////=================")
        X0=X
        step_num+=1
    x_out=X
    return x_out

X_out=UST(0,0,0.1)
print("X*= "+str(X_out)+"  "+"f(X*)= "+str(f(X_out[0],X_out[1])))
