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

def find_bottleneck_on_augmenting_path(odwiedzone, graph):
    index = zrodlo
    visited = []
    visited.append(index)
    queue = []
    queue.append(index)
    while queue:
        index = queue[0]
        queue.pop(0)
        if index == ujscie:
            break
        nastepni = list(graph.successors(index))
        for node in nastepni:
            if przepustowosc_residualna[index][node] > 0 and node not in visited:
                visited.append(node)
                queue.append(node)
    if ujscie not in visited:
        return 0
    bottle_neck = 100000
    v = ujscie
    size = len(visited) - 2
    while size >= 0:
        if przepustowosc_residualna[visited[size]][visited[size+1]] > 0:
            if visited[size+1] not in odwiedzone:
                odwiedzone.append(visited[size+1])
            if visited[size] not in odwiedzone:
                odwiedzone.append(visited[size])
            bottle_neck = min(bottle_neck, przepustowosc_residualna[visited[size]][visited[size+1]])
    odwiedzone = odwiedzone.reverse()
    return bottle_neck


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

def max_przeplyw():
    istnieje = True
    bottle_necks = []
    while istnieje:
        odwiedzone = []
        przepustowosc_residualna_licz(graf)
        siec =stworz_siec_residualna()
        wartosc = find_bottleneck_on_augmenting_path(odwiedzone, siec)
        if wartosc == 0:
            istnieje = False
        bottle_necks.append(wartosc)
        for i in odwiedzone:
            if i != ujscie:
                nastepni = list(graf.successors(i))
                if (i+1) in nastepni:
                    graf[i][i+1]['przeplyw'] += wartosc
                else:
                    graf[i+1][i]['przeplyw'] -= wartosc
        odwiedzone.clear()
    max_flow = 0
    for i in bottle_necks:
        max_flow += i
    return max_flow


# x = max_przeplyw()
# print(x)

