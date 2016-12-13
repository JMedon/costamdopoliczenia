# costamdopoliczenia

=== Xt ===
*import briefing.com
INPUT: URL
-Python kopiowanie tabeli do csv
kod nei dziala!!!
-formatowanie danych w excel
OUTPUT: Excel import_briefing.com
-??dane w jednej kolumnie???
-??dane z datami jako actual i change

 https://docs.python.org/3.3/library/stdtypes.html#bytes.decode
 http://stackoverflow.com/questions/17013089/python-get-rid-of-bytes-b
 
 
*import stooq.pl economic
INPUT: URL
-import historii
-import kolejnych danych codziennie
OUTPUT: Excel import_stooq.com
-??dane w jednej kolumnie???
-??dane z datami jako actual i change

*import Cot data and convert
INPUT: URL
-python zapisanei pliku z url i rozpakowanie zip
-tabela z datami publikacji
-Excel obrobka danych
OUTPUT: Excel import_CoT

=== Yt ===
*import stooq daily data
-only Opens, 
-all OHLC
　
=== AlgoSort ===
INPUT:
-Xt macro/CoT
-Yt market data
-Extremum_threshold=10%
-Better_threshold=30%
-Mid_Date=2016-01-01
　
* 4 rodzaje Xt
* mid sample 2016
OUTPUT: matrix daily forecast
　
=== daily forecast ===
　
=== kompilacja zmiennych ===
*posortowanie najlepszych zmiennych
*dodawanie kolejnych i ustalanie progu kompilacji
　
　'ZMIANY W ALGO SORT'15min'off'wywalenie rozmiarDanych z funckji i wstawienie przedzialu z jakiego ma byc liczone'30MIN'dom'procedura rozdzielenia danych na in sample mid sample i all sample'30min'dom'utworzenie procedury do samego algo sort poprzez sprawdzenie czterech zmiennych i wybranie njalepszej i wyrzuceniem wyniku do pliku'ZEBRANIE DANYCH FF'15min'utworzeni danych nominal i adustment na bazie AllData'15min'dodanie do algosort dat ze wszystkimi mozliwymi datami w bazie'30min'UFORMOWANIE ALGOSORT DO FF'zapisanie do tablei keirunkow dla danego rynku'zapisanie poprzendiego kierunku jesli nic nie bylo'KOMPILACJA KIERUNKOW'30min'dodanie wyniku out of sample'sprawdzenie roznych dllgosci insample'sprawdzenie progu korelacji i czy dodawac przesuniecie progu'sprawdzenie czy korelacje cos pomagaja w wyborze zmiennych i jaki typ da najlepszy wynik'sprawdzenie sharpe ratio * kierunek'30MIN'zrobienie sredniej z kierunkow a nie sumy'1H'dom'wygenerowanie gotowych keirunkow dla Cot by sprawdzic recznie i wybrac najlepsze dzialajace'ALGO 300K (zmiany do algosort)'15min'pobranie danych z lastnext'stworzenie danych 1h?'15min'wygenerowanie kombinacji 300k - import do bazy'15min'pobranie zmiennych X i Y do algosort'1h'wygenerowanie wyniku nawet z jednym kierunkiem L lub S'dopisanie do wektora sumy kierunkow'sprawdzenie czy zadziala sharpe*kierunek''KOMPILACJA METOD'wygenerowanie kierunkow do dat lastnext'wygnerowane kompilacji recznie? jaki psosob sumowania cot+macro+300k, czy same kierunki czy sharpekierunki'*wygenerowanie inverted lastnext na bazie makro/cot'*sprawdzenie 300k na tej bazie'*prognoza zmiennosci na bazie FF i CoT'*prognoza sezonowosci na bazie FF'*sprawdzenie 300k na bazie eventow FF'wyliczenie stopow do grania / zapisanie eureki w vba'MT4'refactoring starej eureki'odczytywanie kierunku z pliku'odczytywanie SL z pliku'PROD'pobieranie danych CoT'pobieranie danych FF'pobieranie danych z mt4 i tworzenie last next'dopisywanie zmiennych dzialajacych'dodawanie dobrycxh dat do CoT'sciaganie FF bazy danych na 4 tyg do przodu'dopisywanie zmiennych FF'generowanie zmiennych do modeli'generowanie kierunkow'sumowanie keirunkow'generowanie gotowych kierunkow dla danego rynku'generowanie stop losow na bazie lasttnext mt4'zapisanie do pliku aktualnych kierunkow'macro ktore runuje wszystko i sprawdza czy cos wpadlo nowego
