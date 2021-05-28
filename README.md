# Teoria grafów - metoda Forda-Fulkersona - projekt

## A. Część analityczna
- Odpowiedzi do zadań z części analitycznej znajdują się w pliku **czesc_analityczna_aleksander_mazur.pdf** w katalogu **czesc_analityczna/**

## B. Część programistyczna
### 1. Analiza algorytmu
- Informacje o algorytmie znajdują się w pliku **informacje_o_algorytmie.docx** w katalogu **czesc_programistyczna/**
### 2. Implementacja
- Wszystko co związane z implementacją jest zawarte w katalogu **czesc_programistyczna/metoda_forda_fulkersona/**
#### 2.1. Działanie programu
Program wczytuje z wybranego pliku dane opisujące graf, następnie podaje maksymalny przepływ w grafie oraz szczegółowe informacje dotyczące przepływu i przepustowości każdej krawędzi zawarte w specjalnej macierzy sąsiedztwa, w osobnym oknie pojawia się też wygenerowany szkic grafu 
#### 2.2. Format danych wejściowych 
- Program wczytuje pliki zapisane w formacie JSON
- Dane dostarczane są w postaci zmodyfikowanej macierzy sąsiedztwa, zawierającej informacje o wagach krawędzi pomiędzy wierzchołkami.
Wartość w *i*-tym wierszu i *j*-tej kolumnie jest wagą krawędzi prowadzącej od wierzchołka *i* do wierzchołka *j* (0 oznacza brak krawędzi)

**!!!** Zawsze należy pamiętać, że **źródło** jest **pierwszym (0)** wierzchołkiem, a **ujście ostatnim** **!!!**

Przykładowy graf: 
<img align="center" width="200" height="200" src="https://github.com/Aleksander2a/teoria_grafow_projekt/blob/main/przyklad_grafu.jpg">

Reprezentacja macierzowa tego grafu wygląda następująco: 
| Wierzchołki | 0 | 1 | 2 |
|-------------|---|---|---|
|      0      | 0 | 3 | 1 |
|      1      | 0 | 0 | 4 |
|      2      | 0 | 0 | 0 |

Plik JSON opisujący ten graf wyglądałby tak:
```
[[0, 3, 1],
 [0, 0, 4],
 [0, 0, 0]]
```
#### 2.3. Uruchomienie programu
 - Istnieją 3 sposoby na uruchomienie programu.
 - Każdy sposób wymaga wykonania **fork**'a [tego](https://github.com/Aleksander2a/teoria_grafow_projekt) repozytorium **lub** pobrania zawartość **Source code** ze strony  [Releases](https://github.com/Aleksander2a/teoria_grafow_projekt/releases/tag/v1.0) (po pobraniu należy rozpakować pliki)
 #### I sposób - uniwersalny
 - Idź do katalogu **czesc_programistyczna/metoda_forda_fulkersona/**
 - Uruchom plik **algorytm.exe**
 - Powinno pojawić się nowe okno terminalowe, postępuj zgodnie ze wskazówkami programu
  #### II sposób - dla systemu Linux
  - Zlokalizuj interpreter Python'a na swoim komputerze (program był tworzony za pomocą Python 3.8.10, więc może być konieczność zainstalowania tej wersji)
  - Idź do katalogu **czesc_programistyczna/metoda_forda_fulkersona/**
  - *(W razie konieczności)* w pliku **algorytm.py** zmień lokalizaje w pierwszej linijce, tak, aby odpowiadała tej na komputerze (domyślnie w pliku jest **/usr/bin/python3**)
  - Z poziomu wiersza poleceń wykonaj polecenie `chmod +x algorytm.py`
  - *(W razie konieczności)* doinstaluj wymagane pakiety za pomocą polecenia `pip install -r requirements.txt`
  - Uruchom program wykonując `./algorytm.py`
  - Program uruchomi się w konsoli, postępuj zgodnie ze wskazówkami
  #### III sposób - z wykorzystaniem zintegorwanego środowisa programistycznego (IDE)
  - Otwórz projekt w wybranym IDE (program powstawał z wykorzystaniem środowiska PyCharm)
  - Wybierz odpowiedni interpreter Python'a (najlepiej Python 3.8.10) oraz pozostałe ustawienia
  - *(W razie konieczności)* doinstaluj wymagane pakiety za pomocą polecenia `pip install -r requirements.txt`
  - Uruchom program **algorytm.py** przyciskiem **Run**
  - Program uruchomi się w konsoli środowiska, postępuj zgodnie ze wskazówkami

#### 2.4. Dodawanie nowych grafów do analizy
- Na start program posiada 3 przykładowe pliki zawierające informacje o trzech różnych grafach (przyklad1.json, przyklad2.json, przyklad3.json)
- Można swobodnie dodawać nowe pliki do analizy, jeżeli spełniają one warunki:
  + pliki są zgodne z [**formatem danych wejściowych**](https://github.com/Aleksander2a/teoria_grafow_projekt/blob/main/README.md#22-format-danych-wej%C5%9Bciowych)
  + pliki znajdują się w **czesc_programistyczna/metoda_forda_fulkersona/** (lub innej lokalizacji zgodnej z plikiem algorytm.exe bądź algorytm.py - w zależności od sposobu uruchomienia)

