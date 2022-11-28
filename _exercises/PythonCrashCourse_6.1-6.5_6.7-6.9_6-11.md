---
layout: page
title: PythonCrashCourse_6.1-6.5_6.7-6.9_6.11
description: Python Basics 4
---

### 6.1


```python
person = {}
```


```python
person['first_name'] = 'Minnie'
person['last_name'] = 'Xie'
person['age'] = '21'
person['city'] = 'Medford'
```


```python
print(person)
```

    {'first_name': 'Minnie', 'last_name': 'Xie', 'age': '21', 'city': 'Medford'}
    

### 6.2


```python
fav_nums = {}
fav_nums['minnie'] = 1
fav_nums['emma'] = 2
fav_nums['casey'] = 3
fav_nums['julien'] = 4
fav_nums['colby'] = 5
print(fav_nums)
```

    {'minnie': 1, 'emma': 2, 'casey': 3, 'julien': 4, 'colby': 5}
    

### 6.3


```python
vocab = {
    'int': 'integer value',
    'string': 'list of chars',
    'elif': 'else if',
    'python': 'coding language',
    'dictionary': 'like a list with keys'
}
print("int: " + vocab['int'])
print("string: " + vocab['string'])
print("elif: " + vocab['elif'])
print("python: " + vocab['python'])
print("dictionary: " + vocab['dictionary'])
```

    int: integer value
    string: list of chars
    elif: else if
    python: coding language
    dictionary: like a list with keys
    

### 6.4


```python
for key,value in vocab.items():
    print(key + ": " + value)
vocab['loop'] = 'helps with iterating'
vocab['variable'] = 'stores information'
vocab['list'] = 'stores a group of variables'
vocab['boolean'] = 'true or false type'
vocab['print'] = 'show output'
```

    int: integer value
    string: list of chars
    elif: else if
    python: coding language
    dictionary: like a list with keys
    loop: helps with iterating
    variable: stores information
    list: stores a group of variables
    boolean: true or false type
    print: show output
    

### 6.5


```python
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'thames': 'england'
}
for name,country in rivers.items():
    print("The " + name.title() + " runs through " + country.title())
    
for name in rivers.keys():
    print(name)
    
for name in rivers.keys():
    print(rivers[name])
```

    The Nile runs through Egypt
    The Mississippi runs through United States
    The Thames runs through England
    nile
    mississippi
    thames
    egypt
    united states
    england
    

### 6.7


```python
me = {}
you = {}
people = [me, you, person]
for curr_person in people:
    print(curr_person)
```

    {}
    {}
    {'first_name': 'Minnie', 'last_name': 'Xie', 'age': '21', 'city': 'Medford'}
    

### 6.8


```python
lucky = {
    'type': 'dog',
    'owner': 'sam'
}

mittens = {
    'type': 'cat',
    'owner': 'sam'
}

pets = [lucky, mittens]

for pet in pets:
    print(pet)
```

    {'type': 'dog', 'owner': 'sam'}
    {'type': 'cat', 'owner': 'sam'}
    

### 6.9


```python
favorite_places = {}

minnie_places = ['here', 'there']
julien_places = ['over here', 'over there']
emma_places = ['over the hill', 'across the river', 'through the woods']

favorite_places = {
    'minnie': minnie_places,
    'julien': julien_places,
    'emma': emma_places,
}

for person in favorite_places.items():
    print(person)

```

    ('minnie', ['here', 'there'])
    ('julien', ['over here', 'over there'])
    ('emma', ['over the hill', 'across the river', 'through the woods'])
    

### 6.11


```python
medford = {
    'country': 'united states',
    'population': 'over 100',
    'fact': 'where Tufts is located'
}
phoenix = {
    'country': 'united states',
    'population': 'over 100',
    'fact': 'where my hometown is located'
}
madrid = {
    'country': 'spain',
    'population': 'over 100',
    'fact': 'the capital of Spain'
}
cities = {
    'Medford'
}

```


```python

```
