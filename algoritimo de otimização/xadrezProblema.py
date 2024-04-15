"""O problema das 8 rainhas consiste no poscionamento das rainhas em um tabuleiro de xadrez, que podem atacar na diagonal, horizontal e vertical a qualquer distância,
de tal forma que elas não possam atacar uma a outra. A melhor forma de resolver esse problema é cada coluna tendo apenas uma rainha posicionada
e que a coluna anterior e posterior a rainha não tenha nenhuma rainha colocada a sua horizontal, vertical ou diagonal.
Assim, podemos representar o problema em um vetor simples em que cada posição indica o posicionamento de cada rainha no tabuleiro.
A bilioteca mlrose vai forncecer os algoritimos necessários para a otimização."
"""

import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
import numpy as np

def custoRainha(tabuleiro):
    custo = 0

    for i in range(len(tabuleiro) - 1):
        for j in (i + 1, len(tabuleiro) - 1):
            if ((tabuleiro[j] == tabuleiro[i]) 
                or (tabuleiro[j] == tabuleiro[i] + (j - i))
                or (tabuleiro[j] == tabuleiro[i] - (j - i))):
                custo += 1
    
    return custo

tabuleiro = np.zeros((8, 8), dtype=str)
tabuleiro[0:8, 0:8] = "*"


fitness = mlrose.CustomFitness(custoRainha)
problema = mlrose.DiscreteOpt(length=8, fitness_fn=fitness, maximize=False, max_val=8)
melhorSolucao, melhorCusto = mlrose.hill_climb(problema)

print(melhorSolucao)
print(melhorCusto)

for i in range(len(melhorSolucao) - 1):
    tabuleiro[melhorSolucao[i]][i] = "8"

quantidadeLinhas = int(tabuleiro.size/len(tabuleiro[0]))

for i in range(quantidadeLinhas - 1):
    for j in range(len(tabuleiro[0]) - 1):
        print(tabuleiro[i][j], end=" ")
    print()