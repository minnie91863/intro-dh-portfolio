---
layout: page
title: NER with Gibbon
description: Class exercise with NER to prepare Gibbon for GIS
---

# Named Entity Recognition (NER)

Named entity recognition (NER) is a branch of natural language processing that focuses on extracting the text of names or other semantically distinct ideas from a larger text and tagging according to its special meaning within a system. NER can be broken into two broad categories: algorithms which use deterministic rules to find names (find all tokens that match the regular expression: `([A-Z][a-z]+)`) and statisical models which make guesses about where an entity begins and ends.

In this class, we'll use `spaCy`'s small English NER (`en_core_web_sm`) model to explore how statistical models can recognize named entities. Then, we'll see some of the practical considerations we must take when working with NER. Our workflow will look like this:
* Reacquaint ourselves with `spaCy`
* Pass a single chapter of Gibbon's *Decline and Fall* into the `spaCy` parser
* Examine the NER results
* Filter out all place names
* Use the Pleiades gazetteer to get coordinates for all valid place names
* Save data to CSV

Finally, you'll have the chance to boil down our process into a function and test it out on other chapters from Gibbon (or other texts). Keep in mind that, for next class, you must have your own version of the data we produce today. That's because, next week, Carolyn Talmadge from the DataLab will be showing us how to turn our CSVs into webmaps and applications. 

## Preparing our data


