"""O problema consiste na escolha de quais produtos serão escolhidos para um caminhão carregar pensando no maior lucro.
Algumas informações importantes:
O caminhão tem 3m³ de capacidade.
A soma dos volumes dos produtos é 4.79m³.
A solução será um vetor em que cada índice será relacionado a um produto considerando a ordem do dicionário que possui as informações dos produtos.
Cada posição no vetor da solução vai assumir valores de 0 ou 1, 0 para não colocar no caminhão e 1 caso o contrário.
"""
import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose

produtos = {}
def adicionarProdutos(nome, volume, preco):
    produtos.setdefault(nome, [])
    produtos[nome].append([volume, preco])

adicionarProdutos("Refrigerador A", 0.751, 999.90)
adicionarProdutos("Nootebook A", 0.00350, 2499.90)
adicionarProdutos("Microondas C", 0.0319, 299.29)
adicionarProdutos("Notebook C", 0.527, 3999)
adicionarProdutos("Celular", 0.0000899, 2199.12)
adicionarProdutos("Ventilador", 0.496, 199.90)
adicionarProdutos("Refrigerador B", 0.635, 849)
adicionarProdutos("TV 55'", 0.400, 4346.99)
adicionarProdutos("TV 50'", 0.290, 3999.90)
adicionarProdutos("Microondas A", 0.0424, 308.66)
adicionarProdutos("Refrigerado C", 0.870, 1199.89)
adicionarProdutos("TV 42'", 0.200, 2999.90)
adicionarProdutos("Microondas B", 0.0544, 429.90)
adicionarProdutos("Notebook B", 0.498, 1999.90)

def fitness(solucao):
    posicao = -1
    precoTotal = 0
    volumeTotal = 0
    for produto in produtos:
        posicao += 1
        if (solucao[posicao] == 1):
            precoTotal += produtos[produto][0][1]
            volumeTotal += produtos[produto][0][0]

    if (volumeTotal > 3):
        return -1
    return precoTotal

def imprimirProdutos(solucao):
    posicao = -1
    for produto in produtos:
        posicao += 1
        if (solucao[posicao] == 1):
            print(produto)
            print(produtos[produto][0][0])
            print(produtos[produto][0][1])
            print("-----------------")


fitness = mlrose.CustomFitness(fitness)
problema = mlrose.DiscreteOpt(length=14, fitness_fn=fitness, maximize=True, max_val=2)

melhorSolucao, maiorCusto = mlrose.hill_climb(problema, random_state=3)
imprimirProdutos(melhorSolucao)
print(maiorCusto)

melhorSolucao, maiorCusto = mlrose.simulated_annealing(problema, mlrose.decay.GeomDecay(10000), random_state=3)
imprimirProdutos(melhorSolucao)
print(maiorCusto)

melhorSolucao, maiorCusto = mlrose.genetic_alg(problema)
imprimirProdutos(melhorSolucao)
print(maiorCusto)
