pessoas = [('Lisboa', 'LIS'),
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'),
           ('Dublin', 'DUB'),
           ('Bruxelas', 'BRU'),
           ('Londres', 'LHR')]
destino = 'FCO'

voos = {}
for linha in open("flights.txt"):
    origem, destino, saida, chegada, preco = linha.split(',')
    voos.setdefault((origem, destino), [])
    voos[(origem, destino)].append([saida, chegada, int(preco)])

def imprimirVoos(agenda):
    idVoo = -1
    custoTotal = 0
    for i in range(len(agenda) // 2):
        cidade = pessoas[i][0]
        origem = pessoas[i][1]
        idVoo += 1
        vooIda = voos[(origem, destino)][agenda[idVoo]]
        custoTotal += vooIda[2]

        idVoo += 1
        vooVolta = voos[(destino, origem)][agenda[idVoo]]
        custoTotal += vooVolta[2]

        print('%10s%10s %5s-%5s %3s %5s-%5s %3s' % (cidade, origem, vooIda[0], vooIda[1], vooIda[2], vooVolta[0], vooVolta[1], vooVolta[2]))
    print(custoTotal)

def fitness(agenda):
    idVoo = -1
    custoTotal = 0
    for i in range(len(agenda) // 2):
        cidade = pessoas[i][0]
        origem = pessoas[i][1]
        idVoo += 1
        vooIda = voos[(origem, destino)][agenda[idVoo]]
        custoTotal += vooIda[2]

        idVoo += 1
        vooVolta = voos[(destino, origem)][agenda[idVoo]]
        custoTotal += vooVolta[2]
    return custoTotal

import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose

fitness = mlrose.CustomFitness(fitness)
problema = mlrose.DiscreteOpt(length=12, fitness_fn=fitness, maximize=False, max_val=10)

melhorSolucao, melhorCusto = mlrose.hill_climb(problema)
imprimirVoos(melhorSolucao)