```python
# redownload spaCy's small model - should see 'requirement already satisfied'
!python -m spacy download en_core_web_sm
```

    Collecting en-core-web-sm==3.4.1
      Downloading https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.4.1/en_core_web_sm-3.4.1-py3-none-any.whl (12.8 MB)
    Requirement already satisfied: spacy<3.5.0,>=3.4.0 in c:\users\minnie\anaconda3\lib\site-packages (from en-core-web-sm==3.4.1) (3.4.2)
    Requirement already satisfied: packaging>=20.0 in c:\users\minnie\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (21.3)
    Requirement already satisfied: catalogue<2.1.0,>=2.0.6 in c:\users\minnie\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (2.0.8)
    Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in c:\users\minnie\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (4.64.0)
    Requirement already satisfied: spacy-legacy<3.1.0,>=3.0.10 in c:\users\minnie\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (3.0.10)
    Requirement already satisfied: jinja2 in c:\users\minnie\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (2.11.3)
    Requirement already satisfied: spacy-loggers<2.0.0,>=1.0.0 in c:\users\minnie\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (1.0.3)
    Requirement already satisfied: setuptools in c:\users\minnie\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (61.2.0)
    Requirement already satisfied: cymem<2.1.0,>=2.0.2 in c:\users\minnie\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (2.0.7)
    Requirement already satisfied: preshed<3.1.0,>=3.0.2 in c:\users\minnie\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (3.0.8)
    Requirement already satisfied: srsly<3.0.0,>=2.4.3 in c:\users\minnie\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (2.4.5)
    Requirement already satisfied: langcodes<4.0.0,>=3.2.0 in c:\users\minnie\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (3.3.0)
    Requirement already satisfied: pydantic!=1.8,!=1.8.1,<1.11.0,>=1.7.4 in c:\users\minnie\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (1.10.2)
    Requirement already satisfied: numpy>=1.15.0 in c:\users\minnie\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (1.21.5)
    Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in c:\users\minnie\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (1.0.9)
    Requirement already satisfied: typer<0.5.0,>=0.3.0 in c:\users\minnie\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (0.4.2)
    Requirement already satisfied: pathy>=0.3.5 in c:\users\minnie\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (0.6.2)
    Requirement already satisfied: wasabi<1.1.0,>=0.9.1 in c:\users\minnie\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (0.10.1)
    Requirement already satisfied: thinc<8.2.0,>=8.1.0 in c:\users\minnie\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (8.1.5)
    Requirement already satisfied: requests<3.0.0,>=2.13.0 in c:\users\minnie\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (2.27.1)
    Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\users\minnie\anaconda3\lib\site-packages (from packaging>=20.0->spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (3.0.4)
    Requirement already satisfied: smart-open<6.0.0,>=5.2.1 in c:\users\minnie\anaconda3\lib\site-packages (from pathy>=0.3.5->spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (5.2.1)
    Requirement already satisfied: typing-extensions>=4.1.0 in c:\users\minnie\anaconda3\lib\site-packages (from pydantic!=1.8,!=1.8.1,<1.11.0,>=1.7.4->spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (4.1.1)
    Requirement already satisfied: charset-normalizer~=2.0.0 in c:\users\minnie\anaconda3\lib\site-packages (from requests<3.0.0,>=2.13.0->spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (2.0.4)
    Requirement already satisfied: idna<4,>=2.5 in c:\users\minnie\anaconda3\lib\site-packages (from requests<3.0.0,>=2.13.0->spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (3.3)
    Requirement already satisfied: certifi>=2017.4.17 in c:\users\minnie\anaconda3\lib\site-packages (from requests<3.0.0,>=2.13.0->spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (2021.10.8)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\users\minnie\anaconda3\lib\site-packages (from requests<3.0.0,>=2.13.0->spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (1.26.9)
    Requirement already satisfied: blis<0.8.0,>=0.7.8 in c:\users\minnie\anaconda3\lib\site-packages (from thinc<8.2.0,>=8.1.0->spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (0.7.9)
    Requirement already satisfied: confection<1.0.0,>=0.0.1 in c:\users\minnie\anaconda3\lib\site-packages (from thinc<8.2.0,>=8.1.0->spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (0.0.3)
    Requirement already satisfied: colorama in c:\users\minnie\anaconda3\lib\site-packages (from tqdm<5.0.0,>=4.38.0->spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (0.4.4)
    Requirement already satisfied: click<9.0.0,>=7.1.1 in c:\users\minnie\anaconda3\lib\site-packages (from typer<0.5.0,>=0.3.0->spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (8.0.4)
    Requirement already satisfied: MarkupSafe>=0.23 in c:\users\minnie\anaconda3\lib\site-packages (from jinja2->spacy<3.5.0,>=3.4.0->en-core-web-sm==3.4.1) (2.0.1)
    [+] Download and installation successful
    You can now load the package via spacy.load('en_core_web_sm')
    


```python
import pandas as pd
import spacy
nlp = spacy.load('en_core_web_sm') # good idea to initialize here
```


```python
# downloading gibbon text from my gh
import wget
import os
if not os.path.isfile('gibbon_text.csv'):
    wget.download('https://raw.githubusercontent.com/pnadelofficial/FallDHCourseMaterials/main/gibbon_text.csv')
```


```python
gibbon_by_chapter = pd.read_csv('gibbon_text.csv').rename(columns={'Unnamed: 0':'chapter'})
gibbon_by_chapter
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>chapter</th>
      <th>StringText</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Chapter 1</td>
      <td>\nIn the second century of the Christian era, ...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Chapter 2</td>
      <td>\nIt is not alone by the rapidity or extent of...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Chapter 3</td>
      <td>\nThe obvious definition of a monarchy seems t...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Chapter 4</td>
      <td>\nThe mildness of Marcus, which the rigid disc...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Chapter 5</td>
      <td>\nThe power of the sword is more sensibly felt...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>66</th>
      <td>Chapter 67</td>
      <td>\nThe respective merits of Rome and Constantin...</td>
    </tr>
    <tr>
      <th>67</th>
      <td>Chapter 68</td>
      <td>\nThe siege of Constantinople by the Turks att...</td>
    </tr>
    <tr>
      <th>68</th>
      <td>Chapter 69</td>
      <td>\nIn the first ages of the decline and fall of...</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Chapter 70</td>
      <td>\nIn the apprehension of modern times, Petrarc...</td>
    </tr>
    <tr>
      <th>70</th>
      <td>Chapter 71</td>
      <td>\nIn the last days of Pope Eugenius the Fourth...</td>
    </tr>
  </tbody>
</table>
<p>71 rows × 2 columns</p>
</div>




```python
first_chapter = gibbon_by_chapter['StringText'][0]
```

## Using `spaCy`'s off-the-shelf NER model

This model was trained on a wide variety of sources, so we can't expect it to be completely accurate. We'll revisit that problem soon. We can train our own NER model and it would do better, but this will take some time to do and requires a lot of set up. If you're interested in training your own model, reach out to me and we can work together on it.


```python
# pass the first chapter into spaCy parser
first_chapter_doc = nlp(first_chapter)
```


```python
for entity in first_chapter_doc.ents: # can access NER with the .ents attribute
    print(entity.text, entity.label_, sep='\t')
```

    the second century	DATE
    Christian	NORP
    Rome	GPE
    Roman	NORP
    more than fourscore years	DATE
    Nerva	GPE
    Trajan	GPE
    Hadrian	NORP
    two	CARDINAL
    Antonines	NORP
    two	CARDINAL
    Marcus Antoninus	GPE
    Romans	NORP
    senate	ORG
    seven first centuries	DATE
    Augustus	ORG
    Rome	GPE
    every day	DATE
    Augustus	ORG
    Rome	GPE
    Parthians	NORP
    Crassus	PRODUCT
    Aethiopia	GPE
    Arabia Felix	PERSON
    a thousand miles	QUANTITY
    Europe	LOC
    Germany	GPE
    first	ORDINAL
    Roman	NORP
    Augustus	PERSON
    senate	ORG
    the Atlantic Ocean	LOC
    Rhine	PERSON
    Danube	PERSON
    Euphrates	LOC
    Arabia	GPE
    Africa	LOC
    Augustus	ORG
    first	ORDINAL
    Caesars	ORG
    Imperial	ORG
    Roman	NORP
    Roman	NORP
    the first century	DATE
    Christian	NORP
    Britain	GPE
    Caesar	ORG
    Augustus	ORG
    Gaul	PERSON
    Britain	GPE
    continental	ORG
    about forty years	DATE
    Roman	NORP
    Britons	PERSON
    Caractacus	ORG
    Boadicea	GPE
    Druids	ORG
    Imperial	ORG
    Domitian	PERSON
    Agricola	ORG
    Caledonians	NORP
    Grampian	NORP
    Roman	NORP
    Britain	GPE
    Agricola	ORG
    Ireland	GPE
    one	CARDINAL
    Britons	PERSON
    Agricola	ORG
    Britain	GPE
    two	CARDINAL
    Scotland	GPE
    about forty miles	QUANTITY
    Antoninus Pius	GPE
    Antoninus	GPE
    Edinburgh	GPE
    Glasgow	PERSON
    Roman	NORP
    Caledonians	NORP
    gloomy hills	GPE
    winter	DATE
    Roman	NORP
    Imperial	ORG
    Augustus	ORG
    Trajan	ORG
    first	ORDINAL
    Trajan	PERSON
    Dacians	NORP
    Danube	PERSON
    Domitian	NORP
    Rome	GPE
    Dacian	NORP
    Trajan	GPE
    five years	DATE
    Dacia	PERSON
    second	ORDINAL
    Augustus	ORG
    about thirteen hundred miles	QUANTITY
    Dniester	ORG
    Theiss	NORP
    Tibiscus	ORG
    the Lower Danube	ORG
    the Euxine Sea	LOC
    Danube	PERSON
    Bender	PERSON
    Turkish	NORP
    Russian	NORP
    Trajan	PERSON
    Alexander	ORG
    Trajan	GPE
    Roman	NORP
    Philip	GPE
    Trajan	ORG
    Parthians	NORP
    Tigris	GPE
    Armenia	GPE
    the Persian gulf	LOC
    first	ORDINAL
    Roman	NORP
    Arabia	GPE
    Trajan	PERSON
    India	GPE
    senate	ORG
    Bosphorus	GPE
    Colchos	GPE
    Iberia	GPE
    Albania	GPE
    Osrhoene	PERSON
    Parthian	NORP
    Median	NORP
    Carduchian	NORP
    Armenia	GPE
    Mesopotamia	GPE
    Assyria	GPE
    Trajan	PERSON
    Capitol	FAC
    one	CARDINAL
    Roman	NORP
    Jupiter	LOC
    Roman	NORP
    many ages	DATE
    Terminus	ORG
    Jupiter	LOC
    Hadrian	NORP
    Trajan	PERSON
    first	ORDINAL
    Parthians	NORP
    Roman	NORP
    Armenia	GPE
    Mesopotamia	GPE
    Assyria	GPE
    Augustus	ORG
    Euphrates	LOC
    Hadrian	NORP
    Trajan	GPE
    Trajan	PERSON
    Hadrian	NORP
    Antoninus	GPE
    Caledonia	GPE
    the Upper Egypt	GPE
    Antoninus Pius	ORG
    Italy	GPE
    the twenty-three years	DATE
    Rome	GPE
    Lanuvian	NORP
    Augustus	ORG
    Hadrian	NORP
    two	CARDINAL
    Antonines	NORP
    Roman	NORP
    forty-three years	DATE
    Hadrian	NORP
    Antoninus Pius	ORG
    Roman	NORP
    Roman	NORP
    Hadrian	NORP
    Antoninus	LOC
    Parthians	NORP
    Germans	NORP
    Marcus	PERSON
    Marcus	GPE
    Euphrates	LOC
    Danube	ORG
    Roman	NORP
    Roman	NORP
    Roman	NORP
    Europe	LOC
    first	ORDINAL
    Roman	NORP
    the hour	TIME
    Roman	NORP
    Imperial	ORG
    Romans	NORP
    the evening	TIME
    daily	DATE
    winter-quarters	DATE
    Roman	NORP
    Pyrrhic	PRODUCT
    Roman	NORP
    Hadrian	NORP
    Trajan	PERSON
    Roman	NORP
    Nine centuries	DATE
    Polybius	ORG
    Punic	ORG
    Caesar	ORG
    Hadrian	NORP
    Antonines	PRODUCT
    Imperial	ORG
    ten	CARDINAL
    fifty-five	CARDINAL
    first	ORDINAL
    eleven hundred and five	CARDINAL
    nine	CARDINAL
    five hundred and fifty-five	CARDINAL
    six thousand one hundred	CARDINAL
    four feet	QUANTITY
    two and a half	DATE
    about six feet	QUANTITY
    eighteen inches	QUANTITY
    only ten or twelve	CARDINAL
    Roman	NORP
    Spanish	LANGUAGE
    eight	CARDINAL
    three feet	QUANTITY
    Greeks	PERSON
    Macedonians	NORP
    sixteen	CARDINAL
    ten	CARDINAL
    first	ORDINAL
    first	ORDINAL
    an hundred and thirty-two	CARDINAL
    nine	CARDINAL
    sixty-six	CARDINAL
    seven hundred and twenty-six	CARDINAL
    Rome	GPE
    Italy	GPE
    Trajan	PERSON
    Hadrian	NORP
    Spain	GPE
    Cappadocia	PERSON
    Roman	NORP
    East	LOC
    oblong	GPE
    Rome	GPE
    Romans	NORP
    Roman	NORP
    ten	CARDINAL
    fifty-five	CARDINAL
    Roman	NORP
    about seven hundred yards	QUANTITY
    twenty thousand	CARDINAL
    Romans	NORP
    two hundred feet	QUANTITY
    twelve feet	QUANTITY
    twelve feet	QUANTITY
    many days	DATE
    about six hours	TIME
    twenty miles	QUANTITY
    first	ORDINAL
    Roman	NORP
    six thousand eight hundred and thirty-one	DATE
    Romans	NORP
    about twelve thousand five hundred	CARDINAL
    Hadrian	NORP
    three hundred and seventy-five thousand	CARDINAL
    Romans	NORP
    Three	CARDINAL
    Britain	GPE
    Rhine	PERSON
    Danube	PERSON
    sixteen	CARDINAL
    two	CARDINAL
    Lower	LOC
    three	CARDINAL
    the Upper Germany	GPE
    one	CARDINAL
    Rhaetia	ORG
    Noricum	GPE
    four	CARDINAL
    Pannonia	GPE
    three	CARDINAL
    Maesia	GPE
    two	CARDINAL
    Dacia	PERSON
    Euphrates	ORG
    eight	CARDINAL
    six	CARDINAL
    Syria	GPE
    two	CARDINAL
    Cappadocia	PERSON
    Egypt	GPE
    Africa	LOC
    Spain	GPE
    Italy	GPE
    twenty thousand	CARDINAL
    City Cohorts and	FAC
    Praetorians	NORP
    navy	ORG
    Romans	NORP
    Tyre	ORG
    Marseilles	GPE
    Romans	NORP
    Mediterranean	LOC
    Augustus	ORG
    two	CARDINAL
    Italy	GPE
    Ravenna	PERSON
    Adriatic	NORP
    Misenum	GPE
    Naples	GPE
    two	CARDINAL
    three	CARDINAL
    Augustus	ORG
    Actium	ORG
    Liburnians	LOC
    Liburnians	NORP
    two	CARDINAL
    Ravenna	PERSON
    Misenum	GPE
    Mediterranean	LOC
    several thousand	CARDINAL
    two	CARDINAL
    Roman	NORP
    Frejus	DATE
    Provence	GPE
    Euxine	PERSON
    forty	CARDINAL
    three thousand	CARDINAL
    Gaul	PERSON
    Britain	GPE
    Rhine	PERSON
    Danube	PERSON
    Imperial	ORG
    more than four hundred and fifty thousand	CARDINAL
    the last century	DATE
    Roman	NORP
    Hadrian	NORP
    Antonines	ORG
    Spain	GPE
    Europe	LOC
    Mediterranean	LOC
    the Atlantic Ocean	LOC
    two	CARDINAL
    Augustus	ORG
    three	CARDINAL
    Lusitania	GPE
    Baetica	GPE
    Tarraconensis	ORG
    Portugal	GPE
    Lusitanians	NORP
    East	LOC
    North	LOC
    Grenada	GPE
    Andalusia	GPE
    Baetica	GPE
    Spain	GPE
    Asturias	GPE
    Biscay	GPE
    Navarre	PERSON
    Leon	PERSON
    two	CARDINAL
    Castilles	GPE
    Murcia	GPE
    Valencia	GPE
    Catalonia	GPE
    Arragon	GPE
    third	ORDINAL
    Roman	NORP
    Tarragona	GPE
    Celtiberians	NORP
    Cantabrians	NORP
    Asturians	NORP
    Rome	GPE
    first	ORDINAL
    Arabs	NORP
    Ancient Gaul	ORG
    Alps	GPE
    Rhine	GPE
    Ocean	LOC
    France	GPE
    Alsace	GPE
    Lorraine	PERSON
    Savoy	ORG
    Switzerland	GPE
    four	CARDINAL
    Rhine	GPE
    Liege	GPE
    Luxemburg	GPE
    Hainault	ORG
    Flanders	ORG
    Brabant	PERSON
    Augustus	PERSON
    Gaul	ORG
    hundred	CARDINAL
    Mediterranean	LOC
    Languedoc	GPE
    Provence	ORG
    Dauphiné	ORG
    Narbonne	PERSON
    Aquitaine	ORG
    Seine	PRODUCT
    the Celtic Gaul	LOC
    Lugdunum	GPE
    Lyons	WORK_OF_ART
    Belgic	PERSON
    Seine	ORG
    Rhine	GPE
    Caesar	ORG
    Germans	NORP
    Belgic	PERSON
    Roman	NORP
    Gallic	PERSON
    Rhine	GPE
    Basil to Leyden	PERSON
    the Lower Germany	GPE
    Antonines	NORP
    six	CARDINAL
    Gaul	ORG
    Narbonnese	NORP
    Aquitaine	ORG
    Celtic	ORG
    Lyonnese	NORP
    Belgic	ORG
    two	CARDINAL
    Britain	GPE
    Roman	NORP
    England	GPE
    Wales	GPE
    Scotland	GPE
    the Friths of Dumbarton	ORG
    Edinburgh	GPE
    Britain	GPE
    Belgae	ORG
    Brigantes	GPE
    North	LOC
    South Wales	GPE
    Iceni	NORP
    Norfolk	GPE
    Suffolk	GPE
    Spain	GPE
    Gaul	ORG
    Britain	GPE
    Roman	NORP
    European	NORP
    Hercules	GPE
    Antoninus	GPE
    Tagus	ORG
    Rhine	PERSON
    Danube	PERSON
    Roman	NORP
    Lombardy	LOC
    Italy	GPE
    Gauls	PERSON
    Po	LOC
    Piedmont	GPE
    Romagna	GPE
    Alps	LOC
    Ligurians	NORP
    Genoa	ORG
    Venice	GPE
    Adige	ORG
    Venetians	NORP
    Tuscany	PERSON
    Etruscans	NORP
    Umbrians	PERSON
    Italy	GPE
    first	ORDINAL
    Tiber	PERSON
    seven	CARDINAL
    Rome	GPE
    Sabines	ORG
    Latins	ORG
    Volsci	PRODUCT
    Naples	GPE
    first	ORDINAL
    Campania	GPE
    Naples	GPE
    Marsi	ORG
    Samnites	ORG
    Apulians	NORP
    Lucanians	NORP
    Augustus	PERSON
    Italy	GPE
    eleven	CARDINAL
    Istria	GPE
    Roman	NORP
    European	NORP
    Rome	GPE
    Rhine	PERSON
    Danube	PERSON
    only thirty miles	QUANTITY
    thirteen hundred miles	QUANTITY
    sixty	CARDINAL
    six	CARDINAL
    Euxine	PERSON
    Danube	PERSON
    Illyricum	GPE
    Illyrian	NORP
    Rhaetia, Noricum	ORG
    Pannonia	GPE
    Dalmatia	ORG
    Dacia	PERSON
    Maesia	GPE
    Thrace	GPE
    Macedonia	GPE
    Greece	GPE
    Rhaetia	ORG
    Vindelicians	NORP
    Alps	LOC
    Danube	ORG
    Inn	ORG
    Bavaria	GPE
    Augsburg	GPE
    German	NORP
    Grisons	PERSON
    Tyrol	ORG
    Austria	GPE
    Inn	ORG
    Danube	ORG
    Save	ORG
    Austria	GPE
    Styria	GPE
    Carinthia	GPE
    Carniola	ORG
    the Lower Hungary	GPE
    Sclavonia	GPE
    Noricum	GPE
    Pannonia	GPE
    Roman	NORP
    German	NORP
    Romans	NORP
    Austrian	NORP
    Bohemia	PERSON
    Moravia	GPE
    Austria	GPE
    Hungary	GPE
    Theiss	NORP
    Danube	PERSON
    Austria	GPE
    Roman	NORP
    Dalmatia	ORG
    Illyricum	GPE
    Save	ORG
    Adriatic	NORP
    Venetian	NORP
    Sclavonian	NORP
    Croatia	GPE
    Bosnia	GPE
    Austrian	NORP
    Turkish	NORP
    Christian	NORP
    Mahometan	NORP
    Danube	PERSON
    Theiss	NORP
    Save	ORG
    Greeks	WORK_OF_ART
    Ister	ORG
    Maesia	GPE
    Dacia	PERSON
    Trajan	ORG
    Danube	PERSON
    Temeswar	ORG
    Transylvania	GPE
    Hungary	GPE
    Moldavia	GPE
    Walachia	GPE
    the Ottoman Porte	GPE
    Danube	ORG
    Maesia	GPE
    the middle ages	DATE
    Servia	GPE
    Bulgaria	GPE
    Turkish	NORP
    Roumelia	PERSON
    Turks	NORP
    Thrace	GPE
    Macedonia	GPE
    Greece	GPE
    Roman	NORP
    Antonines	ORG
    Thrace	ORG
    Haemus	PERSON
    Rhodope	PERSON
    Bosphorus	PERSON
    Hellespont	GPE
    Rome	GPE
    Constantine	ORG
    Bosphorus	PERSON
    Macedonia	GPE
    Alexander	ORG
    Asia	LOC
    two	CARDINAL
    Philips	ORG
    Epirus	ORG
    Thessaly	GPE
    Aegean	NORP
    Ionian	NORP
    Thebes	GPE
    Argos	LOC
    Sparta	GPE
    Athens	GPE
    Greece	GPE
    Roman	NORP
    Achaean	NORP
    Achaia	GPE
    Europe	LOC
    Roman	NORP
    Asia	LOC
    Trajan	GPE
    Turkish	NORP
    Asia Minor	ORG
    Euxine	PERSON
    Mediterranean	LOC
    Euphrates	LOC
    Europe	LOC
    Mount Taurus	FAC
    Halys	PERSON
    Romans	NORP
    Asia	LOC
    Troy	GPE
    Lydia	ORG
    Phrygia	ORG
    Pamphylians	NORP
    Lycians	NORP
    Carians	NORP
    Grecian	NORP
    Ionia	GPE
    Bithynia	GPE
    Pontus	ORG
    Constantinople	GPE
    Trebizond	GPE
    Cilicia	PERSON
    Syria	GPE
    the Roman Asia	LOC
    Halys	PERSON
    Armenia	GPE
    Euphrates	ORG
    Cappadocia	PERSON
    Euxine	PERSON
    Trebizond	GPE
    Asia	LOC
    Danube	PERSON
    Europe	LOC
    Roman	NORP
    Crim Tartary	PERSON
    Circassia	GPE
    Mingrelia	GPE
    Alexander	GPE
    Syria	GPE
    Seleucidae	ORG
    Upper Asia	LOC
    Parthians	NORP
    Euphrates	LOC
    Mediterranean	LOC
    Syria	GPE
    Romans	NORP
    Cappadocia	PERSON
    Egypt	GPE
    the Red Sea	LOC
    Phoenicia	ORG
    Palestine	GPE
    Syria	GPE
    Wales	GPE
    Phoenicia	ORG
    Palestine	GPE
    America	GPE
    Europe	LOC
    Syria	GPE
    Euphrates	LOC
    the Red Sea	LOC
    Arabs	NORP
    Roman	NORP
    Egypt	GPE
    Africa	LOC
    Asia	LOC
    Egypt	GPE
    Roman	NORP
    Ptolemies	ORG
    Mamelukes	ORG
    Turkish	NORP
    Nile	LOC
    five hundred miles	QUANTITY
    Cancer	PERSON
    Mediterranean	LOC
    Cyrene	PERSON
    first	ORDINAL
    Greek	NORP
    Egypt	GPE
    Barca	GPE
    Cyrene	PERSON
    Africa	LOC
    above fifteen hundred miles	QUANTITY
    Mediterranean	LOC
    Sahara	LOC
    an hundred miles	QUANTITY
    Romans	NORP
    Africa	LOC
    Phoenician	NORP
    Libyans	NORP
    Tripoli	GPE
    Algiers	LOC
    Numidia	GPE
    Massinissa	PERSON
    Jugurtha	GPE
    Augustus	ORG
    Numidia	GPE
    at least two-thirds	CARDINAL
    Mauritania	GPE
    Caesariensis	PRODUCT
    Mauritania	GPE
    Moors	ORG
    Tingi	ORG
    Tangier	ORG
    Tingitana	GPE
    Sallè	NORP
    Ocean	LOC
    Romans	NORP
    Mequinez	ORG
    Morocco	GPE
    Segelmessa	PERSON
    Roman	NORP
    Africa	LOC
    Mount Atlas	ORG
    Roman	NORP
    Africa	LOC
    Spain	GPE
    about twelve miles	QUANTITY
    Atlantic	LOC
    Mediterranean	LOC
    Hercules	GPE
    two	CARDINAL
    European	NORP
    Gibraltar	LOC
    the Mediterranean Sea	LOC
    Roman	NORP
    two	CARDINAL
    Baleares	PRODUCT
    Majorca and Minorca	ORG
    Spain	GPE
    Great Britain	GPE
    Corsica	PRODUCT
    Two	CARDINAL
    Italian	NORP
    Sardinia	GPE
    Sicily	GPE
    Crete	ORG
    Candia	PERSON
    Cyprus	PRODUCT
    Greece	GPE
    Asia	LOC
    Turkish	NORP
    Malta	GPE
    Order	ORG
    Roman	NORP
    Rome	GPE
    two thousand miles	QUANTITY
    Antoninus	GPE
    Dacia	PERSON
    Mount Atlas	ORG
    Cancer	WORK_OF_ART
    more than	CARDINAL
    the Western Ocean	LOC
    Euphrates	ORG
    fifty-sixth	CARDINAL
    hundred thousand square miles	QUANTITY
    


```python
# filter by place name
for  entity in first_chapter_doc.ents:
    if (entity.label_ == 'GPE') or (entity.label_ == 'LOC'):
        print(entity.text)
```

    Rome
    Nerva
    Trajan
    Marcus Antoninus
    Rome
    Rome
    Aethiopia
    Europe
    Germany
    the Atlantic Ocean
    Euphrates
    Arabia
    Africa
    Britain
    Britain
    Boadicea
    Britain
    Ireland
    Britain
    Scotland
    Antoninus Pius
    Antoninus
    Edinburgh
    gloomy hills
    Rome
    Trajan
    the Euxine Sea
    Trajan
    Philip
    Tigris
    Armenia
    the Persian gulf
    Arabia
    India
    Bosphorus
    Colchos
    Iberia
    Albania
    Armenia
    Mesopotamia
    Assyria
    Jupiter
    Jupiter
    Armenia
    Mesopotamia
    Assyria
    Euphrates
    Trajan
    Antoninus
    Caledonia
    the Upper Egypt
    Italy
    Rome
    Antoninus
    Marcus
    Euphrates
    Europe
    Rome
    Italy
    Spain
    East
    oblong
    Rome
    Britain
    Lower
    the Upper Germany
    Noricum
    Pannonia
    Maesia
    Syria
    Egypt
    Africa
    Spain
    Italy
    Marseilles
    Mediterranean
    Italy
    Misenum
    Naples
    Liburnians
    Misenum
    Mediterranean
    Provence
    Britain
    Spain
    Europe
    Mediterranean
    the Atlantic Ocean
    Lusitania
    Baetica
    Portugal
    East
    North
    Grenada
    Andalusia
    Baetica
    Spain
    Asturias
    Biscay
    Castilles
    Murcia
    Valencia
    Catalonia
    Arragon
    Tarragona
    Rome
    Alps
    Rhine
    Ocean
    France
    Alsace
    Switzerland
    Rhine
    Liege
    Luxemburg
    Mediterranean
    Languedoc
    the Celtic Gaul
    Lugdunum
    Rhine
    Rhine
    the Lower Germany
    Britain
    England
    Wales
    Scotland
    Edinburgh
    Britain
    Brigantes
    North
    South Wales
    Norfolk
    Suffolk
    Spain
    Britain
    Hercules
    Antoninus
    Lombardy
    Italy
    Po
    Piedmont
    Romagna
    Alps
    Venice
    Italy
    Rome
    Naples
    Campania
    Naples
    Italy
    Istria
    Rome
    Illyricum
    Pannonia
    Maesia
    Thrace
    Macedonia
    Greece
    Alps
    Bavaria
    Augsburg
    Austria
    Austria
    Styria
    Carinthia
    the Lower Hungary
    Sclavonia
    Noricum
    Pannonia
    Moravia
    Austria
    Hungary
    Austria
    Illyricum
    Croatia
    Bosnia
    Maesia
    Transylvania
    Hungary
    Moldavia
    Walachia
    the Ottoman Porte
    Maesia
    Servia
    Bulgaria
    Thrace
    Macedonia
    Greece
    Hellespont
    Rome
    Macedonia
    Asia
    Thessaly
    Thebes
    Argos
    Sparta
    Athens
    Greece
    Achaia
    Europe
    Asia
    Trajan
    Mediterranean
    Euphrates
    Europe
    Asia
    Troy
    Ionia
    Bithynia
    Constantinople
    Trebizond
    Syria
    the Roman Asia
    Armenia
    Trebizond
    Asia
    Europe
    Circassia
    Mingrelia
    Alexander
    Syria
    Upper Asia
    Euphrates
    Mediterranean
    Syria
    Egypt
    the Red Sea
    Palestine
    Syria
    Wales
    Palestine
    America
    Europe
    Syria
    Euphrates
    the Red Sea
    Egypt
    Africa
    Asia
    Egypt
    Nile
    Mediterranean
    Egypt
    Barca
    Africa
    Mediterranean
    Sahara
    Africa
    Tripoli
    Algiers
    Numidia
    Jugurtha
    Numidia
    Mauritania
    Mauritania
    Tingitana
    Ocean
    Morocco
    Africa
    Africa
    Spain
    Atlantic
    Mediterranean
    Hercules
    Gibraltar
    the Mediterranean Sea
    Spain
    Great Britain
    Sardinia
    Sicily
    Greece
    Asia
    Malta
    Rome
    Antoninus
    the Western Ocean
    


```python
# putting all of the data into a dictionary
import collections
place_freq = collections.defaultdict(int)
for entity in first_chapter_doc.ents:
    if (entity.label_ == 'GPE') or (entity.label_ == 'LOC'):
        place_freq[entity.text] += 1 # the utility of defaultdict!
place_freq = dict(place_freq)
```


```python
# dict -> df
place_freq_df = pd.DataFrame.from_dict(place_freq, orient='index').reset_index().rename(columns={'index':'place_name',0:'frequency'})
place_freq_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>place_name</th>
      <th>frequency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rome</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nerva</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Trajan</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Marcus Antoninus</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Aethiopia</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>147</th>
      <td>Great Britain</td>
      <td>1</td>
    </tr>
    <tr>
      <th>148</th>
      <td>Sardinia</td>
      <td>1</td>
    </tr>
    <tr>
      <th>149</th>
      <td>Sicily</td>
      <td>1</td>
    </tr>
    <tr>
      <th>150</th>
      <td>Malta</td>
      <td>1</td>
    </tr>
    <tr>
      <th>151</th>
      <td>the Western Ocean</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>152 rows × 2 columns</p>
</div>




```python
# downloading the Pleiades data we need (also from my gh)
if not os.path.isfile('places.csv'):
    wget.download('https://raw.githubusercontent.com/pnadelofficial/FallDHCourseMaterials/main/places.csv')
if not os.path.isfile('names.csv'):
    wget.download('https://raw.githubusercontent.com/pnadelofficial/FallDHCourseMaterials/main/names.csv')
```


```python
places = pd.read_csv('places.csv')
places.columns
```




    Index(['created', 'description', 'details', 'provenance', 'title', 'uri', 'id',
           'representative_latitude', 'representative_longitude',
           'bounding_box_wkt'],
          dtype='object')




```python
# let's find 'Rome' in places
places.loc[places['title'] == 'Roma']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>created</th>
      <th>description</th>
      <th>details</th>
      <th>provenance</th>
      <th>title</th>
      <th>uri</th>
      <th>id</th>
      <th>representative_latitude</th>
      <th>representative_longitude</th>
      <th>bounding_box_wkt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>21483</th>
      <td>2018-06-07T19:48:13Z</td>
      <td>The capital of the Roman Republic and Empire.</td>
      <td>&lt;p&gt;The Barrington Atlas Directory notes: Roma/...</td>
      <td>Barrington Atlas: BAtlas 43 B2 Roma</td>
      <td>Roma</td>
      <td>https://pleiades.stoa.org/places/423025</td>
      <td>423025</td>
      <td>41.891775</td>
      <td>12.486137</td>
      <td>POLYGON ((12.486137 41.891775, 12.486137 41.89...</td>
    </tr>
  </tbody>
</table>
</div>




```python
names = pd.read_csv('names.csv')
names.columns
```




    Index(['created', 'description', 'details', 'provenance', 'title', 'uri', 'id',
           'place_id', 'name_type', 'language_tag', 'attested_form',
           'romanized_form_1', 'romanized_form_2', 'romanized_form_3',
           'association_certainty', 'transcription_accuracy',
           'transcription_completeness', 'year_after_which', 'year_before_which'],
          dtype='object')




```python
# let's find 'Rome' in names
names.loc[names['romanized_form_1'] == 'Rome'].place_id
```




    20810    423025
    Name: place_id, dtype: int64




```python
def get_pleiades_id(term):
    """
    Iterates through all of the possible names in the names.csv file
    Returns None if no matched names
    """
    name_row = names.loc[names['attested_form'] == term]
    if len(name_row) == 1:
        return int(name_row.place_id.iloc[0])
    else:
        name_row = names.loc[names['romanized_form_1'] == term]
        if len(name_row) == 1:
            return int(name_row.place_id.iloc[0])
        else:
            name_row = names.loc[names['romanized_form_2'] == term]
            if len(name_row) == 1:
                return int(name_row.place_id.iloc[0])
            else:
                name_row = names.loc[names['romanized_form_3'] == term]
                if len(name_row) == 1:
                    return int(name_row.place_id.iloc[0])
                else:
                    return None
```

The above function looks very complicated, but all it's doing is checking the results of several `loc` and `iloc` calls from our `DataFrame`. You will very rarely see `for` loops when using `pandas`. Instead, you will see programmers taking advantage of the very efficient search methods in `pandas` like `loc`, sometimes called 'broadcasting'. Check out this [Medium post](https://medium.com/@michaeleby1/broadcasting-versus-iteration-6c06539dc1d5) for a further discussion of the benefits of broadcasting over writing loops.


```python
place_freq_df['pleiades_id'] = place_freq_df['place_name'].apply(get_pleiades_id)
place_freq_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>place_name</th>
      <th>frequency</th>
      <th>pleiades_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rome</td>
      <td>12</td>
      <td>423025.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nerva</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Trajan</td>
      <td>5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Marcus Antoninus</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Aethiopia</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>147</th>
      <td>Great Britain</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>148</th>
      <td>Sardinia</td>
      <td>1</td>
      <td>472014.0</td>
    </tr>
    <tr>
      <th>149</th>
      <td>Sicily</td>
      <td>1</td>
      <td>462492.0</td>
    </tr>
    <tr>
      <th>150</th>
      <td>Malta</td>
      <td>1</td>
      <td>462311.0</td>
    </tr>
    <tr>
      <th>151</th>
      <td>the Western Ocean</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>152 rows × 3 columns</p>
</div>



Why are there so many `NaN` values? How do we deal with them? How do we want to deal with them?


```python
place_freq_final = place_freq_df.dropna().reset_index(drop=True)
place_freq_final
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>place_name</th>
      <th>frequency</th>
      <th>pleiades_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rome</td>
      <td>12</td>
      <td>423025.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Euphrates</td>
      <td>6</td>
      <td>912849.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Arabia</td>
      <td>2</td>
      <td>981506.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Africa</td>
      <td>7</td>
      <td>775.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Ireland</td>
      <td>1</td>
      <td>20487.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>India</td>
      <td>1</td>
      <td>50004.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Iberia</td>
      <td>1</td>
      <td>863807.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Caledonia</td>
      <td>1</td>
      <td>89132.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Misenum</td>
      <td>2</td>
      <td>432941.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Naples</td>
      <td>3</td>
      <td>433014.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Tarragona</td>
      <td>1</td>
      <td>246349.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Lugdunum</td>
      <td>1</td>
      <td>167717.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Hercules</td>
      <td>2</td>
      <td>266032.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Illyricum</td>
      <td>2</td>
      <td>481865.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Macedonia</td>
      <td>3</td>
      <td>491656.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Augsburg</td>
      <td>1</td>
      <td>118580.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Thebes</td>
      <td>1</td>
      <td>541138.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Argos</td>
      <td>1</td>
      <td>570106.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Sparta</td>
      <td>1</td>
      <td>570685.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Athens</td>
      <td>1</td>
      <td>579885.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Achaia</td>
      <td>1</td>
      <td>570028.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Troy</td>
      <td>1</td>
      <td>550595.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Ionia</td>
      <td>1</td>
      <td>550597.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Constantinople</td>
      <td>1</td>
      <td>520998.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Trebizond</td>
      <td>2</td>
      <td>857359.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Nile</td>
      <td>1</td>
      <td>727172.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Algiers</td>
      <td>1</td>
      <td>295276.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Sardinia</td>
      <td>1</td>
      <td>472014.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Sicily</td>
      <td>1</td>
      <td>462492.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Malta</td>
      <td>1</td>
      <td>462311.0</td>
    </tr>
  </tbody>
</table>
</div>



Now that we have the Pleiades IDs, we can finally get the coordiantes from `places.csv`. Let's look back at the Roman example. 


```python
rid = place_freq_final.pleiades_id.iloc[0]
places.loc[places['id'] == rid].representative_latitude.iloc[0]
```




    41.891775




```python
# could've just one function here, but not too much trouble to do two
def get_lat(pl_id):
    places_row = places.loc[places['id'] == pl_id]
    if len(places_row) == 1:
        return places_row.representative_latitude.iloc[0]
    
def get_long(pl_id):
    places_row = places.loc[places['id'] == pl_id]
    if len(places_row) == 1:
        return places_row.representative_longitude.iloc[0]
```


```python
place_freq_final['lat'] = place_freq_final['pleiades_id'].apply(get_lat)
place_freq_final['long'] = place_freq_final['pleiades_id'].apply(get_long)
```


```python
place_freq_final
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>place_name</th>
      <th>frequency</th>
      <th>pleiades_id</th>
      <th>lat</th>
      <th>long</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rome</td>
      <td>12</td>
      <td>423025.0</td>
      <td>41.891775</td>
      <td>12.486137</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Euphrates</td>
      <td>6</td>
      <td>912849.0</td>
      <td>35.543310</td>
      <td>39.606018</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Arabia</td>
      <td>2</td>
      <td>981506.0</td>
      <td>27.500000</td>
      <td>32.500000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Africa</td>
      <td>7</td>
      <td>775.0</td>
      <td>32.500000</td>
      <td>7.500000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Ireland</td>
      <td>1</td>
      <td>20487.0</td>
      <td>53.184028</td>
      <td>-7.717526</td>
    </tr>
    <tr>
      <th>5</th>
      <td>India</td>
      <td>1</td>
      <td>50004.0</td>
      <td>22.500000</td>
      <td>77.500000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Iberia</td>
      <td>1</td>
      <td>863807.0</td>
      <td>41.836468</td>
      <td>44.689138</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Caledonia</td>
      <td>1</td>
      <td>89132.0</td>
      <td>57.500000</td>
      <td>-4.500000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Misenum</td>
      <td>2</td>
      <td>432941.0</td>
      <td>40.786279</td>
      <td>14.084884</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Naples</td>
      <td>3</td>
      <td>433014.0</td>
      <td>40.839995</td>
      <td>14.252870</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Tarragona</td>
      <td>1</td>
      <td>246349.0</td>
      <td>41.116892</td>
      <td>1.258338</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Lugdunum</td>
      <td>1</td>
      <td>167717.0</td>
      <td>45.758866</td>
      <td>4.819482</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Hercules</td>
      <td>2</td>
      <td>266032.0</td>
      <td>37.500000</td>
      <td>-0.500000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Illyricum</td>
      <td>2</td>
      <td>481865.0</td>
      <td>42.427292</td>
      <td>17.965028</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Macedonia</td>
      <td>3</td>
      <td>491656.0</td>
      <td>41.250000</td>
      <td>21.750000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Augsburg</td>
      <td>1</td>
      <td>118580.0</td>
      <td>48.365463</td>
      <td>10.894765</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Thebes</td>
      <td>1</td>
      <td>541138.0</td>
      <td>38.319156</td>
      <td>23.317577</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Argos</td>
      <td>1</td>
      <td>570106.0</td>
      <td>37.631561</td>
      <td>22.719464</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Sparta</td>
      <td>1</td>
      <td>570685.0</td>
      <td>37.077905</td>
      <td>22.427298</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Athens</td>
      <td>1</td>
      <td>579885.0</td>
      <td>37.972634</td>
      <td>23.722746</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Achaia</td>
      <td>1</td>
      <td>570028.0</td>
      <td>38.102121</td>
      <td>22.224586</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Troy</td>
      <td>1</td>
      <td>550595.0</td>
      <td>39.957433</td>
      <td>26.238459</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Ionia</td>
      <td>1</td>
      <td>550597.0</td>
      <td>38.162194</td>
      <td>27.357498</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Constantinople</td>
      <td>1</td>
      <td>520998.0</td>
      <td>41.006371</td>
      <td>28.965352</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Trebizond</td>
      <td>2</td>
      <td>857359.0</td>
      <td>41.004269</td>
      <td>39.723312</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Nile</td>
      <td>1</td>
      <td>727172.0</td>
      <td>19.211409</td>
      <td>30.567330</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Algiers</td>
      <td>1</td>
      <td>295276.0</td>
      <td>36.768912</td>
      <td>3.053218</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Sardinia</td>
      <td>1</td>
      <td>472014.0</td>
      <td>39.871087</td>
      <td>8.957517</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Sicily</td>
      <td>1</td>
      <td>462492.0</td>
      <td>37.643297</td>
      <td>13.932018</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Malta</td>
      <td>1</td>
      <td>462311.0</td>
      <td>35.908887</td>
      <td>14.408042</td>
    </tr>
  </tbody>
</table>
</div>




```python
place_freq_final.to_csv('ch1gibbon_places.csv')
```

## In-class Activity

Now pair up and try to take all of the above steps and turn it into a single function, so that all you need to do is pass in the text of a chapter and you get back a DataFrame with place names and coordinates. To walkthrough the steps again:

* Consider what all of your inputs are
* Use `spaCy` syntax to parse input text
* Filter and count by place name and label
* Use `pandas` to manipulate the data into a useful form

Try out some different chapters. Do you notice anything about the places? Do the types of places or the accuracy of Pleiades get better or worse over the chapters? I encourage you to Google or look up any entities you don't know on Wikipedia.


```python
def find_name_and_coords(gibbon_chapter):
    second_chapter = gibbon_chapter
    second_chapter_doc = nlp(second_chapter)
    
#    for entity in second_chapter_doc.ents: # can access NER with the .ents attribute
#       print(entity.text, entity.label_, sep='\t')

    import collections
    place_freq = collections.defaultdict(int)
    for entity in second_chapter_doc.ents:
        if (entity.label_ == 'GPE') or (entity.label_ == 'LOC'):
            place_freq[entity.text] += 1 # the utility of defaultdict!
    place_freq = dict(place_freq)
    place_freq_df = pd.DataFrame.from_dict(place_freq, orient='index').reset_index().rename(columns={'index':'place_name',0:'frequency'})
    place_freq_df
    
    places = pd.read_csv('places.csv')
    names = pd.read_csv('names.csv')
    #get_pleiades_id(term)

    place_freq_df['pleiades_id'] = place_freq_df['place_name'].apply(get_pleiades_id)
    place_freq_df
    
    place_freq_final = place_freq_df.dropna().reset_index(drop=True)
    place_freq_final
    
    place_freq_final['lat'] = place_freq_final['pleiades_id'].apply(get_lat)
    place_freq_final['long'] = place_freq_final['pleiades_id'].apply(get_long)
    
    print(place_freq_final)
    place_freq_final.to_csv('gibbon_places.csv')
```


```python
find_name_and_coords()
```

       place_name  frequency  pleiades_id        lat       long
    0        Rome         32     423025.0  41.891775  12.486137
    1        Nile          4     727172.0  19.211409  30.567330
    2      Athens         11     579885.0  37.972634  23.722746
    3      Sparta          1     570685.0  37.077905  22.427298
    4       Padua          2     393473.0  45.409561  11.876975
    5     Arpinum          1     432700.0  41.648422  13.609876
    6     Etruria          1     413122.0  42.758127  11.546721
    7      Latium          2     432900.0  41.590543  13.192265
    8      Alesia          1     177434.0  47.536622   4.503884
    9      Africa          4        775.0  32.500000   7.500000
    10  Euphrates          1     912849.0  35.543310  39.606018
    11      Capua          1     432754.0  41.086092  14.250207
    12     Verona          2     383816.0  45.442130  10.995736
    13      Troas          1     550944.0  39.837052  26.336944
    14      Milan          1     383706.0  45.463746   9.188060
    15     London          1      79574.0  51.513335  -0.088949
    16      Paris          1     109126.0  48.854405   2.346168
    17      Arles          1     148217.0  43.677616   4.630799
    18   Bordeaux          1     138248.0  44.837205  -0.576533
    19      Autun          1     177460.0  46.947240   4.299177
    20     Vienne          1     167719.0  45.524510   4.875982
    21   Hercules          1     266032.0  37.500000  -0.500000
    22     Sicily          1     462492.0  37.643297  13.932018
    23      Media          1     903080.0  34.500000  46.500000
    24     Arabia          2     981506.0  27.500000  32.500000
    25      India          2      50004.0  22.500000  77.500000
    


```python

```
