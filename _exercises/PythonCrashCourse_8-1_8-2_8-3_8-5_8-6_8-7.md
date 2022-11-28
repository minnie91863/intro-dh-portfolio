---
layout: page
title: PythonCrashCourse_8-1_8-2_8-3_8-5_8-6_8-7
description: Python Basics 5
---

### 8-1


```python
def display_message():
    print("Hi everyone! I'm currently learning about functions in Python :)")
    
display_message();
```

    Hi everyone! I'm currently learning about functions in Python :)
    

### 8-2


```python
title = "The Hunger Games"
def favorite_book(title):
    print("A book I enjoyed in middle school was " + title)

favorite_book(title);
```

    A book I enjoyed in middle school was The Hunger Games
    

### 8-3


```python
def make_shirt(size, message):
    print("The shirt will be in size " + size + " and the message will be " + message)

make_shirt("medium", 'Hello World!')
make_shirt(message = 'Hello World!', size = 'medium')
```

    The shirt will be in size medium and the message will be Hello World!
    The shirt will be in size medium and the message will be Hello World!
    

### 8-5


```python
country = 'Canada'
def describe_city(city, country):
    print( "The city of " + city.title() + " is in " + country.title())

describe_city('toronto', country)
describe_city('calgary', country)
describe_city('medford', 'united states')
```

    The city of Toronto is in Canada
    The city of Calgary is in Canada
    The city of Medford is in United States
    

### 8-6


```python
def city_country(city, country):
    return (str(city.title() + ', ' + country.title()))

print(city_country('santiago', 'chile'))
print(city_country('havana', 'cuba'))
print(city_country('sao paulo', 'brazil'))
```

    Santiago, Chile
    Havana, Cuba
    Sao Paulo, Brazil
    

### 8-7


```python
def make_album(artist, album, num_tracks=''):
    artist_album = {'name': artist.title(), 'album': album.title()}
    if num_tracks:
               artist_album['num_tracks'] = num_tracks
    return artist_album

print(make_album('the 1975', 'being funny in a foriegn language'))
print(make_album('taylor swift', 'red'))
print(make_album('beabadoobee', 'beatopia', '14'))

```

    {'name': 'The 1975', 'album': 'Being Funny In A Foriegn Language'}
    {'name': 'Taylor Swift', 'album': 'Red'}
    {'name': 'Beabadoobee', 'album': 'Beatopia', 'num_tracks': '14'}
    


```python

```
