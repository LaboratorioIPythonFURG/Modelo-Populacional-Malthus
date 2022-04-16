import json

arquivos = ['pt1_introducao','pt2_sympy_scipy','pt3_euler','pt4_euler_modificado','pt5_RK4','pt6_comparativo']

with open('./jupyter/{}.ipynb'.format(arquivos[0])) as arquivo_base:
    
    dados = json.load(arquivo_base)

del arquivos[0]

for arquivo in arquivos:
    
    with open('./jupyter/{}.ipynb'.format(arquivo)) as arquivo_nb:
        
        dados_acrescentar = json.load(arquivo_nb)
        dados['cells'] += dados_acrescentar['cells']

with open('./Problema_Resfriamento.ipynb','w') as arquivo_principal:
    json.dump(dados,arquivo_principal,ensure_ascii=False)


