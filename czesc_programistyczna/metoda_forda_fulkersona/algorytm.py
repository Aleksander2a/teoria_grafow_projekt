import json
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

blad = True
while blad:
    try:
        # plik = input("Podaj nazwe pliku z danymi: ")
        with open('przyklad.json') as json_file:
            m_sasiedztwa = json.load(json_file)
            blad = False
    except FileNotFoundError:
        print("Nie ma takiego pliku, sprobuj ponownie")
        blad = True

m_sasiedztwa = np.array(m_sasiedztwa)
print(m_sasiedztwa)

graf = nx.DiGraph()
for i in range(m_sasiedztwa.shape[0]):
    graf.add_node(i, index=i)
print(graf.nodes)

for i in range(m_sasiedztwa.shape[0]):
    for j in range(m_sasiedztwa.shape[1]):
        if m_sasiedztwa[i][j] != 0:
            graf.add_weighted_edges_from([(i, j, m_sasiedztwa[i][j])])
            graf[i][j]["przeplyw"] = 0                                  # inicjalizajca przeplywu krawedzi
            graf[i][j]["poczatek"] = i
            graf[i][j]["koniec"] = j

print(graf.edges)
# print(list(graf.successors(0)))
nx.draw_spectral(graf, with_labels=True, font_weight='bold')
# plt.subplot(122)
# nx.draw_shell(graf, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
plt.show()


def nodes(g):
    return list(g.nodes)

def edges(g):
    return list(g.edges)

wierzcholki = nodes(graf)

krawedzie = edges(graf)

ilosc_wierzcholkow = m_sasiedztwa.shape[0]

# print(wierzcholki[1])
# print(krawedzie[0]['weight'])
# print(krawedzie[1])
# print(graf[0][2])

zrodlo = graf[0]
ujscie = graf[6]

# siec_residualna.add_node(10)
# print(nodes(graf))
# print(graf[0][1]['weight'])

# def przeciwna_krawedz_X(edge):
#     return edge[0]
#
#
# def przeciwna_krawedz_Y(edge):
#     return edge[1]
#
#
przepustowosc_residualna = [[0]*ilosc_wierzcholkow]*ilosc_wierzcholkow
przepustowosc_residualna = np.array(przepustowosc_residualna)

def przepustowosc_residualna_licz(graph):
    for i in range(ilosc_wierzcholkow):
        for j in range(ilosc_wierzcholkow):
            if (i, j) in graph.edges:
                przepustowosc_residualna[i][j] = graph[i][j]['weight'] - graph[i][j]['przeplyw']
            elif (j, i) in graph.edges:
                przepustowosc_residualna[i][j] = graph[j][i]['przeplyw']
            else:
                przepustowosc_residualna[i][j] = 0


przepustowosc_residualna_licz(graf)
print(przepustowosc_residualna)

def stworz_siec_residualna():
    graph = nx.DiGraph()
    for i in range(przepustowosc_residualna.shape[0]):
        graph.add_node(i, index=i)

    for i in range(przepustowosc_residualna.shape[0]):
        for j in range(przepustowosc_residualna.shape[1]):
            if przepustowosc_residualna[i][j] != 0:
                graph.add_weighted_edges_from([(i, j, przepustowosc_residualna[i][j])])
                # graph[i][j]["przeplyw"] = 0  # inicjalizajca przeplywu krawedzi
                graph[i][j]["poczatek"] = i
                graph[i][j]["koniec"] = j

