import numpy as np
from f_malthus import f_malthus
from f_verhulst import f_verhulst
from f_montroll import f_montroll

def sol_euler(vt,P0,modelo):
    
    #Declarando vetor de Habitantes
    P = np.array([P0])
    
    #Obtendo passo de derivação (h)
    h = vt[2] - vt[1]

    #Aproximando P(i) pelo método de Euler segundo o modelo
    for t in vt:
        
        if modelo=='malthus':
            Pi = P[-1]+h*f_malthus(P[-1])
        elif modelo=='verhulst':
            Pi = P[-1]+h*f_verhulst(P[-1]) 
        elif modelo=='montroll':
            Pi = P[-1]+h*f_montroll(P[-1])
        P = np.append(P,Pi)
        
    return P[0:P.shape[0]-1]
