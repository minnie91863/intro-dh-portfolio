---
layout: page
title: Finding Places in Text with the World Historical Gazeteer
description: Programming Historian Lesson on NLP, NER, using spaCy and displaCy, and WHG
---


# Finding Places in Text with the World Historical Gazeteer

## Source

[https://programminghistorian.org/en/lessons/finding-places-world-historical-gazetteer](https://programminghistorian.org/en/lessons/finding-places-world-historical-gazetteer) 

## Reflection

World Historical Gazetteer is a resource similar to Google Maps and ArcGIS in that it can map large datasets of locations. This lesson focused on teaching the basics of how to clean up a dataset to prepare for an external mapping/GIS tool so that the resulting data depicts accurate and correct information. 

I had some issues with this lesson, as some of the coding instructions and explanations were vague. I found myself lost many times with what exactly each of the libraries I imported were doing. After cleaning up the files, I was also met with an issue with the World Historical Gazetteer resource where I couldn’t create a new dataset and upload my files I had processed in the lesson. At the time of writing this reflection, I’m still communicating  with WHG about troubleshooting why my file was not accepted. This troubleshooting highlights a key concept I learned in this lesson: while there are tools to help visualize data, the cleaning and formatting can be as challenging as it is crucial.

One particularly confusing aspect of the lesson was the section that covered Named Entity Linking. The process allowed me to use the example sentence in the lesson as a point to link more data about the subjects of the sentence (in this case about Karl-Heinz Quade), but the linked data, a great resource, is never revisited later in the lesson.

From what I can infer from the remaining walkthrough, the actual World Historical Gazetteer resource seems intuitive and ideal for small-scale datasets focused on historical background. The lesson notes that many digital tools such as ArcGIS are developed to fit modern datasets rather than historical ones, so this resource is valuable for specifically history-based research. 

![png](Finding_Places_Gazeteer/screen_captures/Screenshot%202022-12-14%20140809.png)
![png](Finding_Places_Gazeteer/screen_captures/Screenshot%202022-12-14%20141005.png)

## Code

## Finding Places in Text with Python


```python
text = "Siberia has many rivers"
for index, char in enumerate(text):
    print(index,char)
```

    0 S
    1 i
    2 b
    3 e
    4 r
    5 i
    6 a
    7  
    8 h
    9 a
    10 s
    11  
    12 m
    13 a
    14 n
    15 y
    16  
    17 r
    18 i
    19 v
    20 e
    21 r
    22 s
    


```python
text = "Siberia has many rivers"
text.find("rivers")
```




    17




```python
text.find("Rivers")
```




    -1




```python
text.find("y riv")
```




    15



## Natural language processing


```python
!pip install spacy
```


```python
from spacy.lang.de import German
nlp = German()
doc = nlp("Berlin ist eine Stadt in Deutchland.")
for token in doc:
    print(token.i, token.text)
```

    0 Berlin
    1 ist
    2 eine
    3 Stadt
    4 in
    5 Deutchland
    6 .
    

### Load the gazeteer


```python
from pathlib import Path
```


```python
file = open("gazetteer.txt", encoding = "utf-8")
text = file.read();

print(file)
print("gazeteer.txt")
# print(text)

with open('gazetteer_test.txt', 'w', encoding = 'utf-8') as file:
    file.write(text)

```

    <_io.TextIOWrapper name='gazetteer.txt' mode='r' encoding='utf-8'>
    gazeteer.txt
    


```python
gazetteer = Path('gazetteer_test.txt').read_text(encoding = 'utf-8')
# gazetteer = gazetteer.split("\n")
```


```python
gazetteer = text.split("\n")
```


```python
print(gazetteer)
```

    ['Armenien', 'Aserbaidshan', 'Aserbaidshen', 'Estland', 'Georgien', 'Kasachstan', 'Kirgisien', 'Lettland', 'Litauen', 'Moldawien', 'Russland', 'RSFSR', 'Kazakhstan', 'Turkmenien', 'Usbekistan', 'Ukraine', 'Weißrussland', 'Weissrussland', 'Abchasien', 'Akmola', 'Aktjubinsk', 'Alma Ata', 'Gurjew', 'Karaganda', 'Kostai', 'Ostkasachstan', 'Sudkasachstan', 'Siidkasachstan', 'DshalaLAbad', 'Frunse', 'Osch', 'Basarabeasca', 'Adygejien', 'Altai', 'Archangelsk', 'Astrachan', 'Baschkirien', 'Brjansk', 'Burjatien', 'Dagestan', 'Gorki', 'Gorkif Tschkalowsk', 'Irkutsk', 'Iwanowo', 'Jaroslawl', 'KabardinienBalkarien', 'Kalinin', 'Kaliningrad', 'Kalmykien', 'Kaluga', 'KaratschaiTscherkessien', 'Karelien', 'Kemerowo', 'Kislar', 'Kingissepp', 'Kirow', 'Komi', 'Krasnodar', 'Krasnoyarsk', 'Krim', 'Kuibyschew', 'Kurgan', 'Kursk', 'Leningrad', 'Marij El', 'Molotow', 'Mordowien', 'Moskau', 'Murmansk', 'Nordossetien', 'Nowgorod', 'Nowosibirsk', 'Omsk', 'Ordshonikidse', 'Orjol', 'Oijol', 'Pensa', 'Perm', 'Primorje', 'Pskow', 'Rjasan', 'Rostow am Don', 'Saratow', 'Smolensk', 'Stalingrad', 'Stawropol', 'Swerdlowsk', 'Tambow', 'Tatarstan', 'Tjumen', 'Tula', 'T ula', 'Udmurtien', 'Uljanowsk', 'Tscheljabinsk', 'Tscheijabinsk', 'Tscherkessien', 'TschetschenoInguschetien', 'Tschkalow', 'Tschuwaschien', 'Wladimir', 'Wologda', 'Woronesh', 'Aschchabad', 'Andishan', 'Ferga', 'Taschkent', 'Taschkentj', 'Charkow', 'Chmelnizki', 'Dnepropetrowsk', 'Dnepropetrovsk', 'Drogobytsch', 'KamenezPodolski', 'Kiew', 'Kirowograd', 'Lwow', 'Nikolajew', 'Odessa', 'Poltawa', 'Rowno', 'Saporoshje', 'Shitomir', 'Stalino', 'Stanislaw', 'Sumy', 'Su my', 'Tschernigow', 'Winniza', 'Wolynien', 'Woroschilowgrad', 'Gomel', 'Grodno', 'Minsk', 'Mogiljow', 'Pinsk', 'PoLessje', 'Polozk', 'Wilejka', 'Witebsk', 'Alawerdi', 'Arthik', 'Jerewan', 'Oktemberjan', 'Sewan', 'Talin', 'Chanlar', 'Chilly', 'Daschkesan', 'Nucha', 'Samuch', 'Stadt Baku', 'Stadt Kirowabad', 'Harjumaa', 'MorskoiStadtbezirk Tallinn', 'Paide', 'Parnu', 'Raplamaa', 'Valga', 'Otschamtschira', 'Agbulach', 'Macharadse', 'Tbilissi', 'ZaLendshicha', 'Zchaltubo', 'Wischnjowka', 'TaLdykorgan', 'Makat', 'BalchaschStadt', 'Karsakpai', 'Leninogorsk', 'Syrjanowsk', 'Lenger', 'Pachtaaral', 'Turkestan', 'TaschKumyr', 'Kemin', 'Bauska', 'Cesis', 'Jekabpils', 'Jelgava', 'Liepaja', 'Ogre', 'Riga', 'Saldus', 'Talsi', "Talsi'", 'Tukums', 'Akmene', 'Kaus', 'Siauliai', 'Vilkaviskis', 'Kischinjow', 'Vadul Lui Voda', 'BaruL', 'Sorokino', 'Troizkoje', 'Krasnoborsk', 'Oneshski', 'Plessezk', 'Primorski', 'Wolodarski', 'Belorezk', 'Birsk', 'Djatkowo', 'wlja', 'Potschep', 'Susemka', 'Trubtschewsk', 'Iwolginsk', 'PribaikalskiKreis', "Sa'igrajewo", "Sai'grajewo", 'Selenga', 'Tarbagatai', 'Buiksk', 'Balach', 'Bogorodsk', 'Bor', 'Dsershinsk', 'Linda', 'Kulebaki', 'waschino', 'Schachunja', 'Tonschajewo', 'Tschistoje', 'Uren', 'Worotynez', 'Sljudjanka', 'Gawrilow Possad', 'Jurjewez', 'Jusha', 'Kirshatsch', 'Leshnewo', 'Palech', 'Sereda', 'Tejkowo', 'Brejtowo', 'Nerechta', 'PereslawlSalesski', 'UgLitsch', 'ltschik', 'Firowo', 'Mednoje', 'Rshew', 'Sawidowo', 'Spirowo', 'Torshok', 'Wyschni Wolotschok', 'Lagan', 'Wyssokinitschi', 'MikojanKreis', 'UstDsheguta', 'Belomorsk', 'Kalewaly', 'Medweshjegorsk', 'Pitkaranta', 'Prioneshski', 'Pudosh', 'Segesha', 'Wolossowo', 'Kai', 'Kilmes', 'Werchnekamski', 'Wjatskije Poljany', 'Knjashpogost', 'UstWym', 'Beloretschensk', 'Gelendshik', 'Krasnoarmejskaja', 'Kuschtschewskaja', 'Neftegorsk', 'Pawlowskaja', 'Sewerskaja', 'Sowetskaja', 'Uspenskoje', 'Aluschta', 'Balaklawa', 'Bachtschissarai', 'Jalta', 'JaLtaStadt', 'KarassuBasar', 'Kolai', 'Krasnogwardejskoje', 'Krasnoperekopsk', 'MajakSalynski', 'Saki', 'Seitlerski', 'SewastopolStadt', 'Simferopol', 'Stary Krym', 'Sudak', 'Suja', 'MolotowKreis', 'Schigony', 'Shiguijowsk', 'GLuschkowo', 'Mikojanowka', 'Schebekino', 'Borowitschi', 'Ljubytino', 'Lodejnoje Pole', 'Malaja Wischera', 'Okulowka', 'Opetschenski', 'Pargolowo', 'Pestowo', 'Podporoshje', 'Sluzk', 'Tichwin', 'Utorgosch', 'Wolchow', 'Wsewoloshsk', 'JoschkarOla', 'Jurino', 'Kilemary', 'KiseLStadt', 'Kungur', 'MolotowStadt', 'Ochansk', 'Solikamsk', 'TschussowoiStadt', 'Subowa Polja', 'Temnikow', 'Balaschicha', 'Istra', 'Kaschira', 'Kolom', 'Krasnogorsk', 'Krasja Pachra', 'Krasja Polja', 'Kriwandino', 'Leninski', 'Moshaisk', 'Mytischtschi', 'roFominsk', 'Nowopetrowskoje', 'Osjory', 'Reutow', 'Reutov. Kutschino', 'Rusa', 'Schatura', 'Schtscholkowo', 'Solnetschnogorsk', 'StalinogorskStadt', 'Swenigorod', 'Uchtomski', 'Uwarowka', 'Wolokolamsk', 'Kirowsk', 'Kola', 'Dargkoch', 'Digora', 'AnsheroSudshensk', 'Assino', 'Gurjewsk', 'Jurga', 'Kusedejewo', 'Taiga', 'Taschtagol', 'Tjashinski', 'Apasjenkowskoje', 'Gorjatschewodski', 'Kursawka', 'Nowoalexandrowsk', 'Petrowskoje', 'Komaritschi', 'Urizki', 'Bolschoi Wjass', 'Kondolj Kondol', 'Mokschan', 'Gdow', 'Dankow', 'Kawerino', 'Lebedjan', 'Lew Tolstoi', 'Rybnoje', 'SoLotschinski', 'SpassKLepiki', 'Belaja Kalitwa', 'Matwejew Kurgan', 'NowoschachtinskStadt', 'Oktjabrski', 'Remontnoje', 'Simowniki', 'Swerjewo', 'Atkarsk', 'Kamenka', 'Krasnopartisansld', 'Krasny Kut', 'Rtischtschewo', 'Tatischtschewo', 'Woroschilowsk', 'Gshatsk', 'Isdeschkowo', 'Jarzewo', 'Krasny', 'Tumanowo', 'Balyklej', 'Frolowo', 'Gorodischtsche', 'Kotelnikowo', 'Krasja Sloboda', 'Georgijewsk', 'Isobilny', 'Suworowskaja', 'Alapajewsk', 'Aramil', 'AsbestStadt', 'AsbestĀ« Stadt', 'BerjosowskiStadt', 'Iss', 'Iwdel', 'Jegorschino', 'KirowgradStadt', 'Kirowgrad', 'Krasnoufimsk', 'Newjansk', 'Nishnjaja Saida', 'Nishnije Sergi', 'Nowaja Ljalja', 'PoLewskoi', 'Resh', 'RewdaStadt', 'Sysert', 'Tugulym', 'Werchnjaja Tura', 'Bondjushski', 'Kukmor', 'Nurlaty', 'Takanysch', 'Sawodoukowsk', 'Alexin', 'BogorodizkStadt', 'Bolochowo', 'Donskoi', 'Jepifan', 'Kimowsk', 'Laptewo', 'Mordwess', 'Schtschokino', 'Towarkowski', 'Tschern', 'TulaStadt', 'Uslowaja', 'Pudem', 'Uwa', 'Tscherdakly', 'Jetkul', 'Kussa', 'Minjar', 'Satka', "Atagi'", 'Atschaluki', 'AtschchoiMartan', 'dteretschnoje', 'Prigorodny', 'UrusMartan', 'Busuluk', 'KosLowka', 'GusChrustalny', 'Kameschkowo', 'Kurlowski', 'Sudogda', 'Wjasniki', 'Tschagoda', 'Tscherepowez', 'UstKubinski', 'Grjasi', 'JelanKolenowski', 'Dshalalkuduk', 'Isbaskan', 'Begowat', 'Tschis', 'Tschirtschik', 'IBogoduchow', 'Kegitschowka', 'Nowaja Wodolaga', 'Polonnoje', 'Baryschewka', 'Beresan', 'Christinowka', 'Jagotin', 'Alexandrowka', 'Malaja Wiska', 'Busk', 'Nowy Bug', 'Gaiworon', 'Gruschka', 'Globino', 'Lochwiza', 'Genitschesk', 'Michajlowka', 'Berditschew', 'PopoLnja', 'Charzyssk', 'GorLowkaStadt', 'Krasnoarmejsk', 'MakejewkaStadt', 'Selidowo', 'Jampot', 'Nedrigaitow', 'Utjanowka', 'Neshin', 'PriLuki', 'Litin', 'Turbow', 'Tywrow', 'Perwomaisk Stadt', 'Krasny Lutsch Stadt', 'Uwarowitschi', 'WoLkowysk', 'Puchowitschi', 'Saslawl', 'Beresino', 'Bobruisk', 'Ganzewitschi', 'Orscha', 'Sirotino', 'Ejlar', 'Armlu', 'Ararat', 'Etschmiadsin', 'Molotja', 'Kirowakan', 'Werchni Talin', 'Tumanjan', 'Alabaschly', 'Bajan', 'Baku', 'Kugitschu', 'Nishni Daschkesan', 'Werchni Daschkesan', 'Karadag', 'Kirowobad', 'Kirowabad', 'Kysyldsha', 'Kyrychly', 'Mingetschewir', 'Quba', 'Sabuntschi', 'Saljan', 'Schemacha', 'Sych', 'Adshikent', 'Sumgait', 'Ahtme', 'Loksa', 'Johvi', 'Kivioli', 'KohtlaJarve', 'Kuttejou', 'Lehtse', 'Maardu', 'Narva', 'JarvaJaani', 'Lavassaare', 'Rakvere', 'Jarvakandi', 'Sonda', 'Tallinn', 'Tammiku', 'Tapa', 'Tartu', 'Ulila', 'Loosi', 'Nudrezowo', 'Podra', 'Kingu', 'Vasalemma', 'Vontkula', 'Suchumi', 'Kelasuri', 'Miussera', 'Tkwartscheli', 'Manglissi', 'Awtschala', 'Bachmaro', 'Bergwerkssiedlung Nr. 2', 'Bolnissi', 'Bulutschauri', 'ChezerTeesowchos', 'ChramiWasser kraftwerkssiedlung', 'Dsegwi', 'Dwiri', 'Ingiri', 'Kluchori', 'Ksani', 'KutaĆÆssi', 'KutaTssi', 'Kutaiā€™ssi', 'Kutaissi', 'Kwareli', 'Sairme', 'Mukusani', 'wtLugi', 'Poti', 'Rustawi', 'Samgori', 'Sugdidi', 'Supsa', 'Barmaksis', 'Teegenossenschaft Didatschkon', 'Teegenossenschaft raseni', 'Tk', 'Tschaladidi', 'Tschubrin', 'Ureki', 'Wedjanka', 'Zulukidse', 'Atbassar', 'Jessil', 'Koluton', 'Ko Luton', 'Makinka', 'TekeLi', 'Baischoss', 'DshambuL', 'Agadyr', 'Ar', 'Kounradski', 'Bergwerksiedlung 2626 BIS', 'Bergwerksiedlung 4243', 'KaragandaSortirowotschja', 'Dsheskasgan', 'Kokusek', 'MaiKuduk', 'Nurinskaja', 'Saran', 'SpasskiWerkssiedlung', 'Temirtau', 'Dshetygara', 'Kuschmurun', 'Kysylorda', 'Irtyschgesstroi', 'Beloussowka', 'Jerofejewka', 'Syrjanowskoje', 'UstKamenogorsk', 'Syrdarjinskaja', 'Tschimkent', 'Atschissaj', 'Kantagi', 'KjokDshangak', 'DsheLAryk', 'KisKyja', 'Bystrowka', 'Maimak', 'KysylKyja', 'Suljukta', 'Auce', 'Iecava', 'LIgatne', 'Daugavpils', 'Dzukste', 'Eglaine', 'Jaunjelgava', 'Krustpils', 'Garoza', 'Misa', 'Turmali', 'Jugla', 'Kraslava', 'Kuldiga', 'Pavilosta', 'Satinskoje', 'LTgatne', 'Murjani', 'Kegums', 'Olaine', 'Priedaine', 'Purmsati', 'Rampa', 'Rezekne', 'Balozi', 'Salaspils', 'Stopini', 'Broceni', 'Sarkandaugava', 'Skulte', 'Sloka', 'Suntazi', 'Stende', 'Taurupe', 'T ukums', 'Valmiera', 'Ventspils', 'Bicionys', 'Gaideliai', 'Kaisiadorys', 'Ezerelis', 'Raudelino', 'Samaniai', 'Klaipeda', 'Kretinga', 'Mauruciai', 'ujoji Vilnia', 'Palemos', 'RadviLiskis', 'Taurage', 'Telsiai', 'Kybartai', 'Vilnius', 'Abaklia', 'Balti', 'Tiraspol', 'Orhei', 'Ungheni', 'Maikop', 'Tschesnokowka', 'Bisk', 'Blinowo', 'Rubzowsk', 'Newerowskaja', 'Sarinskaja', 'Schpagino', 'Smasnewo', 'Borowljanka', 'Jemza', 'Jerzewo', 'Jura', 'Kargopol', 'Kisema', 'Kostyljowo', 'Kotlas', 'Ustjewo', 'Molotowsk', 'Moschnoje', 'Njandoma', 'Oboserski', 'wolok', 'Podjuga', 'Solsa', 'Schalakuscha', 'Tschekamino', 'Welsk', 'Kapustin Jar', 'Nikolskoje', 'Perwomaiski', 'Tumanny', 'Werchni Baskuntschak', 'Wladimirowka', 'Wolodarowka', 'Beljagusch', 'Inser', 'Nukatowo', 'Sorwicha', 'Karlaman', 'Manjawa', 'Tschernikowka', 'Tschernikowsk', 'Ufa', 'Besymjanka', 'Bijansk', 'Brjansk1', 'Brjansl<2', 'Brjansk2', 'Bytosch', 'Iwot', 'Star', 'Zementny', 'Karatschew', 'Kletnja', 'KLinzy', 'Altuchowo', 'Nowosybkow', 'Ordshonikidsegrad', 'Palushje', 'Pogreby', 'Ramassucha', 'Selzo', 'Kokorewka', 'Belaja Berjoska', 'Unetscha', 'Wygonitschi', 'Dshida', 'Gorchon', 'Gorodok', 'Sawodskoi', 'JushlagSiedlung', 'Nowoiljinsk', 'Onochoi', 'Pedshino', 'Turka', 'Sagustai', 'Surgalej', 'Schabur', 'Werchnije Talzy', 'Saudinski', 'Gussinoje Osero', 'Oronchoj', 'Selenduma', 'Suchaja Padj', 'UlanUde', 'Werchnjaja Mojsa', 'Chabarowsk', 'Karamachi', 'Derbent', 'Gedshuch', 'Isberbasch', 'Machatschkala', 'Mamedkala', 'Rubas', 'Arja', 'Awarijny', 'Prawdinsk', 'Oranki', 'Kershenez', 'Orlowo', 'Bystrucha', 'Pyra', 'Gluchaja', 'Igumnowo', 'Kiselicha', 'Kolchosny', 'Korelka', 'Krasnenki', 'Manturowo', 'Mochowye gory', 'Mostyrka', 'Mursizy', 'Tjoscha', 'Obchod', 'Sjawa', 'Scharja', 'Schemanicha', 'Sejma', 'Serebrjanka', 'Suchobeswodnoje', 'Tschornoje', 'Usta', 'Michailowski', 'Uwarowskaja', 'Rasneshje', 'Wyksa', 'Baischoss NOTE: Error in book. Makat is in Kazakhstan', 'Sagis. NOTE: Error in book. Makat is in Kazakhstan. Book said RSFSR', 'Siedlung des Werks Nr. 39', 'Strecke IrkutskSljudjanka', 'Strecke PosolskUlanUde', 'Strecke SljudjankaWydrino', 'Listwjanka', 'Strecke WydrinoPosolsk', 'Taischet', 'Demidowo', 'Furmanow', 'Iwankowo', 'Michailowo', 'Mugrejewo', 'Talizy', 'Kineschma', 'Kochma', 'Komsomolsk', 'Kowrow', 'Petrowski', 'Rodniki', 'Schuja', 'Jakowlewskoje', 'Siedlung des SchalowZiegelwerkes', 'Textilny', 'Witschuga', 'Iwkino', 'Chmelniki', 'Gawrilow Jam', 'Jakschanga', 'Kostroma', 'Lorn', 'Neja', 'Kosmynino', 'Perebory', 'Pereslawl', 'Rogosinino', 'Ussolje', 'Petrowsk', 'PriwoLshje', 'Rodionowo', 'Rybinsk', 'Schestichino', 'Schtschelkanskoje Torfopredprijatije', 'Semibratowo', 'Silnizy', 'Suprotiwny', 'Tichmenewo', 'Tutajew', 'Tschernizyno', 'WauLowo', 'Wspolje', 'AksautGretscheski', 'Kenshe', 'Akademitscheskaja', 'Beshezk', 'Bologoje', 'Emmaus', 'Wassiljewski Moch', 'Kimry', 'Kokowo', 'Kuwschinowo', 'Leontjewo', 'Maksaticha', 'Malyschewo', 'rotschino', 'Nelidowo', 'Nowossokolniki', 'Ossetschenka', 'Ostaschkow', 'Poddubki', 'Ranzewo', 'Redkino', 'Konyschewo', 'Olenino', 'Selisharowo', 'Semzy', 'Wydropushsk', 'Staraja Toropa', 'Dmitrowskoje', 'Dumanowo', 'Tschernogubowo', 'Tschorny Dor', 'Udomlja', 'Welikije Luki', 'Krasnomaiski', 'Konigsberg', 'Bagration owsk', 'Gut Romitten', 'Gwardejsk', 'Insterburg', 'Kaukiemis', 'Metgethen', 'Pillau', 'Preu&ischEylau', 'Ragnit', 'Seckenburg', 'Tilsit', 'Trammen', 'Tschernjachowsk', 'Wehlau', 'UlanChol', 'Kanukowo', 'Fajansowaja', 'Kusmitschi', 'Ljudinowo', 'Malojaroslawez', 'Suchinitschi', 'DurowSowchos', 'Chumara', 'Tscherkessk', 'Washnoje', 'Malenga', 'Letneretschenski', 'Saliwy', 'Tegosero', 'Iljinskaja', 'Kepa', 'Kondopoga', 'Medweshja Gora', 'arlahti', 'Pai', 'Petrosawodsk', 'Harlu', 'Laskela', 'Suojarvi', 'Pjashijewa Selga', 'Derewjanka', 'Botschilowo', 'Kolowo', 'Kubowskaja', 'NowoStekljannoje', 'Pjalma', 'Porschta', 'Schala', 'Schalski', 'Tschernoretschenski', 'Petrowski Jam', 'Polga', 'Uchta', 'Uuksu', 'Jurga1', 'Prokopjewsk', 'Stalinsk', 'Kikerino', 'Ardaschi', 'Besboshnik', 'Fosforitja', 'Ima', 'Werchnekamskaja', 'Latyschski', 'Loiga', 'Ljangassowo', 'Omutninsk', 'Posdino', 'Slobodskoi', 'Sosnowka', 'Stalja', 'Suslowka', 'Sosimski', "N. BeLoi'rka", 'WoshajeL', 'Lemju', 'Sewsheldorlag', 'Syktywkar', 'Sheschart', 'Adler', 'Apa', 'Apscheronsk', 'Armawir', 'Chadyshensk', 'Dshugba', 'Gluchari', 'Jurjewka', 'Mogilnoje', 'Kropotkin', 'Krymsk', 'Mogilny', 'Abchasskaja', 'Chadyshenskaa', 'Noworossisk', 'Ilski', 'Sotschi', 'Tichorezk', 'Tuapse', 'BogotoL', 'Sowchos Kastel', 'Belbek', "Tai'r", 'Dshankoi', 'Feodossija', 'Inkerman', 'AiWa nil', 'Alupka', 'Foros', "Korei's", 'Liwadija', 'Oreanda', 'Partenit', 'Jewpatorija', 'Mariano', 'Kertsch', 'Sowchos Bolschewik', 'Bagerowo', 'BuLgak', 'Eschkine', 'Sowchos Tschoschty', 'Tamak', 'Sewastopol', 'Sevastopol', 'Katscha', 'Sowchos KaraKijat', 'Sirenj', 'Siwasch', 'Sowchos AiDani', 'Sowchos Krasny', 'Koktebel', 'Sowchos 1. Fiinfjahrplan', 'Otusy', 'Sowchos Krymskaja Rosa', "Ta'ir", 'Bachilowa Polja', 'Batraki', 'Jablonowy Owrag', 'Jablonewy Owrag', 'Kadej', 'Kinel', 'Krjash', 'Melekess', 'Otwashnoje', 'Nikolajewka', 'Pochwistnewo', 'Sabdowka', 'Petscherskoje', 'Solnoje', 'Solonez', 'Sysran', 'Schadrinsk', 'Belgorod', 'Blagodatenski', 'Derjugino', 'Fatesh', 'Tjotkino', 'Gotnja', 'ShurawLjowka', 'Obojanj', 'Ryschkowo', 'NowoTawoLshanka', 'Tros', 'Waluiki', 'Besborodowo', 'Boksitogorsk', 'Jegla', 'Schibotowo', 'Ustje', 'Chotzy', 'Dibuny', 'Ishora', 'Jedrowo', 'Johannes', 'Kakisalmi', 'Kaskowo', 'Koli', 'Kolpino', 'Kowanko', 'Krasja Mysa', 'Krasnoje Selo', 'Krestzy', 'Kronstadt', 'LadogaSee', 'Ljalizy', 'Komarowo', 'Swirstroi', 'Luga', 'Lungatschi', 'Bolschoje Saborowje', 'Mga', 'Neboltschi', 'ParachinoPoddubje', 'Opetschenski Posad', 'Pesotschny', 'Petrodworez', 'PikaLjowo', 'Washiny', 'Pontonja', 'Puschkin', 'Rautu', 'Rogawka', 'Rudnitschja', 'Sestrorezk', 'Shichaijowo', 'Shicharjowo', 'Antropschino', 'UstIshora', 'Spasskaja Polistj', 'Staraja Russa', 'Stroganowo', 'Swir', 'Taizy', 'Terebutenez', 'Terioki', 'Tosno', 'Tschudowo', 'Turgosch', 'Uglowka', 'Waldaj', 'Sjasstroj', 'Wolchowstroi', 'Wolchowstroi2', 'MorosowSiedlung', 'Rachja', 'Golowino', 'SusLonger', 'Kosmodemjansk', 'Wolshsk', 'Baskaja', 'Beresniki', 'Gremjatschinski', 'Kisel', 'Gubacha', 'Jushny Kospaschski', 'Polowinka', 'Sewerny Kospaschski', 'Uswa', 'WsewolodoWilwa', 'Krasnokamsk', 'Kurja', 'Lyswa', 'Lewschino', 'Obogatitel', 'Obogatitelja', 'JugoKamski', 'Owerjata', 'Ponysch', 'Borowsk', 'Kalijez', 'Tscherdyn', 'Tschussowskaja', 'Paschia', 'Tjoplaja Gora', 'UrizkiBergwerke', 'Potma', 'Saransk', 'Sweshenkaja', 'Baratjewo', 'Akinschino', 'Aprelewka', 'Baranowo', 'Barmino', 'Bogorodskoje', 'Bronnizy', 'Butowo', 'Chimki', 'Chlebnikowo', 'Cholschtschewiki', 'Chotkowo', 'Chowrino', 'Chrapunowo', 'Dmitrow', 'Dolgoprudny', 'Dorochowo', 'Dres', 'Dulewo', 'Elektrostal', 'Fill', 'Golizyno', 'Golutwin', 'Gubanowo', 'Gutschkowo', 'Nowojerusalimskaja', 'Iwantejewka', 'Jegorjewsk', 'KaganowitschWerke', 'Osherelje', 'Katuar', 'Kisseljowo', 'Klin', 'Schtschurowo', 'Kolotsch', 'Koptjewo', 'Kossino', 'Iljinskoje', 'Pawschino', 'Tuschino', 'GosplanLandsiedlung', 'Lunjowo', 'Krasny Stroitel', 'Krjukowo', 'Lebsino', 'Tscherjomuschki', 'Lianosowo', 'Ljuberzy', 'Ljublino', 'Lobnja', 'Lopasnja', 'Luchowizy', 'Jurlowo', 'Obljanischtschewo', 'Schalikowo', 'Moskworezkaja', 'Mosshinka', 'Textilschtschik', 'Noginsk', 'Nowogorsk', 'OrechowoSujewo', 'Ostankino', 'Otdych', 'Otschakowo', 'Perowo', 'Planerja', 'Podlipki', 'Podolsk', 'PokrowskojeStreschnjewo', 'PtscheLowodnoje', 'Puschkino', 'Kutschino', 'Reutowo', 'Reschetnikowo', 'Rumjanzewo', 'Tutschkowo', 'Saraisk', 'Sasonowo', 'Frjasino', 'Semjonowskoje', 'Serebijany Bor', 'Serpuchow', 'Silikatja', 'Snegiri', 'Sorewnowanie', 'Sofrino', 'Rshawka', 'Kijukowo', 'Bergwerkssiedlung 28', 'Stroika', 'Stupino', 'Tomilino', 'Tscherkisowo', 'Tscherusti', 'Tschuchlinka', 'Kraskowo', 'Lytkarino', 'Ugreschskaja', 'Gorbuny', 'Kisseljowka', 'Poretschje', 'Werbilki', 'Wolololamsk', 'Woskressensk', 'Wyssokowsk', 'Kandalakscha', 'Saschejek', 'Kildinstroi', 'Murmaschi', 'Ku', 'Montschegorsk', 'Nikel', 'Olenja', 'Padun', 'Pautscha', 'Werchnjaja Simba', 'Nekrylowo', 'Beslan', 'Kardshin', 'Ursdon', 'Dsaudshikau', 'Krasnowodsk', 'Sadon', 'Wosnessensk', 'Perniza', 'Novosibirsk', 'Abagurowski', 'Alambai', 'Jaja', 'Ansherskaja', 'Artyschta', 'Barabinsk', 'Belowo', 'Bergwerke Jushja', "Salai'r", 'Inskoi', 'Kisseljowsk', 'Kriwoschtschokowo', 'Schuschtalep', 'LeninskKusnezki', 'Myski', 'Nowokusnezk', 'Berdsk', 'Ossinnilci', 'Ossinniki', 'Jaschkino', 'Tatarsk', 'Tjashin', 'Tschulym', 'Ussjaty', 'Issilkul', 'Kulomsino', 'Diwnoje', 'Mineralnyje Wody', 'Newinnomyssk', 'NowoALexandrowka', 'Pjatigorsk', 'Prijutnoje', 'Belyje Berega', 'Fokino', 'Jelez', 'Oelez', 'Mzensk', 'Pogar', 'Polushje', 'Assejewskaja', 'Bednodemjanowsk', 'Tschaadajewka', 'Kusnezk', 'Nikolajewski chutor', 'Nishni Lomow', 'Seliksa', 'Simanschtschino', 'Wertuhowka', 'Jar', 'Bauobjekt 500', 'Slanzy', 'Nowosselje', 'Pljussa', 'Toroschino', 'Tschorskaja', 'Birlcino', 'Chruschtschowo', 'Sowchos Kuibyschew', 'Djagilewo', 'Grotowski', 'Iswest', 'Jambirino', 'Kurscha', 'Sowchos 15 Jahre Oktober', 'Sowchos Agronom', 'Sowchos Gorki', 'sarowka', 'Pronja', 'Kanischtschewskije Wysselki', 'Kriuscha', 'KanischtschewsIcije WysseLki', 'Murmino', 'Wyschgorod', 'Wyssokoje', 'Roshdestwenskoje', 'Roshdestwo', 'Schazk', 'StaroshiLowo', 'Zementja', 'Artjom', 'Bataisk', 'Bogdanowka', 'Bergwerkssiedlung SapadnoKapitalja', 'Bergwerkssiedlung ā€˛0GPU"', 'Gukowo', 'Gundorowski', 'Krasny Sulin', 'Nowikowka', 'RawnopoL', 'deshda', 'Mi ch aj Lo Leo n tj ewskaj a', 'Mich aj Lo Leo n tj e ws kaj a', 'Mi c h aj Lo Le o n tj e ws kaj a', 'MichajLoLeontjewskaja', 'chitschewanDonskaja', 'Nowotscherkassk', 'Nowoschachtinsk', 'MolotowSiedlung', 'Kamenolomni', 'Salsk', 'Schachtja', 'Schachty', 'Sinjawskaja', 'Taganrog', 'Tazinski', 'Arkadak', 'Podgorenka', 'Strecke Atkarsk...', 'Bagajewwka', 'Bagajewka', 'Balakowo', 'Chwalynsk', 'Engels', 'Grimm', 'Jekaterinowka', 'Jelschanka', 'Kologriwowka', 'Gorny', 'Kurdjum', 'Marx', 'Pudowkino', 'Pugatschow', 'Tamala', 'Toptulino', 'Trofimowski', 'Wertunowka', 'Wolsk', 'Dorogobush', 'Durowo', 'Gussino', 'Kolesniki', 'Kolesniki Swischtschewo', 'Kondrowo', 'Kuprino', 'Nikitinka', 'Pjatowskaja', 'Polotnjany Sawod', 'Priselskaja', 'Roslawl', 'Saretschje', 'Semlewo', 'Wjasma', 'Artscheda', 'Gorny Balyklej', 'Beketowka', 'Beketowskaja', 'Dubowka', 'Ilowlja', 'Kamyschin', 'Keller', 'Kotelnikowski', 'Sadowaja', 'Sarepta', 'Staraja Otrada', 'Urjupinsk', 'Wesjolaja Balka', 'Georgijewsk.', 'Neslobja', 'Jessentuki', 'Kislowodsk', 'Kumarinskie Schachty', 'Skatschki', 'Adui', 'Werchnjaja Sinjatschicha', 'Bobrowka', 'Mostyr', 'Altyi', 'Apparatja', 'Asanka', 'Asbest', 'Isumrud', 'Bashenowo', 'Belyje Baraki', 'Beresit', 'Berjosowski', 'Lossiny', 'Bogoslowsk', 'Chabartschicha', 'ChmyLowka', 'Chrompik', 'Chudjakowo', 'Degtjarsk', 'GLucharny', 'GorobLagodatskaja', 'Irbit', 'Kytlym', 'Isset', 'Istok', 'Iwdel2', 'Artjomowski', 'Krasnogwardejski', 'Jeshewaja', 'KamenskUralski', 'Kamyschlow', 'Karpinsk', 'Lewicha', 'Kolzowo', 'Kossulino', 'Kourowka', 'Krasnoturjinsk', 'Krasnotuijinsk', 'Koschai', 'Krasnouralsk', 'Krasny Alut', 'Krasny Jar', 'Krasny Shelesnjak', 'Maly Istok', 'Maramsino', 'Medja Schachta', 'Molwa', 'Monetny', 'Moroskowo', 'Mramorskaja', 'Mugai', 'deshdinsk', 'NejwoSchaitanski', 'WerchNejwinski', 'Basjanowski', 'Werchnije Sergi', 'Nishni Issetsk', 'Nishni Istok', 'Nishni Tagil', 'Nishnjaja Tura', 'Lobwa', 'Perschino', 'PerwouraLsk', 'PodwoLoschja', 'PokLjowskaja', 'Sewerski', 'Rasjesd 173', 'Rewda', 'Degtjarka', 'Sadanije', 'Samozwet', 'Schabrowski', 'Schaitan', 'Schartasch', 'Schuwakisch', 'Seredowi', 'Serow', 'Sewerouralsk', 'Sinjatschicha', 'Soswa', 'SredneuraLsk', 'Suchoi Log', 'BoLschoi Istok', 'TaLy Kljutsch', 'Tawda', 'TjopLy Kljutsch', 'Tschorja Retschka', 'Jertarski', 'Turin sk', 'Turinsk', 'Turinskie rudniki', 'Uktus', 'Urai', 'Werchnjaja Pyschma', 'Werchnjaja Saida', 'Otradnowo', 'Werchoturje', 'Wessjolowka', 'Woltschansk', 'Chobotowo', 'Inshawino', 'Kirsanow', 'Mitschurinsk', 'Morschansk', 'Oboro', 'Rada', 'Sampur', 'Wjashli', 'Kokschan', 'Bugulma', 'Buinsk', 'Jelabuga', 'Kamskoje Ustje', 'Kasan', 'Lubjany', 'Schemordan', 'SelenodoLsk', 'Tschistopol', 'Jalutorowsk', 'Lebedewka', 'WinsiLi', 'Myschega', 'BobrikDonskoi', 'Begitschewski', 'Suchodolski', 'Chomjakowo', 'Dedilowo', 'Sadonje', 'Smorodinka', 'Gorbatschowo', 'Granki', 'Jasja Polja', 'Wladimirskoje', 'Kasanowka', 'Lwowo', 'Maklez', 'Majenki', 'Obidimo', 'Obolenskoje', 'Plawsk', 'Polunino', 'Prisady', 'Sbrodowo', 'Schepeljowo', 'Ogarjowka', 'Serebrjanyje Prudy', 'Shdanka', 'Stalinogorsk', 'Tarusskaja', 'Towarkowo', 'Kossaja Gora', 'Bergwerkssiedlung Nr. 5', 'Torbejewka', 'Wenjow', 'Glasow', 'Ishewsk', 'Lynga', 'NjurdorKotja', 'Perwomaisk', 'Rjabowo', 'Wischur', 'Kondakowka', 'Poliwanowo', 'Taschla', 'Ai', 'Ascha', 'Bischkil', 'JemansheLinka', 'Korkino', 'Kamensk', 'Kamyschinka', 'Karabasch', 'Kartaly', 'Kopejsk', 'Kropatschowo', 'Magnitka', 'Kyschtym', 'Magnitogorsk', 'Mauk', 'Miass', 'Rosa', 'BakaL', 'Sawodskaja', 'Slatoust', 'Tajandy', 'Ufalej', 'Urshumka', 'Wawilowo', 'TschetschenAul', 'Samaschki', 'Gora Gorskaja', 'Grosny', 'AliJurt', 'sran', 'Basorkino', 'Scholkowskaja', 'TangiTschu', 'Tschita', 'Buguruslan', 'Koltubanka', 'Nowotroizk', 'Nowotroizki Maksai', 'Orsk', 'SoLILezk', 'ALatyr', 'Kasch', 'TjurLema', 'SawoLshskoje Torfopredprijatije', 'Tscheboksary', 'Butylizy', 'Anopino', 'Krasnoje Echo', 'Chrapowizkaja 1', 'Chrapowizkaja 2', 'Karabanowo', 'Koltschugino', 'Komissarowka', 'Iljitschowo', 'Melenki', 'Sarja', 'Sobinka', 'Andrejewo', 'Susdal', 'Tschulkowo', 'Undol', 'Mstjora', 'Woschod', 'Wtorowo', "Buschui'cha", 'Charowskaja', 'Dedowo Pole', 'Grjasowez', 'Jadricha', 'Jawenga', 'Kadnikow', 'Kirillow', 'Lesha', 'Petschatkino', 'Scheks', 'Schelomowo', 'Semigorodnjaja', 'Sokol', 'Suda', 'Ustjush', 'Wolonga', 'Woshega', 'Borissoglebsk', 'Chrenowaja', 'Ertil', 'Grafskaja', 'Gribanowka', 'Lipezk', 'Liski', 'Poworino', 'Rossosch', 'Usman', 'Tedshen', 'Jushny Alamyschik', 'Tschuama', 'Kokand', 'Skobelewo', 'Taschkent Tientjaksai', 'Achangaran', 'Angren', 'Angrenschachtstroi', 'Farchad', 'Jangijul', 'Gwardejski', 'Schirin', 'Charkow Ukraine', 'Anjewo', 'Perwuchino', 'Isjum', 'Krasnograd', 'Kupjansk', 'Ljubotin', 'Merefa', 'Nowaja Bawarija', 'Osnowa', 'Panjutino', 'Parchomowka', 'Pokotilowka', 'Rogan', 'Sokolniki', 'Tschugujew', 'Kriwin', 'Poninka', 'Schepetowka', 'Slawuta', 'Baglej', 'Baustelle des SamaraBergwerkes', 'Dneprodsershinsk', 'Dolginzewo', 'Kanderopol', 'Kriwoi Rog', 'Marganez', 'Nikopol', 'Nishnedneprowsk', 'Nowomoskowsk', 'Pereschtschepino', 'Prossjaja', 'Raduschja', 'Tschertomlyk', 'Tscherwonoje', 'Borislaw', 'Chodorow', 'Gelsendorf', 'Morschin', 'Shidatschow', 'Skole', 'Stryj', 'Tschernowizy', 'Belaja Zerkow', 'Borispol', 'Browary', 'Werchnjatschka', 'Darniza', 'Fastow', 'Sgurowka', 'Panfily', 'Schewtschenkowo', 'Schpola', 'Smela', 'Talnoje', 'Tscherkassy', 'Uman', 'Alexandria', 'Alexandrija', 'Kapitanowka', 'Wiska', 'Pantajewka', 'Sacharja', 'Scharowka', 'Schestakowka', 'Negrebki', 'Peremyschljany', 'Rudno', 'Salush', 'Sknilow', 'Skoschlow', 'SoLotschew', 'Berislaw', 'Cherson', 'Jurizino', 'Kopani', 'Partisany', 'SaLkowo', 'SokoLogornoje', 'Ternowka', 'Tschitschkarowka', 'NowoBorissow', 'Ismail', 'Kotowsk', 'Reni', 'Pestschanka', 'Abasowka', 'Chorol', 'Grebjonka', 'Oagotin', 'dagotin', 'Karlowka', 'Kononowka', 'Kotschubejewka', 'Krementschug', 'StaLinZuckerwerk', 'Lubny', 'Mechedowka', 'Pirjatin', 'Romodan', 'Skorochodowo', 'Wesjoly Podol', 'Sarny', 'Sdolbunow', 'Balabi no', 'Bolschoi Tokmak', 'Bolschoi Utljug', 'Georgijewski', 'Grigorjewka', 'Nowoalexejewka', 'Rosowka', 'Matwejewski', 'Melitopol', 'PetroMichajlowka', 'Mokraja', 'Nowogrigorjewka', 'Rodionowka', 'Terpenije', 'Belokorowitschi', 'Lyssaja Gora', 'Skomorochi', 'Chajtschnorin', 'Igtopol', 'Igtpot', 'Jemetjanowka', 'Korosten', 'Kriwoje', 'Matin', 'NowogradWolynski', 'Penisewitschi', 'Kornin', 'Radomyschl', 'Weledniki', 'Artjoma', 'Artjomowsk', 'Bairak', 'Chanshonkowo', 'Sujewka', 'Cholodja Balka', 'Debalzewo', 'Dobropolje', 'Dronowo', 'Drushkowka', 'FenoLja', 'GorLowka', 'Kondratjewski', 'Grechow', 'Jama', 'Jassinowka', 'Jekijewo', 'Kalmius', 'Katyk', 'Konstantinowka', 'Kramatorsk', 'Nowoekonomitscheskoje', 'Krasnoarmejskoe', 'Krasnogorowka', 'Kurachowka', 'Lutugino', 'Magdalinowka', 'Makejewka', 'Pantelejmonowka', 'Mospino', 'Motschalino', 'Motschalinski', 'Muschketowo', 'Nikitowka', 'Nowy Donbass', 'Orlowa Sloboda', 'Petrowka', 'Postnikowo', 'Roja', 'Rutschenkowo', 'Bergwerkssiedlung 12', 'Bergwerkssiedlung 31', 'Bergwerkssiedlung 56', 'Bergwerkssiedlung 78 BIS', 'Bergwerkssiedlung Dsershinka', 'Bergwerkssiedlung imeni Leni', 'Bergwerkssiedlung Kisseljow', 'Schtscheglowka', 'Shdanow', 'Skossyrskaja', 'Slawjansk', 'Smoljanka', 'Sol', 'Studgorodok', 'TroizkoCharzyssk', 'Trudowaja', 'Tschassow Jar', 'Tschistjakowo', 'Tschumakowo', 'Woskressenskaja', 'Zukuricha', 'Kolomyja', 'Lawotschnoje', 'Achtyrka', 'Gluchow', 'Konotop', 'Nepljujewo', 'Terny', 'Neptjujewo', 'PrawdinskiZuckerfabrik', 'Putiwt', 'Toropitowka', 'Torochtjany', 'Ternopot', 'Bobrowizy', 'T schernigow', 'Linowizy', 'Ladan', 'Perelowka', 'Safonowo Guta', 'SafonowoGuta', 'Semjonowka', 'Sorokatitschi', 'Tolsty Les', 'Wiltscha', 'Tschernjowka', 'Tschernowzy', 'GLuchowzy', 'Kasatin', 'Shmerinka', 'Gniwan', 'Manewitschi', 'Almasja', 'Altschewsk', 'Awdakowo', 'Bergwerk 2', 'Darjewka', 'Djakowo', 'Dolshanskaja', 'Golubowka', 'Gorskoje', 'Irmino', 'Iswarino', 'Kadijewka', 'Kamyschewacha', 'Karakas', 'KrasnopoLje', 'Krasny Lutsch', 'Krindatschowka', 'KrupskajaBergwerk', 'Lissitschansk', 'Kriworoshje', 'Manuilowka', 'Ovvragi', 'Parishskaja Kommu', 'Perejesdja', 'Popasja', 'Rowenki', 'Rubeshnoje', 'Schtschotowo', 'Schterowka', 'Sentjanowka', 'Sifonja', 'Simogorje', 'Waljanowski', 'Werchneje', 'Wiljanowo', 'Wolodarsk', 'ZentralnoBokowskoi', 'Chojniki', 'Dobrusch', 'Jelsk', 'Kostjukowka', 'Nowobelizkaja', 'Retschiza', 'Rogatschow', 'Shlobin', 'Sjabrowka', 'Usa', 'Wassilewitschi', 'Lida', 'Mosty', 'SLonim', 'PawLinowo', 'Ross', 'Borissow', 'Fanipol', 'Kolodischtschi', 'Krasnoje Smja', 'Maiji Gorka', 'Sedtscha', 'Shodino', 'SmoLewitschi', 'TaLka', 'Uretschje', 'Gluscha', 'Brosha', 'Bychow', 'Grodsjanka', 'Jasen', 'Kershenka', 'Kopzewitschi', 'Kritschew', 'Ossipowitschi', 'Mosyr', 'Barawucha', 'Tatarka', 'Schklow', 'Timkowitschi', 'Molodetschno', 'Oschmjany', 'Chljustino', 'Krasja', 'Obol', 'Osinowka', 'Ossipowka', 'Borkowitschi', 'Kriste', 'Tolotschin', 'Tschaschniki', 'Ulga', 'Koschtschu', 'Bernjaschen', 'Armenikend', 'Konju', 'Kukruse', 'Ereda', 'Aseri', 'Ellamaa', 'Jeschera', 'Agudseri', 'Gori', 'Borshomi', 'Inguri', 'SaganLugi', 'Sandary', 'MolotowStadtbezirk', 'Didube', 'wtlugi1 ā€¢', 'wibuli', 'Dshalombet', 'Giiterbahnhof', 'Ridder', 'Saschtschita', 'Kflkas', 'Sesava', 'Kalgi', 'Bukas', 'Spopane', 'Rembazkoje', 'Petrasiui', 'Seredzius', 'Lustberg', 'Airiogola', 'Klemiske', 'MaimaksanskiStadtbezirk', 'P ro leta rs ki Sta dtbezi rk', 'Stadtteil Beshiza', 'I wot', 'Kokino', 'Sakamensk', 'Nishnjaja Arakorka', 'Onochoj', 'AwtosawodskiStadtbezirk', 'SormowoStadtbezirk', 'SchumLewaja', 'Sejm a', 'Tschernoramenka', 'Gorschenino', 'not RSFSR as book says', 'Chlebowo', 'Krasny Orjol', 'Berendejewo', 'Karasch', 'Gusjatino', 'Migalewo', 'Grinino', 'Smoschje', 'Gontscharowo', 'Kotarowo', 'Tapiau', 'Jasnoje', 'Prochladja', 'Baltisk', 'Bagrationowsk', 'Neman', 'Sowetsk', 'Tramischen', 'Smensk', 'Sjassosero', 'Kappesalka', 'Kutichosskaja', 'Solomennoje', 'Kukowka', 'Witschka', 'Bessow Nos', 'Wolosniza', 'Pschada', 'Jejsk', 'Turgenewka', 'Subtschaninowka', 'Stary OskoL', 'Schemilowka', 'Ljamisa', 'Mstinski Most', 'Sowetski', 'Priosjorsk', 'Kin', 'Lissi Nos', 'Iwangorod', 'Kamenskoje', 'Seliwanowo', 'KowaLko', 'Dubowizkoje', 'Sosnowo', 'Selenogorsk', 'Kerest', 'UstSchora', 'UstSchory', 'Filippowka', 'Molebny Owrag', 'Stadtteil Rostokino', 'Werchnije Kotly', 'Nishnije Kotly', 'NowoGirejewo', 'Panki', 'Perowo Pole', 'Kurkino', 'Marfino', 'Alexino', 'Beskudnikowo', 'Guba', 'Nishnjaja Simba', 'Wladikawkas', 'Bugry', 'Kriwoschtschowoko', 'MBystraja', 'Dorogoi', 'Bolotowo', 'Kjutschiki', 'Raswilka', 'Jewlaschewo', 'Achuny', 'Machalino', 'Kripun', 'Rasjesd', 'Turns kaja', 'Turn a', 'Lesnoje', 'Sals k', 'NowoAsowka', 'Rostowka', 'Marzewo', 'Peschtschany', 'Sokolowaja Gora', 'Sudowka', 'km 282', 'DsershinskiStadtbezirk', 'JermanskiStadtbezirk', 'J e r m a n s ki Stad tbezi rk', 'TraktorosawodskiStadtbezirk', 'Sowchos Priwolshski', 'Shirnowsk', 'Abgenowo', 'Rasjesd Owrashny', 'Ajat', 'Turjinski', 'Kuschwa', 'Rudnitschny', 'Woltschanka', 'Bergwerk 23', 'Patotschja', 'Rogoshinski', 'Bergwerk 6', 'Stali nogorsk', 'Bergwerk 19', 'Dsjakino', 'Sareka', 'Moissejewka', 'Mjassnikowo', 'Nowoschalaschowo', 'Maksai', 'Korjakino', 'ski', 'Alexejewskoje', 'Makarji Roschtscha', 'Silno', 'Kokawino', 'Ljubomirskaja', 'Wassilkow', 'PostWolynski', 'Kowachino', 'Olesko', 'Sinilow', 'Rabotschi', 'Wetka', 'Kalinowka', 'PetrowoLidijewka', 'DonezkoAmwrossijewka', 'Shelanja', 'Schachtjorsk', 'Ilowaisk', 'Kriwoi Torez', 'Lidijewka', 'IwanoFrankowsk', 'Wiry', 'Jazewo', 'Shidinitschi', 'Uditschew', 'Uditschewo', 'Brjanka', 'DsershinskiBergwerk', 'Toschkowka', 'Maksimowka', 'Bergwerk Nr. 8', 'GLuboki', 'IljitschBergwerk', 'Petrowenki', 'Bergwerkssiedlung Nr. 7', 'Kosyrewo', 'Kasimirowka', 'Norio', 'Dshambejty', 'Komsomolski', 'Spass Saulok', 'B. Saborje', 'Werksiedlung Sulash Gora', 'Kudama', 'Repjowka', 'Sibrowo', 'Lopatkowo', 'Solnjetschja', 'Perewoloki', 'Alexejewka', 'Bachilowo', 'Uman', 'Owrutsch', 'Mariupol', 'Mokwa', 'Massy', 'Lahta', 'Sapjorja', 'Roshdestwennoje', 'Rybniza', 'Brno', 'Sibirien', 'Ural', 'Workuta', 'Magadan', 'Kolyma', 'Norilsk', 'Lubjanka', 'Butyrka', 'Kaliningrad', 'Lager Nr.', 'Lager Nummer']
    

### Matching Place Names


```python
example_sentence = 'Karl-Heinz Quade ist von März 1944 bis August 1948 im Lager 150 in Grjasowez interniert.'
```


```python
from spacy.lang.de import German
from spacy.matcher import Matcher

nlp = German()

doc = nlp(example_sentence)
```


```python
matcher = Matcher(nlp.vocab)
for place in gazetteer:
    pattern = [{'LOWER': place.lower()}]
    matcher.add(place, [pattern])
```


```python
matches = matcher(doc)
for match_d, start, end in matches:
    print(start, end, doc[start:end].text)
```

    13 14 Grjasowez
    


```python
pattern = [{'LOWER': 'lager'}, {'LIKE_NUM': True}]
matcher.add('LAGER_PATTERN', [pattern])
```


```python
matches = matcher(doc)
for match_d, start, end in matches:
    print(start, end, doc[start:end].text)
```

    10 12 Lager 150
    13 14 Grjasowez
    

### Loading Text Files


```python
for file in Path('folder_with_texts').iterdir():
    doc = nlp(file.read_text(encoding = 'utf-8'))
    matches = matcher(doc)
    for match_id, start, end in matches:
        print(file.name, start, end, doc[start:end].text)
```

    gazetteer_test.txt 0 1 Armenien
    gazetteer_test.txt 2 3 Aserbaidshan
    gazetteer_test.txt 4 5 Aserbaidshen
    gazetteer_test.txt 6 7 Estland
    gazetteer_test.txt 8 9 Georgien
    gazetteer_test.txt 10 11 Kasachstan
    gazetteer_test.txt 12 13 Kirgisien
    gazetteer_test.txt 14 15 Lettland
    gazetteer_test.txt 16 17 Litauen
    gazetteer_test.txt 18 19 Moldawien
    gazetteer_test.txt 20 21 Russland
    gazetteer_test.txt 22 23 RSFSR
    gazetteer_test.txt 24 25 Kazakhstan
    gazetteer_test.txt 26 27 Turkmenien
    gazetteer_test.txt 28 29 Usbekistan
    gazetteer_test.txt 30 31 Ukraine
    gazetteer_test.txt 32 33 Weißrussland
    gazetteer_test.txt 34 35 Weissrussland
    gazetteer_test.txt 36 37 Abchasien
    gazetteer_test.txt 38 39 Akmola
    gazetteer_test.txt 40 41 Aktjubinsk
    gazetteer_test.txt 45 46 Gurjew
    gazetteer_test.txt 47 48 Karaganda
    gazetteer_test.txt 49 50 Kostai
    gazetteer_test.txt 51 52 Ostkasachstan
    gazetteer_test.txt 53 54 Sudkasachstan
    gazetteer_test.txt 55 56 Siidkasachstan
    gazetteer_test.txt 57 58 DshalaLAbad
    gazetteer_test.txt 59 60 Frunse
    gazetteer_test.txt 61 62 Osch
    gazetteer_test.txt 63 64 Basarabeasca
    gazetteer_test.txt 65 66 Adygejien
    gazetteer_test.txt 67 68 Altai
    gazetteer_test.txt 69 70 Archangelsk
    gazetteer_test.txt 71 72 Astrachan
    gazetteer_test.txt 73 74 Baschkirien
    gazetteer_test.txt 75 76 Brjansk
    gazetteer_test.txt 77 78 Burjatien
    gazetteer_test.txt 79 80 Dagestan
    gazetteer_test.txt 81 82 Gorki
    gazetteer_test.txt 86 87 Irkutsk
    gazetteer_test.txt 88 89 Iwanowo
    gazetteer_test.txt 90 91 Jaroslawl
    gazetteer_test.txt 92 93 KabardinienBalkarien
    gazetteer_test.txt 94 95 Kalinin
    gazetteer_test.txt 96 97 Kaliningrad
    gazetteer_test.txt 98 99 Kalmykien
    gazetteer_test.txt 100 101 Kaluga
    gazetteer_test.txt 102 103 KaratschaiTscherkessien
    gazetteer_test.txt 104 105 Karelien
    gazetteer_test.txt 106 107 Kemerowo
    gazetteer_test.txt 108 109 Kislar
    gazetteer_test.txt 110 111 Kingissepp
    gazetteer_test.txt 112 113 Kirow
    gazetteer_test.txt 114 115 Komi
    gazetteer_test.txt 116 117 Krasnodar
    gazetteer_test.txt 118 119 Krasnoyarsk
    gazetteer_test.txt 120 121 Krim
    gazetteer_test.txt 122 123 Kuibyschew
    gazetteer_test.txt 124 125 Kurgan
    gazetteer_test.txt 126 127 Kursk
    gazetteer_test.txt 128 129 Leningrad
    gazetteer_test.txt 133 134 Molotow
    gazetteer_test.txt 135 136 Mordowien
    gazetteer_test.txt 137 138 Moskau
    gazetteer_test.txt 139 140 Murmansk
    gazetteer_test.txt 141 142 Nordossetien
    gazetteer_test.txt 143 144 Nowgorod
    gazetteer_test.txt 145 146 Nowosibirsk
    gazetteer_test.txt 147 148 Omsk
    gazetteer_test.txt 149 150 Ordshonikidse
    gazetteer_test.txt 151 152 Orjol
    gazetteer_test.txt 153 154 Oijol
    gazetteer_test.txt 155 156 Pensa
    gazetteer_test.txt 157 158 Perm
    gazetteer_test.txt 159 160 Primorje
    gazetteer_test.txt 161 162 Pskow
    gazetteer_test.txt 163 164 Rjasan
    gazetteer_test.txt 169 170 Saratow
    gazetteer_test.txt 171 172 Smolensk
    gazetteer_test.txt 173 174 Stalingrad
    gazetteer_test.txt 175 176 Stawropol
    gazetteer_test.txt 177 178 Swerdlowsk
    gazetteer_test.txt 179 180 Tambow
    gazetteer_test.txt 181 182 Tatarstan
    gazetteer_test.txt 183 184 Tjumen
    gazetteer_test.txt 185 186 Tula
    gazetteer_test.txt 190 191 Udmurtien
    gazetteer_test.txt 192 193 Uljanowsk
    gazetteer_test.txt 194 195 Tscheljabinsk
    gazetteer_test.txt 196 197 Tscheijabinsk
    gazetteer_test.txt 198 199 Tscherkessien
    gazetteer_test.txt 200 201 TschetschenoInguschetien
    gazetteer_test.txt 202 203 Tschkalow
    gazetteer_test.txt 204 205 Tschuwaschien
    gazetteer_test.txt 206 207 Wladimir
    gazetteer_test.txt 208 209 Wologda
    gazetteer_test.txt 210 211 Woronesh
    gazetteer_test.txt 212 213 Aschchabad
    gazetteer_test.txt 214 215 Andishan
    gazetteer_test.txt 216 217 Ferga
    gazetteer_test.txt 218 219 Taschkent
    gazetteer_test.txt 220 221 Taschkentj
    gazetteer_test.txt 222 223 Charkow
    gazetteer_test.txt 224 225 Chmelnizki
    gazetteer_test.txt 226 227 Dnepropetrowsk
    gazetteer_test.txt 228 229 Dnepropetrovsk
    gazetteer_test.txt 230 231 Drogobytsch
    gazetteer_test.txt 232 233 KamenezPodolski
    gazetteer_test.txt 234 235 Kiew
    gazetteer_test.txt 236 237 Kirowograd
    gazetteer_test.txt 238 239 Lwow
    gazetteer_test.txt 240 241 Nikolajew
    gazetteer_test.txt 242 243 Odessa
    gazetteer_test.txt 244 245 Poltawa
    gazetteer_test.txt 246 247 Rowno
    gazetteer_test.txt 248 249 Saporoshje
    gazetteer_test.txt 250 251 Shitomir
    gazetteer_test.txt 252 253 Stalino
    gazetteer_test.txt 254 255 Stanislaw
    gazetteer_test.txt 256 257 Sumy
    gazetteer_test.txt 261 262 Tschernigow
    gazetteer_test.txt 263 264 Winniza
    gazetteer_test.txt 265 266 Wolynien
    gazetteer_test.txt 267 268 Woroschilowgrad
    gazetteer_test.txt 269 270 Gomel
    gazetteer_test.txt 271 272 Grodno
    gazetteer_test.txt 273 274 Minsk
    gazetteer_test.txt 275 276 Mogiljow
    gazetteer_test.txt 277 278 Pinsk
    gazetteer_test.txt 279 280 PoLessje
    gazetteer_test.txt 281 282 Polozk
    gazetteer_test.txt 283 284 Wilejka
    gazetteer_test.txt 285 286 Witebsk
    gazetteer_test.txt 287 288 Alawerdi
    gazetteer_test.txt 289 290 Arthik
    gazetteer_test.txt 291 292 Jerewan
    gazetteer_test.txt 293 294 Oktemberjan
    gazetteer_test.txt 295 296 Sewan
    gazetteer_test.txt 297 298 Talin
    gazetteer_test.txt 299 300 Chanlar
    gazetteer_test.txt 301 302 Chilly
    gazetteer_test.txt 303 304 Daschkesan
    gazetteer_test.txt 305 306 Nucha
    gazetteer_test.txt 307 308 Samuch
    gazetteer_test.txt 310 311 Baku
    gazetteer_test.txt 313 314 Kirowabad
    gazetteer_test.txt 315 316 Harjumaa
    gazetteer_test.txt 318 319 Tallinn
    gazetteer_test.txt 320 321 Paide
    gazetteer_test.txt 322 323 Parnu
    gazetteer_test.txt 324 325 Raplamaa
    gazetteer_test.txt 326 327 Valga
    gazetteer_test.txt 328 329 Otschamtschira
    gazetteer_test.txt 330 331 Agbulach
    gazetteer_test.txt 332 333 Macharadse
    gazetteer_test.txt 334 335 Tbilissi
    gazetteer_test.txt 336 337 ZaLendshicha
    gazetteer_test.txt 338 339 Zchaltubo
    gazetteer_test.txt 340 341 Wischnjowka
    gazetteer_test.txt 342 343 TaLdykorgan
    gazetteer_test.txt 344 345 Makat
    gazetteer_test.txt 346 347 BalchaschStadt
    gazetteer_test.txt 348 349 Karsakpai
    gazetteer_test.txt 350 351 Leninogorsk
    gazetteer_test.txt 352 353 Syrjanowsk
    gazetteer_test.txt 354 355 Lenger
    gazetteer_test.txt 356 357 Pachtaaral
    gazetteer_test.txt 358 359 Turkestan
    gazetteer_test.txt 360 361 TaschKumyr
    gazetteer_test.txt 362 363 Kemin
    gazetteer_test.txt 364 365 Bauska
    gazetteer_test.txt 366 367 Cesis
    gazetteer_test.txt 368 369 Jekabpils
    gazetteer_test.txt 370 371 Jelgava
    gazetteer_test.txt 372 373 Liepaja
    gazetteer_test.txt 374 375 Ogre
    gazetteer_test.txt 376 377 Riga
    gazetteer_test.txt 378 379 Saldus
    gazetteer_test.txt 380 381 Talsi
    gazetteer_test.txt 382 383 Talsi
    gazetteer_test.txt 385 386 Tukums
    gazetteer_test.txt 387 388 Akmene
    gazetteer_test.txt 389 390 Kaus
    gazetteer_test.txt 391 392 Siauliai
    gazetteer_test.txt 393 394 Vilkaviskis
    gazetteer_test.txt 395 396 Kischinjow
    gazetteer_test.txt 401 402 BaruL
    gazetteer_test.txt 403 404 Sorokino
    gazetteer_test.txt 405 406 Troizkoje
    gazetteer_test.txt 407 408 Krasnoborsk
    gazetteer_test.txt 409 410 Oneshski
    gazetteer_test.txt 411 412 Plessezk
    gazetteer_test.txt 413 414 Primorski
    gazetteer_test.txt 415 416 Wolodarski
    gazetteer_test.txt 417 418 Belorezk
    gazetteer_test.txt 419 420 Birsk
    gazetteer_test.txt 421 422 Djatkowo
    gazetteer_test.txt 423 424 wlja
    gazetteer_test.txt 425 426 Potschep
    gazetteer_test.txt 427 428 Susemka
    gazetteer_test.txt 429 430 Trubtschewsk
    gazetteer_test.txt 431 432 Iwolginsk
    gazetteer_test.txt 433 434 PribaikalskiKreis
    gazetteer_test.txt 435 436 Sa'igrajewo
    gazetteer_test.txt 437 438 Sai'grajewo
    gazetteer_test.txt 439 440 Selenga
    gazetteer_test.txt 441 442 Tarbagatai
    gazetteer_test.txt 443 444 Buiksk
    gazetteer_test.txt 445 446 Balach
    gazetteer_test.txt 447 448 Bogorodsk
    gazetteer_test.txt 449 450 Bor
    gazetteer_test.txt 451 452 Dsershinsk
    gazetteer_test.txt 453 454 Linda
    gazetteer_test.txt 455 456 Kulebaki
    gazetteer_test.txt 457 458 waschino
    gazetteer_test.txt 459 460 Schachunja
    gazetteer_test.txt 461 462 Tonschajewo
    gazetteer_test.txt 463 464 Tschistoje
    gazetteer_test.txt 465 466 Uren
    gazetteer_test.txt 467 468 Worotynez
    gazetteer_test.txt 469 470 Sljudjanka
    gazetteer_test.txt 474 475 Jurjewez
    gazetteer_test.txt 476 477 Jusha
    gazetteer_test.txt 478 479 Kirshatsch
    gazetteer_test.txt 480 481 Leshnewo
    gazetteer_test.txt 482 483 Palech
    gazetteer_test.txt 484 485 Sereda
    gazetteer_test.txt 486 487 Tejkowo
    gazetteer_test.txt 488 489 Brejtowo
    gazetteer_test.txt 490 491 Nerechta
    gazetteer_test.txt 492 493 PereslawlSalesski
    gazetteer_test.txt 494 495 UgLitsch
    gazetteer_test.txt 496 497 ltschik
    gazetteer_test.txt 498 499 Firowo
    gazetteer_test.txt 500 501 Mednoje
    gazetteer_test.txt 502 503 Rshew
    gazetteer_test.txt 504 505 Sawidowo
    gazetteer_test.txt 506 507 Spirowo
    gazetteer_test.txt 508 509 Torshok
    gazetteer_test.txt 513 514 Lagan
    gazetteer_test.txt 515 516 Wyssokinitschi
    gazetteer_test.txt 517 518 MikojanKreis
    gazetteer_test.txt 519 520 UstDsheguta
    gazetteer_test.txt 521 522 Belomorsk
    gazetteer_test.txt 523 524 Kalewaly
    gazetteer_test.txt 525 526 Medweshjegorsk
    gazetteer_test.txt 527 528 Pitkaranta
    gazetteer_test.txt 529 530 Prioneshski
    gazetteer_test.txt 531 532 Pudosh
    gazetteer_test.txt 533 534 Segesha
    gazetteer_test.txt 535 536 Wolossowo
    gazetteer_test.txt 537 538 Kai
    gazetteer_test.txt 539 540 Kilmes
    gazetteer_test.txt 541 542 Werchnekamski
    gazetteer_test.txt 546 547 Knjashpogost
    gazetteer_test.txt 548 549 UstWym
    gazetteer_test.txt 550 551 Beloretschensk
    gazetteer_test.txt 552 553 Gelendshik
    gazetteer_test.txt 554 555 Krasnoarmejskaja
    gazetteer_test.txt 556 557 Kuschtschewskaja
    gazetteer_test.txt 558 559 Neftegorsk
    gazetteer_test.txt 560 561 Pawlowskaja
    gazetteer_test.txt 562 563 Sewerskaja
    gazetteer_test.txt 564 565 Sowetskaja
    gazetteer_test.txt 566 567 Uspenskoje
    gazetteer_test.txt 568 569 Aluschta
    gazetteer_test.txt 570 571 Balaklawa
    gazetteer_test.txt 572 573 Bachtschissarai
    gazetteer_test.txt 574 575 Jalta
    gazetteer_test.txt 576 577 JaLtaStadt
    gazetteer_test.txt 578 579 KarassuBasar
    gazetteer_test.txt 580 581 Kolai
    gazetteer_test.txt 582 583 Krasnogwardejskoje
    gazetteer_test.txt 584 585 Krasnoperekopsk
    gazetteer_test.txt 586 587 MajakSalynski
    gazetteer_test.txt 588 589 Saki
    gazetteer_test.txt 590 591 Seitlerski
    gazetteer_test.txt 592 593 SewastopolStadt
    gazetteer_test.txt 594 595 Simferopol
    gazetteer_test.txt 599 600 Sudak
    gazetteer_test.txt 601 602 Suja
    gazetteer_test.txt 603 604 MolotowKreis
    gazetteer_test.txt 605 606 Schigony
    gazetteer_test.txt 607 608 Shiguijowsk
    gazetteer_test.txt 609 610 GLuschkowo
    gazetteer_test.txt 611 612 Mikojanowka
    gazetteer_test.txt 613 614 Schebekino
    gazetteer_test.txt 615 616 Borowitschi
    gazetteer_test.txt 617 618 Ljubytino
    gazetteer_test.txt 625 626 Okulowka
    gazetteer_test.txt 627 628 Opetschenski
    gazetteer_test.txt 629 630 Pargolowo
    gazetteer_test.txt 631 632 Pestowo
    gazetteer_test.txt 633 634 Podporoshje
    gazetteer_test.txt 635 636 Sluzk
    gazetteer_test.txt 637 638 Tichwin
    gazetteer_test.txt 639 640 Utorgosch
    gazetteer_test.txt 641 642 Wolchow
    gazetteer_test.txt 643 644 Wsewoloshsk
    gazetteer_test.txt 645 646 JoschkarOla
    gazetteer_test.txt 647 648 Jurino
    gazetteer_test.txt 649 650 Kilemary
    gazetteer_test.txt 651 652 KiseLStadt
    gazetteer_test.txt 653 654 Kungur
    gazetteer_test.txt 655 656 MolotowStadt
    gazetteer_test.txt 657 658 Ochansk
    gazetteer_test.txt 659 660 Solikamsk
    gazetteer_test.txt 661 662 TschussowoiStadt
    gazetteer_test.txt 666 667 Temnikow
    gazetteer_test.txt 668 669 Balaschicha
    gazetteer_test.txt 670 671 Istra
    gazetteer_test.txt 672 673 Kaschira
    gazetteer_test.txt 674 675 Kolom
    gazetteer_test.txt 676 677 Krasnogorsk
    gazetteer_test.txt 678 679 Krasja
    gazetteer_test.txt 681 682 Krasja
    gazetteer_test.txt 684 685 Kriwandino
    gazetteer_test.txt 686 687 Leninski
    gazetteer_test.txt 688 689 Moshaisk
    gazetteer_test.txt 690 691 Mytischtschi
    gazetteer_test.txt 692 693 roFominsk
    gazetteer_test.txt 694 695 Nowopetrowskoje
    gazetteer_test.txt 696 697 Osjory
    gazetteer_test.txt 698 699 Reutow
    gazetteer_test.txt 702 703 Kutschino
    gazetteer_test.txt 704 705 Rusa
    gazetteer_test.txt 706 707 Schatura
    gazetteer_test.txt 708 709 Schtscholkowo
    gazetteer_test.txt 710 711 Solnetschnogorsk
    gazetteer_test.txt 712 713 StalinogorskStadt
    gazetteer_test.txt 714 715 Swenigorod
    gazetteer_test.txt 716 717 Uchtomski
    gazetteer_test.txt 718 719 Uwarowka
    gazetteer_test.txt 720 721 Wolokolamsk
    gazetteer_test.txt 722 723 Kirowsk
    gazetteer_test.txt 724 725 Kola
    gazetteer_test.txt 726 727 Dargkoch
    gazetteer_test.txt 728 729 Digora
    gazetteer_test.txt 730 731 AnsheroSudshensk
    gazetteer_test.txt 732 733 Assino
    gazetteer_test.txt 734 735 Gurjewsk
    gazetteer_test.txt 736 737 Jurga
    gazetteer_test.txt 738 739 Kusedejewo
    gazetteer_test.txt 740 741 Taiga
    gazetteer_test.txt 742 743 Taschtagol
    gazetteer_test.txt 744 745 Tjashinski
    gazetteer_test.txt 746 747 Apasjenkowskoje
    gazetteer_test.txt 748 749 Gorjatschewodski
    gazetteer_test.txt 750 751 Kursawka
    gazetteer_test.txt 752 753 Nowoalexandrowsk
    gazetteer_test.txt 754 755 Petrowskoje
    gazetteer_test.txt 756 757 Komaritschi
    gazetteer_test.txt 758 759 Urizki
    gazetteer_test.txt 766 767 Mokschan
    gazetteer_test.txt 768 769 Gdow
    gazetteer_test.txt 770 771 Dankow
    gazetteer_test.txt 772 773 Kawerino
    gazetteer_test.txt 774 775 Lebedjan
    gazetteer_test.txt 779 780 Rybnoje
    gazetteer_test.txt 781 782 SoLotschinski
    gazetteer_test.txt 783 784 SpassKLepiki
    gazetteer_test.txt 789 790 Kurgan
    gazetteer_test.txt 791 792 NowoschachtinskStadt
    gazetteer_test.txt 793 794 Oktjabrski
    gazetteer_test.txt 795 796 Remontnoje
    gazetteer_test.txt 797 798 Simowniki
    gazetteer_test.txt 799 800 Swerjewo
    gazetteer_test.txt 801 802 Atkarsk
    gazetteer_test.txt 803 804 Kamenka
    gazetteer_test.txt 805 806 Krasnopartisansld
    gazetteer_test.txt 807 808 Krasny
    gazetteer_test.txt 810 811 Rtischtschewo
    gazetteer_test.txt 812 813 Tatischtschewo
    gazetteer_test.txt 814 815 Woroschilowsk
    gazetteer_test.txt 816 817 Gshatsk
    gazetteer_test.txt 818 819 Isdeschkowo
    gazetteer_test.txt 820 821 Jarzewo
    gazetteer_test.txt 822 823 Krasny
    gazetteer_test.txt 824 825 Tumanowo
    gazetteer_test.txt 826 827 Balyklej
    gazetteer_test.txt 828 829 Frolowo
    gazetteer_test.txt 830 831 Gorodischtsche
    gazetteer_test.txt 832 833 Kotelnikowo
    gazetteer_test.txt 834 835 Krasja
    gazetteer_test.txt 837 838 Georgijewsk
    gazetteer_test.txt 839 840 Isobilny
    gazetteer_test.txt 841 842 Suworowskaja
    gazetteer_test.txt 843 844 Alapajewsk
    gazetteer_test.txt 845 846 Aramil
    gazetteer_test.txt 847 848 AsbestStadt
    gazetteer_test.txt 853 854 BerjosowskiStadt
    gazetteer_test.txt 855 856 Iss
    gazetteer_test.txt 857 858 Iwdel
    gazetteer_test.txt 859 860 Jegorschino
    gazetteer_test.txt 861 862 KirowgradStadt
    gazetteer_test.txt 863 864 Kirowgrad
    gazetteer_test.txt 865 866 Krasnoufimsk
    gazetteer_test.txt 867 868 Newjansk
    gazetteer_test.txt 878 879 PoLewskoi
    gazetteer_test.txt 880 881 Resh
    gazetteer_test.txt 882 883 RewdaStadt
    gazetteer_test.txt 884 885 Sysert
    gazetteer_test.txt 886 887 Tugulym
    gazetteer_test.txt 891 892 Bondjushski
    gazetteer_test.txt 893 894 Kukmor
    gazetteer_test.txt 895 896 Nurlaty
    gazetteer_test.txt 897 898 Takanysch
    gazetteer_test.txt 899 900 Sawodoukowsk
    gazetteer_test.txt 901 902 Alexin
    gazetteer_test.txt 903 904 BogorodizkStadt
    gazetteer_test.txt 905 906 Bolochowo
    gazetteer_test.txt 907 908 Donskoi
    gazetteer_test.txt 909 910 Jepifan
    gazetteer_test.txt 911 912 Kimowsk
    gazetteer_test.txt 913 914 Laptewo
    gazetteer_test.txt 915 916 Mordwess
    gazetteer_test.txt 917 918 Schtschokino
    gazetteer_test.txt 919 920 Towarkowski
    gazetteer_test.txt 921 922 Tschern
    gazetteer_test.txt 923 924 TulaStadt
    gazetteer_test.txt 925 926 Uslowaja
    gazetteer_test.txt 927 928 Pudem
    gazetteer_test.txt 929 930 Uwa
    gazetteer_test.txt 931 932 Tscherdakly
    gazetteer_test.txt 933 934 Jetkul
    gazetteer_test.txt 935 936 Kussa
    gazetteer_test.txt 937 938 Minjar
    gazetteer_test.txt 939 940 Satka
    gazetteer_test.txt 944 945 Atschaluki
    gazetteer_test.txt 946 947 AtschchoiMartan
    gazetteer_test.txt 948 949 dteretschnoje
    gazetteer_test.txt 950 951 Prigorodny
    gazetteer_test.txt 952 953 UrusMartan
    gazetteer_test.txt 954 955 Busuluk
    gazetteer_test.txt 956 957 KosLowka
    gazetteer_test.txt 958 959 GusChrustalny
    gazetteer_test.txt 960 961 Kameschkowo
    gazetteer_test.txt 962 963 Kurlowski
    gazetteer_test.txt 964 965 Sudogda
    gazetteer_test.txt 966 967 Wjasniki
    gazetteer_test.txt 968 969 Tschagoda
    gazetteer_test.txt 970 971 Tscherepowez
    gazetteer_test.txt 972 973 UstKubinski
    gazetteer_test.txt 974 975 Grjasi
    gazetteer_test.txt 976 977 JelanKolenowski
    gazetteer_test.txt 978 979 Dshalalkuduk
    gazetteer_test.txt 980 981 Isbaskan
    gazetteer_test.txt 982 983 Begowat
    gazetteer_test.txt 984 985 Tschis
    gazetteer_test.txt 986 987 Tschirtschik
    gazetteer_test.txt 988 989 IBogoduchow
    gazetteer_test.txt 990 991 Kegitschowka
    gazetteer_test.txt 995 996 Polonnoje
    gazetteer_test.txt 997 998 Baryschewka
    gazetteer_test.txt 999 1000 Beresan
    gazetteer_test.txt 1001 1002 Christinowka
    gazetteer_test.txt 1003 1004 Jagotin
    gazetteer_test.txt 1005 1006 Alexandrowka
    gazetteer_test.txt 1008 1009 Wiska
    gazetteer_test.txt 1010 1011 Busk
    gazetteer_test.txt 1015 1016 Gaiworon
    gazetteer_test.txt 1017 1018 Gruschka
    gazetteer_test.txt 1019 1020 Globino
    gazetteer_test.txt 1021 1022 Lochwiza
    gazetteer_test.txt 1023 1024 Genitschesk
    gazetteer_test.txt 1025 1026 Michajlowka
    gazetteer_test.txt 1027 1028 Berditschew
    gazetteer_test.txt 1029 1030 PopoLnja
    gazetteer_test.txt 1031 1032 Charzyssk
    gazetteer_test.txt 1033 1034 GorLowkaStadt
    gazetteer_test.txt 1035 1036 Krasnoarmejsk
    gazetteer_test.txt 1037 1038 MakejewkaStadt
    gazetteer_test.txt 1039 1040 Selidowo
    gazetteer_test.txt 1041 1042 Jampot
    gazetteer_test.txt 1043 1044 Nedrigaitow
    gazetteer_test.txt 1045 1046 Utjanowka
    gazetteer_test.txt 1047 1048 Neshin
    gazetteer_test.txt 1049 1050 PriLuki
    gazetteer_test.txt 1051 1052 Litin
    gazetteer_test.txt 1053 1054 Turbow
    gazetteer_test.txt 1055 1056 Tywrow
    gazetteer_test.txt 1057 1058 Perwomaisk
    gazetteer_test.txt 1060 1061 Krasny
    gazetteer_test.txt 1064 1065 Uwarowitschi
    gazetteer_test.txt 1066 1067 WoLkowysk
    gazetteer_test.txt 1068 1069 Puchowitschi
    gazetteer_test.txt 1070 1071 Saslawl
    gazetteer_test.txt 1072 1073 Beresino
    gazetteer_test.txt 1074 1075 Bobruisk
    gazetteer_test.txt 1076 1077 Ganzewitschi
    gazetteer_test.txt 1078 1079 Orscha
    gazetteer_test.txt 1080 1081 Sirotino
    gazetteer_test.txt 1082 1083 Ejlar
    gazetteer_test.txt 1084 1085 Armlu
    gazetteer_test.txt 1086 1087 Ararat
    gazetteer_test.txt 1088 1089 Etschmiadsin
    gazetteer_test.txt 1090 1091 Molotja
    gazetteer_test.txt 1092 1093 Kirowakan
    gazetteer_test.txt 1095 1096 Talin
    gazetteer_test.txt 1097 1098 Tumanjan
    gazetteer_test.txt 1099 1100 Alabaschly
    gazetteer_test.txt 1101 1102 Bajan
    gazetteer_test.txt 1103 1104 Baku
    gazetteer_test.txt 1105 1106 Kugitschu
    gazetteer_test.txt 1108 1109 Daschkesan
    gazetteer_test.txt 1111 1112 Daschkesan
    gazetteer_test.txt 1113 1114 Karadag
    gazetteer_test.txt 1115 1116 Kirowobad
    gazetteer_test.txt 1117 1118 Kirowabad
    gazetteer_test.txt 1119 1120 Kysyldsha
    gazetteer_test.txt 1121 1122 Kyrychly
    gazetteer_test.txt 1123 1124 Mingetschewir
    gazetteer_test.txt 1125 1126 Quba
    gazetteer_test.txt 1127 1128 Sabuntschi
    gazetteer_test.txt 1129 1130 Saljan
    gazetteer_test.txt 1131 1132 Schemacha
    gazetteer_test.txt 1133 1134 Sych
    gazetteer_test.txt 1135 1136 Adshikent
    gazetteer_test.txt 1137 1138 Sumgait
    gazetteer_test.txt 1139 1140 Ahtme
    gazetteer_test.txt 1141 1142 Loksa
    gazetteer_test.txt 1143 1144 Johvi
    gazetteer_test.txt 1145 1146 Kivioli
    gazetteer_test.txt 1147 1148 KohtlaJarve
    gazetteer_test.txt 1149 1150 Kuttejou
    gazetteer_test.txt 1151 1152 Lehtse
    gazetteer_test.txt 1153 1154 Maardu
    gazetteer_test.txt 1155 1156 Narva
    gazetteer_test.txt 1157 1158 JarvaJaani
    gazetteer_test.txt 1159 1160 Lavassaare
    gazetteer_test.txt 1161 1162 Rakvere
    gazetteer_test.txt 1163 1164 Jarvakandi
    gazetteer_test.txt 1165 1166 Sonda
    gazetteer_test.txt 1167 1168 Tallinn
    gazetteer_test.txt 1169 1170 Tammiku
    gazetteer_test.txt 1171 1172 Tapa
    gazetteer_test.txt 1173 1174 Tartu
    gazetteer_test.txt 1175 1176 Ulila
    gazetteer_test.txt 1177 1178 Loosi
    gazetteer_test.txt 1179 1180 Nudrezowo
    gazetteer_test.txt 1181 1182 Podra
    gazetteer_test.txt 1183 1184 Kingu
    gazetteer_test.txt 1185 1186 Vasalemma
    gazetteer_test.txt 1187 1188 Vontkula
    gazetteer_test.txt 1189 1190 Suchumi
    gazetteer_test.txt 1191 1192 Kelasuri
    gazetteer_test.txt 1193 1194 Miussera
    gazetteer_test.txt 1195 1196 Tkwartscheli
    gazetteer_test.txt 1197 1198 Manglissi
    gazetteer_test.txt 1199 1200 Awtschala
    gazetteer_test.txt 1201 1202 Bachmaro
    gazetteer_test.txt 1207 1208 Bolnissi
    gazetteer_test.txt 1209 1210 Bulutschauri
    gazetteer_test.txt 1211 1212 ChezerTeesowchos
    gazetteer_test.txt 1216 1217 Dsegwi
    gazetteer_test.txt 1218 1219 Dwiri
    gazetteer_test.txt 1220 1221 Ingiri
    gazetteer_test.txt 1222 1223 Kluchori
    gazetteer_test.txt 1224 1225 Ksani
    gazetteer_test.txt 1226 1227 KutaĆÆssi
    gazetteer_test.txt 1228 1229 KutaTssi
    gazetteer_test.txt 1234 1235 Kutaissi
    gazetteer_test.txt 1236 1237 Kwareli
    gazetteer_test.txt 1238 1239 Sairme
    gazetteer_test.txt 1240 1241 Mukusani
    gazetteer_test.txt 1242 1243 wtLugi
    gazetteer_test.txt 1244 1245 Poti
    gazetteer_test.txt 1246 1247 Rustawi
    gazetteer_test.txt 1248 1249 Samgori
    gazetteer_test.txt 1250 1251 Sugdidi
    gazetteer_test.txt 1252 1253 Supsa
    gazetteer_test.txt 1254 1255 Barmaksis
    gazetteer_test.txt 1262 1263 Tk
    gazetteer_test.txt 1264 1265 Tschaladidi
    gazetteer_test.txt 1266 1267 Tschubrin
    gazetteer_test.txt 1268 1269 Ureki
    gazetteer_test.txt 1270 1271 Wedjanka
    gazetteer_test.txt 1272 1273 Zulukidse
    gazetteer_test.txt 1274 1275 Atbassar
    gazetteer_test.txt 1276 1277 Jessil
    gazetteer_test.txt 1278 1279 Koluton
    gazetteer_test.txt 1283 1284 Makinka
    gazetteer_test.txt 1285 1286 TekeLi
    gazetteer_test.txt 1287 1288 Baischoss
    gazetteer_test.txt 1289 1290 DshambuL
    gazetteer_test.txt 1291 1292 Agadyr
    gazetteer_test.txt 1293 1294 Ar
    gazetteer_test.txt 1295 1296 Kounradski
    gazetteer_test.txt 1304 1305 KaragandaSortirowotschja
    gazetteer_test.txt 1306 1307 Dsheskasgan
    gazetteer_test.txt 1308 1309 Kokusek
    gazetteer_test.txt 1310 1311 MaiKuduk
    gazetteer_test.txt 1312 1313 Nurinskaja
    gazetteer_test.txt 1314 1315 Saran
    gazetteer_test.txt 1316 1317 SpasskiWerkssiedlung
    gazetteer_test.txt 1318 1319 Temirtau
    gazetteer_test.txt 1320 1321 Dshetygara
    gazetteer_test.txt 1322 1323 Kuschmurun
    gazetteer_test.txt 1324 1325 Kysylorda
    gazetteer_test.txt 1326 1327 Irtyschgesstroi
    gazetteer_test.txt 1328 1329 Beloussowka
    gazetteer_test.txt 1330 1331 Jerofejewka
    gazetteer_test.txt 1332 1333 Syrjanowskoje
    gazetteer_test.txt 1334 1335 UstKamenogorsk
    gazetteer_test.txt 1336 1337 Syrdarjinskaja
    gazetteer_test.txt 1338 1339 Tschimkent
    gazetteer_test.txt 1340 1341 Atschissaj
    gazetteer_test.txt 1342 1343 Kantagi
    gazetteer_test.txt 1344 1345 KjokDshangak
    gazetteer_test.txt 1346 1347 DsheLAryk
    gazetteer_test.txt 1348 1349 KisKyja
    gazetteer_test.txt 1350 1351 Bystrowka
    gazetteer_test.txt 1352 1353 Maimak
    gazetteer_test.txt 1354 1355 KysylKyja
    gazetteer_test.txt 1356 1357 Suljukta
    gazetteer_test.txt 1358 1359 Auce
    gazetteer_test.txt 1360 1361 Iecava
    gazetteer_test.txt 1362 1363 LIgatne
    gazetteer_test.txt 1364 1365 Daugavpils
    gazetteer_test.txt 1366 1367 Dzukste
    gazetteer_test.txt 1368 1369 Eglaine
    gazetteer_test.txt 1370 1371 Jaunjelgava
    gazetteer_test.txt 1372 1373 Krustpils
    gazetteer_test.txt 1374 1375 Garoza
    gazetteer_test.txt 1376 1377 Misa
    gazetteer_test.txt 1378 1379 Turmali
    gazetteer_test.txt 1380 1381 Jugla
    gazetteer_test.txt 1382 1383 Kraslava
    gazetteer_test.txt 1384 1385 Kuldiga
    gazetteer_test.txt 1386 1387 Pavilosta
    gazetteer_test.txt 1388 1389 Satinskoje
    gazetteer_test.txt 1390 1391 LTgatne
    gazetteer_test.txt 1392 1393 Murjani
    gazetteer_test.txt 1394 1395 Kegums
    gazetteer_test.txt 1396 1397 Olaine
    gazetteer_test.txt 1398 1399 Priedaine
    gazetteer_test.txt 1400 1401 Purmsati
    gazetteer_test.txt 1402 1403 Rampa
    gazetteer_test.txt 1404 1405 Rezekne
    gazetteer_test.txt 1406 1407 Balozi
    gazetteer_test.txt 1408 1409 Salaspils
    gazetteer_test.txt 1410 1411 Stopini
    gazetteer_test.txt 1412 1413 Broceni
    gazetteer_test.txt 1414 1415 Sarkandaugava
    gazetteer_test.txt 1416 1417 Skulte
    gazetteer_test.txt 1418 1419 Sloka
    gazetteer_test.txt 1420 1421 Suntazi
    gazetteer_test.txt 1422 1423 Stende
    gazetteer_test.txt 1424 1425 Taurupe
    gazetteer_test.txt 1429 1430 Valmiera
    gazetteer_test.txt 1431 1432 Ventspils
    gazetteer_test.txt 1433 1434 Bicionys
    gazetteer_test.txt 1435 1436 Gaideliai
    gazetteer_test.txt 1437 1438 Kaisiadorys
    gazetteer_test.txt 1439 1440 Ezerelis
    gazetteer_test.txt 1441 1442 Raudelino
    gazetteer_test.txt 1443 1444 Samaniai
    gazetteer_test.txt 1445 1446 Klaipeda
    gazetteer_test.txt 1447 1448 Kretinga
    gazetteer_test.txt 1449 1450 Mauruciai
    gazetteer_test.txt 1454 1455 Palemos
    gazetteer_test.txt 1456 1457 RadviLiskis
    gazetteer_test.txt 1458 1459 Taurage
    gazetteer_test.txt 1460 1461 Telsiai
    gazetteer_test.txt 1462 1463 Kybartai
    gazetteer_test.txt 1464 1465 Vilnius
    gazetteer_test.txt 1466 1467 Abaklia
    gazetteer_test.txt 1468 1469 Balti
    gazetteer_test.txt 1470 1471 Tiraspol
    gazetteer_test.txt 1472 1473 Orhei
    gazetteer_test.txt 1474 1475 Ungheni
    gazetteer_test.txt 1476 1477 Maikop
    gazetteer_test.txt 1478 1479 Tschesnokowka
    gazetteer_test.txt 1480 1481 Bisk
    gazetteer_test.txt 1482 1483 Blinowo
    gazetteer_test.txt 1484 1485 Rubzowsk
    gazetteer_test.txt 1486 1487 Newerowskaja
    gazetteer_test.txt 1488 1489 Sarinskaja
    gazetteer_test.txt 1490 1491 Schpagino
    gazetteer_test.txt 1492 1493 Smasnewo
    gazetteer_test.txt 1494 1495 Borowljanka
    gazetteer_test.txt 1496 1497 Jemza
    gazetteer_test.txt 1498 1499 Jerzewo
    gazetteer_test.txt 1500 1501 Jura
    gazetteer_test.txt 1502 1503 Kargopol
    gazetteer_test.txt 1504 1505 Kisema
    gazetteer_test.txt 1506 1507 Kostyljowo
    gazetteer_test.txt 1508 1509 Kotlas
    gazetteer_test.txt 1510 1511 Ustjewo
    gazetteer_test.txt 1512 1513 Molotowsk
    gazetteer_test.txt 1514 1515 Moschnoje
    gazetteer_test.txt 1516 1517 Njandoma
    gazetteer_test.txt 1518 1519 Oboserski
    gazetteer_test.txt 1520 1521 wolok
    gazetteer_test.txt 1522 1523 Podjuga
    gazetteer_test.txt 1524 1525 Solsa
    gazetteer_test.txt 1526 1527 Schalakuscha
    gazetteer_test.txt 1528 1529 Tschekamino
    gazetteer_test.txt 1530 1531 Welsk
    gazetteer_test.txt 1533 1534 Jar
    gazetteer_test.txt 1535 1536 Nikolskoje
    gazetteer_test.txt 1537 1538 Perwomaiski
    gazetteer_test.txt 1539 1540 Tumanny
    gazetteer_test.txt 1544 1545 Wladimirowka
    gazetteer_test.txt 1546 1547 Wolodarowka
    gazetteer_test.txt 1548 1549 Beljagusch
    gazetteer_test.txt 1550 1551 Inser
    gazetteer_test.txt 1552 1553 Nukatowo
    gazetteer_test.txt 1554 1555 Sorwicha
    gazetteer_test.txt 1556 1557 Karlaman
    gazetteer_test.txt 1558 1559 Manjawa
    gazetteer_test.txt 1560 1561 Tschernikowka
    gazetteer_test.txt 1562 1563 Tschernikowsk
    gazetteer_test.txt 1564 1565 Ufa
    gazetteer_test.txt 1566 1567 Besymjanka
    gazetteer_test.txt 1568 1569 Bijansk
    gazetteer_test.txt 1570 1571 Brjansk1
    gazetteer_test.txt 1572 1573 Brjansl<2
    gazetteer_test.txt 1574 1575 Brjansk2
    gazetteer_test.txt 1576 1577 Bytosch
    gazetteer_test.txt 1578 1579 Iwot
    gazetteer_test.txt 1580 1581 Star
    gazetteer_test.txt 1582 1583 Zementny
    gazetteer_test.txt 1584 1585 Karatschew
    gazetteer_test.txt 1586 1587 Kletnja
    gazetteer_test.txt 1588 1589 KLinzy
    gazetteer_test.txt 1590 1591 Altuchowo
    gazetteer_test.txt 1592 1593 Nowosybkow
    gazetteer_test.txt 1594 1595 Ordshonikidsegrad
    gazetteer_test.txt 1596 1597 Palushje
    gazetteer_test.txt 1598 1599 Pogreby
    gazetteer_test.txt 1600 1601 Ramassucha
    gazetteer_test.txt 1602 1603 Selzo
    gazetteer_test.txt 1604 1605 Kokorewka
    gazetteer_test.txt 1609 1610 Unetscha
    gazetteer_test.txt 1611 1612 Wygonitschi
    gazetteer_test.txt 1613 1614 Dshida
    gazetteer_test.txt 1615 1616 Gorchon
    gazetteer_test.txt 1617 1618 Gorodok
    gazetteer_test.txt 1619 1620 Sawodskoi
    gazetteer_test.txt 1621 1622 JushlagSiedlung
    gazetteer_test.txt 1623 1624 Nowoiljinsk
    gazetteer_test.txt 1625 1626 Onochoi
    gazetteer_test.txt 1627 1628 Pedshino
    gazetteer_test.txt 1629 1630 Turka
    gazetteer_test.txt 1631 1632 Sagustai
    gazetteer_test.txt 1633 1634 Surgalej
    gazetteer_test.txt 1635 1636 Schabur
    gazetteer_test.txt 1640 1641 Saudinski
    gazetteer_test.txt 1645 1646 Oronchoj
    gazetteer_test.txt 1647 1648 Selenduma
    gazetteer_test.txt 1652 1653 UlanUde
    gazetteer_test.txt 1657 1658 Chabarowsk
    gazetteer_test.txt 1659 1660 Karamachi
    gazetteer_test.txt 1661 1662 Derbent
    gazetteer_test.txt 1663 1664 Gedshuch
    gazetteer_test.txt 1665 1666 Isberbasch
    gazetteer_test.txt 1667 1668 Machatschkala
    gazetteer_test.txt 1669 1670 Mamedkala
    gazetteer_test.txt 1671 1672 Rubas
    gazetteer_test.txt 1673 1674 Arja
    gazetteer_test.txt 1675 1676 Awarijny
    gazetteer_test.txt 1677 1678 Prawdinsk
    gazetteer_test.txt 1679 1680 Oranki
    gazetteer_test.txt 1681 1682 Kershenez
    gazetteer_test.txt 1683 1684 Orlowo
    gazetteer_test.txt 1685 1686 Bystrucha
    gazetteer_test.txt 1687 1688 Pyra
    gazetteer_test.txt 1689 1690 Gluchaja
    gazetteer_test.txt 1691 1692 Igumnowo
    gazetteer_test.txt 1693 1694 Kiselicha
    gazetteer_test.txt 1695 1696 Kolchosny
    gazetteer_test.txt 1697 1698 Korelka
    gazetteer_test.txt 1699 1700 Krasnenki
    gazetteer_test.txt 1701 1702 Manturowo
    gazetteer_test.txt 1706 1707 Mostyrka
    gazetteer_test.txt 1708 1709 Mursizy
    gazetteer_test.txt 1710 1711 Tjoscha
    gazetteer_test.txt 1712 1713 Obchod
    gazetteer_test.txt 1714 1715 Sjawa
    gazetteer_test.txt 1716 1717 Scharja
    gazetteer_test.txt 1718 1719 Schemanicha
    gazetteer_test.txt 1720 1721 Sejma
    gazetteer_test.txt 1722 1723 Serebrjanka
    gazetteer_test.txt 1724 1725 Suchobeswodnoje
    gazetteer_test.txt 1726 1727 Tschornoje
    gazetteer_test.txt 1728 1729 Usta
    gazetteer_test.txt 1730 1731 Michailowski
    gazetteer_test.txt 1732 1733 Uwarowskaja
    gazetteer_test.txt 1734 1735 Rasneshje
    gazetteer_test.txt 1736 1737 Wyksa
    gazetteer_test.txt 1738 1739 Baischoss
    gazetteer_test.txt 1745 1746 Makat
    gazetteer_test.txt 1748 1749 Kazakhstan
    gazetteer_test.txt 1758 1759 Makat
    gazetteer_test.txt 1761 1762 Kazakhstan
    gazetteer_test.txt 1765 1766 RSFSR
    gazetteer_test.txt 1782 1783 Listwjanka
    gazetteer_test.txt 1787 1788 Taischet
    gazetteer_test.txt 1789 1790 Demidowo
    gazetteer_test.txt 1791 1792 Furmanow
    gazetteer_test.txt 1793 1794 Iwankowo
    gazetteer_test.txt 1795 1796 Michailowo
    gazetteer_test.txt 1797 1798 Mugrejewo
    gazetteer_test.txt 1799 1800 Talizy
    gazetteer_test.txt 1801 1802 Kineschma
    gazetteer_test.txt 1803 1804 Kochma
    gazetteer_test.txt 1805 1806 Komsomolsk
    gazetteer_test.txt 1807 1808 Kowrow
    gazetteer_test.txt 1809 1810 Petrowski
    gazetteer_test.txt 1811 1812 Rodniki
    gazetteer_test.txt 1813 1814 Schuja
    gazetteer_test.txt 1815 1816 Jakowlewskoje
    gazetteer_test.txt 1821 1822 Textilny
    gazetteer_test.txt 1823 1824 Witschuga
    gazetteer_test.txt 1825 1826 Iwkino
    gazetteer_test.txt 1827 1828 Chmelniki
    gazetteer_test.txt 1832 1833 Jakschanga
    gazetteer_test.txt 1834 1835 Kostroma
    gazetteer_test.txt 1836 1837 Lorn
    gazetteer_test.txt 1838 1839 Neja
    gazetteer_test.txt 1840 1841 Kosmynino
    gazetteer_test.txt 1842 1843 Perebory
    gazetteer_test.txt 1844 1845 Pereslawl
    gazetteer_test.txt 1846 1847 Rogosinino
    gazetteer_test.txt 1848 1849 Ussolje
    gazetteer_test.txt 1850 1851 Petrowsk
    gazetteer_test.txt 1852 1853 PriwoLshje
    gazetteer_test.txt 1854 1855 Rodionowo
    gazetteer_test.txt 1856 1857 Rybinsk
    gazetteer_test.txt 1858 1859 Schestichino
    gazetteer_test.txt 1863 1864 Semibratowo
    gazetteer_test.txt 1865 1866 Silnizy
    gazetteer_test.txt 1867 1868 Suprotiwny
    gazetteer_test.txt 1869 1870 Tichmenewo
    gazetteer_test.txt 1871 1872 Tutajew
    gazetteer_test.txt 1873 1874 Tschernizyno
    gazetteer_test.txt 1875 1876 WauLowo
    gazetteer_test.txt 1877 1878 Wspolje
    gazetteer_test.txt 1879 1880 AksautGretscheski
    gazetteer_test.txt 1881 1882 Kenshe
    gazetteer_test.txt 1883 1884 Akademitscheskaja
    gazetteer_test.txt 1885 1886 Beshezk
    gazetteer_test.txt 1887 1888 Bologoje
    gazetteer_test.txt 1889 1890 Emmaus
    gazetteer_test.txt 1894 1895 Kimry
    gazetteer_test.txt 1896 1897 Kokowo
    gazetteer_test.txt 1898 1899 Kuwschinowo
    gazetteer_test.txt 1900 1901 Leontjewo
    gazetteer_test.txt 1902 1903 Maksaticha
    gazetteer_test.txt 1904 1905 Malyschewo
    gazetteer_test.txt 1906 1907 rotschino
    gazetteer_test.txt 1908 1909 Nelidowo
    gazetteer_test.txt 1910 1911 Nowossokolniki
    gazetteer_test.txt 1912 1913 Ossetschenka
    gazetteer_test.txt 1914 1915 Ostaschkow
    gazetteer_test.txt 1916 1917 Poddubki
    gazetteer_test.txt 1918 1919 Ranzewo
    gazetteer_test.txt 1920 1921 Redkino
    gazetteer_test.txt 1922 1923 Konyschewo
    gazetteer_test.txt 1924 1925 Olenino
    gazetteer_test.txt 1926 1927 Selisharowo
    gazetteer_test.txt 1928 1929 Semzy
    gazetteer_test.txt 1930 1931 Wydropushsk
    gazetteer_test.txt 1935 1936 Dmitrowskoje
    gazetteer_test.txt 1937 1938 Dumanowo
    gazetteer_test.txt 1939 1940 Tschernogubowo
    gazetteer_test.txt 1944 1945 Udomlja
    gazetteer_test.txt 1949 1950 Krasnomaiski
    gazetteer_test.txt 1951 1952 Konigsberg
    gazetteer_test.txt 1959 1960 Gwardejsk
    gazetteer_test.txt 1961 1962 Insterburg
    gazetteer_test.txt 1963 1964 Kaukiemis
    gazetteer_test.txt 1965 1966 Metgethen
    gazetteer_test.txt 1967 1968 Pillau
    gazetteer_test.txt 1969 1970 Preu&ischEylau
    gazetteer_test.txt 1971 1972 Ragnit
    gazetteer_test.txt 1973 1974 Seckenburg
    gazetteer_test.txt 1975 1976 Tilsit
    gazetteer_test.txt 1977 1978 Trammen
    gazetteer_test.txt 1979 1980 Tschernjachowsk
    gazetteer_test.txt 1981 1982 Wehlau
    gazetteer_test.txt 1983 1984 UlanChol
    gazetteer_test.txt 1985 1986 Kanukowo
    gazetteer_test.txt 1987 1988 Fajansowaja
    gazetteer_test.txt 1989 1990 Kusmitschi
    gazetteer_test.txt 1991 1992 Ljudinowo
    gazetteer_test.txt 1993 1994 Malojaroslawez
    gazetteer_test.txt 1995 1996 Suchinitschi
    gazetteer_test.txt 1997 1998 DurowSowchos
    gazetteer_test.txt 1999 2000 Chumara
    gazetteer_test.txt 2001 2002 Tscherkessk
    gazetteer_test.txt 2003 2004 Washnoje
    gazetteer_test.txt 2005 2006 Malenga
    gazetteer_test.txt 2007 2008 Letneretschenski
    gazetteer_test.txt 2009 2010 Saliwy
    gazetteer_test.txt 2011 2012 Tegosero
    gazetteer_test.txt 2013 2014 Iljinskaja
    gazetteer_test.txt 2015 2016 Kepa
    gazetteer_test.txt 2017 2018 Kondopoga
    gazetteer_test.txt 2022 2023 arlahti
    gazetteer_test.txt 2024 2025 Pai
    gazetteer_test.txt 2026 2027 Petrosawodsk
    gazetteer_test.txt 2028 2029 Harlu
    gazetteer_test.txt 2030 2031 Laskela
    gazetteer_test.txt 2032 2033 Suojarvi
    gazetteer_test.txt 2037 2038 Derewjanka
    gazetteer_test.txt 2039 2040 Botschilowo
    gazetteer_test.txt 2041 2042 Kolowo
    gazetteer_test.txt 2043 2044 Kubowskaja
    gazetteer_test.txt 2045 2046 NowoStekljannoje
    gazetteer_test.txt 2047 2048 Pjalma
    gazetteer_test.txt 2049 2050 Porschta
    gazetteer_test.txt 2051 2052 Schala
    gazetteer_test.txt 2053 2054 Schalski
    gazetteer_test.txt 2055 2056 Tschernoretschenski
    gazetteer_test.txt 2057 2058 Petrowski
    gazetteer_test.txt 2060 2061 Polga
    gazetteer_test.txt 2062 2063 Uchta
    gazetteer_test.txt 2064 2065 Uuksu
    gazetteer_test.txt 2066 2067 Jurga1
    gazetteer_test.txt 2068 2069 Prokopjewsk
    gazetteer_test.txt 2070 2071 Stalinsk
    gazetteer_test.txt 2072 2073 Kikerino
    gazetteer_test.txt 2074 2075 Ardaschi
    gazetteer_test.txt 2076 2077 Besboshnik
    gazetteer_test.txt 2078 2079 Fosforitja
    gazetteer_test.txt 2080 2081 Ima
    gazetteer_test.txt 2082 2083 Werchnekamskaja
    gazetteer_test.txt 2084 2085 Latyschski
    gazetteer_test.txt 2086 2087 Loiga
    gazetteer_test.txt 2088 2089 Ljangassowo
    gazetteer_test.txt 2090 2091 Omutninsk
    gazetteer_test.txt 2092 2093 Posdino
    gazetteer_test.txt 2094 2095 Slobodskoi
    gazetteer_test.txt 2096 2097 Sosnowka
    gazetteer_test.txt 2098 2099 Stalja
    gazetteer_test.txt 2100 2101 Suslowka
    gazetteer_test.txt 2102 2103 Sosimski
    gazetteer_test.txt 2107 2108 WoshajeL
    gazetteer_test.txt 2109 2110 Lemju
    gazetteer_test.txt 2111 2112 Sewsheldorlag
    gazetteer_test.txt 2113 2114 Syktywkar
    gazetteer_test.txt 2115 2116 Sheschart
    gazetteer_test.txt 2117 2118 Adler
    gazetteer_test.txt 2119 2120 Apa
    gazetteer_test.txt 2121 2122 Apscheronsk
    gazetteer_test.txt 2123 2124 Armawir
    gazetteer_test.txt 2125 2126 Chadyshensk
    gazetteer_test.txt 2127 2128 Dshugba
    gazetteer_test.txt 2129 2130 Gluchari
    gazetteer_test.txt 2131 2132 Jurjewka
    gazetteer_test.txt 2133 2134 Mogilnoje
    gazetteer_test.txt 2135 2136 Kropotkin
    gazetteer_test.txt 2137 2138 Krymsk
    gazetteer_test.txt 2139 2140 Mogilny
    gazetteer_test.txt 2141 2142 Abchasskaja
    gazetteer_test.txt 2143 2144 Chadyshenskaa
    gazetteer_test.txt 2145 2146 Noworossisk
    gazetteer_test.txt 2147 2148 Ilski
    gazetteer_test.txt 2149 2150 Sotschi
    gazetteer_test.txt 2151 2152 Tichorezk
    gazetteer_test.txt 2153 2154 Tuapse
    gazetteer_test.txt 2155 2156 BogotoL
    gazetteer_test.txt 2160 2161 Belbek
    gazetteer_test.txt 2162 2163 Tai'r
    gazetteer_test.txt 2164 2165 Dshankoi
    gazetteer_test.txt 2166 2167 Feodossija
    gazetteer_test.txt 2168 2169 Inkerman
    gazetteer_test.txt 2173 2174 Alupka
    gazetteer_test.txt 2175 2176 Foros
    gazetteer_test.txt 2177 2178 Korei's
    gazetteer_test.txt 2179 2180 Liwadija
    gazetteer_test.txt 2181 2182 Oreanda
    gazetteer_test.txt 2183 2184 Partenit
    gazetteer_test.txt 2185 2186 Jewpatorija
    gazetteer_test.txt 2187 2188 Mariano
    gazetteer_test.txt 2189 2190 Kertsch
    gazetteer_test.txt 2194 2195 Bagerowo
    gazetteer_test.txt 2196 2197 BuLgak
    gazetteer_test.txt 2198 2199 Eschkine
    gazetteer_test.txt 2203 2204 Tamak
    gazetteer_test.txt 2205 2206 Sewastopol
    gazetteer_test.txt 2207 2208 Sevastopol
    gazetteer_test.txt 2209 2210 Katscha
    gazetteer_test.txt 2214 2215 Sirenj
    gazetteer_test.txt 2216 2217 Siwasch
    gazetteer_test.txt 2222 2223 Krasny
    gazetteer_test.txt 2224 2225 Koktebel
    gazetteer_test.txt 2230 2231 Otusy
    gazetteer_test.txt 2234 2235 Rosa
    gazetteer_test.txt 2236 2237 Ta'ir
    gazetteer_test.txt 2241 2242 Batraki
    gazetteer_test.txt 2249 2250 Kadej
    gazetteer_test.txt 2251 2252 Kinel
    gazetteer_test.txt 2253 2254 Krjash
    gazetteer_test.txt 2255 2256 Melekess
    gazetteer_test.txt 2257 2258 Otwashnoje
    gazetteer_test.txt 2259 2260 Nikolajewka
    gazetteer_test.txt 2261 2262 Pochwistnewo
    gazetteer_test.txt 2263 2264 Sabdowka
    gazetteer_test.txt 2265 2266 Petscherskoje
    gazetteer_test.txt 2267 2268 Solnoje
    gazetteer_test.txt 2269 2270 Solonez
    gazetteer_test.txt 2271 2272 Sysran
    gazetteer_test.txt 2273 2274 Schadrinsk
    gazetteer_test.txt 2275 2276 Belgorod
    gazetteer_test.txt 2277 2278 Blagodatenski
    gazetteer_test.txt 2279 2280 Derjugino
    gazetteer_test.txt 2281 2282 Fatesh
    gazetteer_test.txt 2283 2284 Tjotkino
    gazetteer_test.txt 2285 2286 Gotnja
    gazetteer_test.txt 2287 2288 ShurawLjowka
    gazetteer_test.txt 2289 2290 Obojanj
    gazetteer_test.txt 2291 2292 Ryschkowo
    gazetteer_test.txt 2293 2294 NowoTawoLshanka
    gazetteer_test.txt 2295 2296 Tros
    gazetteer_test.txt 2297 2298 Waluiki
    gazetteer_test.txt 2299 2300 Besborodowo
    gazetteer_test.txt 2301 2302 Boksitogorsk
    gazetteer_test.txt 2303 2304 Jegla
    gazetteer_test.txt 2305 2306 Schibotowo
    gazetteer_test.txt 2307 2308 Ustje
    gazetteer_test.txt 2309 2310 Chotzy
    gazetteer_test.txt 2311 2312 Dibuny
    gazetteer_test.txt 2313 2314 Ishora
    gazetteer_test.txt 2315 2316 Jedrowo
    gazetteer_test.txt 2317 2318 Johannes
    gazetteer_test.txt 2319 2320 Kakisalmi
    gazetteer_test.txt 2321 2322 Kaskowo
    gazetteer_test.txt 2323 2324 Koli
    gazetteer_test.txt 2325 2326 Kolpino
    gazetteer_test.txt 2327 2328 Kowanko
    gazetteer_test.txt 2329 2330 Krasja
    gazetteer_test.txt 2335 2336 Krestzy
    gazetteer_test.txt 2337 2338 Kronstadt
    gazetteer_test.txt 2339 2340 LadogaSee
    gazetteer_test.txt 2341 2342 Ljalizy
    gazetteer_test.txt 2343 2344 Komarowo
    gazetteer_test.txt 2345 2346 Swirstroi
    gazetteer_test.txt 2347 2348 Luga
    gazetteer_test.txt 2349 2350 Lungatschi
    gazetteer_test.txt 2354 2355 Mga
    gazetteer_test.txt 2356 2357 Neboltschi
    gazetteer_test.txt 2358 2359 ParachinoPoddubje
    gazetteer_test.txt 2360 2361 Opetschenski
    gazetteer_test.txt 2363 2364 Pesotschny
    gazetteer_test.txt 2365 2366 Petrodworez
    gazetteer_test.txt 2367 2368 PikaLjowo
    gazetteer_test.txt 2369 2370 Washiny
    gazetteer_test.txt 2371 2372 Pontonja
    gazetteer_test.txt 2373 2374 Puschkin
    gazetteer_test.txt 2375 2376 Rautu
    gazetteer_test.txt 2377 2378 Rogawka
    gazetteer_test.txt 2379 2380 Rudnitschja
    gazetteer_test.txt 2381 2382 Sestrorezk
    gazetteer_test.txt 2383 2384 Shichaijowo
    gazetteer_test.txt 2385 2386 Shicharjowo
    gazetteer_test.txt 2387 2388 Antropschino
    gazetteer_test.txt 2389 2390 UstIshora
    gazetteer_test.txt 2397 2398 Stroganowo
    gazetteer_test.txt 2399 2400 Swir
    gazetteer_test.txt 2401 2402 Taizy
    gazetteer_test.txt 2403 2404 Terebutenez
    gazetteer_test.txt 2405 2406 Terioki
    gazetteer_test.txt 2407 2408 Tosno
    gazetteer_test.txt 2409 2410 Tschudowo
    gazetteer_test.txt 2411 2412 Turgosch
    gazetteer_test.txt 2413 2414 Uglowka
    gazetteer_test.txt 2415 2416 Waldaj
    gazetteer_test.txt 2417 2418 Sjasstroj
    gazetteer_test.txt 2419 2420 Wolchowstroi
    gazetteer_test.txt 2421 2422 Wolchowstroi2
    gazetteer_test.txt 2423 2424 MorosowSiedlung
    gazetteer_test.txt 2425 2426 Rachja
    gazetteer_test.txt 2427 2428 Golowino
    gazetteer_test.txt 2429 2430 SusLonger
    gazetteer_test.txt 2431 2432 Kosmodemjansk
    gazetteer_test.txt 2433 2434 Wolshsk
    gazetteer_test.txt 2435 2436 Baskaja
    gazetteer_test.txt 2437 2438 Beresniki
    gazetteer_test.txt 2439 2440 Gremjatschinski
    gazetteer_test.txt 2441 2442 Kisel
    gazetteer_test.txt 2443 2444 Gubacha
    gazetteer_test.txt 2448 2449 Polowinka
    gazetteer_test.txt 2453 2454 Uswa
    gazetteer_test.txt 2455 2456 WsewolodoWilwa
    gazetteer_test.txt 2457 2458 Krasnokamsk
    gazetteer_test.txt 2459 2460 Kurja
    gazetteer_test.txt 2461 2462 Lyswa
    gazetteer_test.txt 2463 2464 Lewschino
    gazetteer_test.txt 2465 2466 Obogatitel
    gazetteer_test.txt 2467 2468 Obogatitelja
    gazetteer_test.txt 2469 2470 JugoKamski
    gazetteer_test.txt 2471 2472 Owerjata
    gazetteer_test.txt 2473 2474 Ponysch
    gazetteer_test.txt 2475 2476 Borowsk
    gazetteer_test.txt 2477 2478 Kalijez
    gazetteer_test.txt 2479 2480 Tscherdyn
    gazetteer_test.txt 2481 2482 Tschussowskaja
    gazetteer_test.txt 2483 2484 Paschia
    gazetteer_test.txt 2488 2489 UrizkiBergwerke
    gazetteer_test.txt 2490 2491 Potma
    gazetteer_test.txt 2492 2493 Saransk
    gazetteer_test.txt 2494 2495 Sweshenkaja
    gazetteer_test.txt 2496 2497 Baratjewo
    gazetteer_test.txt 2498 2499 Akinschino
    gazetteer_test.txt 2500 2501 Aprelewka
    gazetteer_test.txt 2502 2503 Baranowo
    gazetteer_test.txt 2504 2505 Barmino
    gazetteer_test.txt 2506 2507 Bogorodskoje
    gazetteer_test.txt 2508 2509 Bronnizy
    gazetteer_test.txt 2510 2511 Butowo
    gazetteer_test.txt 2512 2513 Chimki
    gazetteer_test.txt 2514 2515 Chlebnikowo
    gazetteer_test.txt 2516 2517 Cholschtschewiki
    gazetteer_test.txt 2518 2519 Chotkowo
    gazetteer_test.txt 2520 2521 Chowrino
    gazetteer_test.txt 2522 2523 Chrapunowo
    gazetteer_test.txt 2524 2525 Dmitrow
    gazetteer_test.txt 2526 2527 Dolgoprudny
    gazetteer_test.txt 2528 2529 Dorochowo
    gazetteer_test.txt 2530 2531 Dres
    gazetteer_test.txt 2532 2533 Dulewo
    gazetteer_test.txt 2534 2535 Elektrostal
    gazetteer_test.txt 2536 2537 Fill
    gazetteer_test.txt 2538 2539 Golizyno
    gazetteer_test.txt 2540 2541 Golutwin
    gazetteer_test.txt 2542 2543 Gubanowo
    gazetteer_test.txt 2544 2545 Gutschkowo
    gazetteer_test.txt 2546 2547 Nowojerusalimskaja
    gazetteer_test.txt 2548 2549 Iwantejewka
    gazetteer_test.txt 2550 2551 Jegorjewsk
    gazetteer_test.txt 2552 2553 KaganowitschWerke
    gazetteer_test.txt 2554 2555 Osherelje
    gazetteer_test.txt 2556 2557 Katuar
    gazetteer_test.txt 2558 2559 Kisseljowo
    gazetteer_test.txt 2560 2561 Klin
    gazetteer_test.txt 2562 2563 Schtschurowo
    gazetteer_test.txt 2564 2565 Kolotsch
    gazetteer_test.txt 2566 2567 Koptjewo
    gazetteer_test.txt 2568 2569 Kossino
    gazetteer_test.txt 2570 2571 Iljinskoje
    gazetteer_test.txt 2572 2573 Pawschino
    gazetteer_test.txt 2574 2575 Tuschino
    gazetteer_test.txt 2576 2577 GosplanLandsiedlung
    gazetteer_test.txt 2578 2579 Lunjowo
    gazetteer_test.txt 2580 2581 Krasny
    gazetteer_test.txt 2583 2584 Krjukowo
    gazetteer_test.txt 2585 2586 Lebsino
    gazetteer_test.txt 2587 2588 Tscherjomuschki
    gazetteer_test.txt 2589 2590 Lianosowo
    gazetteer_test.txt 2591 2592 Ljuberzy
    gazetteer_test.txt 2593 2594 Ljublino
    gazetteer_test.txt 2595 2596 Lobnja
    gazetteer_test.txt 2597 2598 Lopasnja
    gazetteer_test.txt 2599 2600 Luchowizy
    gazetteer_test.txt 2601 2602 Jurlowo
    gazetteer_test.txt 2603 2604 Obljanischtschewo
    gazetteer_test.txt 2605 2606 Schalikowo
    gazetteer_test.txt 2607 2608 Moskworezkaja
    gazetteer_test.txt 2609 2610 Mosshinka
    gazetteer_test.txt 2611 2612 Textilschtschik
    gazetteer_test.txt 2613 2614 Noginsk
    gazetteer_test.txt 2615 2616 Nowogorsk
    gazetteer_test.txt 2617 2618 OrechowoSujewo
    gazetteer_test.txt 2619 2620 Ostankino
    gazetteer_test.txt 2621 2622 Otdych
    gazetteer_test.txt 2623 2624 Otschakowo
    gazetteer_test.txt 2625 2626 Perowo
    gazetteer_test.txt 2627 2628 Planerja
    gazetteer_test.txt 2629 2630 Podlipki
    gazetteer_test.txt 2631 2632 Podolsk
    gazetteer_test.txt 2633 2634 PokrowskojeStreschnjewo
    gazetteer_test.txt 2635 2636 PtscheLowodnoje
    gazetteer_test.txt 2637 2638 Puschkino
    gazetteer_test.txt 2639 2640 Kutschino
    gazetteer_test.txt 2641 2642 Reutowo
    gazetteer_test.txt 2643 2644 Reschetnikowo
    gazetteer_test.txt 2645 2646 Rumjanzewo
    gazetteer_test.txt 2647 2648 Tutschkowo
    gazetteer_test.txt 2649 2650 Saraisk
    gazetteer_test.txt 2651 2652 Sasonowo
    gazetteer_test.txt 2653 2654 Frjasino
    gazetteer_test.txt 2655 2656 Semjonowskoje
    gazetteer_test.txt 2658 2659 Bor
    gazetteer_test.txt 2660 2661 Serpuchow
    gazetteer_test.txt 2662 2663 Silikatja
    gazetteer_test.txt 2664 2665 Snegiri
    gazetteer_test.txt 2666 2667 Sorewnowanie
    gazetteer_test.txt 2668 2669 Sofrino
    gazetteer_test.txt 2670 2671 Rshawka
    gazetteer_test.txt 2672 2673 Kijukowo
    gazetteer_test.txt 2677 2678 Stroika
    gazetteer_test.txt 2679 2680 Stupino
    gazetteer_test.txt 2681 2682 Tomilino
    gazetteer_test.txt 2683 2684 Tscherkisowo
    gazetteer_test.txt 2685 2686 Tscherusti
    gazetteer_test.txt 2687 2688 Tschuchlinka
    gazetteer_test.txt 2689 2690 Kraskowo
    gazetteer_test.txt 2691 2692 Lytkarino
    gazetteer_test.txt 2693 2694 Ugreschskaja
    gazetteer_test.txt 2695 2696 Gorbuny
    gazetteer_test.txt 2697 2698 Kisseljowka
    gazetteer_test.txt 2699 2700 Poretschje
    gazetteer_test.txt 2701 2702 Werbilki
    gazetteer_test.txt 2703 2704 Wolololamsk
    gazetteer_test.txt 2705 2706 Woskressensk
    gazetteer_test.txt 2707 2708 Wyssokowsk
    gazetteer_test.txt 2709 2710 Kandalakscha
    gazetteer_test.txt 2711 2712 Saschejek
    gazetteer_test.txt 2713 2714 Kildinstroi
    gazetteer_test.txt 2715 2716 Murmaschi
    gazetteer_test.txt 2717 2718 Ku
    gazetteer_test.txt 2719 2720 Montschegorsk
    gazetteer_test.txt 2721 2722 Nikel
    gazetteer_test.txt 2723 2724 Olenja
    gazetteer_test.txt 2725 2726 Padun
    gazetteer_test.txt 2727 2728 Pautscha
    gazetteer_test.txt 2732 2733 Nekrylowo
    gazetteer_test.txt 2734 2735 Beslan
    gazetteer_test.txt 2736 2737 Kardshin
    gazetteer_test.txt 2738 2739 Ursdon
    gazetteer_test.txt 2740 2741 Dsaudshikau
    gazetteer_test.txt 2742 2743 Krasnowodsk
    gazetteer_test.txt 2744 2745 Sadon
    gazetteer_test.txt 2746 2747 Wosnessensk
    gazetteer_test.txt 2748 2749 Perniza
    gazetteer_test.txt 2750 2751 Novosibirsk
    gazetteer_test.txt 2752 2753 Abagurowski
    gazetteer_test.txt 2754 2755 Alambai
    gazetteer_test.txt 2756 2757 Jaja
    gazetteer_test.txt 2758 2759 Ansherskaja
    gazetteer_test.txt 2760 2761 Artyschta
    gazetteer_test.txt 2762 2763 Barabinsk
    gazetteer_test.txt 2764 2765 Belowo
    gazetteer_test.txt 2769 2770 Salai'r
    gazetteer_test.txt 2771 2772 Inskoi
    gazetteer_test.txt 2773 2774 Kisseljowsk
    gazetteer_test.txt 2775 2776 Kriwoschtschokowo
    gazetteer_test.txt 2777 2778 Schuschtalep
    gazetteer_test.txt 2779 2780 LeninskKusnezki
    gazetteer_test.txt 2781 2782 Myski
    gazetteer_test.txt 2783 2784 Nowokusnezk
    gazetteer_test.txt 2785 2786 Berdsk
    gazetteer_test.txt 2787 2788 Ossinnilci
    gazetteer_test.txt 2789 2790 Ossinniki
    gazetteer_test.txt 2791 2792 Jaschkino
    gazetteer_test.txt 2793 2794 Tatarsk
    gazetteer_test.txt 2795 2796 Tjashin
    gazetteer_test.txt 2797 2798 Tschulym
    gazetteer_test.txt 2799 2800 Ussjaty
    gazetteer_test.txt 2801 2802 Issilkul
    gazetteer_test.txt 2803 2804 Kulomsino
    gazetteer_test.txt 2805 2806 Diwnoje
    gazetteer_test.txt 2810 2811 Newinnomyssk
    gazetteer_test.txt 2812 2813 NowoALexandrowka
    gazetteer_test.txt 2814 2815 Pjatigorsk
    gazetteer_test.txt 2816 2817 Prijutnoje
    gazetteer_test.txt 2821 2822 Fokino
    gazetteer_test.txt 2823 2824 Jelez
    gazetteer_test.txt 2825 2826 Oelez
    gazetteer_test.txt 2827 2828 Mzensk
    gazetteer_test.txt 2829 2830 Pogar
    gazetteer_test.txt 2831 2832 Polushje
    gazetteer_test.txt 2833 2834 Assejewskaja
    gazetteer_test.txt 2835 2836 Bednodemjanowsk
    gazetteer_test.txt 2837 2838 Tschaadajewka
    gazetteer_test.txt 2839 2840 Kusnezk
    gazetteer_test.txt 2847 2848 Seliksa
    gazetteer_test.txt 2849 2850 Simanschtschino
    gazetteer_test.txt 2851 2852 Wertuhowka
    gazetteer_test.txt 2853 2854 Jar
    gazetteer_test.txt 2858 2859 Slanzy
    gazetteer_test.txt 2860 2861 Nowosselje
    gazetteer_test.txt 2862 2863 Pljussa
    gazetteer_test.txt 2864 2865 Toroschino
    gazetteer_test.txt 2866 2867 Tschorskaja
    gazetteer_test.txt 2868 2869 Birlcino
    gazetteer_test.txt 2870 2871 Chruschtschowo
    gazetteer_test.txt 2873 2874 Kuibyschew
    gazetteer_test.txt 2875 2876 Djagilewo
    gazetteer_test.txt 2877 2878 Grotowski
    gazetteer_test.txt 2879 2880 Iswest
    gazetteer_test.txt 2881 2882 Jambirino
    gazetteer_test.txt 2883 2884 Kurscha
    gazetteer_test.txt 2894 2895 Gorki
    gazetteer_test.txt 2896 2897 sarowka
    gazetteer_test.txt 2898 2899 Pronja
    gazetteer_test.txt 2903 2904 Kriuscha
    gazetteer_test.txt 2908 2909 Murmino
    gazetteer_test.txt 2910 2911 Wyschgorod
    gazetteer_test.txt 2912 2913 Wyssokoje
    gazetteer_test.txt 2914 2915 Roshdestwenskoje
    gazetteer_test.txt 2916 2917 Roshdestwo
    gazetteer_test.txt 2918 2919 Schazk
    gazetteer_test.txt 2920 2921 StaroshiLowo
    gazetteer_test.txt 2922 2923 Zementja
    gazetteer_test.txt 2924 2925 Artjom
    gazetteer_test.txt 2926 2927 Bataisk
    gazetteer_test.txt 2928 2929 Bogdanowka
    gazetteer_test.txt 2937 2938 Gukowo
    gazetteer_test.txt 2939 2940 Gundorowski
    gazetteer_test.txt 2941 2942 Krasny
    gazetteer_test.txt 2944 2945 Nowikowka
    gazetteer_test.txt 2946 2947 RawnopoL
    gazetteer_test.txt 2948 2949 deshda
    gazetteer_test.txt 2985 2986 MichajLoLeontjewskaja
    gazetteer_test.txt 2987 2988 chitschewanDonskaja
    gazetteer_test.txt 2989 2990 Nowotscherkassk
    gazetteer_test.txt 2991 2992 Nowoschachtinsk
    gazetteer_test.txt 2993 2994 MolotowSiedlung
    gazetteer_test.txt 2995 2996 Kamenolomni
    gazetteer_test.txt 2997 2998 Salsk
    gazetteer_test.txt 2999 3000 Schachtja
    gazetteer_test.txt 3001 3002 Schachty
    gazetteer_test.txt 3003 3004 Sinjawskaja
    gazetteer_test.txt 3005 3006 Taganrog
    gazetteer_test.txt 3007 3008 Tazinski
    gazetteer_test.txt 3009 3010 Arkadak
    gazetteer_test.txt 3011 3012 Podgorenka
    gazetteer_test.txt 3014 3015 Atkarsk
    gazetteer_test.txt 3017 3018 Bagajewwka
    gazetteer_test.txt 3019 3020 Bagajewka
    gazetteer_test.txt 3021 3022 Balakowo
    gazetteer_test.txt 3023 3024 Chwalynsk
    gazetteer_test.txt 3025 3026 Engels
    gazetteer_test.txt 3027 3028 Grimm
    gazetteer_test.txt 3029 3030 Jekaterinowka
    gazetteer_test.txt 3031 3032 Jelschanka
    gazetteer_test.txt 3033 3034 Kologriwowka
    gazetteer_test.txt 3035 3036 Gorny
    gazetteer_test.txt 3037 3038 Kurdjum
    gazetteer_test.txt 3039 3040 Marx
    gazetteer_test.txt 3041 3042 Pudowkino
    gazetteer_test.txt 3043 3044 Pugatschow
    gazetteer_test.txt 3045 3046 Tamala
    gazetteer_test.txt 3047 3048 Toptulino
    gazetteer_test.txt 3049 3050 Trofimowski
    gazetteer_test.txt 3051 3052 Wertunowka
    gazetteer_test.txt 3053 3054 Wolsk
    gazetteer_test.txt 3055 3056 Dorogobush
    gazetteer_test.txt 3057 3058 Durowo
    gazetteer_test.txt 3059 3060 Gussino
    gazetteer_test.txt 3061 3062 Kolesniki
    gazetteer_test.txt 3063 3064 Kolesniki
    gazetteer_test.txt 3066 3067 Kondrowo
    gazetteer_test.txt 3068 3069 Kuprino
    gazetteer_test.txt 3070 3071 Nikitinka
    gazetteer_test.txt 3072 3073 Pjatowskaja
    gazetteer_test.txt 3077 3078 Priselskaja
    gazetteer_test.txt 3079 3080 Roslawl
    gazetteer_test.txt 3081 3082 Saretschje
    gazetteer_test.txt 3083 3084 Semlewo
    gazetteer_test.txt 3085 3086 Wjasma
    gazetteer_test.txt 3087 3088 Artscheda
    gazetteer_test.txt 3089 3090 Gorny
    gazetteer_test.txt 3090 3091 Balyklej
    gazetteer_test.txt 3092 3093 Beketowka
    gazetteer_test.txt 3094 3095 Beketowskaja
    gazetteer_test.txt 3096 3097 Dubowka
    gazetteer_test.txt 3098 3099 Ilowlja
    gazetteer_test.txt 3100 3101 Kamyschin
    gazetteer_test.txt 3102 3103 Keller
    gazetteer_test.txt 3104 3105 Kotelnikowski
    gazetteer_test.txt 3106 3107 Sadowaja
    gazetteer_test.txt 3108 3109 Sarepta
    gazetteer_test.txt 3113 3114 Urjupinsk
    gazetteer_test.txt 3118 3119 Georgijewsk
    gazetteer_test.txt 3121 3122 Neslobja
    gazetteer_test.txt 3123 3124 Jessentuki
    gazetteer_test.txt 3125 3126 Kislowodsk
    gazetteer_test.txt 3128 3129 Schachty
    gazetteer_test.txt 3130 3131 Skatschki
    gazetteer_test.txt 3132 3133 Adui
    gazetteer_test.txt 3135 3136 Sinjatschicha
    gazetteer_test.txt 3137 3138 Bobrowka
    gazetteer_test.txt 3139 3140 Mostyr
    gazetteer_test.txt 3141 3142 Altyi
    gazetteer_test.txt 3143 3144 Apparatja
    gazetteer_test.txt 3145 3146 Asanka
    gazetteer_test.txt 3147 3148 Asbest
    gazetteer_test.txt 3149 3150 Isumrud
    gazetteer_test.txt 3151 3152 Bashenowo
    gazetteer_test.txt 3156 3157 Beresit
    gazetteer_test.txt 3158 3159 Berjosowski
    gazetteer_test.txt 3160 3161 Lossiny
    gazetteer_test.txt 3162 3163 Bogoslowsk
    gazetteer_test.txt 3164 3165 Chabartschicha
    gazetteer_test.txt 3166 3167 ChmyLowka
    gazetteer_test.txt 3168 3169 Chrompik
    gazetteer_test.txt 3170 3171 Chudjakowo
    gazetteer_test.txt 3172 3173 Degtjarsk
    gazetteer_test.txt 3174 3175 GLucharny
    gazetteer_test.txt 3176 3177 GorobLagodatskaja
    gazetteer_test.txt 3178 3179 Irbit
    gazetteer_test.txt 3180 3181 Kytlym
    gazetteer_test.txt 3182 3183 Isset
    gazetteer_test.txt 3184 3185 Istok
    gazetteer_test.txt 3186 3187 Iwdel2
    gazetteer_test.txt 3188 3189 Artjomowski
    gazetteer_test.txt 3190 3191 Krasnogwardejski
    gazetteer_test.txt 3192 3193 Jeshewaja
    gazetteer_test.txt 3194 3195 KamenskUralski
    gazetteer_test.txt 3196 3197 Kamyschlow
    gazetteer_test.txt 3198 3199 Karpinsk
    gazetteer_test.txt 3200 3201 Lewicha
    gazetteer_test.txt 3202 3203 Kolzowo
    gazetteer_test.txt 3204 3205 Kossulino
    gazetteer_test.txt 3206 3207 Kourowka
    gazetteer_test.txt 3208 3209 Krasnoturjinsk
    gazetteer_test.txt 3210 3211 Krasnotuijinsk
    gazetteer_test.txt 3212 3213 Koschai
    gazetteer_test.txt 3214 3215 Krasnouralsk
    gazetteer_test.txt 3216 3217 Krasny
    gazetteer_test.txt 3219 3220 Krasny
    gazetteer_test.txt 3220 3221 Jar
    gazetteer_test.txt 3222 3223 Krasny
    gazetteer_test.txt 3226 3227 Istok
    gazetteer_test.txt 3228 3229 Maramsino
    gazetteer_test.txt 3233 3234 Molwa
    gazetteer_test.txt 3235 3236 Monetny
    gazetteer_test.txt 3237 3238 Moroskowo
    gazetteer_test.txt 3239 3240 Mramorskaja
    gazetteer_test.txt 3241 3242 Mugai
    gazetteer_test.txt 3243 3244 deshdinsk
    gazetteer_test.txt 3245 3246 NejwoSchaitanski
    gazetteer_test.txt 3247 3248 WerchNejwinski
    gazetteer_test.txt 3249 3250 Basjanowski
    gazetteer_test.txt 3258 3259 Istok
    gazetteer_test.txt 3266 3267 Lobwa
    gazetteer_test.txt 3268 3269 Perschino
    gazetteer_test.txt 3270 3271 PerwouraLsk
    gazetteer_test.txt 3272 3273 PodwoLoschja
    gazetteer_test.txt 3274 3275 PokLjowskaja
    gazetteer_test.txt 3276 3277 Sewerski
    gazetteer_test.txt 3278 3279 Rasjesd
    gazetteer_test.txt 3281 3282 Rewda
    gazetteer_test.txt 3283 3284 Degtjarka
    gazetteer_test.txt 3285 3286 Sadanije
    gazetteer_test.txt 3287 3288 Samozwet
    gazetteer_test.txt 3289 3290 Schabrowski
    gazetteer_test.txt 3291 3292 Schaitan
    gazetteer_test.txt 3293 3294 Schartasch
    gazetteer_test.txt 3295 3296 Schuwakisch
    gazetteer_test.txt 3297 3298 Seredowi
    gazetteer_test.txt 3299 3300 Serow
    gazetteer_test.txt 3301 3302 Sewerouralsk
    gazetteer_test.txt 3303 3304 Sinjatschicha
    gazetteer_test.txt 3305 3306 Soswa
    gazetteer_test.txt 3307 3308 SredneuraLsk
    gazetteer_test.txt 3313 3314 Istok
    gazetteer_test.txt 3318 3319 Tawda
    gazetteer_test.txt 3326 3327 Jertarski
    gazetteer_test.txt 3331 3332 Turinsk
    gazetteer_test.txt 3336 3337 Uktus
    gazetteer_test.txt 3338 3339 Urai
    gazetteer_test.txt 3346 3347 Otradnowo
    gazetteer_test.txt 3348 3349 Werchoturje
    gazetteer_test.txt 3350 3351 Wessjolowka
    gazetteer_test.txt 3352 3353 Woltschansk
    gazetteer_test.txt 3354 3355 Chobotowo
    gazetteer_test.txt 3356 3357 Inshawino
    gazetteer_test.txt 3358 3359 Kirsanow
    gazetteer_test.txt 3360 3361 Mitschurinsk
    gazetteer_test.txt 3362 3363 Morschansk
    gazetteer_test.txt 3364 3365 Oboro
    gazetteer_test.txt 3366 3367 Rada
    gazetteer_test.txt 3368 3369 Sampur
    gazetteer_test.txt 3370 3371 Wjashli
    gazetteer_test.txt 3372 3373 Kokschan
    gazetteer_test.txt 3374 3375 Bugulma
    gazetteer_test.txt 3376 3377 Buinsk
    gazetteer_test.txt 3378 3379 Jelabuga
    gazetteer_test.txt 3381 3382 Ustje
    gazetteer_test.txt 3383 3384 Kasan
    gazetteer_test.txt 3385 3386 Lubjany
    gazetteer_test.txt 3387 3388 Schemordan
    gazetteer_test.txt 3389 3390 SelenodoLsk
    gazetteer_test.txt 3391 3392 Tschistopol
    gazetteer_test.txt 3393 3394 Jalutorowsk
    gazetteer_test.txt 3395 3396 Lebedewka
    gazetteer_test.txt 3397 3398 WinsiLi
    gazetteer_test.txt 3399 3400 Myschega
    gazetteer_test.txt 3401 3402 BobrikDonskoi
    gazetteer_test.txt 3403 3404 Begitschewski
    gazetteer_test.txt 3405 3406 Suchodolski
    gazetteer_test.txt 3407 3408 Chomjakowo
    gazetteer_test.txt 3409 3410 Dedilowo
    gazetteer_test.txt 3411 3412 Sadonje
    gazetteer_test.txt 3413 3414 Smorodinka
    gazetteer_test.txt 3415 3416 Gorbatschowo
    gazetteer_test.txt 3417 3418 Granki
    gazetteer_test.txt 3422 3423 Wladimirskoje
    gazetteer_test.txt 3424 3425 Kasanowka
    gazetteer_test.txt 3426 3427 Lwowo
    gazetteer_test.txt 3428 3429 Maklez
    gazetteer_test.txt 3430 3431 Majenki
    gazetteer_test.txt 3432 3433 Obidimo
    gazetteer_test.txt 3434 3435 Obolenskoje
    gazetteer_test.txt 3436 3437 Plawsk
    gazetteer_test.txt 3438 3439 Polunino
    gazetteer_test.txt 3440 3441 Prisady
    gazetteer_test.txt 3442 3443 Sbrodowo
    gazetteer_test.txt 3444 3445 Schepeljowo
    gazetteer_test.txt 3446 3447 Ogarjowka
    gazetteer_test.txt 3451 3452 Shdanka
    gazetteer_test.txt 3453 3454 Stalinogorsk
    gazetteer_test.txt 3455 3456 Tarusskaja
    gazetteer_test.txt 3457 3458 Towarkowo
    gazetteer_test.txt 3466 3467 Torbejewka
    gazetteer_test.txt 3468 3469 Wenjow
    gazetteer_test.txt 3470 3471 Glasow
    gazetteer_test.txt 3472 3473 Ishewsk
    gazetteer_test.txt 3474 3475 Lynga
    gazetteer_test.txt 3476 3477 NjurdorKotja
    gazetteer_test.txt 3478 3479 Perwomaisk
    gazetteer_test.txt 3480 3481 Rjabowo
    gazetteer_test.txt 3482 3483 Wischur
    gazetteer_test.txt 3484 3485 Kondakowka
    gazetteer_test.txt 3486 3487 Poliwanowo
    gazetteer_test.txt 3488 3489 Taschla
    gazetteer_test.txt 3490 3491 Ai
    gazetteer_test.txt 3492 3493 Ascha
    gazetteer_test.txt 3494 3495 Bischkil
    gazetteer_test.txt 3496 3497 JemansheLinka
    gazetteer_test.txt 3498 3499 Korkino
    gazetteer_test.txt 3500 3501 Kamensk
    gazetteer_test.txt 3502 3503 Kamyschinka
    gazetteer_test.txt 3504 3505 Karabasch
    gazetteer_test.txt 3506 3507 Kartaly
    gazetteer_test.txt 3508 3509 Kopejsk
    gazetteer_test.txt 3510 3511 Kropatschowo
    gazetteer_test.txt 3512 3513 Magnitka
    gazetteer_test.txt 3514 3515 Kyschtym
    gazetteer_test.txt 3516 3517 Magnitogorsk
    gazetteer_test.txt 3518 3519 Mauk
    gazetteer_test.txt 3520 3521 Miass
    gazetteer_test.txt 3522 3523 Rosa
    gazetteer_test.txt 3524 3525 BakaL
    gazetteer_test.txt 3526 3527 Sawodskaja
    gazetteer_test.txt 3528 3529 Slatoust
    gazetteer_test.txt 3530 3531 Tajandy
    gazetteer_test.txt 3532 3533 Ufalej
    gazetteer_test.txt 3534 3535 Urshumka
    gazetteer_test.txt 3536 3537 Wawilowo
    gazetteer_test.txt 3538 3539 TschetschenAul
    gazetteer_test.txt 3540 3541 Samaschki
    gazetteer_test.txt 3545 3546 Grosny
    gazetteer_test.txt 3547 3548 AliJurt
    gazetteer_test.txt 3549 3550 sran
    gazetteer_test.txt 3551 3552 Basorkino
    gazetteer_test.txt 3553 3554 Scholkowskaja
    gazetteer_test.txt 3555 3556 TangiTschu
    gazetteer_test.txt 3557 3558 Tschita
    gazetteer_test.txt 3559 3560 Buguruslan
    gazetteer_test.txt 3561 3562 Koltubanka
    gazetteer_test.txt 3563 3564 Nowotroizk
    gazetteer_test.txt 3566 3567 Maksai
    gazetteer_test.txt 3568 3569 Orsk
    gazetteer_test.txt 3570 3571 SoLILezk
    gazetteer_test.txt 3572 3573 ALatyr
    gazetteer_test.txt 3574 3575 Kasch
    gazetteer_test.txt 3576 3577 TjurLema
    gazetteer_test.txt 3581 3582 Tscheboksary
    gazetteer_test.txt 3583 3584 Butylizy
    gazetteer_test.txt 3585 3586 Anopino
    gazetteer_test.txt 3596 3597 Karabanowo
    gazetteer_test.txt 3598 3599 Koltschugino
    gazetteer_test.txt 3600 3601 Komissarowka
    gazetteer_test.txt 3602 3603 Iljitschowo
    gazetteer_test.txt 3604 3605 Melenki
    gazetteer_test.txt 3606 3607 Sarja
    gazetteer_test.txt 3608 3609 Sobinka
    gazetteer_test.txt 3610 3611 Andrejewo
    gazetteer_test.txt 3612 3613 Susdal
    gazetteer_test.txt 3614 3615 Tschulkowo
    gazetteer_test.txt 3616 3617 Undol
    gazetteer_test.txt 3618 3619 Mstjora
    gazetteer_test.txt 3620 3621 Woschod
    gazetteer_test.txt 3622 3623 Wtorowo
    gazetteer_test.txt 3624 3625 Buschui'cha
    gazetteer_test.txt 3626 3627 Charowskaja
    gazetteer_test.txt 3631 3632 Grjasowez
    gazetteer_test.txt 3633 3634 Jadricha
    gazetteer_test.txt 3635 3636 Jawenga
    gazetteer_test.txt 3637 3638 Kadnikow
    gazetteer_test.txt 3639 3640 Kirillow
    gazetteer_test.txt 3641 3642 Lesha
    gazetteer_test.txt 3643 3644 Petschatkino
    gazetteer_test.txt 3645 3646 Scheks
    gazetteer_test.txt 3647 3648 Schelomowo
    gazetteer_test.txt 3649 3650 Semigorodnjaja
    gazetteer_test.txt 3651 3652 Sokol
    gazetteer_test.txt 3653 3654 Suda
    gazetteer_test.txt 3655 3656 Ustjush
    gazetteer_test.txt 3657 3658 Wolonga
    gazetteer_test.txt 3659 3660 Woshega
    gazetteer_test.txt 3661 3662 Borissoglebsk
    gazetteer_test.txt 3663 3664 Chrenowaja
    gazetteer_test.txt 3665 3666 Ertil
    gazetteer_test.txt 3667 3668 Grafskaja
    gazetteer_test.txt 3669 3670 Gribanowka
    gazetteer_test.txt 3671 3672 Lipezk
    gazetteer_test.txt 3673 3674 Liski
    gazetteer_test.txt 3675 3676 Poworino
    gazetteer_test.txt 3677 3678 Rossosch
    gazetteer_test.txt 3679 3680 Usman
    gazetteer_test.txt 3681 3682 Tedshen
    gazetteer_test.txt 3686 3687 Tschuama
    gazetteer_test.txt 3688 3689 Kokand
    gazetteer_test.txt 3690 3691 Skobelewo
    gazetteer_test.txt 3692 3693 Taschkent
    gazetteer_test.txt 3695 3696 Achangaran
    gazetteer_test.txt 3697 3698 Angren
    gazetteer_test.txt 3699 3700 Angrenschachtstroi
    gazetteer_test.txt 3701 3702 Farchad
    gazetteer_test.txt 3703 3704 Jangijul
    gazetteer_test.txt 3705 3706 Gwardejski
    gazetteer_test.txt 3707 3708 Schirin
    gazetteer_test.txt 3709 3710 Charkow
    gazetteer_test.txt 3710 3711 Ukraine
    gazetteer_test.txt 3712 3713 Anjewo
    gazetteer_test.txt 3714 3715 Perwuchino
    gazetteer_test.txt 3716 3717 Isjum
    gazetteer_test.txt 3718 3719 Krasnograd
    gazetteer_test.txt 3720 3721 Kupjansk
    gazetteer_test.txt 3722 3723 Ljubotin
    gazetteer_test.txt 3724 3725 Merefa
    gazetteer_test.txt 3729 3730 Osnowa
    gazetteer_test.txt 3731 3732 Panjutino
    gazetteer_test.txt 3733 3734 Parchomowka
    gazetteer_test.txt 3735 3736 Pokotilowka
    gazetteer_test.txt 3737 3738 Rogan
    gazetteer_test.txt 3739 3740 Sokolniki
    gazetteer_test.txt 3741 3742 Tschugujew
    gazetteer_test.txt 3743 3744 Kriwin
    gazetteer_test.txt 3745 3746 Poninka
    gazetteer_test.txt 3747 3748 Schepetowka
    gazetteer_test.txt 3749 3750 Slawuta
    gazetteer_test.txt 3751 3752 Baglej
    gazetteer_test.txt 3757 3758 Dneprodsershinsk
    gazetteer_test.txt 3759 3760 Dolginzewo
    gazetteer_test.txt 3761 3762 Kanderopol
    gazetteer_test.txt 3766 3767 Marganez
    gazetteer_test.txt 3768 3769 Nikopol
    gazetteer_test.txt 3770 3771 Nishnedneprowsk
    gazetteer_test.txt 3772 3773 Nowomoskowsk
    gazetteer_test.txt 3774 3775 Pereschtschepino
    gazetteer_test.txt 3776 3777 Prossjaja
    gazetteer_test.txt 3778 3779 Raduschja
    gazetteer_test.txt 3780 3781 Tschertomlyk
    gazetteer_test.txt 3782 3783 Tscherwonoje
    gazetteer_test.txt 3784 3785 Borislaw
    gazetteer_test.txt 3786 3787 Chodorow
    gazetteer_test.txt 3788 3789 Gelsendorf
    gazetteer_test.txt 3790 3791 Morschin
    gazetteer_test.txt 3792 3793 Shidatschow
    gazetteer_test.txt 3794 3795 Skole
    gazetteer_test.txt 3796 3797 Stryj
    gazetteer_test.txt 3798 3799 Tschernowizy
    gazetteer_test.txt 3803 3804 Borispol
    gazetteer_test.txt 3805 3806 Browary
    gazetteer_test.txt 3807 3808 Werchnjatschka
    gazetteer_test.txt 3809 3810 Darniza
    gazetteer_test.txt 3811 3812 Fastow
    gazetteer_test.txt 3813 3814 Sgurowka
    gazetteer_test.txt 3815 3816 Panfily
    gazetteer_test.txt 3817 3818 Schewtschenkowo
    gazetteer_test.txt 3819 3820 Schpola
    gazetteer_test.txt 3821 3822 Smela
    gazetteer_test.txt 3823 3824 Talnoje
    gazetteer_test.txt 3825 3826 Tscherkassy
    gazetteer_test.txt 3827 3828 Uman
    gazetteer_test.txt 3829 3830 Alexandria
    gazetteer_test.txt 3831 3832 Alexandrija
    gazetteer_test.txt 3833 3834 Kapitanowka
    gazetteer_test.txt 3835 3836 Wiska
    gazetteer_test.txt 3837 3838 Pantajewka
    gazetteer_test.txt 3839 3840 Sacharja
    gazetteer_test.txt 3841 3842 Scharowka
    gazetteer_test.txt 3843 3844 Schestakowka
    gazetteer_test.txt 3845 3846 Negrebki
    gazetteer_test.txt 3847 3848 Peremyschljany
    gazetteer_test.txt 3849 3850 Rudno
    gazetteer_test.txt 3851 3852 Salush
    gazetteer_test.txt 3853 3854 Sknilow
    gazetteer_test.txt 3855 3856 Skoschlow
    gazetteer_test.txt 3857 3858 SoLotschew
    gazetteer_test.txt 3859 3860 Berislaw
    gazetteer_test.txt 3861 3862 Cherson
    gazetteer_test.txt 3863 3864 Jurizino
    gazetteer_test.txt 3865 3866 Kopani
    gazetteer_test.txt 3867 3868 Partisany
    gazetteer_test.txt 3869 3870 SaLkowo
    gazetteer_test.txt 3871 3872 SokoLogornoje
    gazetteer_test.txt 3873 3874 Ternowka
    gazetteer_test.txt 3875 3876 Tschitschkarowka
    gazetteer_test.txt 3877 3878 NowoBorissow
    gazetteer_test.txt 3879 3880 Ismail
    gazetteer_test.txt 3881 3882 Kotowsk
    gazetteer_test.txt 3883 3884 Reni
    gazetteer_test.txt 3885 3886 Pestschanka
    gazetteer_test.txt 3887 3888 Abasowka
    gazetteer_test.txt 3889 3890 Chorol
    gazetteer_test.txt 3891 3892 Grebjonka
    gazetteer_test.txt 3893 3894 Oagotin
    gazetteer_test.txt 3895 3896 dagotin
    gazetteer_test.txt 3897 3898 Karlowka
    gazetteer_test.txt 3899 3900 Kononowka
    gazetteer_test.txt 3901 3902 Kotschubejewka
    gazetteer_test.txt 3903 3904 Krementschug
    gazetteer_test.txt 3905 3906 StaLinZuckerwerk
    gazetteer_test.txt 3907 3908 Lubny
    gazetteer_test.txt 3909 3910 Mechedowka
    gazetteer_test.txt 3911 3912 Pirjatin
    gazetteer_test.txt 3913 3914 Romodan
    gazetteer_test.txt 3915 3916 Skorochodowo
    gazetteer_test.txt 3920 3921 Sarny
    gazetteer_test.txt 3922 3923 Sdolbunow
    gazetteer_test.txt 3933 3934 Georgijewski
    gazetteer_test.txt 3935 3936 Grigorjewka
    gazetteer_test.txt 3937 3938 Nowoalexejewka
    gazetteer_test.txt 3939 3940 Rosowka
    gazetteer_test.txt 3941 3942 Matwejewski
    gazetteer_test.txt 3943 3944 Melitopol
    gazetteer_test.txt 3945 3946 PetroMichajlowka
    gazetteer_test.txt 3947 3948 Mokraja
    gazetteer_test.txt 3949 3950 Nowogrigorjewka
    gazetteer_test.txt 3951 3952 Rodionowka
    gazetteer_test.txt 3953 3954 Terpenije
    gazetteer_test.txt 3955 3956 Belokorowitschi
    gazetteer_test.txt 3960 3961 Skomorochi
    gazetteer_test.txt 3962 3963 Chajtschnorin
    gazetteer_test.txt 3964 3965 Igtopol
    gazetteer_test.txt 3966 3967 Igtpot
    gazetteer_test.txt 3968 3969 Jemetjanowka
    gazetteer_test.txt 3970 3971 Korosten
    gazetteer_test.txt 3972 3973 Kriwoje
    gazetteer_test.txt 3974 3975 Matin
    gazetteer_test.txt 3976 3977 NowogradWolynski
    gazetteer_test.txt 3978 3979 Penisewitschi
    gazetteer_test.txt 3980 3981 Kornin
    gazetteer_test.txt 3982 3983 Radomyschl
    gazetteer_test.txt 3984 3985 Weledniki
    gazetteer_test.txt 3986 3987 Artjoma
    gazetteer_test.txt 3988 3989 Artjomowsk
    gazetteer_test.txt 3990 3991 Bairak
    gazetteer_test.txt 3992 3993 Chanshonkowo
    gazetteer_test.txt 3994 3995 Sujewka
    gazetteer_test.txt 3999 4000 Debalzewo
    gazetteer_test.txt 4001 4002 Dobropolje
    gazetteer_test.txt 4003 4004 Dronowo
    gazetteer_test.txt 4005 4006 Drushkowka
    gazetteer_test.txt 4007 4008 FenoLja
    gazetteer_test.txt 4009 4010 GorLowka
    gazetteer_test.txt 4011 4012 Kondratjewski
    gazetteer_test.txt 4013 4014 Grechow
    gazetteer_test.txt 4015 4016 Jama
    gazetteer_test.txt 4017 4018 Jassinowka
    gazetteer_test.txt 4019 4020 Jekijewo
    gazetteer_test.txt 4021 4022 Kalmius
    gazetteer_test.txt 4023 4024 Katyk
    gazetteer_test.txt 4025 4026 Konstantinowka
    gazetteer_test.txt 4027 4028 Kramatorsk
    gazetteer_test.txt 4029 4030 Nowoekonomitscheskoje
    gazetteer_test.txt 4031 4032 Krasnoarmejskoe
    gazetteer_test.txt 4033 4034 Krasnogorowka
    gazetteer_test.txt 4035 4036 Kurachowka
    gazetteer_test.txt 4037 4038 Lutugino
    gazetteer_test.txt 4039 4040 Magdalinowka
    gazetteer_test.txt 4041 4042 Makejewka
    gazetteer_test.txt 4043 4044 Pantelejmonowka
    gazetteer_test.txt 4045 4046 Mospino
    gazetteer_test.txt 4047 4048 Motschalino
    gazetteer_test.txt 4049 4050 Motschalinski
    gazetteer_test.txt 4051 4052 Muschketowo
    gazetteer_test.txt 4053 4054 Nikitowka
    gazetteer_test.txt 4061 4062 Petrowka
    gazetteer_test.txt 4063 4064 Postnikowo
    gazetteer_test.txt 4065 4066 Roja
    gazetteer_test.txt 4067 4068 Rutschenkowo
    gazetteer_test.txt 4092 4093 Schtscheglowka
    gazetteer_test.txt 4094 4095 Shdanow
    gazetteer_test.txt 4096 4097 Skossyrskaja
    gazetteer_test.txt 4098 4099 Slawjansk
    gazetteer_test.txt 4100 4101 Smoljanka
    gazetteer_test.txt 4102 4103 Sol
    gazetteer_test.txt 4104 4105 Studgorodok
    gazetteer_test.txt 4106 4107 TroizkoCharzyssk
    gazetteer_test.txt 4108 4109 Trudowaja
    gazetteer_test.txt 4111 4112 Jar
    gazetteer_test.txt 4113 4114 Tschistjakowo
    gazetteer_test.txt 4115 4116 Tschumakowo
    gazetteer_test.txt 4117 4118 Woskressenskaja
    gazetteer_test.txt 4119 4120 Zukuricha
    gazetteer_test.txt 4121 4122 Kolomyja
    gazetteer_test.txt 4123 4124 Lawotschnoje
    gazetteer_test.txt 4125 4126 Achtyrka
    gazetteer_test.txt 4127 4128 Gluchow
    gazetteer_test.txt 4129 4130 Konotop
    gazetteer_test.txt 4131 4132 Nepljujewo
    gazetteer_test.txt 4133 4134 Terny
    gazetteer_test.txt 4135 4136 Neptjujewo
    gazetteer_test.txt 4137 4138 PrawdinskiZuckerfabrik
    gazetteer_test.txt 4139 4140 Putiwt
    gazetteer_test.txt 4141 4142 Toropitowka
    gazetteer_test.txt 4143 4144 Torochtjany
    gazetteer_test.txt 4145 4146 Ternopot
    gazetteer_test.txt 4147 4148 Bobrowizy
    gazetteer_test.txt 4152 4153 Linowizy
    gazetteer_test.txt 4154 4155 Ladan
    gazetteer_test.txt 4156 4157 Perelowka
    gazetteer_test.txt 4161 4162 SafonowoGuta
    gazetteer_test.txt 4163 4164 Semjonowka
    gazetteer_test.txt 4165 4166 Sorokatitschi
    gazetteer_test.txt 4170 4171 Wiltscha
    gazetteer_test.txt 4172 4173 Tschernjowka
    gazetteer_test.txt 4174 4175 Tschernowzy
    gazetteer_test.txt 4176 4177 GLuchowzy
    gazetteer_test.txt 4178 4179 Kasatin
    gazetteer_test.txt 4180 4181 Shmerinka
    gazetteer_test.txt 4182 4183 Gniwan
    gazetteer_test.txt 4184 4185 Manewitschi
    gazetteer_test.txt 4186 4187 Almasja
    gazetteer_test.txt 4188 4189 Altschewsk
    gazetteer_test.txt 4190 4191 Awdakowo
    gazetteer_test.txt 4195 4196 Darjewka
    gazetteer_test.txt 4197 4198 Djakowo
    gazetteer_test.txt 4199 4200 Dolshanskaja
    gazetteer_test.txt 4201 4202 Golubowka
    gazetteer_test.txt 4203 4204 Gorskoje
    gazetteer_test.txt 4205 4206 Irmino
    gazetteer_test.txt 4207 4208 Iswarino
    gazetteer_test.txt 4209 4210 Kadijewka
    gazetteer_test.txt 4211 4212 Kamyschewacha
    gazetteer_test.txt 4213 4214 Karakas
    gazetteer_test.txt 4215 4216 KrasnopoLje
    gazetteer_test.txt 4217 4218 Krasny
    gazetteer_test.txt 4220 4221 Krindatschowka
    gazetteer_test.txt 4222 4223 KrupskajaBergwerk
    gazetteer_test.txt 4224 4225 Lissitschansk
    gazetteer_test.txt 4226 4227 Kriworoshje
    gazetteer_test.txt 4228 4229 Manuilowka
    gazetteer_test.txt 4230 4231 Ovvragi
    gazetteer_test.txt 4235 4236 Perejesdja
    gazetteer_test.txt 4237 4238 Popasja
    gazetteer_test.txt 4239 4240 Rowenki
    gazetteer_test.txt 4241 4242 Rubeshnoje
    gazetteer_test.txt 4243 4244 Schtschotowo
    gazetteer_test.txt 4245 4246 Schterowka
    gazetteer_test.txt 4247 4248 Sentjanowka
    gazetteer_test.txt 4249 4250 Sifonja
    gazetteer_test.txt 4251 4252 Simogorje
    gazetteer_test.txt 4253 4254 Waljanowski
    gazetteer_test.txt 4255 4256 Werchneje
    gazetteer_test.txt 4257 4258 Wiljanowo
    gazetteer_test.txt 4259 4260 Wolodarsk
    gazetteer_test.txt 4261 4262 ZentralnoBokowskoi
    gazetteer_test.txt 4263 4264 Chojniki
    gazetteer_test.txt 4265 4266 Dobrusch
    gazetteer_test.txt 4267 4268 Jelsk
    gazetteer_test.txt 4269 4270 Kostjukowka
    gazetteer_test.txt 4271 4272 Nowobelizkaja
    gazetteer_test.txt 4273 4274 Retschiza
    gazetteer_test.txt 4275 4276 Rogatschow
    gazetteer_test.txt 4277 4278 Shlobin
    gazetteer_test.txt 4279 4280 Sjabrowka
    gazetteer_test.txt 4281 4282 Usa
    gazetteer_test.txt 4283 4284 Wassilewitschi
    gazetteer_test.txt 4285 4286 Lida
    gazetteer_test.txt 4287 4288 Mosty
    gazetteer_test.txt 4289 4290 SLonim
    gazetteer_test.txt 4291 4292 PawLinowo
    gazetteer_test.txt 4293 4294 Ross
    gazetteer_test.txt 4295 4296 Borissow
    gazetteer_test.txt 4297 4298 Fanipol
    gazetteer_test.txt 4299 4300 Kolodischtschi
    gazetteer_test.txt 4307 4308 Sedtscha
    gazetteer_test.txt 4309 4310 Shodino
    gazetteer_test.txt 4311 4312 SmoLewitschi
    gazetteer_test.txt 4313 4314 TaLka
    gazetteer_test.txt 4315 4316 Uretschje
    gazetteer_test.txt 4317 4318 Gluscha
    gazetteer_test.txt 4319 4320 Brosha
    gazetteer_test.txt 4321 4322 Bychow
    gazetteer_test.txt 4323 4324 Grodsjanka
    gazetteer_test.txt 4325 4326 Jasen
    gazetteer_test.txt 4327 4328 Kershenka
    gazetteer_test.txt 4329 4330 Kopzewitschi
    gazetteer_test.txt 4331 4332 Kritschew
    gazetteer_test.txt 4333 4334 Ossipowitschi
    gazetteer_test.txt 4335 4336 Mosyr
    gazetteer_test.txt 4337 4338 Barawucha
    gazetteer_test.txt 4339 4340 Tatarka
    gazetteer_test.txt 4341 4342 Schklow
    gazetteer_test.txt 4343 4344 Timkowitschi
    gazetteer_test.txt 4345 4346 Molodetschno
    gazetteer_test.txt 4347 4348 Oschmjany
    gazetteer_test.txt 4349 4350 Chljustino
    gazetteer_test.txt 4351 4352 Krasja
    gazetteer_test.txt 4353 4354 Obol
    gazetteer_test.txt 4355 4356 Osinowka
    gazetteer_test.txt 4357 4358 Ossipowka
    gazetteer_test.txt 4359 4360 Borkowitschi
    gazetteer_test.txt 4361 4362 Kriste
    gazetteer_test.txt 4363 4364 Tolotschin
    gazetteer_test.txt 4365 4366 Tschaschniki
    gazetteer_test.txt 4367 4368 Ulga
    gazetteer_test.txt 4369 4370 Koschtschu
    gazetteer_test.txt 4371 4372 Bernjaschen
    gazetteer_test.txt 4373 4374 Armenikend
    gazetteer_test.txt 4375 4376 Konju
    gazetteer_test.txt 4377 4378 Kukruse
    gazetteer_test.txt 4379 4380 Ereda
    gazetteer_test.txt 4381 4382 Aseri
    gazetteer_test.txt 4383 4384 Ellamaa
    gazetteer_test.txt 4385 4386 Jeschera
    gazetteer_test.txt 4387 4388 Agudseri
    gazetteer_test.txt 4389 4390 Gori
    gazetteer_test.txt 4391 4392 Borshomi
    gazetteer_test.txt 4393 4394 Inguri
    gazetteer_test.txt 4395 4396 SaganLugi
    gazetteer_test.txt 4397 4398 Sandary
    gazetteer_test.txt 4399 4400 MolotowStadtbezirk
    gazetteer_test.txt 4401 4402 Didube
    gazetteer_test.txt 4406 4407 wibuli
    gazetteer_test.txt 4408 4409 Dshalombet
    gazetteer_test.txt 4410 4411 Giiterbahnhof
    gazetteer_test.txt 4412 4413 Ridder
    gazetteer_test.txt 4414 4415 Saschtschita
    gazetteer_test.txt 4416 4417 Kflkas
    gazetteer_test.txt 4418 4419 Sesava
    gazetteer_test.txt 4420 4421 Kalgi
    gazetteer_test.txt 4422 4423 Bukas
    gazetteer_test.txt 4424 4425 Spopane
    gazetteer_test.txt 4426 4427 Rembazkoje
    gazetteer_test.txt 4428 4429 Petrasiui
    gazetteer_test.txt 4430 4431 Seredzius
    gazetteer_test.txt 4432 4433 Lustberg
    gazetteer_test.txt 4434 4435 Airiogola
    gazetteer_test.txt 4436 4437 Klemiske
    gazetteer_test.txt 4438 4439 MaimaksanskiStadtbezirk
    gazetteer_test.txt 4455 4456 Kokino
    gazetteer_test.txt 4457 4458 Sakamensk
    gazetteer_test.txt 4462 4463 Onochoj
    gazetteer_test.txt 4464 4465 AwtosawodskiStadtbezirk
    gazetteer_test.txt 4466 4467 SormowoStadtbezirk
    gazetteer_test.txt 4468 4469 SchumLewaja
    gazetteer_test.txt 4473 4474 Tschernoramenka
    gazetteer_test.txt 4475 4476 Gorschenino
    gazetteer_test.txt 4478 4479 RSFSR
    gazetteer_test.txt 4483 4484 Chlebowo
    gazetteer_test.txt 4485 4486 Krasny
    gazetteer_test.txt 4486 4487 Orjol
    gazetteer_test.txt 4488 4489 Berendejewo
    gazetteer_test.txt 4490 4491 Karasch
    gazetteer_test.txt 4492 4493 Gusjatino
    gazetteer_test.txt 4494 4495 Migalewo
    gazetteer_test.txt 4496 4497 Grinino
    gazetteer_test.txt 4498 4499 Smoschje
    gazetteer_test.txt 4500 4501 Gontscharowo
    gazetteer_test.txt 4502 4503 Kotarowo
    gazetteer_test.txt 4504 4505 Tapiau
    gazetteer_test.txt 4506 4507 Jasnoje
    gazetteer_test.txt 4508 4509 Prochladja
    gazetteer_test.txt 4510 4511 Baltisk
    gazetteer_test.txt 4512 4513 Bagrationowsk
    gazetteer_test.txt 4514 4515 Neman
    gazetteer_test.txt 4516 4517 Sowetsk
    gazetteer_test.txt 4518 4519 Tramischen
    gazetteer_test.txt 4520 4521 Smensk
    gazetteer_test.txt 4522 4523 Sjassosero
    gazetteer_test.txt 4524 4525 Kappesalka
    gazetteer_test.txt 4526 4527 Kutichosskaja
    gazetteer_test.txt 4528 4529 Solomennoje
    gazetteer_test.txt 4530 4531 Kukowka
    gazetteer_test.txt 4532 4533 Witschka
    gazetteer_test.txt 4537 4538 Wolosniza
    gazetteer_test.txt 4539 4540 Pschada
    gazetteer_test.txt 4541 4542 Jejsk
    gazetteer_test.txt 4543 4544 Turgenewka
    gazetteer_test.txt 4545 4546 Subtschaninowka
    gazetteer_test.txt 4550 4551 Schemilowka
    gazetteer_test.txt 4552 4553 Ljamisa
    gazetteer_test.txt 4557 4558 Sowetski
    gazetteer_test.txt 4559 4560 Priosjorsk
    gazetteer_test.txt 4561 4562 Kin
    gazetteer_test.txt 4566 4567 Iwangorod
    gazetteer_test.txt 4568 4569 Kamenskoje
    gazetteer_test.txt 4570 4571 Seliwanowo
    gazetteer_test.txt 4572 4573 KowaLko
    gazetteer_test.txt 4574 4575 Dubowizkoje
    gazetteer_test.txt 4576 4577 Sosnowo
    gazetteer_test.txt 4578 4579 Selenogorsk
    gazetteer_test.txt 4580 4581 Kerest
    gazetteer_test.txt 4582 4583 UstSchora
    gazetteer_test.txt 4584 4585 UstSchory
    gazetteer_test.txt 4586 4587 Filippowka
    gazetteer_test.txt 4600 4601 NowoGirejewo
    gazetteer_test.txt 4602 4603 Panki
    gazetteer_test.txt 4604 4605 Perowo
    gazetteer_test.txt 4607 4608 Kurkino
    gazetteer_test.txt 4609 4610 Marfino
    gazetteer_test.txt 4611 4612 Alexino
    gazetteer_test.txt 4613 4614 Beskudnikowo
    gazetteer_test.txt 4615 4616 Guba
    gazetteer_test.txt 4620 4621 Wladikawkas
    gazetteer_test.txt 4622 4623 Bugry
    gazetteer_test.txt 4624 4625 Kriwoschtschowoko
    gazetteer_test.txt 4626 4627 MBystraja
    gazetteer_test.txt 4628 4629 Dorogoi
    gazetteer_test.txt 4630 4631 Bolotowo
    gazetteer_test.txt 4632 4633 Kjutschiki
    gazetteer_test.txt 4634 4635 Raswilka
    gazetteer_test.txt 4636 4637 Jewlaschewo
    gazetteer_test.txt 4638 4639 Achuny
    gazetteer_test.txt 4640 4641 Machalino
    gazetteer_test.txt 4642 4643 Kripun
    gazetteer_test.txt 4644 4645 Rasjesd
    gazetteer_test.txt 4652 4653 Lesnoje
    gazetteer_test.txt 4657 4658 NowoAsowka
    gazetteer_test.txt 4659 4660 Rostowka
    gazetteer_test.txt 4661 4662 Marzewo
    gazetteer_test.txt 4663 4664 Peschtschany
    gazetteer_test.txt 4668 4669 Sudowka
    gazetteer_test.txt 4673 4674 DsershinskiStadtbezirk
    gazetteer_test.txt 4675 4676 JermanskiStadtbezirk
    gazetteer_test.txt 4689 4690 TraktorosawodskiStadtbezirk
    gazetteer_test.txt 4694 4695 Shirnowsk
    gazetteer_test.txt 4696 4697 Abgenowo
    gazetteer_test.txt 4698 4699 Rasjesd
    gazetteer_test.txt 4701 4702 Ajat
    gazetteer_test.txt 4703 4704 Turjinski
    gazetteer_test.txt 4705 4706 Kuschwa
    gazetteer_test.txt 4707 4708 Rudnitschny
    gazetteer_test.txt 4709 4710 Woltschanka
    gazetteer_test.txt 4714 4715 Patotschja
    gazetteer_test.txt 4716 4717 Rogoshinski
    gazetteer_test.txt 4727 4728 Dsjakino
    gazetteer_test.txt 4729 4730 Sareka
    gazetteer_test.txt 4731 4732 Moissejewka
    gazetteer_test.txt 4733 4734 Mjassnikowo
    gazetteer_test.txt 4735 4736 Nowoschalaschowo
    gazetteer_test.txt 4737 4738 Maksai
    gazetteer_test.txt 4739 4740 Korjakino
    gazetteer_test.txt 4741 4742 ski
    gazetteer_test.txt 4743 4744 Alexejewskoje
    gazetteer_test.txt 4748 4749 Silno
    gazetteer_test.txt 4750 4751 Kokawino
    gazetteer_test.txt 4752 4753 Ljubomirskaja
    gazetteer_test.txt 4754 4755 Wassilkow
    gazetteer_test.txt 4756 4757 PostWolynski
    gazetteer_test.txt 4758 4759 Kowachino
    gazetteer_test.txt 4760 4761 Olesko
    gazetteer_test.txt 4762 4763 Sinilow
    gazetteer_test.txt 4764 4765 Rabotschi
    gazetteer_test.txt 4766 4767 Wetka
    gazetteer_test.txt 4768 4769 Kalinowka
    gazetteer_test.txt 4770 4771 PetrowoLidijewka
    gazetteer_test.txt 4772 4773 DonezkoAmwrossijewka
    gazetteer_test.txt 4774 4775 Shelanja
    gazetteer_test.txt 4776 4777 Schachtjorsk
    gazetteer_test.txt 4778 4779 Ilowaisk
    gazetteer_test.txt 4783 4784 Lidijewka
    gazetteer_test.txt 4785 4786 IwanoFrankowsk
    gazetteer_test.txt 4787 4788 Wiry
    gazetteer_test.txt 4789 4790 Jazewo
    gazetteer_test.txt 4791 4792 Shidinitschi
    gazetteer_test.txt 4793 4794 Uditschew
    gazetteer_test.txt 4795 4796 Uditschewo
    gazetteer_test.txt 4797 4798 Brjanka
    gazetteer_test.txt 4799 4800 DsershinskiBergwerk
    gazetteer_test.txt 4801 4802 Toschkowka
    gazetteer_test.txt 4803 4804 Maksimowka
    gazetteer_test.txt 4809 4810 GLuboki
    gazetteer_test.txt 4811 4812 IljitschBergwerk
    gazetteer_test.txt 4813 4814 Petrowenki
    gazetteer_test.txt 4819 4820 Kosyrewo
    gazetteer_test.txt 4821 4822 Kasimirowka
    gazetteer_test.txt 4823 4824 Norio
    gazetteer_test.txt 4825 4826 Dshambejty
    gazetteer_test.txt 4827 4828 Komsomolski
    gazetteer_test.txt 4839 4840 Kudama
    gazetteer_test.txt 4841 4842 Repjowka
    gazetteer_test.txt 4843 4844 Sibrowo
    gazetteer_test.txt 4845 4846 Lopatkowo
    gazetteer_test.txt 4847 4848 Solnjetschja
    gazetteer_test.txt 4849 4850 Perewoloki
    gazetteer_test.txt 4851 4852 Alexejewka
    gazetteer_test.txt 4853 4854 Bachilowo
    gazetteer_test.txt 4855 4856 Uman
    gazetteer_test.txt 4857 4858 Owrutsch
    gazetteer_test.txt 4859 4860 Mariupol
    gazetteer_test.txt 4861 4862 Mokwa
    gazetteer_test.txt 4863 4864 Massy
    gazetteer_test.txt 4865 4866 Lahta
    gazetteer_test.txt 4867 4868 Sapjorja
    gazetteer_test.txt 4869 4870 Roshdestwennoje
    gazetteer_test.txt 4871 4872 Rybniza
    gazetteer_test.txt 4873 4874 Brno
    gazetteer_test.txt 4875 4876 Sibirien
    gazetteer_test.txt 4877 4878 Ural
    gazetteer_test.txt 4879 4880 Workuta
    gazetteer_test.txt 4881 4882 Magadan
    gazetteer_test.txt 4883 4884 Kolyma
    gazetteer_test.txt 4885 4886 Norilsk
    gazetteer_test.txt 4887 4888 Lubjanka
    gazetteer_test.txt 4889 4890 Butyrka
    gazetteer_test.txt 4891 4892 Kaliningrad
    place_texts.txt 16 17 Stalingrad
    place_texts.txt 33 34 Workuta
    place_texts.txt 35 36 Astrachan
    place_texts.txt 65 66 Stalingrad
    place_texts.txt 77 78 Stalingrad
    place_texts.txt 104 105 Stalingrad
    place_texts.txt 106 107 Saratow
    place_texts.txt 180 181 Stalingrad
    place_texts.txt 190 191 Jelabuga
    place_texts.txt 193 194 Stalingrad
    place_texts.txt 222 223 Stalingrad
    place_texts.txt 240 241 Jelabuga
    place_texts.txt 382 383 Stalingrad
    place_texts.txt 396 397 Stalingrad
    place_texts.txt 416 417 Stalingrad
    place_texts.txt 456 457 Stalingrad
    place_texts.txt 483 484 Stalingrad
    place_texts.txt 521 522 Stalingrad
    place_texts.txt 600 601 Moskau
    place_texts.txt 649 650 Stalingrad
    place_texts.txt 663 664 Stalingrad
    place_texts.txt 715 716 Stalingrad
    place_texts.txt 730 731 Stalingrad
    place_texts.txt 794 795 Stalingrad
    place_texts.txt 825 826 Russland
    place_texts.txt 861 862 Stalingrad
    place_texts.txt 880 881 Stalingrad
    place_texts.txt 971 972 Stalingrad
    place_texts.txt 1056 1057 Stalingrad
    place_texts.txt 1081 1082 Stalingrad
    place_texts.txt 1119 1120 Stalingrad
    place_texts.txt 1140 1141 Stalingrad
    place_texts.txt 1166 1167 Stalingrad
    place_texts.txt 1186 1187 Stalingrad
    place_texts.txt 1241 1242 Stalingrad
    place_texts.txt 1275 1276 Stalingrad
    place_texts.txt 1336 1337 Stalingrad
    place_texts.txt 1456 1457 Stalingrad
    place_texts.txt 1483 1484 Russland
    place_texts.txt 1506 1507 Stalingrad
    place_texts.txt 1563 1564 Stalingrad
    place_texts.txt 1631 1632 Stalingrad
    place_texts.txt 1682 1683 Stalingrad
    place_texts.txt 1744 1745 Stalingrad
    place_texts.txt 1769 1770 Russland
    place_texts.txt 1795 1796 Stalingrad
    place_texts.txt 1830 1831 Stalingrad
    place_texts.txt 1919 1920 Stalingrad
    place_texts.txt 1931 1932 Stalingrad
    place_texts.txt 1940 1941 Russland
    place_texts.txt 1949 1950 Stalingrad
    place_texts.txt 1977 1978 Stalingrad
    place_texts.txt 1985 1986 Stalingrad
    place_texts.txt 2133 2134 Stalingrad
    place_texts.txt 2364 2365 Keller
    place_texts.txt 2484 2485 Stalingrad
    place_texts.txt 2516 2517 Stalingrad
    place_texts.txt 2558 2559 Gorki
    place_texts.txt 2570 2571 Moskau
    place_texts.txt 2592 2593 Stalingrad
    place_texts.txt 2594 2595 Saratow
    place_texts.txt 2596 2597 Wolsk
    place_texts.txt 2598 2599 Sysran
    place_texts.txt 2600 2601 Kuibyschew
    place_texts.txt 2604 2605 Uljanowsk
    place_texts.txt 2606 2607 Kasan
    place_texts.txt 2610 2611 Kasan
    place_texts.txt 2612 2613 Moskau
    place_texts.txt 2714 2715 Kasan
    place_texts.txt 2765 2766 Stalingrad
    place_texts.txt 2834 2835 Stalingrad
    place_texts.txt 3002 3003 Kasan
    place_texts.txt 3039 3040 Kasan
    place_texts.txt 3079 3080 Kasan
    place_texts.txt 3113 3114 Tscheboksary
    place_texts.txt 3139 3140 Tula
    place_texts.txt 3193 3194 Russland
    place_texts.txt 3259 3260 Moskau
    place_texts.txt 3267 3268 Jelabuga
    place_texts.txt 3520 3521 Kaluga
    place_texts.txt 3529 3530 Tula
    place_texts.txt 3553 3554 Moskau
    place_texts.txt 3570 3571 Derbent
    place_texts.txt 3574 3575 Baku
    place_texts.txt 3587 3588 Astrachan
    place_texts.txt 3592 3593 Moskau
    place_texts.txt 3608 3609 Pugatschow
    place_texts.txt 3626 3627 Moskau
    place_texts.txt 3714 3715 Ural
    place_texts.txt 3721 3722 Ural
    place_texts.txt 3730 3731 Kasan
    place_texts.txt 3733 3734 Pugatschow
    place_texts.txt 3738 3739 Moskau
    place_texts.txt 4066 4067 Moskau
    place_texts.txt 4121 4122 Smolensk
    place_texts.txt 4139 4140 Smolensk
    place_texts.txt 4237 4238 Workuta
    place_texts.txt 4239 4240 Astrachan
    place_texts.txt 4311 4312 Smolensk
    place_texts.txt 4323 4324 Sibirien
    place_texts.txt 4466 4467 Smolensk
    place_texts.txt 4494 4495 Smolensk
    place_texts.txt 4568 4569 Smolensk
    place_texts.txt 4596 4597 Johannes
    place_texts.txt 4604 4605 Smolensk
    place_texts.txt 4627 4628 Smolensk
    place_texts.txt 5097 5098 Borowitschi
    place_texts.txt 5121 5122 KALININ
    place_texts.txt 5127 5128 Borissow
    place_texts.txt 5130 5131 MINSK
    place_texts.txt 5132 5133 Orscha
    place_texts.txt 5138 5139 WITEBSK
    place_texts.txt 5156 5157 LWOW
    place_texts.txt 5167 5168 Stanislaw
    place_texts.txt 5180 5181 Winniza
    place_texts.txt 5182 5183 Tscherkassy
    place_texts.txt 5184 5185 Molotowsk
    place_texts.txt 5193 5194 SMOLENSK
    place_texts.txt 5196 5197 MOSKAU
    place_texts.txt 5200 5201 KALUGA
    place_texts.txt 5217 5218 BRJANSK
    place_texts.txt 5221 5222 Lebedjan
    place_texts.txt 5224 5225 ARCHANGELSK
    place_texts.txt 5227 5228 Temnikow
    place_texts.txt 5230 5231 PENSA
    place_texts.txt 5232 5233 Wolsk
    place_texts.txt 5248 5249 Kineschma
    place_texts.txt 5257 5258 Susdal
    place_texts.txt 5263 5264 WLADIMIR
    place_texts.txt 5294 5295 KURSK
    place_texts.txt 5297 5298 Sumy
    place_texts.txt 5312 5313 ODESSA
    place_texts.txt 5319 5320 POLTAWA
    place_texts.txt 5320 5321 CHARKOW
    place_texts.txt 5325 5326 Kupjansk
    place_texts.txt 5329 5330 Atkarsk
    place_texts.txt 5331 5332 SARATOW
    place_texts.txt 5333 5334 Urjupinsk
    place_texts.txt 5335 5336 Lissitschansk
    place_texts.txt 5341 5342 Rjasan
    place_texts.txt 5346 5347 Potma
    place_texts.txt 5348 5349 Saransk
    place_texts.txt 5351 5352 Morschansk
    place_texts.txt 5355 5356 Kramatorsk
    place_texts.txt 5360 5361 MAKEJEWKA
    place_texts.txt 5364 5365 STALINO
    place_texts.txt 5370 5371 Melitopol
    place_texts.txt 5373 5374 Taganrog
    place_texts.txt 5381 5382 SIMFEROPOL
    place_texts.txt 5394 5395 Armawir
    place_texts.txt 5401 5402 Nowotscherkassk
    place_texts.txt 5442 5443 Rustawi
    place_texts.txt 5451 5452 TASCHKENT
    place_texts.txt 5453 5454 Tschuama
    place_texts.txt 5459 5460 Kokand
    place_texts.txt 5467 5468 Begowat
    place_texts.txt 5717 5718 Kertsch
    place_texts.txt 5771 5772 Maikop
    place_texts.txt 5878 5879 Baku
    place_texts.txt 5944 5945 Stalingrad
    place_texts.txt 5991 5992 Astrachan
    place_texts.txt 6057 6058 Tichorezk
    place_texts.txt 6082 6083 Stalingrad
    place_texts.txt 6087 6088 Astrachan
    place_texts.txt 6100 6101 Stalingrad
    place_texts.txt 6108 6109 Astrachan
    place_texts.txt 6188 6189 Baku
    place_texts.txt 6297 6298 Kertsch
    place_texts.txt 6343 6344 Kertsch
    place_texts.txt 6440 6441 Leningrad
    place_texts.txt 6497 6498 Krasnogorsk
    place_texts.txt 6499 6500 Moskau
    place_texts.txt 6622 6623 Moskau
    place_texts.txt 6653 6654 Moskau
    place_texts.txt 6671 6672 Moskau
    place_texts.txt 6826 6827 Jelabuga
    place_texts.txt 6884 6885 Engels
    place_texts.txt 6951 6952 Engels
    place_texts.txt 7051 7052 Moskau
    place_texts.txt 7064 7065 Moskau
    place_texts.txt 7074 7075 Moskau
    place_texts.txt 7139 7140 Moskau
    place_texts.txt 7154 7155 Moskau
    place_texts.txt 7177 7178 Krasnogorsk
    place_texts.txt 7201 7202 Moskau
    place_texts.txt 7309 7310 Marx
    place_texts.txt 7364 7365 Gorki
    place_texts.txt 7425 7426 Nowgorod
    place_texts.txt 7428 7429 Gorki
    place_texts.txt 7448 7449 Wladimir
    place_texts.txt 7472 7473 Kasan
    place_texts.txt 7497 7498 Nowgorod
    place_texts.txt 7525 7526 Nowgorod
    place_texts.txt 7557 7558 Moskau
    place_texts.txt 7620 7621 Susdal
    place_texts.txt 7631 7632 Moskau
    place_texts.txt 7638 7639 Jelabuga
    place_texts.txt 7719 7720 Gorki
    place_texts.txt 7722 7723 Moskau
    place_texts.txt 7724 7725 Leningrad
    place_texts.txt 7732 7733 RSFSR
    place_texts.txt 7901 7902 Gorki
    place_texts.txt 7949 7950 Nowgorod
    place_texts.txt 7955 7956 Gorki
    place_texts.txt 7985 7986 Gorki
    place_texts.txt 7988 7989 Nowgorod
    place_texts.txt 8044 8045 Nowgorod
    place_texts.txt 8050 8051 Moskau
    place_texts.txt 8093 8094 Gorki
    place_texts.txt 8235 8236 Jelabuga
    place_texts.txt 8468 8469 Jelabuga
    place_texts.txt 8484 8485 Jelabuga
    place_texts.txt 8518 8519 Jelabuga
    place_texts.txt 8535 8536 Jelabuga
    place_texts.txt 8561 8562 Selenodolsk
    place_texts.txt 8567 8568 Kasan
    place_texts.txt 8573 8574 Selenodolsk
    place_texts.txt 8580 8581 Selenodolsk
    place_texts.txt 8587 8588 Selenodolsk
    place_texts.txt 8602 8603 Moskau
    place_texts.txt 8604 8605 Jarzewo
    place_texts.txt 8610 8611 Jarzewo
    place_texts.txt 8623 8624 Charkow
    place_texts.txt 8635 8636 Charkow
    place_texts.txt 8637 8638 Ukraine
    place_texts.txt 9831 9832 Ukraine
    place_texts.txt 9841 9842 Litauen
    place_texts.txt 9843 9844 Estland
    place_texts.txt 9980 9981 Wladimir
    place_texts.txt 10114 10115 Moskau
    place_texts.txt 10129 10130 Leningrad
    place_texts.txt 10319 10320 Ural
    place_texts.txt 10325 10326 Sibirien
    place_texts.txt 10404 10405 Stalingrad
    place_texts.txt 10590 10591 RSFSR
    place_texts.txt 10597 10598 Ukraine
    place_texts.txt 10601 10602 Usbekistan
    place_texts.txt 10603 10604 Kasachstan
    place_texts.txt 10605 10606 Georgien
    place_texts.txt 10609 10610 Litauen
    place_texts.txt 10611 10612 Estland
    place_texts.txt 10617 10618 Armenien
    place_texts.txt 10623 10624 Lettland
    place_texts.txt 10791 10792 Kyschtym
    place_texts.txt 10795 10796 Tscheljabinsk
    place_texts.txt 10803 10804 Beketowka
    place_texts.txt 10834 10835 Orscha
    place_texts.txt 10836 10837 Beketowka
    place_texts.txt 10838 10839 Wolsk
    place_texts.txt 10865 10866 Kasan
    place_texts.txt 10867 10868 Stalingrad
    place_texts.txt 10878 10879 Workuta
    place_texts.txt 10893 10894 Moskau
    place_texts.txt 10895 10896 Workuta
    place_texts.txt 10948 10949 Riga
    place_texts.txt 10969 10970 Suchumi
    place_texts.txt 10981 10982 Nowoschachtinsk
    place_texts.txt 10993 10994 Brjansk
    place_texts.txt 11009 11010 Stalingrad
    place_texts.txt 11045 11046 Ragnit
    place_texts.txt 11047 11048 Sibirien
    place_texts.txt 11066 11067 Orsk
    place_texts.txt 11085 11086 Moskau
    place_texts.txt 11087 11088 Krasnogorsk
    place_texts.txt 11390 11391 Moskau
    place_texts.txt 11505 11506 Moskau
    place_texts.txt 11519 11520 Moskau
    place_texts.txt 11598 11599 Moskau
    place_texts.txt 11617 11618 Moskau
    place_texts.txt 11642 11643 Moskau
    place_texts.txt 11659 11660 Krjukowo
    place_texts.txt 11661 11662 Kaschira
    place_texts.txt 11671 11672 Moskau
    place_texts.txt 11690 11691 Moskau
    place_texts.txt 11753 11754 Moskau
    place_texts.txt 11963 11964 Moskau
    place_texts.txt 11976 11977 Ural
    place_texts.txt 11981 11982 Moskau
    place_texts.txt 12049 12050 Moskau
    place_texts.txt 12367 12368 Ar
    place_texts.txt 12400 12401 Stalingrad
    place_texts.txt 12431 12432 Stalingrad
    place_texts.txt 12514 12515 Keller
    place_texts.txt 12632 12633 Stalingrad
    place_texts.txt 12645 12646 Stalingrad
    place_texts.txt 12787 12788 Stalingrad
    place_texts.txt 12867 12868 Russland
    place_texts.txt 13011 13012 STALINGRAD
    place_texts.txt 13055 13056 Stalingrad
    place_texts.txt 13288 13289 Nowotroizk
    place_texts.txt 13290 13291 Maksai
    place_texts.txt 13608 13609 Moskau
    place_texts.txt 13694 13695 Stalingrad
    place_texts.txt 13715 13716 Rshew
    place_texts.txt 13748 13749 Bor
    place_texts.txt 13754 13755 Smolensk
    place_texts.txt 13767 13768 Rshew
    place_texts.txt 13772 13773 Gshatsk
    place_texts.txt 13783 13784 Brjansk
    place_texts.txt 13785 13786 Orjol
    place_texts.txt 13793 13794 Smolensk
    place_texts.txt 13821 13822 Witebsk
    place_texts.txt 13833 13834 Roslawl
    place_texts.txt 13845 13846 Brjansk
    place_texts.txt 13852 13853 Smolensk
    place_texts.txt 13875 13876 Minsk
    place_texts.txt 13963 13964 Jelabuga
    place_texts.txt 13995 13996 Kasan
    place_texts.txt 14013 14014 Selenodolsk
    place_texts.txt 14036 14037 Jelabuga
    place_texts.txt 14078 14079 Kasan
    place_texts.txt 14093 14094 Kasan
    place_texts.txt 14111 14112 Selenodolsk
    place_texts.txt 14123 14124 Selenodolsk
    place_texts.txt 14148 14149 Kasan
    place_texts.txt 14197 14198 Kasan
    place_texts.txt 14231 14232 Kasan
    place_texts.txt 14246 14247 Kasan
    place_texts.txt 14267 14268 Kasan
    place_texts.txt 14321 14322 Kasan
    place_texts.txt 14370 14371 Selenodolsk
    place_texts.txt 14533 14534 Selenodolsk
    place_texts.txt 14607 14608 Selenodolsk
    place_texts.txt 14654 14655 Selenodolsk
    place_texts.txt 14721 14722 Riga
    place_texts.txt 14736 14737 Selenodolsk
    place_texts.txt 14769 14770 Selenodolsk
    place_texts.txt 14846 14847 Selenodolsk
    place_texts.txt 14944 14945 Tiraspol
    place_texts.txt 14994 14995 Nikolajew
    place_texts.txt 15108 15109 Odessa
    place_texts.txt 15149 15150 Nikolajew
    place_texts.txt 15195 15196 Nikolajew
    place_texts.txt 15237 15238 Nikolajew
    place_texts.txt 15311 15312 Nikolajew
    place_texts.txt 15419 15420 Odessa
    place_texts.txt 15437 15438 Odessa
    place_texts.txt 15490 15491 Nikolajew
    place_texts.txt 15498 15499 Odessa
    place_texts.txt 15506 15507 Odessa
    place_texts.txt 15523 15524 Odessa
    place_texts.txt 15534 15535 Krim
    place_texts.txt 15547 15548 Odessa
    place_texts.txt 15613 15614 Odessa
    place_texts.txt 15618 15619 Krim
    place_texts.txt 15639 15640 Sibirien
    place_texts.txt 15653 15654 Krim
    place_texts.txt 15667 15668 Krim
    place_texts.txt 15685 15686 Siwasch
    place_texts.txt 15689 15690 Kertsch
    place_texts.txt 15956 15957 Selenodolsk
    place_texts.txt 16021 16022 Selenodolsk
    place_texts.txt 16150 16151 Selenodolsk
    place_texts.txt 16201 16202 Selenodolsk
    place_texts.txt 16257 16258 Selenodolsk
    place_texts.txt 16291 16292 Selenodolsk
    place_texts.txt 16407 16408 Selenodolsk
    place_texts.txt 16512 16513 Jelabuga
    place_texts.txt 16536 16537 Jelabuga
    place_texts.txt 16550 16551 Jelabuga
    place_texts.txt 16571 16572 Selenodolsk
    place_texts.txt 16580 16581 Jelabuga
    place_texts.txt 16598 16599 Selenodolsk
    place_texts.txt 16611 16612 Selenodolsk
    place_texts.txt 16628 16629 Moskau
    place_texts.txt 16639 16640 Jarzewo
    place_texts.txt 16652 16653 Merefa
    place_texts.txt 16677 16678 Charkow
    place_texts.txt 16779 16780 Jelabuga
    place_texts.txt 16863 16864 Moskau
    place_texts.txt 16865 16866 Workuta
    place_texts.txt 17127 17128 Moskau
    place_texts.txt 17136 17137 Lubjanka
    place_texts.txt 17140 17141 Butyrka
    place_texts.txt 17159 17160 Moskau
    place_texts.txt 17162 17163 Workuta
    place_texts.txt 17249 17250 Karaganda
    place_texts.txt 17251 17252 Workuta
    place_texts.txt 17256 17257 Karaganda
    place_texts.txt 17269 17270 Workuta
    place_texts.txt 17338 17339 Workuta
    place_texts.txt 17477 17478 Moskau
    place_texts.txt 17660 17661 Workuta
    place_texts.txt 17684 17685 Stalingrad
    place_texts.txt 17805 17806 Moskau
    place_texts.txt 17810 17811 USA
    place_texts.txt 17877 17878 Jelabuga
    place_texts.txt 18119 18120 Gorodischtsche
    place_texts.txt 18213 18214 Stalingrad
    place_texts.txt 18243 18244 Stalingrad
    place_texts.txt 18276 18277 Stalingrad
    place_texts.txt 18331 18332 Kasan
    place_texts.txt 18359 18360 Jelschanka
    place_texts.txt 18428 18429 Jelschanka
    place_texts.txt 18455 18456 Gorodischtsche
    place_texts.txt 18471 18472 Jelschanka
    place_texts.txt 18540 18541 Stalingrad
    place_texts.txt 18836 18837 Johannes
    place_texts.txt 18877 18878 Krasnodar
    place_texts.txt 18882 18883 Charkow
    place_texts.txt 18899 18900 Minsk
    place_texts.txt 18904 18905 Kiew
    place_texts.txt 18907 18908 Jar
    place_texts.txt 18958 18959 Nikolajew
    place_texts.txt 19020 19021 Johannes
    place_texts.txt 19024 19025 Stalingrad
    place_texts.txt 19030 19031 Stalingrad
    place_texts.txt 19261 19262 Jelabuga
    place_texts.txt 20017 20018 ar
    place_texts.txt 20370 20371 Stalingrad
    place_texts.txt 20411 20412 Stalingrad
    place_texts.txt 20452 20453 Stalingrad
    place_texts.txt 20529 20530 Stalingrad
    place_texts.txt 20591 20592 Stalingrad
    place_texts.txt 20640 20641 Stalingrad
    place_texts.txt 20739 20740 Stalingrad
    place_texts.txt 20761 20762 Stalingrad
    place_texts.txt 20818 20819 Russland
    place_texts.txt 20906 20907 Stalingrad
    place_texts.txt 20941 20942 Russland
    place_texts.txt 20963 20964 Stalingrad
    place_texts.txt 21021 21022 Stalingrad
    place_texts.txt 21069 21070 Jelabuga
    place_texts.txt 21089 21090 Stalingrad
    place_texts.txt 21233 21234 Stalingrad
    place_texts.txt 21284 21285 Stalingrad
    place_texts.txt 21897 21898 Adler
    place_texts.txt 22069 22070 Adler
    place_texts.txt 22083 22084 Adler
    place_texts.txt 22253 22254 Kursk
    place_texts.txt 22333 22334 Wjasma
    place_texts.txt 22335 22336 Gshatsk
    place_texts.txt 22339 22340 Smolensk
    place_texts.txt 22350 22351 Kursk
    place_texts.txt 22371 22372 Smolensk
    place_texts.txt 22394 22395 Smolensk
    place_texts.txt 22396 22397 Roslawl
    place_texts.txt 22410 22411 Roslawl
    place_texts.txt 22448 22449 Smolensk
    place_texts.txt 22450 22451 Roslawl
    place_texts.txt 22477 22478 Smolensk
    place_texts.txt 22500 22501 Gomel
    place_texts.txt 22570 22571 Witebsk
    place_texts.txt 22737 22738 Witebsk
    place_texts.txt 22739 22740 Borissow
    place_texts.txt 22741 22742 Bobruisk
    place_texts.txt 23209 23210 Moskau
    place_texts.txt 23413 23414 Stalingrad
    place_texts.txt 23506 23507 Stalingrad
    place_texts.txt 23790 23791 Dwiri
    place_texts.txt 23795 23796 Georgien
    place_texts.txt 23996 23997 Jelabuga
    place_texts.txt 24018 24019 Jelabuga
    place_texts.txt 24077 24078 Stalingrad
    place_texts.txt 24103 24104 Kasan
    place_texts.txt 24173 24174 Jelabuga
    place_texts.txt 24321 24322 Stalingrad
    place_texts.txt 24329 24330 Stalingrad
    place_texts.txt 24486 24487 Jelabuga
    place_texts.txt 24529 24530 Jelabuga
    place_texts.txt 24538 24539 Kasan
    place_texts.txt 24932 24933 Stalingrad
    place_texts.txt 24991 24992 Workuta
    place_texts.txt 24993 24994 Astrachan
    place_texts.txt 25029 25030 Stalingrad
    place_texts.txt 25072 25073 Johannes
    place_texts.txt 25605 25606 jelabuga
    place_texts.txt 25638 25639 Selenodolsk
    place_texts.txt 25670 25671 Jelabuga
    place_texts.txt 25688 25689 Moskau
    place_texts.txt 25690 25691 Jarzewo
    place_texts.txt 25696 25697 Moskau
    place_texts.txt 25702 25703 Minsk
    place_texts.txt 25717 25718 Jarzewo
    place_texts.txt 25763 25764 Merefa
    place_texts.txt 25767 25768 Charkow
    place_texts.txt 26099 26100 Jelabuga
    place_texts.txt 26101 26102 Selenodolsk
    place_texts.txt 26108 26109 Jelabuga
    place_texts.txt 26391 26392 Stalingrad
    place_texts.txt 26407 26408 Stalingrad
    place_texts.txt 26440 26441 Stalingrad
    place_texts.txt 26518 26519 Kasan
    place_texts.txt 26533 26534 Stalingrad
    place_texts.txt 26688 26689 Pensa
    place_texts.txt 26694 26695 Pensa
    place_texts.txt 26724 26725 Moskau
    place_texts.txt 26737 26738 Pensa
    place_texts.txt 26762 26763 Moskau
    place_texts.txt 26825 26826 Moskau
    place_texts.txt 26827 26828 Kuibyschew
    place_texts.txt 26838 26839 Kuibyschew
    place_texts.txt 26860 26861 Moskau
    place_texts.txt 26898 26899 Stalingrad
    place_texts.txt 26909 26910 Pensa
    place_texts.txt 26911 26912 Kuibyschew
    place_texts.txt 26990 26991 Jelabuga
    place_texts.txt 27096 27097 Moskau
    place_texts.txt 27160 27161 Jelabuga
    place_texts.txt 27165 27166 Kasan
    place_texts.txt 27167 27168 Pensa
    place_texts.txt 27337 27338 Ukraine
    place_texts.txt 27366 27367 Fastow
    place_texts.txt 27368 27369 Shitomir
    place_texts.txt 27372 27373 Owrutsch
    place_texts.txt 27484 27485 Kursk
    place_texts.txt 27486 27487 Orjol
    place_texts.txt 27561 27562 Kiew
    place_texts.txt 27575 27576 Kiew
    place_texts.txt 27775 27776 Pronja
    place_texts.txt 27804 27805 Gomel
    place_texts.txt 27826 27827 Bobruisk
    place_texts.txt 27837 27838 Moskau
    place_texts.txt 27846 27847 Gomel
    place_texts.txt 27853 27854 Retschiza
    place_texts.txt 27864 27865 Shlobin
    place_texts.txt 27866 27867 Mosyr
    place_texts.txt 27885 27886 Retschiza
    place_texts.txt 28076 28077 Krasnogorsk
    place_texts.txt 28122 28123 Stalingrad
    place_texts.txt 28126 28127 Kameschkowo
    place_texts.txt 28184 28185 Stalingrad
    place_texts.txt 28382 28383 Stalingrad
    place_texts.txt 28397 28398 Stalingrad
    place_texts.txt 28403 28404 Kameschkowo
    place_texts.txt 28489 28490 Kasan
    place_texts.txt 28504 28505 Kameschkowo
    place_texts.txt 28659 28660 Stalingrad
    place_texts.txt 28684 28685 STALINGRAD
    

### Term Frequency


```python
from collections import Counter

count_list = []
for match_id, start, end in matches:
    count_list.append(doc[start:end].text)

counter = Counter(count_list)

for term, count in counter.most_common(10):
    print(term, count)
```

    Stalingrad 100
    Moskau 55
    Jelabuga 30
    Selenodolsk 26
    Kasan 25
    Smolensk 16
    Workuta 11
    Russland 8
    Gorki 8
    Odessa 8
    

### Named Entity Recognition


```python
!python -m spacy download de_core_news_sm
```

    Collecting de-core-news-sm==3.4.0
      Downloading https://github.com/explosion/spacy-models/releases/download/de_core_news_sm-3.4.0/de_core_news_sm-3.4.0-py3-none-any.whl (14.6 MB)
         --------------------------------------- 14.6/14.6 MB 12.3 MB/s eta 0:00:00
    Requirement already satisfied: spacy<3.5.0,>=3.4.0 in c:\users\minni\anaconda3\lib\site-packages (from de-core-news-sm==3.4.0) (3.4.3)
    Requirement already satisfied: catalogue<2.1.0,>=2.0.6 in c:\users\minni\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (2.0.8)
    Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in c:\users\minni\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (1.0.9)
    Requirement already satisfied: requests<3.0.0,>=2.13.0 in c:\users\minni\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (2.28.1)
    Requirement already satisfied: langcodes<4.0.0,>=3.2.0 in c:\users\minni\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (3.3.0)
    Requirement already satisfied: typer<0.8.0,>=0.3.0 in c:\users\minni\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (0.7.0)
    Requirement already satisfied: setuptools in c:\users\minni\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (63.4.1)
    Requirement already satisfied: pathy>=0.3.5 in c:\users\minni\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (0.10.0)
    Requirement already satisfied: preshed<3.1.0,>=3.0.2 in c:\users\minni\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (3.0.8)
    Requirement already satisfied: spacy-loggers<2.0.0,>=1.0.0 in c:\users\minni\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (1.0.3)
    Requirement already satisfied: cymem<2.1.0,>=2.0.2 in c:\users\minni\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (2.0.7)
    Requirement already satisfied: packaging>=20.0 in c:\users\minni\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (21.3)
    Requirement already satisfied: srsly<3.0.0,>=2.4.3 in c:\users\minni\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (2.4.5)
    Requirement already satisfied: jinja2 in c:\users\minni\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (2.11.3)
    Requirement already satisfied: pydantic!=1.8,!=1.8.1,<1.11.0,>=1.7.4 in c:\users\minni\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (1.10.2)
    Requirement already satisfied: spacy-legacy<3.1.0,>=3.0.10 in c:\users\minni\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (3.0.10)
    Requirement already satisfied: wasabi<1.1.0,>=0.9.1 in c:\users\minni\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (0.10.1)
    Requirement already satisfied: numpy>=1.15.0 in c:\users\minni\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (1.21.5)
    Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in c:\users\minni\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (4.64.1)
    Requirement already satisfied: thinc<8.2.0,>=8.1.0 in c:\users\minni\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (8.1.5)
    Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\users\minni\anaconda3\lib\site-packages (from packaging>=20.0->spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (3.0.9)
    Requirement already satisfied: smart-open<6.0.0,>=5.2.1 in c:\users\minni\anaconda3\lib\site-packages (from pathy>=0.3.5->spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (5.2.1)
    Requirement already satisfied: typing-extensions>=4.1.0 in c:\users\minni\anaconda3\lib\site-packages (from pydantic!=1.8,!=1.8.1,<1.11.0,>=1.7.4->spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (4.3.0)
    Requirement already satisfied: certifi>=2017.4.17 in c:\users\minni\anaconda3\lib\site-packages (from requests<3.0.0,>=2.13.0->spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (2022.9.14)
    Requirement already satisfied: charset-normalizer<3,>=2 in c:\users\minni\anaconda3\lib\site-packages (from requests<3.0.0,>=2.13.0->spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (2.0.4)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\users\minni\anaconda3\lib\site-packages (from requests<3.0.0,>=2.13.0->spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (1.26.11)
    Requirement already satisfied: idna<4,>=2.5 in c:\users\minni\anaconda3\lib\site-packages (from requests<3.0.0,>=2.13.0->spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (3.3)
    Requirement already satisfied: blis<0.8.0,>=0.7.8 in c:\users\minni\anaconda3\lib\site-packages (from thinc<8.2.0,>=8.1.0->spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (0.7.9)
    Requirement already satisfied: confection<1.0.0,>=0.0.1 in c:\users\minni\anaconda3\lib\site-packages (from thinc<8.2.0,>=8.1.0->spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (0.0.3)
    Requirement already satisfied: colorama in c:\users\minni\anaconda3\lib\site-packages (from tqdm<5.0.0,>=4.38.0->spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (0.4.5)
    Requirement already satisfied: click<9.0.0,>=7.1.1 in c:\users\minni\anaconda3\lib\site-packages (from typer<0.8.0,>=0.3.0->spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (8.0.4)
    Requirement already satisfied: MarkupSafe>=0.23 in c:\users\minni\anaconda3\lib\site-packages (from jinja2->spacy<3.5.0,>=3.4.0->de-core-news-sm==3.4.0) (2.0.1)
    [+] Download and installation successful
    You can now load the package via spacy.load('de_core_news_sm')
    


```python
import spacy
nlp = spacy.load("de_core_news_sm")

doc = nlp(example_sentence)
for ent in doc.ents:
    print(ent.text, ent.label_, ent.start, ent.end)
```

    Karl-Heinz Quade PER 0 2
    Grjasowez LOC 13 14
    

### DisplaCy


```python
from spacy import displacy
displacy.render(doc, style = "ent")
```


<span class="tex2jax_ignore"><div class="entities" style="line-height: 2.5; direction: ltr">
<mark class="entity" style="background: #ddd; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">
    Karl-Heinz Quade
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; vertical-align: middle; margin-left: 0.5rem">PER</span>
</mark>
 ist von März 1944 bis August 1948 im Lager 150 in 
<mark class="entity" style="background: #ff9561; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">
    Grjasowez
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; vertical-align: middle; margin-left: 0.5rem">LOC</span>
</mark>
 interniert.</div></span>



```python
displacy.render(doc, jupyter = True, style = "ent")
```


<span class="tex2jax_ignore"><div class="entities" style="line-height: 2.5; direction: ltr">
<mark class="entity" style="background: #ddd; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">
    Karl-Heinz Quade
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; vertical-align: middle; margin-left: 0.5rem">PER</span>
</mark>
 ist von März 1944 bis August 1948 im Lager 150 in 
<mark class="entity" style="background: #ff9561; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">
    Grjasowez
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; vertical-align: middle; margin-left: 0.5rem">LOC</span>
</mark>
 interniert.</div></span>



```python
displacy.render(doc, jupyter = True, style = "dep")
```


<span class="tex2jax_ignore"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="de" id="bb47b4ac0fc848e9a0542bf1754cb24c-0" class="displacy" width="2675" height="662.0" direction="ltr" style="max-width: none; height: 662.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="50">Karl-Heinz</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">PROPN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="225">Quade</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">PROPN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="400">ist</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">AUX</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="575">von</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="750">März</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="925">1944</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">NUM</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">bis</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">August</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">1948</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">NUM</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">im</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">Lager</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1975">150</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">NUM</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2150">in</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2325">Grjasowez</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">PROPN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2500">interniert.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">VERB</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-0" stroke-width="2px" d="M70,527.0 C70,439.5 200.0,439.5 200.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pnc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,529.0 L62,517.0 78,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-1" stroke-width="2px" d="M245,527.0 C245,439.5 375.0,439.5 375.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">sb</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,529.0 L237,517.0 253,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-2" stroke-width="2px" d="M595,527.0 C595,89.5 2495.0,89.5 2495.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">mo</textPath>
    </text>
    <path class="displacy-arrowhead" d="M595,529.0 L587,517.0 603,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-3" stroke-width="2px" d="M595,527.0 C595,439.5 725.0,439.5 725.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nk</textPath>
    </text>
    <path class="displacy-arrowhead" d="M725.0,529.0 L733.0,517.0 717.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-4" stroke-width="2px" d="M770,527.0 C770,439.5 900.0,439.5 900.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nk</textPath>
    </text>
    <path class="displacy-arrowhead" d="M900.0,529.0 L908.0,517.0 892.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-5" stroke-width="2px" d="M1120,527.0 C1120,177.0 2490.0,177.0 2490.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">mo</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,529.0 L1112,517.0 1128,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-6" stroke-width="2px" d="M1120,527.0 C1120,439.5 1250.0,439.5 1250.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nk</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1250.0,529.0 L1258.0,517.0 1242.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-7" stroke-width="2px" d="M1295,527.0 C1295,439.5 1425.0,439.5 1425.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nk</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1425.0,529.0 L1433.0,517.0 1417.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-8" stroke-width="2px" d="M1645,527.0 C1645,264.5 2485.0,264.5 2485.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">mo</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,529.0 L1637,517.0 1653,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-9" stroke-width="2px" d="M1645,527.0 C1645,439.5 1775.0,439.5 1775.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nk</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1775.0,529.0 L1783.0,517.0 1767.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-10" stroke-width="2px" d="M1820,527.0 C1820,439.5 1950.0,439.5 1950.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nk</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1950.0,529.0 L1958.0,517.0 1942.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-11" stroke-width="2px" d="M2170,527.0 C2170,352.0 2480.0,352.0 2480.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">mo</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2170,529.0 L2162,517.0 2178,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-12" stroke-width="2px" d="M2170,527.0 C2170,439.5 2300.0,439.5 2300.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nk</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2300.0,529.0 L2308.0,517.0 2292.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-13" stroke-width="2px" d="M420,527.0 C420,2.0 2500.0,2.0 2500.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bb47b4ac0fc848e9a0542bf1754cb24c-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">oc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2500.0,529.0 L2508.0,517.0 2492.0,517.0" fill="currentColor"/>
</g>
</svg></span>


Couln't save image


```python
svg = displacy.render(doc, style="dep")

# output_path = Path("./sentence.svg") 
# # you can keep there only "dependency_plot.svg" if you want to save it in the same folder where you run the script 
# output_path.open("w", encoding="utf-8").write(svg)

type(svg)
```


```python
# svg = displacy.render(doc, jupyter = True, style = "dep")
# output_path = Path("sentence.svg")
# output_path.write(svg)
```

### Named Entity Linking


```python
!pip install spacy-dbpedia-spotlight
```


```python
import spacy
nlp = spacy.load('de_core_news_sm')
nlp.add_pipe('dbpedia_spotlight', config={'language_code': 'de'})

doc = nlp(example_sentence)
for ent in doc.ents:
    print(ent.text, ent.label_, ent.kb_id_)
```

    Grjasowez DBPEDIA_ENT http://de.dbpedia.org/resource/Grjasowez
    interniert DBPEDIA_ENT http://de.dbpedia.org/resource/Internierung
    




```python
import requests
data = requests.get("http://de.dbpedia.org/data/Grjasowez.json").json()
```


```python
print(data)
```

    {'http://de.dbpedia.org/resource/Obnora': {'http://dbpedia.org/ontology/sourceConfluence': [{'type': 'uri', 'value': 'http://de.dbpedia.org/resource/Grjasowez'}]}, 'http://de.dbpedia.org/resource/Grjasowez': {'http://www.w3.org/1999/02/22-rdf-syntax-ns#type': [{'type': 'uri', 'value': 'http://schema.org/Place'}, {'type': 'uri', 'value': 'http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing'}, {'type': 'uri', 'value': 'http://www.w3.org/2002/07/owl#Thing'}, {'type': 'uri', 'value': 'http://dbpedia.org/ontology/Settlement'}, {'type': 'uri', 'value': 'http://dbpedia.org/ontology/PopulatedPlace'}, {'type': 'uri', 'value': 'http://dbpedia.org/ontology/Location'}, {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q486972'}, {'type': 'uri', 'value': 'http://dbpedia.org/ontology/Place'}], 'http://www.w3.org/2000/01/rdf-schema#label': [{'type': 'literal', 'value': 'Grjasowez', 'lang': 'de'}], 'http://www.w3.org/2000/01/rdf-schema#comment': [{'type': 'literal', 'value': 'Grjasowez (russisch Грязовец) ist eine kleine Kreisstadt mit 15.528 Einwohnern (Stand 14. Oktober 2010) in der Oblast Wologda im Norden des europäischen Teils Russlands.', 'lang': 'de'}], 'http://www.w3.org/2002/07/owl#sameAs': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Gryazovets'}, {'type': 'uri', 'value': 'http://fr.dbpedia.org/resource/Griazovets'}, {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q134667'}, {'type': 'uri', 'value': 'http://wikidata.dbpedia.org/resource/Q134667'}, {'type': 'uri', 'value': 'http://de.dbpedia.org/resource/Grjasowez'}, {'type': 'uri', 'value': 'http://rdf.freebase.com/ns/m.0gpnx7'}, {'type': 'uri', 'value': 'http://ko.dbpedia.org/resource/그랴조베츠'}, {'type': 'uri', 'value': 'http://it.dbpedia.org/resource/Grjazovec'}, {'type': 'uri', 'value': 'http://pl.dbpedia.org/resource/Griazowiec'}], 'http://www.georss.org/georss/point': [{'type': 'literal', 'value': '58.88333333333333 40.25'}], 'http://xmlns.com/foaf/0.1/name': [{'type': 'literal', 'value': 'Grjasowez', 'lang': 'de'}, {'type': 'literal', 'value': 'Грязовец', 'lang': 'de'}], 'http://www.w3.org/2003/01/geo/wgs84_pos#lat': [{'type': 'literal', 'value': 58.88333511352539, 'datatype': 'http://www.w3.org/2001/XMLSchema#float'}], 'http://www.w3.org/2003/01/geo/wgs84_pos#long': [{'type': 'literal', 'value': 40.25, 'datatype': 'http://www.w3.org/2001/XMLSchema#float'}], 'http://xmlns.com/foaf/0.1/depiction': [{'type': 'uri', 'value': 'http://commons.wikimedia.org/wiki/Special:FilePath/Coat_of_Arms_of_Gryazovets_(Vologda_oblast)_(1781).png'}], 'http://xmlns.com/foaf/0.1/homepage': [{'type': 'uri', 'value': 'http://gradm.ru/'}], 'http://purl.org/dc/terms/subject': [{'type': 'uri', 'value': 'http://de.dbpedia.org/resource/Kategorie:Ort_in_der_Oblast_Wologda'}], 'http://xmlns.com/foaf/0.1/isPrimaryTopicOf': [{'type': 'uri', 'value': 'http://de.wikipedia.org/wiki/Grjasowez'}], 'http://dbpedia.org/ontology/wikiPageID': [{'type': 'literal', 'value': 2159725, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://dbpedia.org/ontology/wikiPageRevisionID': [{'type': 'literal', 'value': 156713958, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://dbpedia.org/ontology/wikiPageExternalLink': [{'type': 'uri', 'value': 'http://gryazovec.ru/'}, {'type': 'uri', 'value': 'http://russki-plen.ucoz.ru/_ld/0/93_lagergeschichte.pdf'}, {'type': 'uri', 'value': 'http://www.mojgorod.ru/vologod_obl/grjazovec/index.html'}, {'type': 'uri', 'value': 'http://gradm.ru/'}], 'http://de.dbpedia.org/property/artDesGebietes': [{'type': 'literal', 'value': 'Rajon', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}], 'http://de.dbpedia.org/property/ersteErwähnung': [{'type': 'literal', 'value': 1538, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://de.dbpedia.org/property/gebiet': [{'type': 'literal', 'value': 'Grjasowez', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}], 'http://de.dbpedia.org/property/latDeg': [{'type': 'literal', 'value': 58, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://de.dbpedia.org/property/latMin': [{'type': 'literal', 'value': 53, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://de.dbpedia.org/property/latSec': [{'type': 'literal', 'value': 0, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://de.dbpedia.org/property/lonDeg': [{'type': 'literal', 'value': 40, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://de.dbpedia.org/property/lonMin': [{'type': 'literal', 'value': 15, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://de.dbpedia.org/property/lonSec': [{'type': 'literal', 'value': 0, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://de.dbpedia.org/property/oberhaupt': [{'type': 'literal', 'value': 'Michail Rudakow', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}], 'http://de.dbpedia.org/property/okato': [{'type': 'literal', 'value': 19224501, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://de.dbpedia.org/property/status': [{'type': 'literal', 'value': 'Stadt', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}], 'http://de.dbpedia.org/property/statusSeit': [{'type': 'literal', 'value': 1780, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://de.dbpedia.org/property/wappen': [{'type': 'literal', 'value': 'Coat of Arms of Gryazovets  .png', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}], 'http://www.w3.org/ns/prov#wasDerivedFrom': [{'type': 'uri', 'value': 'http://de.wikipedia.org/wiki/Grjasowez?oldid=156713958'}], 'http://dbpedia.org/ontology/PopulatedPlace/areaTotal': [{'type': 'literal', 'value': '14.0', 'datatype': 'http://dbpedia.org/datatype/squareKilometre'}], 'http://dbpedia.org/ontology/abstract': [{'type': 'literal', 'value': 'Grjasowez (russisch Грязовец) ist eine kleine Kreisstadt mit 15.528 Einwohnern (Stand 14. Oktober 2010) in der Oblast Wologda im Norden des europäischen Teils Russlands.', 'lang': 'de'}], 'http://dbpedia.org/ontology/areaCode': [{'type': 'literal', 'value': '(+7) 81755'}], 'http://dbpedia.org/ontology/areaTotal': [{'type': 'literal', 'value': 14000000, 'datatype': 'http://www.w3.org/2001/XMLSchema#double'}], 'http://dbpedia.org/ontology/elevation': [{'type': 'literal', 'value': 185, 'datatype': 'http://www.w3.org/2001/XMLSchema#double'}], 'http://dbpedia.org/ontology/leaderTitle': [{'type': 'literal', 'value': 'Bürgermeister', 'lang': 'de'}], 'http://dbpedia.org/ontology/postalCode': [{'type': 'literal', 'value': '162000–162002'}], 'http://dbpedia.org/ontology/thumbnail': [{'type': 'uri', 'value': 'http://commons.wikimedia.org/wiki/Special:FilePath/Coat_of_Arms_of_Gryazovets_(Vologda_oblast)_(1781).png?width=300'}]}, 'http://de.dbpedia.org/resource/Lew_Alexandrowitsch_Tschugajew': {'http://dbpedia.org/ontology/deathPlace': [{'type': 'uri', 'value': 'http://de.dbpedia.org/resource/Grjasowez'}]}, 'http://de.dbpedia.org/resource/Gryazovets': {'http://dbpedia.org/ontology/wikiPageRedirects': [{'type': 'uri', 'value': 'http://de.dbpedia.org/resource/Grjasowez'}]}, 'http://de.wikipedia.org/wiki/Grjasowez': {'http://xmlns.com/foaf/0.1/primaryTopic': [{'type': 'uri', 'value': 'http://de.dbpedia.org/resource/Grjasowez'}]}}
    


```python
data.keys()
```




    dict_keys(['http://de.dbpedia.org/resource/Obnora', 'http://de.dbpedia.org/resource/Grjasowez', 'http://de.dbpedia.org/resource/Lew_Alexandrowitsch_Tschugajew', 'http://de.dbpedia.org/resource/Gryazovets', 'http://de.wikipedia.org/wiki/Grjasowez'])



note: output not the same as example output in lesson, likely due to earlier error

### Export Our Data


```python
start_date = "1800" #YYYY-MM-DD
end_date = "2000"
source_title = "Karl-Heinz Quade Diary"

output_text = ""
column_header = "id\ttitle\ttitle_source\tstart\tend\n"  
output_text += column_header  

places_list = []
if matches:
    places_list.extend([ doc[start:end].text for match_id, start, end in matches ])
if doc.ents:
    places_list.extend([ ent.text for ent in doc.ents if ent.label_ == "GPE" or ent.label_ == "LOC"])

# remove duplicate place names by creating a list of names and then converting the list to a set
unique_places = set(places_list)

for id, place in enumerate(unique_places):
    output_text += f"{id}\t{place}\t{source_title}\t{start_date}\t{end_date}\n"
#     output_text += f"{id},{place},{source_title},{start_date},{end_date}\n"


filename = source_title.lower().replace(' ','_') + '.tsv'
Path(filename).write_text(output_text)
print('created: ', filename)
```

    created:  karl-heinz_quade_diary.tsv
    

Note: After attempting to troubleshoot w/ the help of Prof. Micah, the output file changed to be missing information

## Uploading to the World Historical Gazetteer

Note: complete this section once you hear back about the error from wh gazetteer

I was unable to complete this section due to the WHG resource having issues with the file I attempted to upload


```python

```
