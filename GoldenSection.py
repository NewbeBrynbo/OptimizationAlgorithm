# -*-coding:utf-8 -*-
import math

'''
Function Interface:
'''
def f(x):      
    y=x*(x+2)
    return y


def golden(a,b,theta):      
    #Iteration Definition
    alpha=(math.sqrt(5)-1)/2
    t1=a+(1-alpha)*(b-a)
    t2=a+alpha*(b-a)

    step_num=0
    
    while abs(t1-t2)>=theta:
        step_num+=1
        
        f1=f(t1)
        f2=f(t2)
        print("Step: "+str(step_num))
        print("t1: "+str(t1)+"  "+"t2: "+str(t2))
        print("ERR: "+str(abs(t1-t2)))
        print("f(t1): "+str(f1)+"    "+"f(t2): "+str(f2))
        print("===============///////////=================")
        if f1<f2:
            b=t2
            t2=t1
            f2=f1
            t1=a+(1-alpha)*(b-a)
        else:
            a=t1
            t1=t2
            f1=f2
            t2=a+alpha*(b-a)
    t_opt=(t1+t2)/2
    f_opt=f(t_opt)
    print("t*= "+str(t_opt))
    print("f*= "+str(f_opt))

    return a,b,t_opt,f_opt,step_num

l,r,t_opt,f_opt,step_num=golden(-3,5,0.001)
print("a: "+str(l)+"  "+"b: "+str(r))
