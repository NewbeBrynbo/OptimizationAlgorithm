# -*-coding:utf-8 -*-

import math
import numpy as np 

'''
Function Interface:
'''
def f(x):
    y=8*x**3-2*x**2-7*x+3
    return y


def ParaCalc(t1,t0,t2):
    if f(t1)<f(t0) or f(t0)>f(t2):
        print("Unfilled")
        return 
    
    A=[[1,t1,t1**2],[1,t0,t0**2],[1,t2,t2**2]]
    b=[f(t1),f(t0),f(t2)]
    X=np.linalg.solve(A,b)
    a0=X[0]
    a1=X[1]
    a2=X[2]
    x=-a1/(2*a2)
    return x
   
def ParaIntep(a,tmp,b,eps):
    x=ParaCalc(a,tmp,b)
    print("x: "+str(x))

    step_num=0

    f1=f(a)
    f0=f(tmp)
    f2=f(b)
    fx=f(x)
    print("a: "+str(a)+"  "+"t0: "+str(tmp)+"  "+"b: "+str(b))
    while abs(tmp-x)>=eps:
        step_num+=1
        print("Step: "+str(step_num))
        print("t_: "+str(x)+"  "+"t0: "+str(tmp))
        print("ERR: "+str(abs(tmp-x)))
        print("f(t_): "+str(fx)+"    "+"f(t0): "+str(f0))
        print("===============///////////=================")
        if x>tmp:
            if f(x)<=f(tmp):
                a=tmp
                f1=f0
                tmp=x
                f0=fx
            else:
                b=x
                f2=fx
        else:
            if f(x)<=f(tmp):
                b=tmp
                f2=f0
                tmp=x
                f0=fx
            else:
                a=x
                f1=fx
        x=ParaCalc(a,tmp,b)
    t_opt=x
    f_opt=f(t_opt)

    print("t*: "+str(t_opt)+"  "+"f*: "+str(f_opt))

    return t_opt,f_opt

t_opt,f_opt=ParaIntep(0,1,2,0.001)
