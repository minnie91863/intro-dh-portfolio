# Mapping the Migration of Work at the CMOA using ArcGIS

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

On the other hand, some of the matched cases were only partially accurate, since some artists had multiple nationalities. In this case where the artist was British and Italian, ArcGIS was only able to recognize the Italian part, since their birth and death places were both in Italy. 

Clearly, this dataset still needs much more refinement. I decided from this point to scrap the hosted feature layers I had just attempted to make, and instead work on cleaning up the data. In order to make the dataset easier to use for this assignment, I narrowed the scope even further by only considering work listed under the “Fine Arts” department, and only considering the artists’ nationalities. For artists that have multiple nationalities, I will be arbitrarily selecting the first one listed. 



```python

```

TODO (Insert photos here of data preparation process in arcgis)

## Code

(idk write some code that calculates the distances and plots them on a map?)

## Artifact

Below are screencaptures of my resulting GIS visualization on the distance between the work and the CMOA museum

A link to my ArcGIS map can be found here

## Analysis


```python

```

## Conclusion


```python

```
