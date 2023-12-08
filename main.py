from calcTempExec import calcTempExec
from casamentoDeCadeiasForçaBruta import casamentoForcaBruta
from plotGraphResults import plotGraphResults

# Banco de testes

texto = "ACTG"
padrao = "CTGA"
tamanhos = [1000, 2000, 5000, 10000, 50000, 100000, 200000, 500000, 800000, 1000000]  # Tamanhos diferentes de dados para testar
tempoExecList = []

for tamanho in tamanhos: # 10 testes
    textTam = texto * tamanho
    alg, tempExec = calcTempExec(casamentoForcaBruta, textTam, len(textTam), padrao, len(padrao))
    tempoExecList.append(tempExec)

plotGraphResults(tamanhos, tempoExecList)