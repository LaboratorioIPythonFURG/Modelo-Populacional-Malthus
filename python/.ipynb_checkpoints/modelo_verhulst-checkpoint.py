#Definindo o modelo populacional
def modelo_verhulst(t,P):
    L = 300000
    k = 0.01553891418938226
    return  (k*(1-P/L))*P
