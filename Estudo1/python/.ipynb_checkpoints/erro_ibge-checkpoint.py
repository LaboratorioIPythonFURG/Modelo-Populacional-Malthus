
import numpy as np

def erro_ibge(index,solucao_IBGE,solucoes,metodos):
    
    dados = [[0, 0, 0]]
    
    for i in index:
        erro_hab = solucao_IBGE - solucoes[i]
        erro_perc = (erro_hab/solucao_IBGE)*100
        #Adicionando linhas à matriz (tabela)
        dados = np.vstack([dados,[metodos[i],round(erro_hab),str(round(erro_perc,2))+'%']])
        
    #remove a primeira linha da matriz
    dados = np.delete(dados, 0, 0)
    
    return dados
