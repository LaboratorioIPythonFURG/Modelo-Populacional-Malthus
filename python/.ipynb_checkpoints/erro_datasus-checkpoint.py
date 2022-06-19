import numpy as np

def erro_datasus(dados_datasus,solucoes,metodo):
    
    dados = [[0, 0, 0]]
    
    for i in range(0,3):
        
        if metodo=='lsoda':
            
            erro_hab = dados_datasus[i] - solucoes[i][0]
            print(erro_hab)
            erro_perc = (erro_hab/dados_datasus[i])*100
            #Adicionando linhas à matriz (tabela)
            dados = np.vstack([dados,[solucoes[i][0],round(erro_hab),str(round(erro_perc,2))+'%']])
            
        elif metodo=='rk45':
            
            erro_hab = dados_datasus[i] - solucoes[i]
            print(erro_hab)
            erro_perc = (erro_hab/dados_datasus[i])*100
            #Adicionando linhas à matriz (tabela)
            dados = np.vstack([dados,[solucoes[i],round(erro_hab),str(round(erro_perc,2))+'%']])
            
        else:
            
            erro_hab = dados_datasus[i] - solucoes[i]
            print(erro_hab)
            erro_perc = (erro_hab/dados_datasus[i])*100
            #Adicionando linhas à matriz (tabela)
            dados = np.vstack([dados,[solucoes[i],round(erro_hab),str(round(erro_perc,2))+'%']])
        
    #remove a primeira linha da matriz
    dados = np.delete(dados, 0, 0)
    
    return dados