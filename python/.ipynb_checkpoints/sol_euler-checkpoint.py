#dependências
import numpy as np
from f_malthus import f_malthus
from f_verhulst import f_verhulst

def sol_euler(vt,P0,modelo):
    
    #Declarando vetor de Habitantes
    P = np.array([P0])
    
    #Obtendo passo de derivação (h)
    h = vt[2] - vt[1]

    #Aproximando P(i) pelo método de Euler
    for t in vt:
        
        if modelo=='malthus':
            Pi = P[-1]+h*f_malthus(P[-1])
        elif modelo=='verhulst':
            Pi = P[-1]+h*f_verhulst(P[-1])            
        P = np.append(P,Pi)
        
    return P[0:P.shape[0]-1]
