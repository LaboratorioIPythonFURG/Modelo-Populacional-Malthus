import numpy as np
from sol_euler import sol_euler
import matplotlib.pyplot as plt

def diferentes_passos(ti,tf,passos,P0,cores,modelo,metodo):
    #Criando loop que percorre os elementos de passos
    for passo in passos:

        #Criando vetor tempo
        vt = np.arange(ti,tf,passo)
        
        if modelo == 'Malthus' and metodo == 'sol_euler':            
            #Chamando a função sol_euler 
            P = sol_euler(vt,P0,'malthus')
        
        #Grafico da curva    
        plt.plot(vt,P,'{}'.format(cores[np.where(passos==passo)[0][0]]),label='h = {}'.format(passo))


    #Exibindo figura
    plt.title("Simulação populacional para diferentes passos de derivação")
    plt.xlabel("Anos (Ano+2*10^3)")
    plt.ylabel("Número de habitantes")
    plt.show()
    
    return P