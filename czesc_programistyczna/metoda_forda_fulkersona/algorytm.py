import json
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

blad = True
while blad:
    try:
        plik = input("Podaj nazwe pliku z danymi: ")
        with open(plik) as json_file:
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
# graf.add_nodes_from(range(m_sasiedztwa.shape[0]))
print(graf.nodes)

for i in range(m_sasiedztwa.shape[0]):
    for j in range(m_sasiedztwa.shape[1]):
        if m_sasiedztwa[i][j] != 0:
            graf.add_weighted_edges_from([(i, j, m_sasiedztwa[i][j])])

print(graf.edges)
# print(list(graf.successors(0)))
nx.draw_spectral(graf, with_labels=True, font_weight='bold')
# plt.subplot(122)
# nx.draw_shell(graf, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
plt.show()
