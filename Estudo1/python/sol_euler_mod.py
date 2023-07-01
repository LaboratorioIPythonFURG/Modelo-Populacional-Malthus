
import numpy as np #Biblioteca

def sol_euler_mod(vt,P0,modelo): #Função Euler Modificado
    
    P = np.array([P0]) #Vetor população
    
    h = vt[2] - vt[1] #Passo de derivação

    for t in vt: #Aproximando T(i) pelo método de Euler modificado
        
        Pi = P[-1]+(h/2)*(modelo(P[-1])+modelo(P[-1]+h*modelo(P[-1])))
        
        P = np.append(P,Pi)
        
    return P[0:P.shape[0]-1]
