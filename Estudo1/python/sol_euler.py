
import numpy as np #Biblioteca

def sol_euler(vt,P0,modelo): #Função Euler
        
    P = np.array([P0]) #Vetor população
    
    h = vt[2] - vt[1] #Passo de derivação

    for t in vt: #Aproximando P(i) pelo método de Euler
        
        Pi = P[-1]+h*modelo(P[-1])        
        
        P = np.append(P,Pi)
        
    return P[0:P.shape[0]-1]
