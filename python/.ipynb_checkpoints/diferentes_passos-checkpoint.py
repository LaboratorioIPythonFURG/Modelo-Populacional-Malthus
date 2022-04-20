import numpy as np
from sol_euler import sol_euler
from sol_euler_mod import sol_euler_mod
from sol_rk4 import sol_rk4
import matplotlib.pyplot as plt

def diferentes_passos(ti,tf,passos,P0,cores,modelo,metodo):
    #Criando loop que percorre os elementos de passos
    for passo in passos:

        #Criando vetor tempo
        vt = np.arange(ti,tf,passo)
        
        if modelo == 'Malthus':
            
            if metodo == 'sol_euler':
                                
                P = sol_euler(vt,P0,'malthus')
                
            elif metodo == 'sol_euler_mod':
                
                P = sol_euler_mod(vt,P0,'malthus')
            
            elif metodo == 'sol_rk4':
                
                P = sol_rk4(vt,P0,'malthus')
        
        elif modelo == 'Verhulst':
            
            if metodo == 'sol_euler':
                
                P = sol_euler(vt,P0,'verhulst')
                
            elif metodo == 'sol_euler_mod':
                
                P = sol_euler_mod(vt,P0,'verhulst')
                
            elif metodo == 'sol_rk4':
                
                P = sol_rk4(vt,P0,'verhulst')
            
                
        #Grafico da curva    
        plt.plot(vt,P,'{}'.format(cores[np.where(passos==passo)[0][0]]),label='h = {}'.format(passo))


    #Exibindo figura
    plt.title("Simulação populacional para diferentes passos de derivação")
    plt.xlabel("Anos (Ano+2*10^3)")
    plt.ylabel("Número de habitantes")
    plt.legend()
    plt.show()
    
    return P