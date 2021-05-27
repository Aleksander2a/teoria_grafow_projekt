# Teoria grafów - metoda Forda-Fulkersona - projekt

## A. Część analityczna
- Odpowiedzi do zadań z części analitycznej znajdują się w pliku **czesc_analityczna_aleksander_mazur.pdf** w katalogu **czesc_analityczna/**

## B. Część programistyczna
### 1. Analiza algorytmu
- Informacje o algorytmie znajdują się w pliku **informacje_o_algorytmie.docx** w katalogu **czesc_programistyczna/**
### 2. Implementacja
- Wszystko co związane z implementacją jest zawarte w katalogu **czesc_programistyczna/metoda_forda_fulkersona/**
#### 2.1. Format danych wejściowych 
- Program wczytuje pliki zapisane w formacie JSON
- Dane dostarczane są w postaci zmodyfikowanej macierzy sąsiedztwa, zawierającej informacje o wagach krawędzi pomiędzy wierzchołkami
Wartość w *i*-tym wierszu i *j*-tej kolumnie jest wagą krawędzi prowadzącej od wierzchołka *i* do wierzchołka *j* (0 oznacza brak krawędzi)

Przykładowy graf: 
<img align="center" width="200" height="200" src="https://github.com/Aleksander2a/teoria_grafow_projekt/blob/main/przyklad_grafu.jpg">

<p align="right">
Reprezentacja macierzowa tego grafu wygląda następująco: 
| Wierzchołki | 0 | 1 | 2 |
|-------------|---|---|---|
|      0      | 0 | 3 | 1 |
|      1      | 0 | 0 | 4 |
|      2      | 0 | 0 | 0 |
  </p>

Linux:
W razie konieczności zmienić sieżkę do interpretera pythona (plik algorytm.py, linijka 1)
chmod +x algorytm.py
pip install -r requirements.txt
./algorytm.py
