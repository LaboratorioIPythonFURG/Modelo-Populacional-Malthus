import numpy as np
import scipy.integrate as sciInt

from sol_euler import sol_euler
from sol_euler_mod import sol_euler_mod
from sol_rk4 import sol_rk4

from modelo_malthus import modelo_malthus
from modelo_verhulst import modelo_verhulst

def menor_passo(ti,tf,h,decrescimo,P0,solucao_IBGE ,dados,metodo,modelo):
    
    err = 0
    err_perc = 0
    P = 0
    trava = False

    #excede while err>3194:
    while trava==False and h>0:
        #try:
        #passo
        h = h - decrescimo

        print('- Iteração. Passo atual (h): ',h)

        if (h<0):
            print('passo negativo:',h)
            h = h + decrescimo
            trava=True
             #break
        else:

            #vetor tempo
            vt = np.arange(ti,tf,h)

            if metodo == 'Euler':

                #solução
                P = sol_euler(vt,P0,modelo)

            elif metodo == 'Euler Modificado':

                #solução
                P = sol_euler_mod(vt,P0,modelo)

            elif metodo == 'RK4':

                #solução
                P = sol_rk4(vt,P0,modelo)
                
            elif metodo == 'LSODA' and modelo=='malthus':
                
                P = sciInt.odeint(modelo_malthus, y0=P0, t=vt, tfirst=True)                
                
            elif metodo == 'RK45' and modelo=='malthus':
                
                P = sciInt.solve_ivp(modelo_malthus, t_span=(0,max(vt)), y0=[P0], t_eval=vt)
                P = P.y[0]
                
            elif metodo == 'LSODA' and modelo == 'verhulst':
                
                P = sciInt.odeint(modelo_verhulst, y0=P0, t=vt, tfirst=True)
                
            elif metodo == 'RK45' and modelo == 'verhulst'

                P = sciInt.solve_ivp(modelo_verhulst, t_span=(0,max(vt)), y0=[P0], t_eval=vt)
                P = P.y[0]
            
            else:
                print('O nome do método foi digitado incorretamente')
                #break

        #erro abs      
        err = solucao_IBGE - np.amax(P)

        #erro percentual
        err_perc = (err/solucao_IBGE)*100

    print('Erro absoluto (hab): ',err)
    print('Erro absoluto arredondado (hab): ',round(err,0))
    print('Erro percentual arredondado {}%'.format(round(err_perc,2)))
    print('Erro percentual {}%'.format(err_perc))
    print('Passo atual: ',h)

 
    dados = np.vstack([dados,[metodo,h,round(err),str(round(err_perc,2))+'%']])
    
    return dados