# Mapping the CMOA
## Mapping the Migration of Work at the CMOA using ArcGIS

## Overview

Archives, libraries, and museums  document, preserve, and inform us on our complex histories. They provide insight into our heritage, our evolution, and our interests. They inform our behavior, pass down generations of knowledge, and illustrate our experiences through a myriad of mediums. They provide insight into what it has meant to be human, and what it may mean now. It is without a doubt that recording our history has affected how we interact with the world, whether that be culturally, politically, or spiritually. 

Museums serve as resources, often for the public, which  investigate all descriptions of human behavior. For my final project, I would like to consider the logistics behind the pieces that are displayed and shared at museums. Who has the authority to inform the public with their collection? How can one define the ethics behind developing a collection? Why do we place value on the pieces that are preserved, displayed, and studied? I would like to mention that I am no expert in museum studies, so there may be notable debates and solutions  surrounding these questions that I am not aware of. I plan to research, at an introductory level, the issue of piece/artifact  migration for the sake of a museum collection. 

I will be investigating the geographical distribution of the origins of works and artifacts in museums by completing a shallow case study on the Carnegie Museum of Art (CMOA). The dataset I will be using (https://github.com/cmoa/collection )  includes information on approximately 28269 objects across all departments of the museum, with details such as the title, creation date, medium, physical location, dimensions, and artist biography. I plan to use the GIS tool ArcGIS to create a visual of these geographical distances between where the artist came from and where the work now lies. I expect most of the works’ physical locations to be generalized to the location of the CMOA  and the artist origins to be spread across the globe, potentially with more origins from North America and Europe.  

While I had initially intended on exploring the collection of the British Museum, as its nation state holds a long and complex history of colonization, I was unable to find a database of their collection which included cleaned data about each piece and its geographical origin. The datasets I found for the British Museum collection seemed to be outdated and inaccessible (https://github.com/culturehack/data-tool/blob/master/sources/37251018-British-Museum-object-catalog.md ). Their website (https://www.britishmuseum.org/collection ) proved to be helpful for close readings at specific artifacts, but difficult for a computer to do a distant read. I was ultimately limited by my ability to webscrape, so I opted to use the collection at the CMOA. This may not give as much of a historically significant look into the migration of artifacts/work, but we can also consider an analysis of artists’ works, the artists’ origins, and the type of work they created using the same visualization techniques with the CMOA dataset.

It’s important to note that the British Museum provides some context on its website addressing “How objects come into the collection” (https://www.britishmuseum.org/about-us/british-museum-story/collecting-histories ). While it is crucial to take British colonial history into great consideration when interpreting and visualizing these distances between the work’s estimated or known origin and the British Museum, the complexity of their colonial history extends beyond the scope of this project.

Moreover, the museum is sponsored by the UK Parliament's  Department for Digital, Culture, Media & Sport (https://www.britishmuseum.org/about-us/governance#:~:text=The%20British%20Museum%20is%20a,(Opens%20in%20new%20window). ) as an additional factor to consider, whereas the CMOA is backed by the Carnegie Institute (https://cmoa.org/ ), which is a private academic institution. As a government-directed collection, the curation of objects within the British Museum directly represents how the country wishes to be perceived. This applies not only to other countries, but also internally between Scotland, Wales, Northern Ireland, and England, which has its own  nuanced history of power dynamics and culture. 

The British Museum’s collection website cites their first acquisition as the purchase of Sir Hans Sloane’s collection with the 1753 Act of Parliament. The website acknowledges that “[s]ome ways in which objects entered the British Museum are no longer current or acceptable”. This prompts discourse regarding where these items belong, and in whose possession they should be. Some may argue that since many, if not the vast majority, of these artifacts were stolen from their places of origin as a byproduct of British colonization, they should be unconditionally returned to their respective origins, if known. Others consider it to be beneficial that such artifacts are preserved in the museum  and are available for public viewing. Questions regarding postcolonial theory come into play.

Issues on colonialism may not be as relevant to CMOA’s collection. Instead, we can consider a more general read on what’s deemed valuable and representative of art history in the Western world. It’s unlikely that the origin of every work in the CMOA is known, since a piece may be imagined, realized, and curated in different locations. For the sake of simplicity, I will be generalizing the work’s origin to the documented origin of the artist. By doing so, certain trends may arise describing the differences in work created in different locations, and potential reasonings behind the migration of the works. 

Representation holds incredible power in the public landscape. Especially when it comes to museums, which are typically well-respected and held to a high standard, the pieces and artifacts presented directly correlate to what’s assigned value. By observing the movement and migration of work in the CMOA, we can grasp a general understanding of which geographical regions are deemed as museum-worthy in the United States Northeast.  

What can be inferred by mapping and visualizing the distance between an artifact or artwork’s physical location and its potential origin? Let’s investigate.


## Data Preparation

For this project, not much preparation was needed for cleaning the data. If I had successfully web-scraped the British Museum’s collection, I would have been required to clean the data, since the website formatting and other variables add complexity to making the information organized and readable by a computer. However, due to technical restraints, I will be using an already-prepared .csv dataset of the works at CMOA. My data preparation will be all for the sake of narrowing the scope of the dataset 

Since the dataset I used for this project is much larger than what ArcGIS is capable of holding on one layer, I needed to create a hosted layer to separate out the information in my .csv to be able to import the information. I followed the steps outlined here. 
https://doc.arcgis.com/en/arcgis-online/manage-data/publish-features.htm

At a quick glance at the .csv, the locations of the artists’ birth and death origins are not always provided, and are listed in the format of “city, country”. Their nationality is also provided when available. Since my locations are not provided as latitude/longitude coordinates, I used a special ArcGIS function that required the use of credits (of which I automatically had 2000 provided by Tufts). In order to simplify the project, I will be generalizing the origin of the work as the birthplace of the artist, since it is the closest point of information we can use from the dataset to generalize where the work originated from.

By using the artists’ birthplaces and nationalities, rather than mapping the migration of the work as I had initially hoped to do, this project will instead provide a visualization of the representation of work and artists at the CMOA. However, I wanted to visualize as many relevant options as I could, so I listed the location information as present in multiple fields. This way, I could also include the artists’ nationality and place of death. 

Out of the entire dataset, there were only 244 location matches of the 28269 items. In this case, if I wanted to track all of the work in the dataset, I would need to manually mark the locations to the places on the map for every missed option. The first unmatched location, for instance, listed what was supposed to be New York City, New York as Newyork, Argyll, and Bute, Scotland. 

![png](/_final_project/screen_captures/wront_newyork.png)

On the other hand, some of the matched cases were only partially accurate, since some artists had multiple nationalities. In this case where the artist was British and Italian, ArcGIS was only able to recognize the Italian part, since their birth and death places were both in Italy. 

![png](/_final_project/screen_captures/multinational.png)

Clearly, this dataset still needs much more refinement. I decided from this point to scrap the hosted feature layers I had just attempted to make, and instead work on cleaning up the data. In order to make the dataset easier to use for this assignment, I narrowed the scope even further by only considering work listed under the “Fine Arts” department, and only considering the artists’ nationalities. For artists that have multiple nationalities, I will be arbitrarily selecting the first one listed. 

However, I wasn't able to make the nationalities legible to ArcGIS. The nationalities weren't formatted as location names, and those with multiple nationalities continued pose issues for interpreting the data correctly. I opted for birthplaces instead.

![png](/_final_project/screen_captures/second_attempt_still_wrong.png)

This change made much more useful results!

![png](/_final_project/screen_captures/much_better.png)

I attempted to run a distance analysis between the CMOA and each location, but it never completed. I instead included a widget in the website to add and measure custom distances.

![png](/_final_project/screen_captures/pending_results.png)

Please refer to the code section below to walkthorugh the steps on how I prepared the csv file to fit the scope of this project


## Code

For the unabridged version of the code, please review the file "Data Preparation" in my portfolio github repo.


```python
import spacy
import csv
import pandas as pd
```

Isolating work just in the Fine Arts department


```python
with open('cmoa.csv', 'rt', encoding = 'utf8') as inp, open('cmoa_fine_art.csv', 'wt', encoding = 'utf8') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[9] == "Fine Arts":
            writer.writerow(row)
```

At a glance, it seems like each row has an arbitrary row of whitespace separating each of the rows that have information, so I'll attempt to remove those


```python
df = pd.read_csv('cmoa_fine_art.csv')
df.to_csv('cmoa_fine_art1.csv', index = False)
```

I also need to remove any "Notes" since they may cause issues in the csv file format.


```python
df = pd.read_csv('cmoa_fine_art1.csv', error_bad_lines = False).dropna()
df.to_csv('cmoa_fine_art2.csv', index = False)
```

After attempting to also copy over the header of the csv file, I realized it would be quicker to simploy copy and paste it manually

Let's also remove all the rows that do not include a nationality, which is at index 24. Alternatively, we can reference that information with the "nationality" key word


```python
filter = df["nationality"] != ""
df_clean = df[filter]
```


```python
df.to_csv('cmoa_fine_art3.csv', index = False)
```

Let's compare the lengths of the csv files to see if any changes were made


```python
original = pd.read_csv('cmoa.csv')
results0 = pd.read_csv('cmoa_fine_art.csv')
results1 = pd.read_csv('cmoa_fine_art1.csv')
results2 = pd.read_csv('cmoa_fine_art2.csv')
results3 = pd.read_csv('cmoa_fine_art3.csv')
```


```python
print(len(original))
print(len(results0))
print(len(results1))
print(len(results2))
print(len(results3))
```

28269
8972
8972
1177
1177


While some of the cleaning may have been done incorrectly or may have been repetative, the resulting 1177 rows is now much more usable than the original 28269 for this project-- 4.16% of the number of pieces we began with!

The largest change was when I reduced the scope from the entire collection to the Fine Arts department. This superficially showcases the proportion of work in the CMOA that is considered as Fine Art (although what can be defined as such is an entirely separate discussion). Interestingly enough, in this dataset, Contemporary Art is labelled as a separate department. I can therefore infer that the work in the Fine Arts department is somewhat historical.


```python
df = pd.read_csv("cmoa_fine_art3.csv")
df.loc[:, "nationality"]
```

Below, I'm printing out specific information to get a glance at how usable the information is in order to narrow down what I include in my hosted feature layer


```python
df.loc[:, "death_place"]
```

I'm going to try to input the nationality data into ArcGIS to see if it can recognize the phrasing as a location. If not, I will need to continue to process the data to convert the nationality to a location. If all ese fails, I may need to use alternative methods to visualize this dataset.

While ArcGIS was able to recognize more locations this time around, it still struggled to handle multiple nationalities, and misinterpreted many as incorrect locations. This means I need to either continue cleaning the naitonalities data, or use an alternative data point such as the birth location.

Let's do a quick test on ArcGIS using the birth location instead

ArcGIS handleded the birth_place information much better, and only struggled to match up Tokyo. Since there weren't many unmatched plots, I went ahead and matched those manually. After this process, 221 of the 1176 works remained unmatched. In my cleaning process, since I didn't focus on birth_place, I didn't remove the values that had null or blank fiends for the birth_place. The remainig 221 works did not have birth_place information, so for the sake of this assignment they will be left out.

## Artifact

Below are screencaptures of my resulting GIS visualization on the artists represented in the CMOA collection's fine art department compared to the location of the CMOA adn world GDPs from 1960-2016.

A link to my ArcGIS map can be found [here](https://tuftsgis.maps.arcgis.com/apps/webappviewer/index.html?id=ad3872fe290d4bdaa0b55dcd9df75bc5)

[https://tuftsgis.maps.arcgis.com/apps/webappviewer/index.html?id=ad3872fe290d4bdaa0b55dcd9df75bc5](https://tuftsgis.maps.arcgis.com/apps/webappviewer/index.html?id=ad3872fe290d4bdaa0b55dcd9df75bc5)

![png](/_final_project/screen_captures/building_web_app.png)

![png](/_final_project/screen_captures/using_web_app.png)


## Analysis

The results of mapping out the birthplaces of the Fine Art artists in the CMOA dataset reveal some strong trends. 

The majority of the artists whose work is considered to be in the Fine Art department were born in Europe, more specifically Western Europe. It’s important to note that each pin represents a work, and not the artist. Therefore, certain locations have multiple pins, since some artists have multiple works in the CMOA collection. This distant read leaves me questioning the definition of fine art, and why it was distinct from contemporary art in the dataset--what does this showcase about the CMOA’s value system, or how it defines historical significance? 

The preservation and physical documentation of history through art --the backbone of museums--is not practiced equally across the globe, which may also impact whose work is represented at the CMOA. The map visualizes which regions of the world favor this form of historical documentation, and which regions the CMOA considers worth representing. Boundaries such as culture, language, and politics may also impact who the CMOA includes in their collection.

I included an online layer of the world GDP from the past few decades to compare with the edited CMOA dataset. Considering the correlation between fine art with modern economic wealth, there is somewhat of a link between areas of economic power and areas whose history in the form of fine art is considered valuable enough to be preserved in the Western lens. It’s interesting to see these value systems align, considering that both definitions of value by the CMOA and World Bank, headquartered in Washington D.C., are under American eyes. Through this pattern, one can infer that economic and historic values are closely related in the United States. 



## Conclusion


Although these results did not offer insight into British colonialism, they did provide equally interesting results. I originally planned to investigate the migration of artwork. Instead, I ended up with a wonderful visualization of representation in museums, considerations on how the CMOA defines fine art, and questions about how the United States assigns value, therefore affecting the education of the general public. Who and what gets represented in higher institutions such as museums can impact their and other groups' social reputations. It is up to the musem to decide how they want to curate their view of past and present,  authentically or not.
