import numpy as np

def Euler(vt,P0,f,params): 
        
    P = np.array([P0]) 

    for t in vt:
        
        h = vt[np.where(vt==t)[0][0]] - vt[np.where(vt==t)[0][0]+1]

        Pi = P[-1]+h*f(P[-1],params)        
        
        P = np.append(P,Pi)
        
    return P[0:P.shape[0]-1]

def EulerModificado(vt,P0,f,params): 
    
    P = np.array([P0]) 
    
    h = vt[2] - vt[1] 

    for t in vt: 
        
        Pi = P[-1]+(h/2)*(f(P[-1],params)+f(P[-1]+h*f(P[-1],params),params))
        
        P = np.append(P,Pi)
        
    return P[0:P.shape[0]-1]

def RK4(vt,P0,f,params): 
    
    P = np.array([P0]) 
    
    h = vt[2] - vt[1] 

    for t in vt: 
        
        k1 = f(P[-1],params)
        k2 = f(P[-1]+(h/2)*k1,params)
        k3 = f(P[-1]+(h/2)*k2,params)
        k4 = f(P[-1]+h*k3,params)
        K = (1/6)*(k1+2*(k2+k3)+k4)
        Pi = P[-1]+h*K
        P = np.append(P,Pi)
        
    return P[0:P.shape[0]-1]