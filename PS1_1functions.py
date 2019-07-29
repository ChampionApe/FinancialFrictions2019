from scipy import optimize
import numpy as np

def IR_constraint(Rtype,pH,pL,B,A,p):
    if Rtype=='sqroot':
        
        def f(x,a):
            return pH*(x**(0.5)-B*x/(pH-pL))-(x-a)
        def grad(x):
            return pH*0.5*x**(-0.5)-pH*B/(pH-pL)-1

        sol = np.zeros((A.size))
        for i in range(0, A.size):
            def g(x):
                return f(x,A[i])
            sol[i] = optimize.newton(g,1,fprime=grad)
        return sol
            
    if Rtype=='ln':
        def f(x,a): 
            return pH*(np.log(x)-B*x/(pH-pL))-(x-a)

        def grad(x):
            return pH*(1/x-B/(pH-pL))-1

        sol = np.zeros((A.size))
        for i in range(0, A.size):
            def g(x):
                return f(x,A[i])
            sol[i] = optimize.newton(g,1,fprime=grad)
        return sol

    if Rtype=='FlexiblePower':
        def f(x,a):
            return pH*(x**(p)-B*x/(pH-pL))-(x-a)

        def grad(x):
            return pH*(p*x**(p-1)-B/(pH-pL))-1
        
        sol = np.zeros((A.size))
        
        for i in range(0, A.size):
            def g(x):
                return f(x,A[i])
            sol[i] = optimize.newton(g,1,fprime=grad)
        
        return sol
    

def Istar(Rtype, pH, p):
    if Rtype=='sqroot':
        return (pH/2)**2
    if Rtype=='ln':
        return pH
    if Rtype=='FlexiblePower':
        return (p*pH)**(1/(1-p))


