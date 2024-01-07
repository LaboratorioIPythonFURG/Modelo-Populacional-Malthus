import numpy as np #Biblioteca

def sol_rk4(vt,P0,modelo): #Função RK4
    
    P = np.array([P0]) #Vetor população  
    h = vt[2] - vt[1] #Passo de integração

    for t in vt:
        k1 = modelo(P[-1])
        k2 = modelo(P[-1]+(h/2)*k1)
        k3 = modelo(P[-1]+(h/2)*k2)
        k4 = modelo(P[-1]+h*k3)
        K = (1/6)*(k1+2*(k2+k3)+k4)
        Pi = P[-1]+h*K
        P = np.append(P,Pi)
        
    return P[0:P.shape[0]-1]
