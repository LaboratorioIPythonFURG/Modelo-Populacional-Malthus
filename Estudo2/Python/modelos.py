def Malthus(P,params):
    return params['r']*P

def Verhulst(P,params):
    return  (params['r']*(1-P/params['K']))*P

def Montroll(t,P):
    L = 218858
    k = 0.004
    l = 107.83
    return  k*P*(1-(P/L)**l)