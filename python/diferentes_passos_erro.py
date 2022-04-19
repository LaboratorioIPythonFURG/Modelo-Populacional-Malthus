import numpy as np
from sol_euler import sol_euler
import matplotlib.pyplot as plt
from f_erro import f_erro

def diferentes_passos_erro(ti,tf,passos,P0,cores,modelo,metodo):

    err = 0
    P = 0
    
    #Criando loop para diferentes passos de derivação
    for passo in passos:

        #Criando vetor tempo 
        vt = np.arange(ti,tf,passo)
        
        if modelo == 'Malthus':                        
                
            #Gerando solução analítica
            sol_analitica = 186488*np.exp(0.0056*vt)

            if metodo == 'sol_euler':
            
                #Chamando a função sol_euler 
                P = sol_euler(vt,P0,'malthus')
            
                #Chamando a função erro
                err = f_erro(sol_analitica,P)
                
        elif modelo == 'Verhulst':
            
            #Gerando solução analítica
            sol_analitica = 186488*np.exp(0.0056*vt)
            
            if metodo == 'sol_euler':
            
                #Chamando a função sol_euler 
                P = sol_euler(vt,P0,'verhulst')
            
                #Chamando a função erro
                err = f_erro(sol_analitica,P)
                
        else:
            
            print('Modelo não suportado')
            
        #Grafico da curva    
        plt.plot(vt,err,'{}'.format(cores[np.where(passos==passo)[0][0]]),label='h = {}'.format(passo))

    #Exibindo figura
    plt.title("Erro entre a solução analítica e o método de Euler")
    plt.xlabel("Anos (Ano+2*10^3)")
    plt.ylabel("Número de habitantes")
    plt.legend()
    plt.show()

    return P