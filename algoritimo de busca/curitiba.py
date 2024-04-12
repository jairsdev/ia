class Vertice:
    def __init__(self, rotulo, distanciaObjetivo):
        self.rotulo = rotulo
        self.distanciaObjetivo = distanciaObjetivo
        self.adjacentes = []
        self.visitado = False

    def inserirAdjacente(self, adjacente):
        self.adjacentes.append(adjacente)
    
class Adjacente:
    def __init__(self, vertice, custo):
        self.custo = custo
        self.vertice = vertice
        self.custoAEstrela = self.custo + vertice.distanciaObjetivo

class Grafo:
    portoUniao = Vertice('Porto União', 203)
    pauloFrontin = Vertice('Paulo Frontin', 172)
    canoinhas = Vertice('Canoinhas', 141)
    tresBarras = Vertice('Três Barras', 131)
    saoMateusSul = Vertice('São Mateus do Sul', 123)
    irati = Vertice('Irati', 139)
    curitiba = Vertice('Curitiba', 0)
    palmeira = Vertice('Palmeira', 59)
    mafra = Vertice('Mafra', 94)
    campoLargo = Vertice('Campo Largo', 27)
    balsaNova = Vertice('Balsa Nova', 41)
    lapa = Vertice('Lapa', 74)
    tijucasSul = Vertice('Tijucas do Sul', 56)
    araucaria = Vertice('Araucária', 23)
    saoJosePinhas = Vertice('São José dos Pinhais', 13)
    contenda = Vertice('Contenda', 39)

    portoUniao.inserirAdjacente(Adjacente(pauloFrontin, 46))
    portoUniao.inserirAdjacente(Adjacente(canoinhas, 78))
    portoUniao.inserirAdjacente(Adjacente(saoMateusSul, 87))

    pauloFrontin.inserirAdjacente(Adjacente(portoUniao, 46))
    pauloFrontin.inserirAdjacente(Adjacente(irati, 75))

    canoinhas.inserirAdjacente(Adjacente(portoUniao, 78))
    canoinhas.inserirAdjacente(Adjacente(tresBarras, 12))
    canoinhas.inserirAdjacente(Adjacente(mafra, 66))

    tresBarras.inserirAdjacente(Adjacente(canoinhas, 12))
    tresBarras.inserirAdjacente(Adjacente(saoMateusSul, 43))

    saoMateusSul.inserirAdjacente(Adjacente(tresBarras, 43))
    saoMateusSul.inserirAdjacente(Adjacente(portoUniao, 87))
    saoMateusSul.inserirAdjacente(Adjacente(irati, 57))
    saoMateusSul.inserirAdjacente(Adjacente(lapa, 60))
    saoMateusSul.inserirAdjacente(Adjacente(palmeira, 77))

    irati.inserirAdjacente(Adjacente(pauloFrontin, 75))
    irati.inserirAdjacente(Adjacente(palmeira, 75))

    curitiba.inserirAdjacente(Adjacente(campoLargo, 29))
    curitiba.inserirAdjacente(Adjacente(balsaNova, 51))
    curitiba.inserirAdjacente(Adjacente(araucaria, 37))
    curitiba.inserirAdjacente(Adjacente(saoJosePinhas, 15))

    palmeira.inserirAdjacente(Adjacente(irati, 75))
    palmeira.inserirAdjacente(Adjacente(campoLargo, 55))
    palmeira.inserirAdjacente(Adjacente(saoMateusSul, 77))

    mafra.inserirAdjacente(Adjacente(canoinhas, 66))
    mafra.inserirAdjacente(Adjacente(lapa, 57))
    mafra.inserirAdjacente(Adjacente(tijucasSul, 99))

    campoLargo.inserirAdjacente(Adjacente(palmeira, 55))
    campoLargo.inserirAdjacente(Adjacente(balsaNova, 22))
    campoLargo.inserirAdjacente(Adjacente(curitiba, 29))

    balsaNova.inserirAdjacente(Adjacente(campoLargo, 22))
    balsaNova.inserirAdjacente(Adjacente(contenda, 19))
    balsaNova.inserirAdjacente(Adjacente(curitiba, 51))

    lapa.inserirAdjacente(Adjacente(contenda, 26))
    lapa.inserirAdjacente(Adjacente(mafra, 57))
    lapa.inserirAdjacente(Adjacente(saoMateusSul, 60))

    tijucasSul.inserirAdjacente(Adjacente(mafra, 99))
    tijucasSul.inserirAdjacente(Adjacente(saoJosePinhas, 49))

    araucaria.inserirAdjacente(Adjacente(contenda, 18))
    araucaria.inserirAdjacente(Adjacente(curitiba, 37))

    saoJosePinhas.inserirAdjacente(Adjacente(curitiba, 15))
    saoJosePinhas.inserirAdjacente(Adjacente(tijucasSul, 49))

    contenda.inserirAdjacente(Adjacente(lapa, 26))
    contenda.inserirAdjacente(Adjacente(balsaNova, 19))
    contenda.inserirAdjacente(Adjacente(araucaria, 18))

import numpy as np
class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = np.empty(self.capacidade, dtype=object)

    def inserir(self, adjacente):
        if (self.ultimaPosicao == self.capacidade):
            print("Capacidade máxima atingida!!!")
            return
        posicao = 0
        for i in range(self.ultimaPosicao + 1):
            if (adjacente.custoAEstrela < self.valores[i].custoAEstrela):
                posicao = i
                break
            if (i == self.ultimaPosicao):
                posicao = self.ultimaPosicao + 1
        x = self.ultimaPosicao
        while (x >=  posicao): 
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = adjacente
        self.ultimaPosicao += 1

    def imprimir(self):
        if (self.ultimaPosicao == -1):
            print("O vetor está vázio!!!")
            return
        for i in range(self.ultimaPosicao + 1):
            print(i, ' - ', self.valores[i].vertice.rotulo, self.valores[i].custo, self.valores[i].vertice.distanciaObjetivo, self.valores[i].custoAEstrela)

class BuscaAEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False
    
    def buscar(self, atual):
        print('Atual: {}'.format(atual.rotulo))
        if (atual == self.objetivo):
            self.encontrado = True
            return

        adjacentes = VetorOrdenado(len(atual.adjacentes))
        for adjacente in atual.adjacentes:
            if (adjacente.vertice.visitado == False):
                adjacente.vertice.visitado = True
                adjacentes.inserir(adjacente)
        adjacentes.imprimir()
        if (adjacentes.valores[0] != None):
            self.buscar(adjacentes.valores[0].vertice)

grafo = Grafo()
busca = BuscaAEstrela(grafo.curitiba)
busca.buscar(grafo.portoUniao)