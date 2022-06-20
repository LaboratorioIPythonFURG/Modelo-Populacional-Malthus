
import numpy as np

def erro_datasus(dados_datasus,solucoes,metodo):
    
    dados = [[0, 0, 0, 0, 0]]
    
    for i in range(0,3):
        
        if metodo=='lsoda':
            
            solucao = solucoes[i][0]
            
        elif metodo=='rk45':
            
            solucao = solucoes.y[0][i]
        
        else:
            
            solucao = solucoes[i]
            
        erro_hab = dados_datasus[i] - solucao
        #print(erro_hab)
        erro_perc = (erro_hab/dados_datasus[i])*100
        #Adicionando linhas à matriz (tabela)
        dados = np.vstack([dados,[i,dados_datasus[i],round(solucao,2),round(erro_hab),str(round(erro_perc,2))+'%']])
        
    #remove a primeira linha da matriz
    dados = np.delete(dados, 0, 0)
    
    return dados
