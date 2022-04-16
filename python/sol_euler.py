#dependências
import numpy as np
from f_malthus import f

def sol_euler(vt,P0):
    
    #Declarando vetor de Habitantes
    P = np.array([P0])
    
    #Obtendo passo de derivação (h)
    h = vt[2] - vt[1]

    #Aproximando P(i) pelo método de Euler
    for t in vt:
        Pi = P[-1]+h*f(P[-1])
        P = np.append(P,Pi)
        
    return P[0:P.shape[0]-1]
