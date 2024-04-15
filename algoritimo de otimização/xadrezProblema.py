"""O problema das 8 rainhas consiste no poscionamento das rainhas em um tabuleiro de xadrez, que podem atacar na diagonal, horizontal e vertical a qualquer distância,
de tal forma que elas não possam atacar uma a outra. A melhor forma de resolver esse problema é cada coluna tendo apenas uma rainha posicionada
e que a a coluna anterior e posterior a rainha não tenha nenhuma rainha posta a sua horizontal, vertical ou diagonal.
Assim, podemos representar o problema em um vetor simples em que cada posição indica o posicionamento de cada rainha no tabuleiro.
Foi utilizado a função discreta da biblioteca mlrose, já que o resultado é uma sequência de valores inteiro em que cada posição tem um determinado
conjunto de valores que ele pode assumir.
"""

import mlrose

def custoRainha(tabuleiro):
    custo = 0

    for i in range(len(tabuleiro) - 1):
        for j in (i + 1, len(tabuleiro)):
            if (tabuleiro[i] != tabuleiro[j] and 
                tabuleiro[j] != tabuleiro[i] + (j - i) and
                tabuleiro[j] != tabuleiro[i] - (j - i)):
                custo += 1
    
    return custo

fitness = mlrose.CustomFitness(custoRainha)
problema = mlrose.DiscreteOpt(8, fitness_fn=fitness, maximize=False, max_val=8)