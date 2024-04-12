pessoas = [('Lisboa', 'LIS'),
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'),
           ('Dublin', 'DUB'),
           ('Bruxelas', 'BRU'),
           ('Londres', 'LHR')]
print(pessoas[5][1])
destino = 'FCO'

voos = {('CDG', 'DUB'): ['13:37', '14:49', 176]}

for linha in open("flights.txt"):
    origem, destino, saida, chegada, preco = linha.split(',')
    voos.setdefault((origem, destino), [])
    voos[(origem, destino)].append([saida, chegada, int(preco)])

for voo in voos:
    print(voo)
    print(voos[voo])