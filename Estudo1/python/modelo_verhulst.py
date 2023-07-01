#Definindo o modelo populacional
def modelo_verhulst(t,P):
    L = 218858
    k = 0.04285
    return  (k*(1-P/L))*P
