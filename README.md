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
@ZMIANY W ALGO SORT@30MIN procedura rozdzielenia danych na in sample mid sample i all sample@30min utworzenie procedury do samego algo sort poprzez sprawdzenie czterech zmiennych i wybranie njalepszej i wyrzuceniem wyniku do pliku
@KOMPILACJA KIERUNKOW@30MIN zrobienie sredniej z kierunkow a nie sumy (szczegolnie wazne dla CoT)@sprawdzenie roznych dllgosci insample@wygenerowanie kierunkow do dat lastnext@wygnerowane kompilacji recznie? jaki psosob sumowania cot+macro+300k,@*przy generowaniu zmiennych zostawic tylko te co zarabiaja rok w rok (bez jednego roku)@*przy wybieraniu zmiennych exportowac odrazu do dat lastnext + wygenerowac glowny kierunek
@ALGO 300K (zmiany do algosort)@15min pobranie danych z lastnext 1h@import do bazy kombinacji 300k@15min utworzenie zmiennych X i Y do algosort@1h wygenerowanie wyniku nawet z jednym kierunkiem L lub S (algosort dla 300k)@dopisanie do wektora sumy kierunkow@sprawdzenie czy zadziala sharpe*kierunek@export kierunkow 1h do dat lastNext@czy dodawac nonstop L/S jaki to bedzie mialo wynik jakie dac ekstremum brzegowe, czy robic srednia z kierunkow@z jakiego okresu liczyc insample?
@EUREKA@*baza kierunkow glownych zmiennych@*wersje kanal i zmiennosci@*wygenerowanie zysku z spreadem i stopami
@*wygenerowanie inverted lastnext na bazie makro/cot@*sprawdzenie 300k na tej bazie@*prognoza zmiennosci na bazie FF i CoT@*prognoza sezonowosci na bazie FF@*sprawdzenie 300k na bazie eventow FF
@wyliczenie stopow do grania / zapisanie eureki w vba
@MT4@refactoring starej eureki@odczytywanie kierunku z pliku@odczytywanie SL z pliku
@PROD@pobieranie danych CoT@pobieranie danych FF@pobieranie danych z mt4 i tworzenie last next@dopisywanie zmiennych dzialajacych@dodawanie dobrycxh dat do CoT@sciaganie FF bazy danych na 4 tyg do przodu@dopisywanie zmiennych FF@generowanie zmiennych do modeli@generowanie kierunkow@sumowanie keirunkow@generowanie gotowych kierunkow dla danego rynku@generowanie stop losow na bazie lasttnext mt4@zapisanie do pliku aktualnych kierunkow@macro ktore runuje wszystko i sprawdza czy cos wpadlo nowego
