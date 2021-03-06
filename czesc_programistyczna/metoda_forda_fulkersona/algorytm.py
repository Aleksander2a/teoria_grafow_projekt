#!/usr/bin/python3

import json
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

print("\nWitaj w programie do obliczania maksymalnego przepływu w grafie!!!\nGotowe przykłady to:\nprzyklad1.json   przyklad2.json   przyklad3.json")

blad = True
while blad:
    try:
        plik = input("Wybierz jeden z gotowych plików lub podaj nazwę własnego pliku z danymi: ")
        with open(plik) as json_file:
            m_sasiedztwa = json.load(json_file)
            blad = False
    except FileNotFoundError:
        print("Nie ma takiego pliku, sprobuj ponownie")
        blad = True

m_sasiedztwa = np.array(m_sasiedztwa)

graf = nx.DiGraph()
for i in range(m_sasiedztwa.shape[0]):
    graf.add_node(i)

for i in range(m_sasiedztwa.shape[0]):
    for j in range(m_sasiedztwa.shape[1]):
        if m_sasiedztwa[i][j] != 0:
            graf.add_weighted_edges_from([(i, j, m_sasiedztwa[i][j])])
            graf[i][j]["przeplyw"] = 0                                  # inicjalizajca przeplywu krawedzi

ilosc_wierzcholkow = m_sasiedztwa.shape[0]

zrodlo = 0
ujscie = m_sasiedztwa.shape[0] - 1

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


def stworz_siec_residualna(macierz):
    graph = nx.DiGraph()
    for i in range(macierz.shape[0]):
        graph.add_node(i)

    for i in range(macierz.shape[0]):
        for j in range(macierz.shape[1]):
            if macierz[i][j] != 0:
                graph.add_weighted_edges_from([(i, j, macierz[i][j])])
                graph[i][j]["przeplyw"] = 0
    return graph


def znajd_sciezke(G):
    sciezka = []
    wszystkie_sciezki = []
    minim_dlugosc = 10000
    for i in nx.all_simple_paths(G, zrodlo, ujscie):
        wszystkie_sciezki.append(i)
        if len(i) < minim_dlugosc:                  # wybór najkrótszej ścieżki
            minim_dlugosc = len(i)
            sciezka = i
    return sciezka


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
        siec_residualna = stworz_siec_residualna(przepustowosc_residualna)
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

macierz_przeplywu = [[0]*ilosc_wierzcholkow]*ilosc_wierzcholkow
macierz_przeplywu = np.array(macierz_przeplywu)
for i in range(macierz_przeplywu.shape[0]):
    for j in range(macierz_przeplywu.shape[1]):
        if m_sasiedztwa[i][j] != 0:
            macierz_przeplywu[i][j] = graf[i][j]['przeplyw']

print(0, "- Źródło   ", ilosc_wierzcholkow-1, "- Ujście")

print("Macierz sąsiedztwa z wartościami przepływu/przepustowości dla danego grafu to: ")

my_table = PrettyTable()
naglowki = []
naglowki.append("Wierzchołki")
for i in graf.nodes:
    naglowki.append(str(i))
my_table.field_names = naglowki
row = []
for i in range(ilosc_wierzcholkow):
    row.append(str(i))
    for j in range(ilosc_wierzcholkow):
        row.append(str(macierz_przeplywu[i][j]) + "/" + str(m_sasiedztwa[i][j]))
    my_table.add_row(row)
    row.clear()
print(my_table)

pos = nx.spectral_layout(graf)

labels = {}
for edge in list(graf.edges):
    labels[edge] = str(graf[edge[0]][edge[1]]['przeplyw']) + "/" + str(graf[edge[0]][edge[1]]['weight'])

print("Maksymalny przeplyw w danym grafie wynosi: ", x)

nx.draw_networkx_nodes(graf, pos)
nx.draw_networkx_labels(graf, pos)
nx.draw_networkx_edges(graf, pos)

nx.draw_networkx_edge_labels(graf, pos, label_pos=0.5, edge_labels=labels)
plt.show()
