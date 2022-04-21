import numpy as np
from f_malthus import f_malthus
from f_verhulst import f_verhulst

def sol_euler_mod(vt,T0,modelo):
    
    #Declarando vetor de temperaturas
    T = np.array([T0])
    
    #Obtendo passo de derivação (h)
    h = vt[2] - vt[1]

    #Aproximando T(i) pelo método de Euler modificado
    for t in vt:
        
        if modelo=='malthus':
            Ti = T[-1]+(h/2)*(f_malthus(T[-1])+f_malthus(T[-1]+h*f_malthus(T[-1])))
        elif modelo=='verhulst':
            Ti = T[-1]+(h/2)*(f_verhulst(T[-1])+f_verhulst(T[-1]+h*f_verhulst(T[-1])))
        
        T = np.append(T,Ti)
        
    return T[0:T.shape[0]-1]
