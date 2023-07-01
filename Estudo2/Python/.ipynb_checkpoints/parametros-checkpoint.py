import numpy as np
from scipy.optimize import curve_fit

def polinomio(x,a,b,c):
    return a*x**3+b*x**2+c*x

def r_Malthus(P0,Pt,t): #P0: População inicial; Pt: População no ano t; t: ano, t>0.
    return (1/t)*np.log(Pt/P0)

def K_Verhulst(P0,P1,P2): #Pi com i=1,2,3: Populações igualmente espaçadas em T anos.
    return P1*(P0*P1+P1*P2-2*P0*P2)/(P1**2-P0*P2)

def r_Verhulst(P0,P1,K,T): #Pi com i=1,2,3: Populações igualmente espaçadas em T anos; K: Capacidade suporte.
    return (1/T)*np.log((1/P0-1/K)/(1/P1-1/K))

def tm(f,x,y):
    return curve_fit(f, x, y)
    