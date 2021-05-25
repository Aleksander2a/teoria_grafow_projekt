import json
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

blad = True
while blad:
    try:
        # plik = input("Podaj nazwe pliku z danymi: ")
        with open('przyklad2.json') as json_file:
            m_sasiedztwa = json.load(json_file)
            blad = False
    except FileNotFoundError:
        print("Nie ma takiego pliku, sprobuj ponownie")
        blad = True

m_sasiedztwa = np.array(m_sasiedztwa)
# print(m_sasiedztwa)

graf = nx.DiGraph()
for i in range(m_sasiedztwa.shape[0]):
    graf.add_node(i)

# print(graf.nodes)

for i in range(m_sasiedztwa.shape[0]):
    for j in range(m_sasiedztwa.shape[1]):
        if m_sasiedztwa[i][j] != 0:
            graf.add_weighted_edges_from([(i, j, m_sasiedztwa[i][j])])
            graf[i][j]["przeplyw"] = 0                                  # inicjalizajca przeplywu krawedzi
            graf[i][j]["poczatek"] = i
            graf[i][j]["koniec"] = j

# print(graf.edges)
# print(list(graf.successors(0)))
nx.draw_spectral(graf, with_labels=True, font_weight='bold')
# plt.subplot(122)
# nx.draw_shell(graf, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
# plt.show()



wierzcholki = list(graf.nodes)

krawedzie = list(graf.edges)

ilosc_wierzcholkow = m_sasiedztwa.shape[0]

# print(wierzcholki[1])
# print(krawedzie[0]['weight'])
# print(krawedzie[1])
# print(graf[0][2])

zrodlo = 0
ujscie = m_sasiedztwa.shape[0] - 1

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


# przepustowosc_residualna_licz(graf)
# print(przepustowosc_residualna)

def stworz_siec_residualna():
    graph = nx.DiGraph()
    for i in range(przepustowosc_residualna.shape[0]):
        graph.add_node(i)

    for i in range(przepustowosc_residualna.shape[0]):
        for j in range(przepustowosc_residualna.shape[1]):
            if przepustowosc_residualna[i][j] != 0:
                graph.add_weighted_edges_from([(i, j, przepustowosc_residualna[i][j])])
                graph[i][j]["przeplyw"] = 0  # inicjalizajca przeplywu krawedzi
                graph[i][j]["poczatek"] = i
                graph[i][j]["koniec"] = j
    return graph


# print(list(graf.predecessors(6)))
    # index = zrodlo
    # przepustowosc_residualna_licz(graf)
    # siec_residualna = stworz_siec_residualna()
    # visited = []
    # visited.append(zrodlo)
    # bottlnecks_values = []
    # while index != ujscie:
    #     nastepni = list(siec_residualna.successors(index))
    #     for i in nastepni:
    #         if przepustowosc_residualna[index][i] > 0 and i not in visited:
    #             bottlnecks_values.append(przepustowosc_residualna[index][i])
    #             index = i
    #             visited.append(i)
    #             break
    #
    # odwiedzone = visited
    # return min(bottlnecks_values)
# print("-------------------------")
# x = max_przeplyw()
# print(x)
# sciezki = []
# for i in nx.all_simple_paths(graf, zrodlo, ujscie):
#     print(i)
#     sciezki.append(i)
# print("min")
# print(min(sciezki))
def znajd_sciezke(G):
    sciezka = []
    wszystkie_sciezki = []
    minim_dlugosc = 10000
    for i in nx.all_simple_paths(G, zrodlo, ujscie):
        wszystkie_sciezki.append(i)
        if len(i) < minim_dlugosc:
            minim_dlugosc = len(i)
            sciezka = i
    return sciezka
# przepustowosc_residualna_licz(graf)
# siec = stworz_siec_residualna()
# print("+++++++++++++++++")
# print(znajd_sciezke(siec))
def find_bottle_neck(sciezka):
    istnieje = True
    bottle_necks = []
    while istnieje:
        p = sciezka
        if not p:
            istnieje = False
        index = 0
        while index < len(p) - 1:
            bottle_necks.append(przepustowosc_residualna[p[index]][p[index+1]])
            index += 1
        return min(bottle_necks)
    return 0


def max_flow(G):
    istnieje = True
    min_bottle_necks = []
    while istnieje:
        przepustowosc_residualna_licz(graf)
        siec_residualna = stworz_siec_residualna()
        sciezka = znajd_sciezke(siec_residualna)
        if not sciezka:
            istnieje = False
        else:
            bottle_neck = find_bottle_neck(sciezka)
            min_bottle_necks.append(bottle_neck)
            index = 0
            while index < len(sciezka) - 1:
                if m_sasiedztwa[sciezka[index]][sciezka[index+1]] > 0:
                    G[sciezka[index]][sciezka[index+1]]['przeplyw'] += bottle_neck
                else:
                    G[sciezka[index+1]][sciezka[index]]['przeplyw'] -= bottle_neck
                index += 1
    suma = 0
    for i in min_bottle_necks:
        suma += i
    return suma

x = max_flow(graf)
print("MAX: ")
print(x)
