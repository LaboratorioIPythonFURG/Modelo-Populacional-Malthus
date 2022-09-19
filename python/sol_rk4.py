#dependencias 
import numpy as np
from f_malthus import f_malthus
from f_verhulst import f_verhulst
from f_montroll import f_montroll

def sol_rk4(vt,P0,modelo):
    
    #Declarando vetor de temperaturas
    P = np.array([P0])
    
    #Obtendo passo de derivação (h)
    h = vt[2] - vt[1]

    #Aproximando T(i) pelo método de Euler modificado
    for t in vt:
        
        if modelo == 'malthus':
            k1 = f_malthus(P[-1])
            k2 = f_malthus(P[-1]+(h/2)*k1)
            k3 = f_malthus(P[-1]+(h/2)*k2)
            k4 = f_malthus(P[-1]+h*k3)
        elif modelo == 'verhulst':
            k1 = f_verhulst(P[-1])
            k2 = f_verhulst(P[-1]+(h/2)*k1)
            k3 = f_verhulst(P[-1]+(h/2)*k2)
            k4 = f_verhulst(P[-1]+h*k3)
        elif modelo == 'montroll':
            k1 = f_montroll(P[-1])
            k2 = f_montroll(P[-1]+(h/2)*k1)
            k3 = f_montroll(P[-1]+(h/2)*k2)
            k4 = f_montroll(P[-1]+h*k3)
        
        K = (1/6)*(k1+2*(k2+k3)+k4)
        Pi = P[-1]+h*K
        P = np.append(P,Pi)
        
    return P[0:P.shape[0]-1]
