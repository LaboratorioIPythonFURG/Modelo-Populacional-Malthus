#Definindo o modelo populacional
def modelo_montroll(t,P):
    L = 218858
    k = 0.004
    l = 107.83
    return  k*P*(1-(P/L)**l)
