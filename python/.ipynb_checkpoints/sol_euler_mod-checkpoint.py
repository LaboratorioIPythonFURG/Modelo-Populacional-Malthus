import numpy as np
from f_malthus import f_malthus
from f_verhulst import f_verhulst

def sol_euler_mod(vt,P0,modelo):
    
    #Declarando vetor de temperaturas
    P = np.array([P0])
    
    #Obtendo passo de derivação (h)
    h = vt[2] - vt[1]

    #Aproximando T(i) pelo método de Euler modificado
    for t in vt:
        
        if modelo=='malthus':
            Pi = P[-1]+(h/2)*(f_malthus(P[-1])+f_malthus(P[-1]+h*f_malthus(P[-1])))
        elif modelo=='verhulst':
            Pi = P[-1]+(h/2)*(f_verhulst(P[-1])+f_verhulst(P[-1]+h*f_verhulst(P[-1])))
        
        P = np.append(P,Pi)
        
    return P[0:P.shape[0]-1]
