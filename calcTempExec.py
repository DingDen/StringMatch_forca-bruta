import time

def calcTempExec(algoritmo, *args):
    inicio = time.time()
    alg = algoritmo(*args)
    final = time.time()
    tempo_exec = final - inicio

    return alg, tempo_exec 