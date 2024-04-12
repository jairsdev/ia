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

agenda = [1,2, 3,2, 7,3, 6,3, 2,4, 5,3]

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

imprimirVoos(agenda)
