import matplotlib.pyplot as plt

def plotGraphResults(tamanho, tempoExec):
    plt.plot(tamanho, tempoExec, marker='o')
    plt.title("Casamento de cadeia força-bruta")
    plt.xlabel("Tamanho da entrada de dados")
    plt.ylabel("Tempo de execução (segundos)")
    plt.show()