
import numpy as np

def erro_n(dados,hab_real,approx,metodo):
    
    erro_hab = abs(hab_real - approx)
    erro_perc = (erro_hab/hab_real)*100
    dados = np.vstack([dados,[str(metodo),hab_real,round(approx,2),round(erro_hab),str(round(erro_perc,2))+'%']])
    
    return dados
