# Algoritmo força-bruta 

def casamentoForcaBruta(texto, tamanho_texto:int, padrao: str, tamanho_padrao:int) -> int:
    pos = []
    for i in range(0, tamanho_texto - tamanho_padrao + 1):
        j = 0
        while j < tamanho_padrao and texto[i + j] == padrao[j]:
            j += 1
        if j == tamanho_padrao: # Correspondência Encontrada
            pos.append(i)
        
    return pos
